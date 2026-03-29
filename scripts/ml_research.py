#!/usr/bin/env python
"""Launch the autoresearch experiment loop."""
import argparse

from rich.console import Console

from onto_market.ml_research.runner import run_experiment_loop

console = Console()


def main():
    parser = argparse.ArgumentParser(description="Run autoresearch experiment loop")
    parser.add_argument("--iterations", type=int, default=10)
    parser.add_argument("--db-path", type=str, default=None)
    parser.add_argument("--artifact-dir", type=str, default="data/ml_artifacts")
    args = parser.parse_args()

    console.print(f"[bold cyan]Starting autoresearch loop ({args.iterations} iterations)...[/]")

    result = run_experiment_loop(
        max_iterations=args.iterations,
        db_path=args.db_path,
        artifact_dir=args.artifact_dir,
    )

    console.print(f"\n[bold green]=== Autoresearch Complete ===[/]")
    console.print(f"  Iterations:   {result['iterations']}")
    console.print(f"  Improvements: {result['improvements']}")
    console.print(f"  Best Brier:   {result['best_brier']}")
    console.print(f"  Best Version: v{result.get('best_version', 0):03d}")


if __name__ == "__main__":
    main()
