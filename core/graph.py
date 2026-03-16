"""Graph registry and common orchestration logic."""
from typing import Any, Callable

from langgraph.graph import StateGraph

_graphs: dict[str, Callable[[], Any]] = {}


def register_graph(name: str):
    """Decorator to register a graph factory function."""
    def decorator(func: Callable[[], Any]):
        _graphs[name] = func
        return func
    return decorator


def get_graph(name: str) -> Any:
    """Instantiate a graph by name."""
    if name not in _graphs:
        raise ValueError(f"Graph '{name}' not found in registry")
    return _graphs[name]()


def list_graphs() -> list[str]:
    """List all registered graphs."""
    return list(_graphs.keys())
