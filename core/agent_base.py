"""Base abstractions for agents and tools."""
from abc import ABC, abstractmethod
from typing import Any, Protocol

from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph

from core.state import AgentState


class AgentProtocol(Protocol):
    """Protocol for any agent implementation."""

    def compile(self) -> Any:
        ...

    def invoke(self, input: dict, config: dict | None = None) -> dict:
        ...


class BaseAgent(ABC):
    """Abstract base class for building LangGraph agents."""

    def __init__(self, state_schema: type[AgentState] = AgentState):
        self.state_schema = state_schema
        self.graph = StateGraph(state_schema)

    @abstractmethod
    def build_graph(self) -> StateGraph:
        """Define nodes and edges in this method."""
        pass

    def compile(self) -> Any:
        """Compile the graph for use."""
        self.build_graph()
        return self.graph.compile()
