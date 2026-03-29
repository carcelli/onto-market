# Autoresearch Program — Polymarket Forecaster

## Objective

Minimize **Brier score** on the held-out validation set of resolved Polymarket
binary markets.  Lower is better; 0.25 is the naive baseline (always predict 0.5).

## Frozen evaluator contract

The evaluator (`evaluate.py`) is **never edited** by the autoresearch loop.
It judges candidate models on four axes:

1. **Forecast quality** — Brier score (primary), log-loss, calibration error (ECE).
2. **Economic quality** — simulated PnL after 2% fees + 50 bps slippage, ROI.
3. **Stability** — max drawdown, turnover fraction.
4. **Honesty** — point-in-time features only, walk-forward temporal split, no leakage.

### Promotion gates (hard constraints)

A candidate is **rejected** if any gate fails, even if Brier improves:

| Gate               | Threshold          |
|--------------------|--------------------|
| `sufficient_samples` | n >= 20            |
| `calibrated`       | ECE <= 0.15        |
| `turnover_ok`      | trades/n <= 0.80   |

### Composite score

When all gates pass, a composite score is computed:
`(0.25 - brier) * 4.0 + roi * 0.5 - ece * 2.0` — higher is better.

The researcher should aim to improve Brier while staying calibrated and
avoiding strategies that trade on every market (overtrading).

## Researcher LLM

The researcher can run on a **local Ollama model** (e.g. `gpt-oss:20b`) on
CPU/RAM while training uses the GPU.  This is set via `--researcher local`
on the CLI or `researcher="local"` in the API.

To force CPU-only Ollama (keeps GPU free for PyTorch):
```bash
CUDA_VISIBLE_DEVICES=-1 ollama serve   # terminal 1
make ml-research-local-torch            # terminal 2
```

---

## sklearn mode (default)

You are editing `train.py` — the only mutable file in this mode.

### Allowed edits

- `MODEL_PARAMS` — any hyperparameters accepted by scikit-learn estimators.
- `build_model()` — swap to any scikit-learn classifier (RandomForest,
  LogisticRegression, GradientBoosting, stacking ensembles, etc.).
- `USE_VOCAB` / `MAX_VOCAB` — toggle bag-of-words features from question text.
- Feature engineering inside `train()` — you may add derived features, apply
  transforms (StandardScaler, QuantileTransformer), or combine features, as
  long as you call `extract_matrix()` to get the base features.
- Ensemble multiple models and blend their probabilities.
- Calibrate with `sklearn.calibration.CalibratedClassifierCV`.

### Forbidden edits

- Do NOT change the `train()` function signature.
- Do NOT remove the `brier: <float>` print statement.
- Do NOT change imports from sibling modules (`dataset`, `features`, `evaluate`).
- Do NOT add dependencies beyond scikit-learn and numpy.
- Do NOT use information from the validation set during training (no leakage).
- Do NOT read or write files other than through the provided API.

### Strategy hints

1. Start with hyperparameter tuning — `learning_rate`, `max_depth`, `max_iter`.
2. Try enabling bag-of-words features (`USE_VOCAB = True`).
3. Experiment with `CalibratedClassifierCV` for better probability calibration.
4. Try stacking: train a meta-model on out-of-fold predictions.
5. The implied_prob feature already contains strong market signal — models that
   learn to correct market mispricing will outperform.
6. Watch for overfitting on small datasets; prefer regularization.

---

## torch mode (PyTorch / RTX 3050)

You are editing `torch_train.py` — the only mutable file in this mode.

### Available architectures (from `models.py`)

- **TinyForecaster** — configurable MLP (hidden, depth, dropout).
- **TinyTransformerForecaster** — 2-layer transformer encoder on tabular features
  (d_model, n_heads, n_layers, dropout).

All architectures enforce hard caps: hidden <= 128, depth <= 4, batch <= 512.

### Allowed edits

- `MODEL_PARAMS` — hidden size, depth, dropout, etc.
- `LR`, `WEIGHT_DECAY`, `BATCH_SIZE`, `MAX_EPOCHS`, `TIME_BUDGET`.
- `USE_VOCAB` / `MAX_VOCAB` — toggle bag-of-words features.
- `build_model()` — swap between TinyForecaster and TinyTransformerForecaster,
  or adjust their constructor arguments.
- Add learning-rate schedulers (CosineAnnealingLR, OneCycleLR, etc.).
- Add gradient clipping, label smoothing, or mixup augmentation.
- Add early stopping with patience.
- Change the loss function (focal loss, log-loss, etc.) as long as Brier is
  still the reported metric.
- Feature engineering inside `train()` — derived features, normalization, etc.

### Forbidden edits

- Do NOT change the `train()` function signature.
- Do NOT remove the `brier:`, `training_seconds:`, or `peak_vram_mb:` print
  statements.
- Do NOT change imports from sibling modules (`dataset`, `features`, `evaluate`,
  `models`).
- Do NOT add dependencies beyond torch, numpy, and sklearn.
- Do NOT use information from the validation set during training (no leakage).
- Do NOT exceed VRAM budget: keep hidden <= 128, depth <= 4, batch <= 512.

### Strategy hints

1. Start with the default MLP and tune LR + weight_decay.
2. Try CosineAnnealingLR or OneCycleLR for better convergence.
3. Enable bag-of-words (`USE_VOCAB = True`) — the transformer handles sparse
   features naturally.
4. Try TinyTransformerForecaster — it can learn feature interactions that an
   MLP misses.
5. Add dropout (0.1–0.3) and weight decay (1e-4 to 1e-2) to prevent
   overfitting on small datasets.
6. Use gradient clipping (`torch.nn.utils.clip_grad_norm_`) if training is
   unstable.
7. The implied_prob feature is the strongest signal — the model should learn
   residual corrections on top of it.
8. Monitor peak_vram_mb; if it exceeds 3500 MB, reduce batch size or hidden.

---

## Evaluation

The runner parses `brier: <float>` from stdout.  If the Brier score improves
over the current best **and** passes all promotion gates, the model is saved
as a new artifact and promoted.  If it regresses or any gate fails, the
training file is reverted to its previous version.

Each sklearn iteration must complete in under 120 seconds.
Each torch iteration must complete in under 300 seconds (5 minutes).

### Available metrics (from `evaluate.py`)

| Function              | Returns                                         |
|-----------------------|-------------------------------------------------|
| `brier_score`         | float — primary optimization target             |
| `log_loss`            | float — secondary quality signal                |
| `calibration_error`   | float — ECE, gated at 0.15                      |
| `calibration_buckets` | list[dict] — reliability diagram data            |
| `edge_backtest`       | dict — model vs market Brier, lift, mean edge   |
| `simulated_pnl`       | dict — PnL, trades, win_rate, drawdown, ROI     |
| `promotion_score`     | dict — composite + gates + all sub-metrics      |
