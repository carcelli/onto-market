# Autoresearch Program — Polymarket Forecaster

## Objective

Minimize **Brier score** on the held-out validation set of resolved Polymarket
binary markets.  Lower is better; 0.25 is the naïve baseline (always predict 0.5).

## What you may change

You are editing `train.py` — the only mutable file in this loop.

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

## Strategy hints

1. Start with hyperparameter tuning — `learning_rate`, `max_depth`, `max_iter`.
2. Try enabling bag-of-words features (`USE_VOCAB = True`).
3. Experiment with `CalibratedClassifierCV` for better probability calibration.
4. Try stacking: train a meta-model on out-of-fold predictions.
5. The implied_prob feature already contains strong market signal — models that
   learn to correct market mispricing will outperform.
6. Watch for overfitting on small datasets; prefer regularization.

## Evaluation

The runner parses `brier: <float>` from stdout.  If the Brier score improves
over the current best, the model is saved as a new artifact and promoted.
If it regresses, `train.py` is reverted to its previous version.

Each iteration must complete in under 120 seconds.
