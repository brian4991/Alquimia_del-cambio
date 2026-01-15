"""
Brand Guardian Agent.

Validates brand consistency and voice alignment.
"""

from typing import Optional, Dict, Any

from marketing.agents.base.base_agent import BaseAgent
from marketing.domain.entities.agent_response import AgentResponse


class BrandGuardianAgent(BaseAgent):
    """
    Brand Guardian Agent.
    
    Responsible for:
    - Validating content alignment with Nicole's voice
    - Ensuring tone consistency
    - Detecting brand deviations
    - Protecting authenticity and credibility
    """
    
    @property
    def role(self) -> str:
        return "brand_guardian"
    
    async def process(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Process a brand validation task.
        
        Args:
            task: Task/content to validate.
            context: Additional context.
            
        Returns:
            Brand validation response.
        """
        agent_context = context or await self._get_context(task)
        
        prompt = f"""Como Guardián de Marca, evalúa el siguiente contenido:

**Contenido a validar:**
{task}

Realiza una validación completa:

1. **Autenticidad** (1-10)
   - ¿Suena como Nicole lo diría?
   - ¿Es genuino o suena artificial?

2. **Tono de marca** (1-10)
   - ¿Es empoderador, cálido, profesional?
   - ¿Evita ser agresivo o manipulador?

3. **Coherencia** (1-10)
   - ¿Es consistente con publicaciones anteriores?
   - ¿Mantiene la esencia de la marca?

4. **Valor aportado** (1-10)
   - ¿Aporta valor real a la audiencia?
   - ¿Educa, inspira o entretiene?

5. **Ética profesional** (1-10)
   - ¿Respeta la ética de psicología?
   - ¿Evita promesas exageradas?

6. **Problemas detectados**
   - Lista de issues específicos

7. **Correcciones sugeridas**
   - Cambios concretos para mejorar

8. **Veredicto final**
   - APROBADO / APROBADO CON CAMBIOS / RECHAZADO
   - Nivel de acuerdo general: (1-10)"""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="validation",
            confidence=0.9,
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
        Critique a proposal from brand perspective.
        
        Args:
            proposal: Proposal to critique.
            proposer: Role of proposer.
            context: Additional context.
            
        Returns:
            Brand critique.
        """
        # Brand Guardian uses the same validation logic for critiques
        return await self.process(
            task=f"Propuesta de {proposer}:\n\n{proposal}",
            context=context
        )
    
    async def validate_content_batch(
        self,
        contents: list[str],
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Validate multiple content pieces.
        
        Args:
            contents: List of content to validate.
            context: Additional context.
            
        Returns:
            Batch validation results.
        """
        agent_context = context or await self._get_context("batch validation")
        
        contents_formatted = "\n\n---\n\n".join([
            f"**Contenido {i+1}:**\n{content}"
            for i, content in enumerate(contents)
        ])
        
        prompt = f"""Como Guardián de Marca, valida los siguientes contenidos:

{contents_formatted}

Para CADA contenido, proporciona:
1. Puntuación de autenticidad (1-10)
2. Puntuación de tono (1-10)
3. Issues detectados (si hay)
4. Veredicto: APROBADO / CAMBIOS NECESARIOS / RECHAZADO

Al final, proporciona:
- Resumen general de la calidad del batch
- Patrones problemáticos detectados
- Recomendaciones generales"""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="batch_validation",
            confidence=0.85,
        )
    
    async def suggest_voice_improvements(
        self,
        content: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Suggest specific improvements to match Nicole's voice.
        
        Args:
            content: Content to improve.
            context: Additional context.
            
        Returns:
            Voice improvement suggestions.
        """
        agent_context = context or await self._get_context(content)
        
        prompt = f"""El siguiente contenido necesita ajustes para sonar más como Nicole:

**Contenido original:**
{content}

Proporciona:

1. **Análisis del problema**
   - ¿Qué específicamente no suena como Nicole?
   - ¿Qué elementos son genéricos o artificiales?

2. **Versión mejorada**
   - Reescribe el contenido completo
   - Mantén el mensaje pero ajusta el tono

3. **Cambios específicos realizados**
   - Lista de qué cambiaste y por qué

4. **Tips para futuros contenidos**
   - Qué recordar para mantener la voz de Nicole

La voz de Nicole es:
- Cercana y empática
- Profesional pero cálida
- Usa preguntas reflexivas
- Evita jerga excesiva
- Es vulnerable y auténtica"""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="voice_improvement",
            confidence=0.85,
        )
