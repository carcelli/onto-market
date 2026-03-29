#!/usr/bin/env python
"""Single PyTorch training run — trains a model and saves the artifact."""
import argparse
import sys

from rich.console import Console

from onto_market.ml_research.artifacts import promote, save_artifact

console = Console()


def main():
    parser = argparse.ArgumentParser(description="Train PyTorch forecaster on resolved markets")
    parser.add_argument("--db-path", type=str, default=None)
    parser.add_argument("--artifact-dir", type=str, default="data/ml_artifacts")
    args = parser.parse_args()

    console.print("[bold cyan]Training PyTorch forecaster...[/]")

    from onto_market.ml_research.torch_train import train

    model, brier = train(db_path=args.db_path)

    if model is None:
        console.print("[bold red]Training failed — not enough data.[/]")
        sys.exit(1)

    version = save_artifact(
        model,
        {"brier": brier, "model_type": "torch"},
        artifact_dir=args.artifact_dir,
    )
    promote(version, artifact_dir=args.artifact_dir)
    console.print(f"[bold green]Done — v{version:03d} saved (Brier={brier:.6f})[/]")


if __name__ == "__main__":
    main()
