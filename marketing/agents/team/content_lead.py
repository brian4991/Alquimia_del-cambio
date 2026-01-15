"""
Content Lead Agent.

Develops narrative structure and storytelling.
"""

from typing import Optional, Dict, Any

from marketing.agents.base.base_agent import BaseAgent
from marketing.domain.entities.agent_response import AgentResponse


class ContentLeadAgent(BaseAgent):
    """
    Content Lead Agent.
    
    Responsible for:
    - Developing narrative structure
    - Creating content series
    - Defining themes and angles
    - Ensuring emotional connection through storytelling
    """
    
    @property
    def role(self) -> str:
        return "content_lead"
    
    async def process(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Process a content task.
        
        Args:
            task: Task description.
            context: Additional context.
            
        Returns:
            Content proposal.
        """
        agent_context = context or await self._get_context(task)
        
        prompt = f"""Como Content Lead del equipo, desarrolla una propuesta de contenido para:

**Tarea:**
{task}

Responde con:
1. **Concepto narrativo**: La historia o ángulo principal
2. **Estructura propuesta**: Cómo organizar el contenido
3. **Temas a abordar**: Puntos clave a comunicar
4. **Conexión emocional**: Cómo conectar con la audiencia
5. **Serie/continuidad**: Si aplica, cómo extender el contenido
6. **Nivel de acuerdo**: (1-10) si es una propuesta existente

Asegúrate de que el contenido sea auténtico y alineado con el estilo de Nicole."""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="proposal",
            confidence=0.85,
            agreement_level=self._parse_agreement_level(response_text),
            suggestions=self._extract_suggestions(response_text),
        )
    
    async def critique(
        self,
        proposal: str,
        proposer: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Critique a proposal from content perspective.
        
        Args:
            proposal: Proposal to critique.
            proposer: Role of proposer.
            context: Additional context.
            
        Returns:
            Content critique.
        """
        agent_context = context or await self._get_context(proposal)
        
        prompt = f"""Como Content Lead, evalúa la siguiente propuesta de {proposer}:

**Propuesta:**
{proposal}

Evalúa desde la perspectiva de contenido:
1. **Narrativa**: ¿La historia es compelling?
2. **Estructura**: ¿Está bien organizado?
3. **Valor**: ¿Aporta valor a la audiencia?
4. **Autenticidad**: ¿Suena auténtico para Nicole?
5. **Mejoras sugeridas**: ¿Cómo mejorar el storytelling?
6. **Nivel de acuerdo**: (1-10)

Sé constructivo y enfócate en el impacto narrativo."""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="critique",
            confidence=0.8,
            agreement_level=self._parse_agreement_level(response_text),
            suggestions=self._extract_suggestions(response_text),
        )
    
    async def develop_content_series(
        self,
        topic: str,
        num_pieces: int = 5,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Develop a content series on a topic.
        
        Args:
            topic: Main topic.
            num_pieces: Number of content pieces.
            context: Additional context.
            
        Returns:
            Content series proposal.
        """
        agent_context = context or await self._get_context(topic)
        
        prompt = f"""Desarrolla una serie de {num_pieces} piezas de contenido sobre:

**Tema principal:**
{topic}

Para cada pieza, proporciona:
1. **Título/Concepto**
2. **Ángulo específico**
3. **Formato sugerido** (post, reel, carousel, etc.)
4. **Hook principal**
5. **Mensaje clave**
6. **Conexión con la siguiente pieza**

La serie debe:
- Tener un arco narrativo coherente
- Ir de lo general a lo específico
- Incluir variedad de formatos
- Terminar con un CTA hacia el programa o retiro

Asegúrate de que cada pieza pueda funcionar sola pero también como parte de la serie."""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="content_series",
            confidence=0.85,
        )
