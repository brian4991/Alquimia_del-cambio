"""
Creative Director Agent.

Defines visual direction and Canva briefs.
"""

from typing import Optional, Dict, Any

from marketing.agents.base.base_agent import BaseAgent
from marketing.domain.entities.agent_response import AgentResponse


class CreativeDirectorAgent(BaseAgent):
    """
    Creative Director Agent.
    
    Responsible for:
    - Defining visual direction
    - Creating Canva briefs
    - Ensuring brand visual consistency
    - Proposing innovative visual concepts
    """
    
    @property
    def role(self) -> str:
        return "creative_director"
    
    async def process(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Process a creative task.
        
        Args:
            task: Task description.
            context: Additional context.
            
        Returns:
            Creative proposal.
        """
        agent_context = context or await self._get_context(task)
        
        prompt = f"""Como Director Creativo del equipo, desarrolla la dirección visual para:

**Tarea:**
{task}

Responde con:
1. **Concepto visual**: La idea visual principal
2. **Paleta de colores**: Colores específicos a usar
3. **Elementos visuales**: Qué incluir en el diseño
4. **Tipografía**: Estilo de texto recomendado
5. **Composición**: Cómo organizar los elementos
6. **Nivel de acuerdo**: (1-10) si es una propuesta existente

Recuerda el Brand Kit de Nicole:
- Tonos tierra, sage, crema (cálidos y naturales)
- Estilo profesional pero cercano
- Fotografías auténticas, luz natural"""

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
        Critique a proposal from visual perspective.
        
        Args:
            proposal: Proposal to critique.
            proposer: Role of proposer.
            context: Additional context.
            
        Returns:
            Visual critique.
        """
        agent_context = context or await self._get_context(proposal)
        
        prompt = f"""Como Director Creativo, evalúa la siguiente propuesta de {proposer}:

**Propuesta:**
{proposal}

Evalúa desde la perspectiva visual:
1. **Coherencia de marca**: ¿Se alinea con el Brand Kit?
2. **Impacto visual**: ¿Captará atención?
3. **Claridad**: ¿El mensaje visual es claro?
4. **Originalidad**: ¿Es fresco o genérico?
5. **Mejoras visuales sugeridas**
6. **Nivel de acuerdo**: (1-10)

Sé específico con las recomendaciones visuales."""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="critique",
            confidence=0.8,
            agreement_level=self._parse_agreement_level(response_text),
            suggestions=self._extract_suggestions(response_text),
        )
    
    async def create_visual_brief(
        self,
        content: str,
        platform: str,
        content_type: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Create a detailed visual brief for Canva.
        
        Args:
            content: Text content to visualize.
            platform: Target platform.
            content_type: Type of content (post, reel, story, etc.).
            context: Additional context.
            
        Returns:
            Visual brief.
        """
        dimensions = {
            "instagram_post": "1080x1080 o 1080x1350",
            "instagram_story": "1080x1920",
            "instagram_reel": "1080x1920",
            "tiktok": "1080x1920",
            "youtube_thumbnail": "1280x720",
            "linkedin": "1200x627",
            "facebook": "1200x630",
        }
        
        dim_key = f"{platform}_{content_type}".lower()
        dimension = dimensions.get(dim_key, "1080x1080")
        
        agent_context = context or await self._get_context(content)
        
        prompt = f"""Crea un brief visual detallado para Canva:

**Contenido:**
{content}

**Plataforma:** {platform}
**Tipo:** {content_type}
**Dimensiones:** {dimension}

Genera un brief completo que incluya:

1. **Concepto Visual**
   - Idea principal del diseño
   - Mood/atmósfera

2. **Layout/Composición**
   - Distribución de elementos
   - Jerarquía visual

3. **Fondo**
   - Color o imagen de fondo
   - Texturas o patrones

4. **Tipografía**
   - Texto principal (tamaño, posición)
   - Texto secundario si aplica
   - Fuentes sugeridas

5. **Elementos Gráficos**
   - Iconos o ilustraciones
   - Formas decorativas
   - Líneas o separadores

6. **Fotografía** (si aplica)
   - Tipo de imagen necesaria
   - Posición en el diseño

7. **Colores Específicos**
   - Códigos hex si es posible
   - Basados en Brand Kit de Nicole

8. **Notas para el Diseñador**
   - Aspectos importantes a cuidar
   - Errores a evitar"""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="visual_brief",
            confidence=0.9,
        )
