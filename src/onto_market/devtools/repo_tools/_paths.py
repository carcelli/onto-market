from __future__ import annotations

from pathlib import Path

PACKAGE_ROOT_HINT = Path(__file__).resolve().parents[4]


def _find_repo_root(start: Path) -> Path | None:
    current = start.expanduser().resolve()
    for candidate in (current, *current.parents):
        if (candidate / "pyproject.toml").exists():
            return candidate
    return None


def resolve_repo_root(root: str | Path | None = None) -> Path:
    if root is None:
        cwd_root = _find_repo_root(Path.cwd())
        if cwd_root is not None:
            return cwd_root

        package_root = _find_repo_root(PACKAGE_ROOT_HINT)
        if package_root is not None:
            return package_root

        return Path.cwd().resolve()
    return Path(root).expanduser().resolve()


def resolve_output_path(root: Path, output_path: str | Path | None, default_name: str) -> Path:
    if output_path is None:
        return root / default_name
    path = Path(output_path).expanduser()
    if path.is_absolute():
        return path
    return root / path
