"""
Script pour créer le Thème 3 COMPLET du Module 3
Thème 3: Del amor propio al amor compartido (3 subtemas)
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Theme, ThemeCard

# Styles
FONT = "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
C_TEXT = "#2d2d2d"
C_TITLE = "#6b745a"
C_ACCENT = "#a28d72"
C_BG_LIGHT = "#f5f5f0"
C_BG_GRAY = "#cbcbcc"

def css():
    return f'color: {C_TEXT}; font-family: {FONT}; line-height: 1.8; max-width: 800px;'

def create_theme3(db: Session, module_id: int):
    """Créer le Thème 3"""
    print("\n📚 Création du Thème 3...")
    theme = Theme(
        title="Del amor propio al amor compartido",
        content="El amor propio es el cimiento sobre el cual construimos nuestras relaciones. Si no nos conocemos, valoramos y respetamos a nosotros mismos, es difícil establecer vínculos sanos con los demás.",
        order_number=3,
        module_id=module_id
    )
    db.add(theme)
    db.flush()
    print(f"✅ Thème 3 créé (ID: {theme.id})")
    return theme

def create_theme3_cards(db: Session, theme_id: int):
    """Créer toutes les cards du Thème 3"""
    print("\n🎴 Création des cards du Thème 3...")
    
    cards = []
    order = 1
    
    # Introduction
    cards.append({
        "title": "Bienvenida al Tema 3",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Del Amor Propio al Amor Compartido</h1>

<p style="margin-bottom: 16px; font-size: 1.1em;">El amor propio es el cimiento sobre el cual construimos nuestras relaciones. Si no nos conocemos, valoramos y respetamos a nosotros mismos, es difícil establecer vínculos sanos con los demás.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Una Verdad Fundamental</h3>
<p style="margin-bottom: 0;">Sin embargo, el amor propio no significa aislamiento o autosuficiencia extrema; más bien, es el punto de partida para compartir nuestra vida con alguien sin perder nuestra esencia.</p>
</div>

<p style="margin-bottom: 16px;">Muchas veces, las relaciones fallan no porque no haya amor, sino porque las personas entran en ellas sin haber construido primero una relación sólida consigo mismas.</p>

<p style="margin-bottom: 16px;">Sin una base firme de autoconocimiento, es fácil caer en patrones de dependencia, expectativas poco realistas o dinámicas de control.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">El Desafío</h3>
<p style="margin-bottom: 0;">El desafío está en aprender a mantener el equilibrio: amar al otro sin dejar de amarnos a nosotros mismos.</p>
</div>

<p style="margin-bottom: 16px;">Para lograrlo, es fundamental desarrollar habilidades clave como la comunicación consciente, la resolución de conflictos y la capacidad de compartir nuestra vida con alguien sin perdernos en el proceso.</p>
</div>""",
        "card_type": "intro",
        "order_number": order
    })
    order += 1
    
    # SUBTEMA 1: Comunicación consciente (cards 2-9)
    cards.extend([
        {
            "title": "Subtema 1: Comunicación Consciente - Introducción",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Comunicación Consciente</h1>

<p style="margin-bottom: 16px; font-size: 1.1em;">La comunicación es el puente que conecta a dos personas. Sin embargo, no basta con hablar; es necesario aprender a expresarnos de manera clara, respetuosa y efectiva, y al mismo tiempo, desarrollar la capacidad de escuchar con empatía.</p>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">En las relaciones, muchas discusiones no surgen por falta de amor, sino por formas poco saludables de comunicarse:</h3>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;">• Reacciones impulsivas en lugar de respuestas reflexionadas.</p>
<p style="margin-bottom: 12px;">• Suposiciones en lugar de aclaraciones.</p>
<p style="margin-bottom: 0;">• Expectativas no expresadas en lugar de peticiones claras.</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Comunicación Consciente - Vulnerabilidad",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">1. Hablar desde la vulnerabilidad, no desde la acusación</h2>

<p style="margin-bottom: 16px;">Cuando surge un conflicto, es fácil señalar al otro: "Nunca me escuchas", "Siempre haces lo mismo".</p>

<p style="margin-bottom: 16px;">Sin embargo, esta forma de comunicación genera defensas y distancia.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">En lugar de eso, practica la comunicación desde el "yo":</h3>
<p style="margin-bottom: 12px;"><strong style="color: #d9534f;">❌ "Nunca me prestas atención cuando hablo."</strong></p>
<p style="margin-bottom: 0;"><strong style="color: #5cb85c;">✅ "Me siento ignorado/a cuando no me miras mientras hablo, y eso me hace sentir desconectado/a de ti."</strong></p>
</div>

<p style="margin-bottom: 16px;">Hablar desde la propia experiencia y las emociones en lugar de culpar al otro, permite que la conversación fluya sin generar resistencia.</p>
</div>""",
            "card_type": "practical",
            "order_number": order + 1
        },
        {
            "title": "Comunicación Consciente - Escucha Activa",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">2. Escucha para comprender, no para responder</h2>

<p style="margin-bottom: 16px;">Muchas veces, mientras la otra persona habla, ya estamos preparando nuestra respuesta mentalmente en lugar de escuchar realmente lo que nos está diciendo.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">La escucha activa implica:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Hacer contacto visual y asentir para mostrar interés.</p>
<p style="margin-bottom: 12px;">• No interrumpir ni apresurarse a dar consejos.</p>
<p style="margin-bottom: 0;">• Repetir o parafrasear lo que el otro dijo para confirmar que lo entendimos bien: <em>"Si entiendo bien, lo que te molesta es que no te aviso cuando cambio mis planes, ¿cierto?"</em></p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Resultado</h3>
<p style="margin-bottom: 0;">Cuando alguien se siente escuchado de verdad, es más probable que baje la guardia y la conversación fluya de manera más sana.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 2
        },
        {
            "title": "Comunicación Consciente - Expresar Necesidades",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">3. Expresar necesidades en lugar de esperar que el otro adivine</h2>

<p style="margin-bottom: 16px;">Muchas frustraciones en pareja vienen de la expectativa de que el otro "debería saber" lo que necesitamos. Pero las personas no leen mentes.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Un buen ejercicio es preguntarte:</h3>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;">• ¿Qué necesito realmente en esta situación?</p>
<p style="margin-bottom: 0;">• ¿Lo he comunicado de forma clara y directa?</p>
</div>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;"><strong style="color: #d9534f;">❌ "Últimamente siento que no te importo."</strong></p>
<p style="margin-bottom: 0;"><strong style="color: #5cb85c;">✅ "Me gustaría que planificáramos más tiempo juntos porque eso me hace sentir valorado/a en la relación."</strong></p>
</div>

<p style="margin-bottom: 16px;">Hablar desde la claridad evita malentendidos y genera vínculos más sólidos.</p>
</div>""",
            "card_type": "practical",
            "order_number": order + 3
        },
        {
            "title": "Comunicación Consciente - El Vaso de Agua",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_ACCENT}; font-size: 1.7em; margin-bottom: 20px;">Ejemplo práctico: "El vaso de agua"</h2>

<p style="margin-bottom: 16px;">Imagina que tienes sed y esperas que tu pareja te traiga un vaso de agua. No dices nada, pero en tu mente piensas: <em>"Si realmente me quisiera, me traería agua sin que yo tenga que pedirlo."</em></p>

<p style="margin-bottom: 16px;">Si después de un rato la otra persona no lo hace, te sientes molesto y piensas que no le importas.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0;">
<h3 style="margin-top: 0; color: white;">Ahora, observa la alternativa:</h3>
<p style="margin-bottom: 12px; font-size: 1.1em;">✅ En lugar de esperar, le dices: <em>"Me encantaría un vaso de agua, ¿me lo podrías traer?"</em></p>
<p style="margin-bottom: 0; font-weight: 600;">Resultado: Expresaste tu necesidad de forma clara y la otra persona sabe qué hacer para responder a ella.</p>
</div>

<p style="margin-bottom: 16px; font-size: 1.1em;">Este mismo principio aplica en la comunicación con los otros.</p>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-weight: 600; color: {C_ACCENT};">Si no expresamos lo que queremos o necesitamos, es injusto esperar que el otro lo adivine.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 4
        },
        {
            "title": "Ejercicio: Comunicación Consciente",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Aplica Herramientas de la Comunicación</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas aplicar herramientas de la comunicación.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3: Del Amor Propio al Amor Compartido</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 3.1: Comunicación Asertiva en las Relaciones</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 5
        }
    ])
    order += 6
    
    # SUBTEMA 2: Resolución de conflictos (cards 8-15)
    cards.extend([
        {
            "title": "Subtema 2: Resolución de Conflictos - Introducción",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: Resolución de Conflictos</h1>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Una Nueva Perspectiva</h3>
<p style="margin-bottom: 0; font-size: 1.1em;">El conflicto en una relación no es una señal de fracaso, sino una oportunidad de crecimiento.</p>
</div>

<p style="margin-bottom: 16px;">No hay relaciones sin desacuerdos, pero la diferencia entre una relación saludable y una destructiva está en cómo enfrentamos esos conflictos.</p>

<p style="margin-bottom: 16px;">Muchas personas ven el conflicto como algo negativo porque lo asocian con peleas, distanciamiento o dolor emocional.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<p style="margin: 0; font-size: 1.05em;">Sin embargo, cuando se maneja con consciencia, el conflicto puede fortalecer la conexión en lugar de debilitarla.</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Resolución de Conflictos - Cómo Manejamos",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">1. El problema no es el conflicto, sino cómo lo manejamos</h2>

<p style="margin-bottom: 16px;">Piensa en una pareja que discute constantemente porque uno de los dos siente que no recibe suficiente atención. La manera en la que aborden este problema definirá el impacto en su relación:</p>

<h3 style="color: #d9534f; margin-top: 24px; margin-bottom: 16px;">❌ Enfoque destructivo:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Culpar al otro: "Nunca me prestas atención, solo piensas en ti."</p>
<p style="margin-bottom: 12px;">• Evitar el problema: "No quiero hablar de esto, siempre es lo mismo."</p>
<p style="margin-bottom: 0;">• Actuar con resentimiento: Hacer "silencio" y distanciarse sin resolver el problema.</p>
</div>

<h3 style="color: #5cb85c; margin-top: 24px; margin-bottom: 16px;">✅ Enfoque constructivo:</h3>

<div style="background: #f0fff0; border-left: 5px solid #5cb85c; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Expresar sentimientos sin culpar: "Me siento solo cuando pasas tanto tiempo en el teléfono. Me gustaría que dediquemos más tiempo de calidad juntos."</p>
<p style="margin-bottom: 12px;">• Escuchar con empatía: Preguntar al otro cómo se siente en lugar de asumirlo.</p>
<p style="margin-bottom: 0;">• Buscar una solución juntos: "¿Qué podemos hacer para mejorar esto?"</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">La Clave</h3>
<p style="margin-bottom: 12px;">Cuando dejamos de ver al otro como "el enemigo" y empezamos a ver el conflicto como un problema a resolver juntos, la dinámica cambia completamente.</p>
<p style="margin-bottom: 0; font-weight: 600; font-size: 1.1em;">Somos los dos contra el problema NO contra la pareja.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "Resolución de Conflictos - Regulación Emocional",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">2. Regulación emocional antes de resolver un conflicto</h2>

<p style="margin-bottom: 16px;">Cuando una discusión se intensifica, el cerebro entra en modo de lucha o huida, lo que hace difícil pensar con claridad. Es por eso que muchas discusiones terminan con gritos, palabras hirientes o distanciamiento.</p>

<div style="background: {C_ACCENT}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.3em;">Regla de oro:</h3>
<p style="margin-bottom: 0; font-size: 1.1em;">No intentes resolver un conflicto cuando las emociones están fuera de control.</p>
</div>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Si sientes que la discusión está escalando:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;"><strong>1.</strong> Pausa la conversación y di algo como: <em>"Necesito un momento para calmarme y poder hablar con claridad. Sigamos esta conversación en 20 minutos."</em></p>
<p style="margin-bottom: 12px;"><strong>2.</strong> Regula tu emoción antes de continuar: respira, da un paseo o escribe lo que sientes.</p>
<p style="margin-bottom: 0;"><strong>3.</strong> Vuelve al diálogo con apertura: en lugar de reanudar la discusión con reproches, pregúntate: <em>"¿Qué quiero lograr con esta conversación?"</em></p>
</div>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo práctico:</h3>

<p style="margin-bottom: 16px;">Si tu pareja o amigo dice algo que te molesta, en lugar de reaccionar impulsivamente, respira y pregúntate: <em>"¿Estoy interpretando esto de la peor manera posible? ¿Puedo preguntar antes de asumir?"</em></p>
</div>""",
            "card_type": "practical",
            "order_number": order + 2
        },
        {
            "title": "Resolución de Conflictos - Comunicar Sin Atacar",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">3. Aprende a comunicar sin atacar</h2>

<p style="margin-bottom: 16px;">Las palabras que usamos pueden hacer que un conflicto se resuelva o se agrave. La clave está en pasar de la comunicación reactiva a la comunicación consciente.</p>

<h3 style="color: #d9534f; margin-top: 24px; margin-bottom: 16px;">🛑 Errores comunes en una discusión:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Generalizar: "Tú siempre haces esto. Nunca me escuchas."</p>
<p style="margin-bottom: 12px;">• Atacar con críticas: "Eres egoísta. Solo piensas en ti."</p>
<p style="margin-bottom: 0;">• Victimizarse: "Siempre soy yo quien tiene que ceder."</p>
</div>

<h3 style="color: #5cb85c; margin-top: 24px; margin-bottom: 16px;">✅ Estrategias de comunicación consciente:</h3>

<div style="background: #f0fff0; border-left: 5px solid #5cb85c; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Usa frases en primera persona: en lugar de "Me haces sentir mal", prueba "Me siento triste cuando sucede esto."</p>
<p style="margin-bottom: 12px;">• Pregunta antes de asumir: en vez de "No te importa lo que digo", prueba "¿Podemos hablar? Me gustaría entender tu punto de vista."</p>
<p style="margin-bottom: 0;">• Evita el lenguaje absolutista (siempre, nunca, todo, nada), ya que suele hacer que la otra persona se ponga a la defensiva.</p>
</div>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;"><strong style="color: #d9534f;">❌ "Nunca te preocupas por lo que me pasa."</strong></p>
<p style="margin-bottom: 0;"><strong style="color: #5cb85c;">✅ "Me gustaría sentir que tomas en cuenta lo que me preocupa. ¿Podemos hablar de esto juntos?"</strong></p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 3
        },
        {
            "title": "Resolución de Conflictos - Enfocarse en la Solución",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">4. Enfócate en la solución, no en ganar la discusión</h2>

<div style="background: {C_ACCENT}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.3em;">Pregúntate:</h3>
<p style="margin-bottom: 0; font-size: 1.15em;">¿Prefieres tener razón o fortalecer la relación?</p>
</div>

<p style="margin-bottom: 16px;">Muchas veces, en un conflicto nos enfocamos en demostrar que el otro está equivocado en lugar de buscar soluciones.</p>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Haz este cambio de enfoque:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• En lugar de pelear por quién tiene razón, pregúntate: <em>"¿Cómo podemos resolver esto de una manera que nos beneficie a los dos?"</em></p>
<p style="margin-bottom: 0;">• Si la discusión se basa en suposiciones, pregúntate: <em>"¿Estoy seguro de que esto es verdad o estoy interpretándolo desde mi herida?"</em></p>
</div>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<p style="margin-bottom: 12px;">Si sientes que tu pareja no muestra interés en tu día, en lugar de asumir que no le importas, podrías decir:</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin: 0;"><em>"Me haría feliz que me preguntes más sobre mi día. ¿Te gustaría que yo también pregunte más sobre el tuyo?"</em></p>
</div>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 10px; margin: 28px 0;">
<p style="margin: 0; font-weight: 600; color: {C_TITLE};">Las relaciones más fuertes no son aquellas sin problemas, sino aquellas donde ambas personas están dispuestas a enfrentar los conflictos con consciencia, respeto y disposición al cambio.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 4
        },
        {
            "title": "Ejercicio: Resolución de Conflictos",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Aplica Herramientas para Resolver tus Conflictos</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas aplicar herramientas para resolver tus conflictos.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3: Del Amor Propio al Amor Compartido</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 3.2: Resolución de conflictos</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 5
        }
    ])
    order += 6
    
    # SUBTEMA 3: Equilibrio (cards 14-16)
    cards.extend([
        {
            "title": "Subtema 3: Equilibrio - Como Ser con Otro",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 3: Equilibrio: ¿Cómo Ser con Otro?</h1>

<p style="margin-bottom: 16px; font-size: 1.1em;">El amor propio es el pilar de una relación sana, pero ¿cómo llevamos ese amor propio a una relación sin perder nuestra identidad ni caer en el egoísmo?</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Aquí es Donde Entra el Equilibrio</h3>
<p style="margin-bottom: 0;">La capacidad de estar con otro sin dejar de ser uno mismo.</p>
</div>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Muchas veces, las relaciones se desbalancean en dos direcciones:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;"><strong>1. Fusión excesiva:</strong> Donde uno se pierde en el otro, dejando de lado sus propias necesidades y deseos. Aquí, la relación se vuelve una dependencia emocional.</p>
<p style="margin-bottom: 0;"><strong>2. Distancia excesiva:</strong> Donde cada persona protege tanto su individualidad que no hay espacio para la conexión real. Esto genera relaciones frías, donde hay amor, pero no hay cercanía.</p>
</div>

<p style="margin-bottom: 16px; font-size: 1.05em;">El equilibrio en una relación implica encontrar el punto medio: ser capaz de compartir con el otro sin dejar de ser tú mismo.</p>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-weight: 600; color: {C_ACCENT};">No es renunciar a tu esencia, sino integrarla con la del otro de manera armoniosa.</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Equilibrio - El Baile de Pareja",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_ACCENT}; font-size: 1.7em; margin-bottom: 20px;">Ejemplo práctico: El baile de pareja</h2>

<div style="background: {C_BG_GRAY}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<p style="margin-bottom: 0; font-size: 1.05em;">Piensa en una pareja bailando. Si uno de los dos se mueve sin tomar en cuenta al otro, el baile se desordena o se vuelve incómodo. Pero si ambos se sincronizan, sin perder su propia expresión, el baile fluye con armonía. Lo mismo ocurre en las relaciones: necesitas movimiento y conexión, pero sin perderte en la danza del otro.</p>
</div>

<h3 style="color: {C_TITLE}; margin-top: 32px; margin-bottom: 16px;">Claves para encontrar el equilibrio en una relación:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• <strong>Espacio propio y espacio compartido:</strong> Es saludable compartir tiempo juntos, pero también es esencial que cada uno tenga sus propios momentos, hobbies y amigos.</p>
<p style="margin-bottom: 12px;">• <strong>Autoconocimiento:</strong> Saber qué necesitas y qué te hace feliz antes de esperar que la relación lo haga por ti.</p>
<p style="margin-bottom: 12px;">• <strong>Comunicación clara y honesta:</strong> Expresar lo que sientes y necesitas sin miedo a perder al otro.</p>
<p style="margin-bottom: 0;">• <strong>Flexibilidad y adaptabilidad:</strong> No se trata de imponer tu forma de ser ni de ceder completamente, sino de encontrar un punto medio donde ambos se sientan cómodos.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "Equilibrio - En Diferentes Relaciones",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Cómo encontrar el equilibrio en diferentes tipos de relaciones?</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• <strong>En pareja:</strong> Evita caer en el mito de que "el amor todo lo puede". Una relación necesita más que amor: requiere acuerdos, límites y compromiso mutuo.</p>
<p style="margin-bottom: 12px;">• <strong>En la familia:</strong> Acepta que no siempre puedes cambiar la dinámica familiar, pero sí puedes establecer límites saludables para proteger tu bienestar.</p>
<p style="margin-bottom: 0;">• <strong>En la amistad:</strong> Una amistad equilibrada es aquella en la que das y recibes de manera justa, sin sentir que llevas el peso de la relación.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 32px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.3em;">La Verdadera Esencia</h3>
<p style="margin-bottom: 0; font-size: 1.1em;">El amor no se trata de dos mitades que se complementan, sino de dos personas completas que deciden caminar juntas. El verdadero equilibrio surge cuando puedes estar con alguien sin dejar de ser tú.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 2
        },
        {
            "title": "Ejercicio: Equilibrio",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Crea tu Balance</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas crear tu balance.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3: Del Amor Propio al Amor Compartido</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 3.3: Equilibrio: ¿Cómo ser con otro?</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 3
        }
    ])
    order += 4
    
    # Conclusion
    cards.append({
        "title": "Conclusión del Tema 3",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Conclusión del Tema 3</h1>

<p style="margin-bottom: 16px; font-size: 1.1em;">Construir una relación sana no significa perderse en el otro ni cerrarse en una independencia extrema, sino encontrar un equilibrio donde el amor propio y el amor compartido coexistan.</p>

<h3 style="color: {C_TITLE}; margin-top: 28px; margin-bottom: 16px;">Lo Que Has Aprendido:</h3>

<div style="background: {C_BG_LIGHT}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<p style="margin-bottom: 16px;">Para lograrlo, es fundamental desarrollar una <strong>comunicación consciente</strong>, donde podamos expresar nuestras emociones y necesidades sin atacar ni reprimirnos. Aprender a escuchar con empatía y hablar con claridad nos ayuda a construir puentes en lugar de muros.</p>

<p style="margin-bottom: 16px;">Asimismo, en cualquier relación surgirán diferencias, y la <strong>resolución de conflictos</strong> es clave para atravesarlas sin dañar el vínculo. No se trata de evitar los problemas, sino de enfrentarlos con madurez, buscando soluciones en lugar de culpables. Aprender a gestionar desacuerdos desde la calma y el respeto fortalece la conexión con el otro.</p>

<p style="margin-bottom: 0;">Por último, el verdadero desafío es encontrar el <strong>equilibrio en la relación</strong>, es decir, ser parte de un "nosotros" sin dejar de ser "yo". Las relaciones más sólidas no nacen de la dependencia ni de la distancia, sino de la integración de dos personas que eligen crecer juntas, respetando su individualidad y creando un espacio de amor mutuo.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 28px; border-radius: 10px; margin: 32px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.4em;">Recuerda</h3>
<p style="margin-bottom: 0; font-size: 1.15em; line-height: 1.7;">En este camino, recuerda que el amor sano no se trata de llenar vacíos, sino de compartir abundancia.</p>
</div>
</div>""",
        "card_type": "conclusion",
        "order_number": order
    })
    
    for card_data in cards:
        card = ThemeCard(
            title=card_data["title"],
            content=card_data["content"],
            card_type=card_data["card_type"],
            order_number=card_data["order_number"],
            theme_id=theme_id
        )
        db.add(card)
    
    db.commit()
    print(f"✅ {len(cards)} cards créées pour le Thème 3")
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DU THÈME 3 COMPLET - MODULE 3")
        print("=" * 70)
        
        MODULE_ID = 3
        
        # Créer le thème 3
        theme3 = create_theme3(db, MODULE_ID)
        num_cards = create_theme3_cards(db, theme3.id)
        
        print("\n" + "=" * 70)
        print("✅ MODULE 3 COMPLÈTEMENT TERMINÉ!")
        print("=" * 70)
        print(f"📚 Thème 3 créé avec {num_cards} cards")
        print(f"\n🎉 RÉCAPITULATIF MODULE 3:")
        print(f"   • Thème 1: Espejos del alma (19 cards)")
        print(f"   • Thème 2: Cimientos de conexión (31 cards)")
        print(f"   • Thème 3: Del amor propio al amor compartido ({num_cards} cards)")
        print(f"\n✨ Total: {19 + 31 + num_cards} cards pour le Module 3!")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

