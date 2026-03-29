#!/usr/bin/env python
"""Print current ML artifact status."""
import argparse

from onto_market.ml_research.artifacts import status


def main():
    parser = argparse.ArgumentParser(description="Show ML artifact status")
    parser.add_argument("--artifact-dir", type=str, default="data/ml_artifacts")
    args = parser.parse_args()

    print(status(artifact_dir=args.artifact_dir))


if __name__ == "__main__":
    main()
