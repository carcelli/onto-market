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
    memory_context: list[dict]    # markets from local DB
    live_data: list[dict]         # markets from Gamma API (if enriched)
    analysis: str
    decision: dict
    error: str | None


class PlanningState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    query: str
    market_data: list[dict]
    research_context: str
    ontology_context: str           # structured prior knowledge from OntologyGraph
    implied_probability: float
    estimated_probability: float
    edge: float
    expected_value: float
    kelly_fraction: float
    recommendation: dict
    error: str | None
