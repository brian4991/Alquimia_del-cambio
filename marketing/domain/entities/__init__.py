"""Domain entities - Value objects and state structures."""

from marketing.domain.entities.agent_response import AgentResponse
from marketing.domain.entities.debate_state import DebateState, DebateRound
from marketing.domain.entities.meeting_result import MeetingResult, ProposedOption

__all__ = [
    "AgentResponse",
    "DebateState",
    "DebateRound",
    "MeetingResult",
    "ProposedOption",
]
