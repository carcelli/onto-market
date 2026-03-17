"""Shared LangGraph state definitions."""
from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    markets: list[dict]
    forecast_prob: float
    trade_decision: dict
    error: str | None


class MemoryAgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    query: str
    memory_context: list[dict]
    live_data: list[dict]
    analysis: str
    decision: dict
    error: str | None


class PlanningState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    query: str
    market_data: list[dict]
    research_context: str
    ontology_context: str
    implied_probability: float
    estimated_probability: float
    # Swarm consensus fields (populated by swarm_node)
    swarm_consensus: float
    swarm_confidence: float
    swarm_dissent: float
    # Scoring
    edge: float
    expected_value: float
    kelly_fraction: float
    recommendation: dict
    # Trading (populated by trade_node)
    trade_result: dict
    error: str | None
