"""
Copywriter Agent.

Writes captions, hooks, and CTAs.
"""

from typing import Optional, Dict, Any

from marketing.agents.base.base_agent import BaseAgent
from marketing.domain.entities.agent_response import AgentResponse


class CopywriterAgent(BaseAgent):
    """
    Copywriter Agent.
    
    Responsible for:
    - Writing engaging captions
    - Creating hooks that capture attention
    - Developing effective CTAs
    - Adapting tone per platform
    """
    
    @property
    def role(self) -> str:
        return "copywriter"
    
    async def process(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Process a copywriting task.
        
        Args:
            task: Task description.
            context: Additional context.
            
        Returns:
            Copy proposal.
        """
        agent_context = context or await self._get_context(task)
        
        prompt = f"""Como Copywriter del equipo, desarrolla el copy para:

**Tarea:**
{task}

Responde con:
1. **Hook principal**: Primera línea que atrapa
2. **Desarrollo del copy**: El cuerpo del texto
3. **CTA**: Llamado a la acción
4. **Variaciones**: 2-3 alternativas del hook
5. **Hashtags**: 3-5 hashtags relevantes
6. **Nivel de acuerdo**: (1-10) si es una propuesta existente

Recuerda el estilo de Nicole:
- Cercano y empático
- Preguntas reflexivas
- Profesional pero cálido
- CTAs suaves, no agresivos"""

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
        Critique a proposal from copywriting perspective.
        
        Args:
            proposal: Proposal to critique.
            proposer: Role of proposer.
            context: Additional context.
            
        Returns:
            Copy critique.
        """
        agent_context = context or await self._get_context(proposal)
        
        prompt = f"""Como Copywriter, evalúa el texto de la propuesta de {proposer}:

**Propuesta:**
{proposal}

Evalúa desde la perspectiva de copywriting:
1. **Hook**: ¿Captura atención en los primeros segundos?
2. **Claridad**: ¿El mensaje es claro y directo?
3. **Persuasión**: ¿Motiva a la acción?
4. **Tono**: ¿Suena como Nicole?
5. **CTA**: ¿Es efectivo pero no agresivo?
6. **Mejoras de copy sugeridas**
7. **Nivel de acuerdo**: (1-10)

Proporciona alternativas concretas si tienes mejores ideas."""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="critique",
            confidence=0.8,
            agreement_level=self._parse_agreement_level(response_text),
            suggestions=self._extract_suggestions(response_text),
        )
    
    async def write_post_caption(
        self,
        topic: str,
        platform: str,
        objective: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Write a complete post caption.
        
        Args:
            topic: Topic of the post.
            platform: Target platform.
            objective: Objective of the post.
            context: Additional context.
            
        Returns:
            Complete caption.
        """
        agent_context = context or await self._get_context(topic)
        
        prompt = f"""Escribe una caption completa para {platform}:

**Tema:** {topic}
**Objetivo:** {objective}

Genera:

1. **HOOK** (primera línea - CRUCIAL)
   - Versión A (pregunta)
   - Versión B (afirmación impactante)
   - Versión C (historia personal)

2. **CUERPO**
   - Desarrollo del tema
   - Valor para la audiencia
   - Historia o ejemplo si aplica
   - Longitud óptima para {platform}

3. **CTA**
   - Llamado a la acción principal
   - Alternativa más suave

4. **HASHTAGS**
   - 3-5 hashtags relevantes
   - Mix de populares y nicho

5. **CAPTION COMPLETA**
   - Versión final lista para publicar
   - Con emojis si es apropiado para {platform}

Asegúrate de que suene auténtico y como Nicole lo escribiría."""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="caption",
            confidence=0.9,
        )
    
    async def write_reel_script(
        self,
        topic: str,
        duration_seconds: int = 30,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Write a reel/TikTok script.
        
        Args:
            topic: Topic of the reel.
            duration_seconds: Target duration.
            context: Additional context.
            
        Returns:
            Reel script.
        """
        agent_context = context or await self._get_context(topic)
        
        prompt = f"""Escribe un script de Reel/TikTok de {duration_seconds} segundos:

**Tema:** {topic}

Genera:

1. **HOOK** (0-3 segundos) - CRUCIAL
   - Frase que detenga el scroll
   - 3 opciones diferentes

2. **SCRIPT COMPLETO**
   ```
   [0-3s] HOOK: "..."
   [3-10s] INTRO: "..."
   [10-20s] CONTENIDO PRINCIPAL: "..."
   [20-{duration_seconds}s] CIERRE + CTA: "..."
   ```

3. **TEXTO EN PANTALLA**
   - Qué texto overlay mostrar
   - En qué momentos

4. **SUGERENCIAS VISUALES**
   - Qué mostrar en cada parte
   - Transiciones sugeridas

5. **AUDIO/MÚSICA**
   - Tipo de música sugerida
   - Si usar voz en off o voz directa

6. **VARIACIÓN CORTA** (15 segundos)
   - Versión condensada del mismo contenido

El script debe:
- Ser natural para hablar
- Tener ritmo dinámico
- Mantener atención todo el tiempo"""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="reel_script",
            confidence=0.85,
        )
