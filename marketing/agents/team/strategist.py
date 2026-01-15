"""
Strategist Agent.

Defines marketing strategies and objectives.
"""

from typing import Optional, Dict, Any

from marketing.agents.base.base_agent import BaseAgent
from marketing.domain.entities.agent_response import AgentResponse


class StrategistAgent(BaseAgent):
    """
    Marketing Strategist Agent.
    
    Responsible for:
    - Defining short/medium/long term strategies
    - Setting objectives and KPIs
    - Identifying market opportunities
    - Aligning actions with business goals
    """
    
    @property
    def role(self) -> str:
        return "strategist"
    
    async def process(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Process a strategic task.
        
        Args:
            task: Task description.
            context: Additional context.
            
        Returns:
            Strategic proposal.
        """
        agent_context = context or await self._get_context(task)
        
        prompt = f"""Como Estratega del equipo, analiza la siguiente tarea y proporciona tu perspectiva estratégica:

**Tarea:**
{task}

Responde con:
1. **Análisis estratégico**: Tu evaluación de la situación
2. **Objetivos propuestos**: Qué deberíamos lograr
3. **Enfoque recomendado**: Cómo abordar esto estratégicamente
4. **KPIs sugeridos**: Cómo medir el éxito
5. **Nivel de acuerdo**: (1-10) si es una propuesta existente

Mantén un enfoque práctico y alineado con los objetivos del negocio de Nicole."""

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
        Critique a proposal from strategic perspective.
        
        Args:
            proposal: Proposal to critique.
            proposer: Role of proposer.
            context: Additional context.
            
        Returns:
            Strategic critique.
        """
        agent_context = context or await self._get_context(proposal)
        
        prompt = f"""Como Estratega, evalúa la siguiente propuesta de {proposer}:

**Propuesta:**
{proposal}

Evalúa desde una perspectiva estratégica:
1. **Alineación con objetivos**: ¿Se alinea con los objetivos de negocio?
2. **Viabilidad**: ¿Es realista y ejecutable?
3. **ROI potencial**: ¿Qué retorno podemos esperar?
4. **Riesgos**: ¿Qué riesgos identificas?
5. **Mejoras sugeridas**: ¿Cómo se podría mejorar?
6. **Nivel de acuerdo**: (1-10)

Sé constructivo pero riguroso en tu evaluación."""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="critique",
            confidence=0.8,
            agreement_level=self._parse_agreement_level(response_text),
            suggestions=self._extract_suggestions(response_text),
        )
    
    async def generate_strategy(
        self,
        strategy_type: str,
        objectives: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Generate a marketing strategy.
        
        Args:
            strategy_type: Type (short, medium, long).
            objectives: Business objectives.
            context: Additional context.
            
        Returns:
            Strategy proposal.
        """
        periods = {
            "short": "1-2 semanas",
            "medium": "1-3 meses",
            "long": "6-12 meses",
        }
        period = periods.get(strategy_type, "1-3 meses")
        
        agent_context = context or await self._get_context(objectives)
        
        prompt = f"""Genera una estrategia de marketing a {strategy_type} plazo ({period}) para Nicole Ramirez PsiCoach.

**Objetivos de negocio:**
{objectives}

**Contexto del negocio:**
- Programa "Alquimia del Cambio": ~600€, evergreen con promos puntuales
- Retiros trimestrales: ~150€, ~20 participantes
- Audiencia: Mujeres 25-50 años hispanohablantes

Desarrolla una estrategia completa que incluya:

1. **Título de la estrategia**
2. **Objetivos específicos** (SMART)
3. **Pilares de contenido** (3-5 temas principales)
4. **Mensajes clave** (lo que queremos comunicar)
5. **Métricas objetivo** (KPIs concretos)
6. **Campañas propuestas** (si aplica)
7. **Calendario de alto nivel**
8. **Recursos necesarios**

Sé específico y actionable."""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="strategy",
            confidence=0.9,
        )
