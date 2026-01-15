"""
Base Agent.

Abstract base class for all marketing team agents.
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List

from marketing.services.llm.azure_openai_client import (
    AzureOpenAIClient,
    get_azure_openai_client,
    ChatMessage,
)
from marketing.services.llm.prompt_templates import PromptTemplates
from marketing.agents.base.agent_config import AgentConfig, get_agent_config
from marketing.agents.base.agent_memory import AgentMemory, get_agent_memory
from marketing.domain.entities.agent_response import AgentResponse


class BaseAgent(ABC):
    """
    Abstract base class for all marketing agents.
    
    Provides common functionality for LLM interaction,
    memory access, and response generation.
    """
    
    def __init__(
        self,
        llm_client: Optional[AzureOpenAIClient] = None,
        memory: Optional[AgentMemory] = None,
        config: Optional[AgentConfig] = None,
    ) -> None:
        """
        Initialize base agent.
        
        Args:
            llm_client: Azure OpenAI client.
            memory: Agent memory for RAG and context.
            config: Agent configuration.
        """
        self._llm = llm_client or get_azure_openai_client()
        self._memory = memory or get_agent_memory()
        self._config = config or get_agent_config(self.role)
    
    @property
    @abstractmethod
    def role(self) -> str:
        """
        Agent's role identifier.
        
        Returns:
            Role string (e.g., "strategist", "copywriter").
        """
        pass
    
    @property
    def display_name(self) -> str:
        """
        Human-readable display name.
        
        Returns:
            Display name from config.
        """
        return self._config.display_name
    
    @property
    def system_prompt(self) -> str:
        """
        Agent's system prompt.
        
        Returns:
            System prompt for this agent's role.
        """
        return PromptTemplates.get_agent_system_prompt(self.role)
    
    async def _get_context(self, query: str) -> Dict[str, Any]:
        """
        Get context for the agent.
        
        Args:
            query: Current query/topic.
            
        Returns:
            Context dictionary.
        """
        return await self._memory.get_context_for_agent(
            query=query,
            include_voice=self._config.use_voice_profile,
            include_strategy=self._config.use_strategy_context,
            rag_types=self._config.rag_search_types,
            rag_limit=self._config.rag_results_limit,
        )
    
    def _build_context_message(self, context: Dict[str, Any]) -> str:
        """
        Build context message from context dict.
        
        Args:
            context: Context dictionary.
            
        Returns:
            Formatted context string.
        """
        parts = []
        
        if context.get("voice_profile"):
            parts.append(f"**Perfil de Voz de Nicole:**\n{context['voice_profile']}")
        
        if context.get("strategies"):
            parts.append(f"**Estrategias Activas:**\n{context['strategies']}")
        
        if context.get("relevant_content"):
            parts.append("**Contenido Relevante (RAG):**")
            for item in context["relevant_content"]:
                parts.append(f"- [{item['type']}] {item['content'][:200]}...")
        
        return "\n\n".join(parts)
    
    async def _call_llm(
        self,
        user_message: str,
        context: Optional[Dict[str, Any]] = None,
        additional_system: Optional[str] = None,
    ) -> str:
        """
        Call the LLM with the agent's configuration.
        
        Args:
            user_message: User/task message.
            context: Context to include.
            additional_system: Additional system instructions.
            
        Returns:
            LLM response content.
        """
        messages = [
            ChatMessage(role="system", content=self.system_prompt),
        ]
        
        # Add additional system instructions if provided
        if additional_system:
            messages.append(ChatMessage(role="system", content=additional_system))
        
        # Add context if provided
        if context:
            context_msg = self._build_context_message(context)
            if context_msg:
                messages.append(ChatMessage(role="system", content=f"Contexto:\n{context_msg}"))
        
        # Add user message
        messages.append(ChatMessage(role="user", content=user_message))
        
        response = await self._llm.chat_completion(
            messages=messages,
            temperature=self._config.temperature,
            max_tokens=self._config.max_tokens,
        )
        
        return response.content
    
    @abstractmethod
    async def process(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Process a task and return response.
        
        Args:
            task: Task description or content to process.
            context: Additional context.
            
        Returns:
            Agent's response.
        """
        pass
    
    @abstractmethod
    async def critique(
        self,
        proposal: str,
        proposer: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Critique another agent's proposal.
        
        Args:
            proposal: Proposal to critique.
            proposer: Role of the proposing agent.
            context: Additional context.
            
        Returns:
            Critique response.
        """
        pass
    
    async def respond_to_feedback(
        self,
        original_content: str,
        feedback: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Respond to feedback and iterate on content.
        
        Args:
            original_content: Original content that received feedback.
            feedback: Feedback to address.
            context: Additional context.
            
        Returns:
            Updated response.
        """
        prompt = f"""Se recibió el siguiente feedback sobre tu propuesta anterior:

**Propuesta Original:**
{original_content}

**Feedback:**
{feedback}

Por favor, genera una versión mejorada que aborde el feedback.
Explica brevemente qué cambios hiciste y por qué."""

        agent_context = await self._get_context(original_content) if not context else context
        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="revision",
            confidence=0.8,
            reasoning="Revisión basada en feedback recibido",
        )
    
    def _parse_agreement_level(self, text: str) -> Optional[int]:
        """
        Parse agreement level from response text.
        
        Args:
            text: Response text that may contain agreement level.
            
        Returns:
            Agreement level (1-10) or None.
        """
        import re
        
        # Look for patterns like "nivel de acuerdo: 8" or "8/10"
        patterns = [
            r'nivel de acuerdo[:\s]+(\d+)',
            r'acuerdo[:\s]+(\d+)',
            r'(\d+)\s*/\s*10',
            r'(\d+)\s+de\s+10',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text.lower())
            if match:
                level = int(match.group(1))
                if 1 <= level <= 10:
                    return level
        
        return None
    
    def _extract_suggestions(self, text: str) -> List[str]:
        """
        Extract suggestions from response text.
        
        Args:
            text: Response text.
            
        Returns:
            List of suggestions found.
        """
        suggestions = []
        
        # Look for bullet points or numbered suggestions
        import re
        
        # Match lines starting with -, *, or numbers
        lines = text.split('\n')
        in_suggestions_section = False
        
        for line in lines:
            line = line.strip()
            
            # Check if we're entering a suggestions section
            if any(word in line.lower() for word in ['sugerencia', 'alternativa', 'propongo', 'sugiero']):
                in_suggestions_section = True
            
            # Extract bullet points
            if line.startswith(('-', '*', '•')) or re.match(r'^\d+[\.\)]', line):
                suggestion = re.sub(r'^[-*•\d\.\)]\s*', '', line)
                if suggestion and len(suggestion) > 10:
                    suggestions.append(suggestion)
        
        return suggestions[:5]  # Limit to 5 suggestions
