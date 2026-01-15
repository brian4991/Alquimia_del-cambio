"""
Debate Manager.

Manages the debate cycles between agents.
"""

from typing import Optional, Dict, Any, List
import asyncio

from marketing.domain.entities.debate_state import DebateState, DebateRound
from marketing.domain.entities.agent_response import AgentResponse
from marketing.agents.team import (
    StrategistAgent,
    ContentLeadAgent,
    CreativeDirectorAgent,
    CommunityManagerAgent,
    AnalystAgent,
    CopywriterAgent,
    BrandGuardianAgent,
)
from marketing.agents.base.agent_memory import AgentMemory, get_agent_memory


class DebateManager:
    """
    Manages debate cycles between marketing agents.
    
    Coordinates agent contributions, tracks consensus,
    and determines when to conclude debates.
    """
    
    def __init__(self, memory: Optional[AgentMemory] = None) -> None:
        """
        Initialize debate manager.
        
        Args:
            memory: Shared agent memory.
        """
        self._memory = memory or get_agent_memory()
        
        # Initialize all team agents
        self._agents = {
            "strategist": StrategistAgent(memory=self._memory),
            "content_lead": ContentLeadAgent(memory=self._memory),
            "creative_director": CreativeDirectorAgent(memory=self._memory),
            "community_manager": CommunityManagerAgent(memory=self._memory),
            "analyst": AnalystAgent(memory=self._memory),
            "copywriter": CopywriterAgent(memory=self._memory),
            "brand_guardian": BrandGuardianAgent(memory=self._memory),
        }
    
    async def run_debate_round(
        self,
        debate_state: DebateState,
        context: Optional[Dict[str, Any]] = None
    ) -> DebateRound:
        """
        Run a single round of debate.
        
        Args:
            debate_state: Current debate state.
            context: Additional context.
            
        Returns:
            Completed debate round.
        """
        # Start new round
        current_round = debate_state.start_new_round()
        
        # Determine which agents should participate based on meeting type
        participating_agents = self._get_participating_agents(debate_state.meeting_type)
        
        # Collect contributions from all agents
        # Run in parallel for efficiency
        tasks = []
        for agent_role in participating_agents:
            agent = self._agents.get(agent_role)
            if agent:
                if debate_state.current_round == 1:
                    # First round: process the initial brief
                    tasks.append(self._get_agent_proposal(
                        agent, debate_state.brief, context
                    ))
                else:
                    # Subsequent rounds: critique previous proposals
                    tasks.append(self._get_agent_critique(
                        agent, debate_state, context
                    ))
        
        # Wait for all agents
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Add valid responses to the round
        for response in responses:
            if isinstance(response, AgentResponse):
                debate_state.add_contribution(response)
        
        # Check for consensus
        debate_state.check_consensus()
        
        # Extract key points and divergences
        current_round.key_points = self._extract_key_points(current_round.contributions)
        current_round.divergences = self._extract_divergences(current_round.contributions)
        
        return current_round
    
    def _get_participating_agents(self, meeting_type: str) -> List[str]:
        """
        Get list of agents that should participate based on meeting type.
        
        Args:
            meeting_type: Type of meeting.
            
        Returns:
            List of agent roles.
        """
        # All agents participate in all meetings, but with different weights
        all_agents = [
            "strategist",
            "content_lead",
            "creative_director",
            "community_manager",
            "analyst",
            "copywriter",
            "brand_guardian",
        ]
        
        # Prioritize certain agents based on meeting type
        priority_map = {
            "brainstorm": ["content_lead", "copywriter", "creative_director"],
            "review": ["brand_guardian", "analyst", "copywriter"],
            "planning": ["strategist", "community_manager", "analyst"],
        }
        
        priority = priority_map.get(meeting_type, [])
        
        # Reorder to put priority agents first
        ordered = priority + [a for a in all_agents if a not in priority]
        
        return ordered
    
    async def _get_agent_proposal(
        self,
        agent,
        brief: str,
        context: Optional[Dict[str, Any]]
    ) -> AgentResponse:
        """
        Get initial proposal from an agent.
        
        Args:
            agent: Agent instance.
            brief: Meeting brief.
            context: Additional context.
            
        Returns:
            Agent's proposal.
        """
        try:
            return await agent.process(brief, context)
        except Exception as e:
            return AgentResponse(
                agent_role=agent.role,
                content=f"Error al procesar: {str(e)}",
                response_type="error",
                confidence=0.0,
            )
    
    async def _get_agent_critique(
        self,
        agent,
        debate_state: DebateState,
        context: Optional[Dict[str, Any]]
    ) -> AgentResponse:
        """
        Get critique from an agent on previous proposals.
        
        Args:
            agent: Agent instance.
            debate_state: Current debate state.
            context: Additional context.
            
        Returns:
            Agent's critique.
        """
        try:
            # Get the most recent proposal to critique
            # (from the previous round, not from the same agent)
            previous_round = debate_state.rounds[-2] if len(debate_state.rounds) > 1 else debate_state.rounds[-1]
            
            # Find a proposal from a different agent
            proposal_to_critique = None
            proposer = None
            
            for contrib in previous_round.contributions:
                if contrib.agent_role != agent.role and contrib.response_type == "proposal":
                    proposal_to_critique = contrib.content
                    proposer = contrib.agent_role
                    break
            
            if proposal_to_critique:
                return await agent.critique(proposal_to_critique, proposer, context)
            else:
                # If no proposal found, process the original brief
                return await agent.process(debate_state.brief, context)
                
        except Exception as e:
            return AgentResponse(
                agent_role=agent.role,
                content=f"Error al criticar: {str(e)}",
                response_type="error",
                confidence=0.0,
            )
    
    def _extract_key_points(self, contributions: List[AgentResponse]) -> List[str]:
        """
        Extract key points from contributions.
        
        Args:
            contributions: List of agent responses.
            
        Returns:
            List of key points.
        """
        key_points = []
        
        for contrib in contributions:
            # Look for high-confidence suggestions
            if contrib.confidence >= 0.8:
                # Extract first sentence as key point
                first_sentence = contrib.content.split('.')[0]
                if len(first_sentence) > 20:
                    key_points.append(f"{contrib.agent_role}: {first_sentence}")
            
            # Add explicit suggestions
            for suggestion in contrib.suggestions[:2]:
                key_points.append(f"{contrib.agent_role} sugiere: {suggestion}")
        
        return key_points[:10]  # Limit to 10 key points
    
    def _extract_divergences(self, contributions: List[AgentResponse]) -> List[str]:
        """
        Extract points of divergence from contributions.
        
        Args:
            contributions: List of agent responses.
            
        Returns:
            List of divergence points.
        """
        divergences = []
        
        # Find low agreement levels
        low_agreement = [c for c in contributions if c.agreement_level and c.agreement_level < 6]
        
        for contrib in low_agreement:
            divergences.append(
                f"{contrib.agent_role} tiene reservas (nivel {contrib.agreement_level}/10)"
            )
        
        # Add concerns
        for contrib in contributions:
            for concern in contrib.concerns[:2]:
                divergences.append(f"{contrib.agent_role}: {concern}")
        
        return divergences[:5]  # Limit to 5 divergences
    
    async def run_full_debate(
        self,
        meeting_type: str,
        brief: str,
        max_rounds: int = 3,
        context: Optional[Dict[str, Any]] = None
    ) -> DebateState:
        """
        Run a complete debate until consensus or max rounds.
        
        Args:
            meeting_type: Type of meeting.
            brief: Initial brief.
            max_rounds: Maximum debate rounds.
            context: Additional context.
            
        Returns:
            Final debate state.
        """
        debate_state = DebateState(
            meeting_type=meeting_type,
            brief=brief,
            max_rounds=max_rounds,
        )
        
        # Add context if provided
        if context:
            debate_state.voice_profile_summary = context.get("voice_profile")
            debate_state.active_strategy_summary = context.get("strategies")
            debate_state.additional_context = context
        
        # Run debate rounds
        while not debate_state.should_conclude():
            await self.run_debate_round(debate_state, context)
        
        # Set final status
        if debate_state.status != "consensus":
            debate_state.status = "needs_decision"
        
        return debate_state
