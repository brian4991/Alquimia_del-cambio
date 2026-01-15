"""
Analyst Agent.

Provides data-driven evaluation and optimization suggestions.
"""

from typing import Optional, Dict, Any

from marketing.agents.base.base_agent import BaseAgent
from marketing.domain.entities.agent_response import AgentResponse


class AnalystAgent(BaseAgent):
    """
    Analyst Agent.
    
    Responsible for:
    - Evaluating proposals with data-driven approach
    - Suggesting optimizations
    - Identifying risks and opportunities
    - Providing objective perspective
    """
    
    @property
    def role(self) -> str:
        return "analyst"
    
    async def process(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Process an analytical task.
        
        Args:
            task: Task description.
            context: Additional context.
            
        Returns:
            Analytical proposal.
        """
        agent_context = context or await self._get_context(task)
        
        prompt = f"""Como Analista del equipo, evalúa objetivamente:

**Tarea:**
{task}

Responde con:
1. **Análisis de viabilidad**: ¿Es realizable?
2. **ROI estimado**: ¿Qué retorno esperamos?
3. **Riesgos identificados**: ¿Qué puede salir mal?
4. **Oportunidades**: ¿Qué podemos aprovechar?
5. **Métricas a monitorear**: ¿Cómo medimos éxito?
6. **Nivel de acuerdo**: (1-10) si es una propuesta existente

Basa tu análisis en mejores prácticas del sector coaching/psicología online."""

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
        Critique a proposal from analytical perspective.
        
        Args:
            proposal: Proposal to critique.
            proposer: Role of proposer.
            context: Additional context.
            
        Returns:
            Analytical critique.
        """
        agent_context = context or await self._get_context(proposal)
        
        prompt = f"""Como Analista, evalúa objetivamente la propuesta de {proposer}:

**Propuesta:**
{proposal}

Evalúa con enfoque data-driven:
1. **Factibilidad**: ¿Es ejecutable con los recursos disponibles?
2. **Efectividad esperada**: ¿Qué resultados podemos esperar?
3. **Costo-beneficio**: ¿Vale la pena el esfuerzo?
4. **Benchmarks**: ¿Cómo se compara con estándares del sector?
5. **Optimizaciones sugeridas**: ¿Cómo mejorar el ROI?
6. **Nivel de acuerdo**: (1-10)

Sé objetivo y constructivo. Usa datos y benchmarks cuando sea posible."""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="critique",
            confidence=0.85,
            agreement_level=self._parse_agreement_level(response_text),
            suggestions=self._extract_suggestions(response_text),
        )
    
    async def analyze_content_performance(
        self,
        content_description: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Analyze expected performance of content.
        
        Args:
            content_description: Description of the content.
            context: Additional context.
            
        Returns:
            Performance analysis.
        """
        agent_context = context or await self._get_context(content_description)
        
        prompt = f"""Analiza el rendimiento esperado del siguiente contenido:

**Contenido:**
{content_description}

Proporciona:

1. **Engagement esperado**
   - Likes estimados (rango)
   - Comentarios esperados
   - Shares/guardados potenciales

2. **Alcance potencial**
   - Orgánico vs viral
   - Factores que pueden amplificar

3. **Conversión**
   - Probabilidad de generar leads
   - Probabilidad de ventas directas

4. **Comparación con benchmarks**
   - Sector coaching/psicología
   - Cuentas similares

5. **Factores de riesgo**
   - Qué podría reducir el rendimiento
   - Cómo mitigar

6. **Recomendaciones de optimización**
   - Cambios para mejorar métricas
   - A/B tests sugeridos

7. **Puntuación general**: /10"""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="analysis",
            confidence=0.8,
        )
