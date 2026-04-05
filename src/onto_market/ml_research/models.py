"""PyTorch model architectures for Polymarket probability forecasting.

All models are sized for RTX 3050 (4-6 GB VRAM).  Hard caps prevent the
autoresearch loop from proposing architectures that OOM the card.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any

try:
    import torch
    import torch.nn as nn

    _TORCH_AVAILABLE = True
except ImportError:
    _TORCH_AVAILABLE = False

# ── Hard caps (RTX 3050 safe) ────────────────────────────────────────────

MAX_HIDDEN = 128
MAX_DEPTH = 4
MAX_BATCH = 512
MAX_VRAM_MB = 3500  # leaves ~1 GB headroom on a 4-6 GB card


def _clamp(value: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, value))


# ── Device helper ────────────────────────────────────────────────────────


@dataclass
class DeviceConfig:
    """Auto-detect CUDA and enforce VRAM budget."""

    device: str = field(init=False)
    dtype: Any = field(init=False)
    max_vram_mb: int = MAX_VRAM_MB

    def __post_init__(self) -> None:
        if not _TORCH_AVAILABLE:
            raise RuntimeError("PyTorch is not installed — pip install -e '.[torch]'")
        if torch.cuda.is_available():
            self.device = "cuda"
            self.dtype = torch.float32
        else:
            self.device = "cpu"
            self.dtype = torch.float32

    def peak_vram_mb(self) -> float:
        if self.device != "cuda":
            return 0.0
        return torch.cuda.max_memory_allocated() / (1024 * 1024)

    def reset_peak(self) -> None:
        if self.device == "cuda":
            torch.cuda.reset_peak_memory_stats()

    def check_vram(self) -> bool:
        """Return True if peak VRAM is within budget."""
        return self.peak_vram_mb() <= self.max_vram_mb


# ── TinyForecaster (MLP) ────────────────────────────────────────────────


def _require_torch() -> None:
    if not _TORCH_AVAILABLE:
        raise RuntimeError("PyTorch is not installed — pip install -e '.[torch]'")


class TinyForecaster(nn.Module):
    """Configurable MLP for binary probability prediction.

    Parameters are clamped to RTX 3050–safe maximums regardless of what
    the autoresearch loop proposes.
    """

    _onto_market_feature_names: list[str]
    _onto_market_category_map: dict[str, int]
    _onto_market_vocab: list[str]
    _onto_market_hyperparams: dict[str, Any]

    def __init__(
        self,
        n_features: int,
        hidden: int = 64,
        depth: int = 2,
        dropout: float = 0.1,
    ) -> None:
        _require_torch()
        super().__init__()

        hidden = _clamp(hidden, 8, MAX_HIDDEN)
        depth = _clamp(depth, 1, MAX_DEPTH)
        dropout = max(0.0, min(0.5, dropout))

        layers: list[nn.Module] = [nn.Linear(n_features, hidden), nn.ReLU()]
        if dropout > 0:
            layers.append(nn.Dropout(dropout))

        for _ in range(depth - 1):
            layers.extend([nn.Linear(hidden, hidden), nn.ReLU()])
            if dropout > 0:
                layers.append(nn.Dropout(dropout))

        layers.extend([nn.Linear(hidden, 1), nn.Sigmoid()])
        self.net = nn.Sequential(*layers)

        self._n_features = n_features
        self._hidden = hidden
        self._depth = depth
        self._dropout = dropout

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x).squeeze(-1)

    def hyperparams(self) -> dict[str, Any]:
        return {
            "architecture": "MLP",
            "n_features": self._n_features,
            "hidden": self._hidden,
            "depth": self._depth,
            "dropout": self._dropout,
        }


# ── TinyTransformerForecaster ────────────────────────────────────────────


class TinyTransformerForecaster(nn.Module):
    """2-layer transformer encoder on tabular features.

    Each feature becomes a token via a learned embedding projection.
    A [CLS]-style readout token aggregates context for the final prediction.
    """

    _onto_market_feature_names: list[str]
    _onto_market_category_map: dict[str, int]
    _onto_market_vocab: list[str]
    _onto_market_hyperparams: dict[str, Any]

    def __init__(
        self,
        n_features: int,
        d_model: int = 32,
        n_heads: int = 2,
        n_layers: int = 2,
        dropout: float = 0.1,
    ) -> None:
        _require_torch()
        super().__init__()

        d_model = _clamp(d_model, 8, MAX_HIDDEN)
        n_layers = _clamp(n_layers, 1, MAX_DEPTH)
        n_heads = _clamp(n_heads, 1, d_model)
        # n_heads must divide d_model
        while d_model % n_heads != 0 and n_heads > 1:
            n_heads -= 1
        dropout = max(0.0, min(0.5, dropout))

        self.feature_proj = nn.Linear(1, d_model)
        self.cls_token = nn.Parameter(torch.randn(1, 1, d_model) * 0.02)
        self.pos_embed = nn.Parameter(
            torch.randn(1, n_features + 1, d_model) * 0.02
        )

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=n_heads,
            dim_feedforward=d_model * 2,
            dropout=dropout,
            batch_first=True,
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)
        self.head = nn.Sequential(
            nn.Linear(d_model, 1),
            nn.Sigmoid(),
        )

        self._n_features = n_features
        self._d_model = d_model
        self._n_heads = n_heads
        self._n_layers = n_layers
        self._dropout = dropout

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        bsz = x.size(0)
        # (bsz, n_features) -> (bsz, n_features, 1) -> (bsz, n_features, d_model)
        tokens = self.feature_proj(x.unsqueeze(-1))
        cls = self.cls_token.expand(bsz, -1, -1)
        tokens = torch.cat([cls, tokens], dim=1)

        seq_len = tokens.size(1)
        tokens = tokens + self.pos_embed[:, :seq_len, :]

        encoded = self.encoder(tokens)
        cls_out = encoded[:, 0, :]
        return self.head(cls_out).squeeze(-1)

    def hyperparams(self) -> dict[str, Any]:
        return {
            "architecture": "Transformer",
            "n_features": self._n_features,
            "d_model": self._d_model,
            "n_heads": self._n_heads,
            "n_layers": self._n_layers,
            "dropout": self._dropout,
        }
