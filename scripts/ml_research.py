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
    parser.add_argument("--mode", type=str, choices=["sklearn", "torch"], default="sklearn")
    parser.add_argument("--timeout", type=int, default=None)
    parser.add_argument(
        "--researcher", type=str, default=None,
        help=(
            "Researcher LLM spec. 'local' = Ollama on CPU/RAM (keeps GPU "
            "free for training). 'local/qwen2:7b' = specific Ollama model."
        ),
    )
    args = parser.parse_args()

    researcher_label = args.researcher or "default"
    console.print(
        f"[bold cyan]Starting autoresearch loop "
        f"[{args.mode}] ({args.iterations} iterations) "
        f"researcher={researcher_label}...[/]"
    )

    result = run_experiment_loop(
        max_iterations=args.iterations,
        db_path=args.db_path,
        artifact_dir=args.artifact_dir,
        mode=args.mode,
        timeout=args.timeout,
        researcher=args.researcher,
    )

    console.print(f"\n[bold green]=== Autoresearch Complete ===[/]")
    console.print(f"  Mode:         {result['mode']}")
    console.print(f"  Researcher:   {researcher_label}")
    console.print(f"  Iterations:   {result['iterations']}")
    console.print(f"  Improvements: {result['improvements']}")
    console.print(f"  Best Brier:   {result['best_brier']}")
    console.print(f"  Best Version: v{result.get('best_version', 0):03d}")


if __name__ == "__main__":
    main()
