"""
Community Manager Agent.

Optimizes timing, engagement, and platform adaptation.
"""

from typing import Optional, Dict, Any

from marketing.agents.base.base_agent import BaseAgent
from marketing.domain.entities.agent_response import AgentResponse


class CommunityManagerAgent(BaseAgent):
    """
    Community Manager Agent.
    
    Responsible for:
    - Optimizing publication timing
    - Adapting content per platform
    - Suggesting engagement strategies
    - Planning publication frequency
    """
    
    @property
    def role(self) -> str:
        return "community_manager"
    
    async def process(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Process a community management task.
        
        Args:
            task: Task description.
            context: Additional context.
            
        Returns:
            CM proposal.
        """
        agent_context = context or await self._get_context(task)
        
        prompt = f"""Como Community Manager del equipo, analiza y proporciona recomendaciones para:

**Tarea:**
{task}

Responde con:
1. **Timing óptimo**: Mejor día y hora para publicar
2. **Adaptación por plataforma**: Cómo ajustar para cada red
3. **Estrategia de engagement**: Cómo fomentar interacción
4. **Hashtags recomendados**: 3-5 hashtags relevantes
5. **Formato sugerido**: El mejor formato para el contenido
6. **Nivel de acuerdo**: (1-10) si es una propuesta existente

Considera la audiencia hispanohablante (México, Colombia, España)."""

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
        Critique a proposal from CM perspective.
        
        Args:
            proposal: Proposal to critique.
            proposer: Role of proposer.
            context: Additional context.
            
        Returns:
            CM critique.
        """
        agent_context = context or await self._get_context(proposal)
        
        prompt = f"""Como Community Manager, evalúa la siguiente propuesta de {proposer}:

**Propuesta:**
{proposal}

Evalúa desde la perspectiva de comunidad y plataformas:
1. **Viralidad potencial**: ¿Tiene potencial de compartirse?
2. **Engagement esperado**: ¿Generará interacción?
3. **Adecuación a plataforma**: ¿Es óptimo para las redes?
4. **Timing**: ¿Es buen momento para este contenido?
5. **Mejoras de engagement sugeridas**
6. **Nivel de acuerdo**: (1-10)

Sé práctico y basado en tendencias actuales."""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="critique",
            confidence=0.8,
            agreement_level=self._parse_agreement_level(response_text),
            suggestions=self._extract_suggestions(response_text),
        )
    
    async def suggest_posting_schedule(
        self,
        content_pieces: int,
        period_days: int,
        platforms: list[str],
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Suggest optimal posting schedule.
        
        Args:
            content_pieces: Number of content pieces.
            period_days: Period in days.
            platforms: Target platforms.
            context: Additional context.
            
        Returns:
            Schedule proposal.
        """
        agent_context = context or await self._get_context("posting schedule")
        
        prompt = f"""Crea un calendario de publicación óptimo:

**Parámetros:**
- Piezas de contenido: {content_pieces}
- Período: {period_days} días
- Plataformas: {', '.join(platforms)}

**Audiencia:** Mujeres hispanohablantes 25-50 años
- México/Colombia: GMT-5/-6
- España: GMT+1

Genera un calendario que incluya:

1. **Distribución semanal**
   - Qué días publicar
   - Cuántos posts por día

2. **Horarios óptimos por plataforma**
   - Instagram: mejor hora
   - TikTok: mejor hora
   - YouTube: mejor hora
   - LinkedIn: mejor hora
   - Facebook: mejor hora

3. **Alternancia de formatos**
   - Posts estáticos
   - Reels/Videos
   - Stories
   - Carousels

4. **Consideraciones especiales**
   - Días a evitar
   - Momentos de alto engagement
   - Tendencias actuales

5. **Propuesta de calendario**
   - Día 1: [plataforma] [hora] [formato]
   - Día 2: ...
   (para todo el período)"""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="schedule",
            confidence=0.85,
        )
