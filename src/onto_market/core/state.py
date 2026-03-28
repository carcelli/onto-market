"""Core state definitions for LangGraph agents."""
from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """The base state for all agents."""
    messages: Annotated[list[BaseMessage], add_messages]
    query: str
    markets: list[dict]
    forecast_prob: float
    trade_decision: dict
    error: str | None
