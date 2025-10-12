"""
Script pour créer tous les exercices du Module 4: De la expectativa a la realidad
3 exercices répartis sur 3 thèmes (Acuerdos, Ser, Realidad)
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exercise

def create_all_exercises_module4(db: Session):
    """Créer tous les exercices du Module 4"""
    
    print("\n" + "=" * 70)
    print("🚀 CRÉATION DE TOUS LES EXERCICES DU MODULE 4")
    print("=" * 70)
    
    # IDs des thèmes du Module 4
    THEME_1_ID = 19  # Rompiendo barreras
    THEME_2_ID = 20  # Despertar auténtico
    THEME_3_ID = 21  # Mapa de acción hacia la autenticidad
    
    exercises_created = []
    
    # ========================================================================================
    # EJERCICIO #1: ACUERDOS (Thème 1)
    # ========================================================================================
    print("\n📝 Création de l'Ejercicio #1: Acuerdos...")
    
    exercise_1_1 = Exercise(
        title="Ejercicio 1.1: Mis acuerdos",
        parent_title="Ejercicio #1: Acuerdos",
        instructions="""<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Rompiendo Barreras</h2>

<p style="font-size: 1.1em; margin-bottom: 16px;">Este ejercicio tiene como propósito ayudarte a <strong>identificar los acuerdos internos</strong> que has hecho a lo largo de tu vida. Muchas veces, estos acuerdos no son conscientes, pero influyen en la manera en que te percibes a ti mismo/a y en cómo te relacionas con el mundo.</p>

<p style="margin-bottom: 16px;">Este ejercicio no se trata de rechazar todo lo aprendido, sino de cuestionarlo con conciencia. Cuestionarlo todo es un poder que nos permite transitar la vida con mayor claridad y elegir de manera consciente qué valores, principios y creencias queremos conservar y cuáles queremos transformar.</p>

<p style="margin-bottom: 16px;"><strong>Tiempo estimado:</strong> 30 minutos</p>
</div>""",
        order_number=1,
        theme_id=THEME_1_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identifica tus acuerdos",
                "instructions": """Antes de comenzar, encuentra un espacio tranquilo donde puedas reflexionar sin interrupciones. Respira profundamente.

Pregúntate:
• ¿Cuáles son las creencias sobre mí mismo/a que han estado presentes desde mi infancia?
• ¿Qué ideas sobre quién soy y qué merezco han influido en mis decisiones?
• ¿He sentido que para ser aceptado/a debo seguir ciertas reglas impuestas por mi entorno?

Escribe al menos 7 acuerdos que sientas que han marcado tu vida. No te preocupes si al principio no los ves con claridad, piensa en frases que repites internamente o en lo que otros te han dicho y que has tomado como verdad.

📌 Ejemplo:
'Debo ser perfecto/a para que me quieran.'
'Si expreso mis emociones, las personas se alejarán.'
'No soy lo suficientemente bueno/a para tener exito.'""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Lista tus 7 acuerdos internos que han marcado tu vida (uno por línea)"
                    }
                ]
            },
            {
                "title": "Paso 2: Reflexiona sobre su impacto",
                "instructions": """Ahora que tienes identificados algunos de tus acuerdos, reflexiona sobre su impacto en tu vida. Para cada uno de ellos, respóndete:

• ¿De dónde viene este acuerdo?
  - ¿Lo aprendí de mi familia, de la escuela, de experiencias pasadas?
  - ¿Lo adopté por miedo, necesidad de aceptación o protección?

• ¿Cómo influye en mi vida actual?
  - ¿Qué decisiones he tomado basándome en esta creencia?
  - ¿Cómo me ha limitado en mi crecimiento o en mis relaciones?

• ¿Cómo me hace sentir?
  - ¿Este acuerdo me genera miedo, ansiedad, inseguridad?
  - ¿Siento que no puedo ser realmente yo mismo/a cuando lo sigo?

📌 Ejemplo:
"Siempre sentí que debía ser perfecto para recibir amor. Esto me ha llevado a ser extremadamente exigente conmigo mismo/a y a temer el fracaso. Cada vez que cometo un error, siento que decepciono a los demás y me critico duramente."""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Analiza el impacto de tus acuerdos en tu vida (describe cómo te han afectado)"
                    }
                ]
            },
            {
                "title": "Paso 3: Transforma tus acuerdos",
                "instructions": """Después de identificar los acuerdos que te limitan, es momento de transformarlos en afirmaciones que te empoderen. Para cada uno de tus acuerdos anteriores, escribe una nueva versión que refleje tu verdadero valor y autenticidad.

Preguntas para guiarte:
• ¿Qué quiero creer en lugar de este acuerdo?
• ¿Cómo puedo empezar a cambiar esta creencia en mi día a día?
• ¿Qué afirmaciones positivas puedo repetirme para reforzar este nuevo acuerdo?

📌 Ejemplo:
❌ Acuerdo limitante: "Debo ser perfecto/a para que me quieran."
✅ Nuevo acuerdo: "Soy valioso/a tal como soy. Mi autenticidad es lo que me hace único/a y digno/a de amor."

❌ Acuerdo limitante: "No soy lo suficientemente bueno/a para lograr mis sueños."
✅ Nuevo acuerdo: "Cada paso que doy me acerca más a la vida que deseo. Confío en mi proceso y en mis capacidades."

🌿 Tómate un momento para leer en voz alta tus nuevos acuerdos. Siente cómo resuenan en ti. Puedes escribirlos en un papel y ponerlos en un lugar visible para recordarlos cada día.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tus nuevos acuerdos transformados (formato: ❌ Acuerdo limitante → ✅ Nuevo acuerdo)"
                    }
                ]
            }
        ])
    )
    db.add(exercise_1_1)
    db.flush()
    exercises_created.append(f"Ejercicio 1.1 (ID: {exercise_1_1.id})")
    print(f"  ✅ Ejercicio 1.1: Mis acuerdos créé (ID: {exercise_1_1.id})")
    
    # EJERCICIO 1.2: La voz interior
    exercise_1_2 = Exercise(
        title="Ejercicio 1.2: La voz interior a la que sirvo",
        parent_title="Ejercicio #1: Acuerdos",
        instructions="""<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">La Voz Interior a la que Sirvo</h2>

<p style="margin-bottom: 16px;"><strong>Tiempo estimado:</strong> 30 minutos</p>
</div>""",
        order_number=2,
        theme_id=THEME_1_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identifica tu voz interior",
                "instructions": """Durante un día, pon atención a cómo te hablas a ti mism@ en diferentes situaciones.

Pregúntate:
• ¿Es una voz de apoyo o de juicio?
• ¿Tiendes a animarte o a criticarte con dureza?
• ¿Cuáles son las frases más recurrentes que te dices?
• Y el descubrimiento más importante, ¿a quién sirve esa voz, es papá, es mamá, alguna persona cercana?

Esta última pregunta será muy útil para que rompas los acuerdos con esa persona y cada vez que vengan pensamientos intrusivos logres silenciar esa voz.

📌 Ejemplo: "Siempre hago todo mal." "No soy lo suficientemente bueno." "Si fallo, los demás me verán como un fracaso."

Escribe las frases más frecuentes que identificas en tu diálogo interno.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué frases recurrentes te dices a ti mismo/a?"
                    },
                    {
                        "type": "text",
                        "question": "¿A quién sirve esa voz? (papá, mamá, otra persona)"
                    }
                ]
            },
            {
                "title": "Paso 2: Cuestiona su veracidad",
                "instructions": """Ahora que has identificado algunas de las frases que te dices, reflexiona sobre su origen y su veracidad:

Pregúntate:
• ¿De dónde viene esta creencia?
• ¿Es un pensamiento basado en hechos o en el miedo?
• ¿Le hablaría de la misma manera a un ser querido?

📌 Ejemplo:
❌ Pensamiento limitante: "Siempre fracaso."
✔ Cuestionamiento: "¿Realmente SIEMPRE fracaso? No, he tenido logros importantes. Esta es una creencia basada en el miedo, no en la realidad."

Escribe una breve reflexión sobre quién fue la persona detrás que sembró la semilla para que siguieras cultivando estas creencias y si realmente reflejan la verdad hoy sobre ti.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Reflexiona: ¿De dónde vienen estas creencias y reflejan la verdad sobre ti hoy?"
                    }
                ]
            },
            {
                "title": "Paso 3: Transforma tu voz interna",
                "instructions": """Es momento de transformar tu voz interna en una aliada. Toma las frases negativas que identificaste y reformúlalas en mensajes positivos y realistas.

📌 Ejemplo:
❌ "No soy lo suficientemente bueno."
✅ "Estoy aprendiendo y mejorando cada día."

❌ "Si fallo, los demás me verán como un fracaso."
✅ "Los errores son parte del aprendizaje y no definen mi valor."

Haz una lista con al menos 7 frases transformadas y repítelas en voz alta.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Lista tus 7 frases transformadas (formato: ❌ Frase negativa → ✅ Frase positiva)"
                    }
                ]
            },
            {
                "title": "Paso 4: Crea afirmaciones diarias",
                "instructions": """Para fortalecer tu nueva voz interna, escribe afirmaciones que refuercen tu confianza y repítelas diariamente.

📌 Ejemplo de afirmaciones:
• "Confío en mi capacidad para tomar decisiones."
• "Soy suficiente tal como soy."
• "Cada día es una oportunidad para crecer y aprender."

Escribe tus propias afirmaciones y colócalas en un lugar visible para recordarlas a diario.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tus afirmaciones diarias (al menos 5)"
                    }
                ]
            },
            {
                "title": "Paso 5: Rodéate de mensajes positivos",
                "instructions": """El entorno influye en nuestra voz interna. Para reforzar tu nueva mentalidad:

• Escucha contenido que fomente una mentalidad positiva
• Evita entornos donde predomine la crítica constante
• Conecta con personas que te inspiren y te apoyen

📌 Acción recomendada: Leer el libro de los 4 acuerdos subido en la sección de Bonus (leer al menos el 1er acuerdo antes de pasar al siguiente ejercicio)

**Meditación complementaria:**
Los 4 ACUERDOS TOLTECAS - Meditación Guiada Vivencial
https://www.youtube.com/watch?v=nn_VJ7ew2cc

☝ Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (ACUERDOS) para saber que has completado esta parte y pases a agendar tu séptima sesión 1:1.

¡Te veo pronto!""",
                "questions": []
            }
        ])
    )
    db.add(exercise_1_2)
    db.flush()
    exercises_created.append(f"Ejercicio 1.2 (ID: {exercise_1_2.id})")
    print(f"  ✅ Ejercicio 1.2: La voz interior créé (ID: {exercise_1_2.id})")
    
    # ========================================================================================
    # EJERCICIO #2: SER (Thème 2)
    # ========================================================================================
    print("\n📝 Création de l'Ejercicio #2: Ser...")
    
    exercise_2_1 = Exercise(
        title="Ejercicio 2.1: Mi ser",
        parent_title="Ejercicio #2: Ser",
        instructions="""<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Rompiendo Barreras</h2>

<p style="font-size: 1.1em; margin-bottom: 16px;">Este ejercicio tiene como propósito ayudarte a <strong>reconocer las capas</strong> que te han alejado de tu verdadera esencia. Muchas veces sin cuestionarlo vivimos desde lo que "deberíamos ser" en lugar de lo que realmente somos.</p>

<p style="margin-bottom: 16px;">El despertar auténtico no es cambiar quién eres, sino reconectar con lo que siempre has sido.</p>

<p style="margin-bottom: 16px;"><strong>Tiempo estimado:</strong> 30 minutos</p>
</div>""",
        order_number=1,
        theme_id=THEME_2_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identifica lo aprendido vs lo auténtico",
                "instructions": """Siéntate en un lugar tranquilo, cierra los ojos y respira profundamente. Permítete explorar aquellas partes de ti que sientes que no provienen de tu elección libre, sino de lo que aprendiste o absorbiste de tu entorno (familia, amigos, sociedad).

Pregúntate:
• ¿Cuáles de mis rasgos, gustos o creencias provienen de mi esencia y cuáles se deben a la influencia de otros?
• ¿Cuándo me siento más auténtic@ y cuándo siento que actúo para complacer a alguien o encajar en un grupo?
• ¿Qué situaciones o comentarios de mi pasado me empujaron a ser o comportarme de cierta manera, incluso si no resonaba realmente conmigo?

Escribe lo que surja, sin juzgarte. Sé honest@ contigo mism@. Observa si hay patrones o rasgos que en realidad no te representan pero que sigues repitiendo por costumbre o temor al rechazo.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué partes de ti provienen de la influencia de otros y no de tu esencia?"
                    }
                ]
            },
            {
                "title": "Paso 2: Reconoce tu verdadero ser",
                "instructions": """Ahora que has reflexionado sobre lo que quizás no es tuyo, identifica los rasgos y cualidades que sí sientes como parte de tu verdadero ser.

Pregúntate:
• ¿Qué aspectos de mi personalidad me hacen sentir libre y genuino@?
• ¿Cuándo experimento alegría y fluidez porque estoy siendo congruente con mis deseos y valores?
• Si pudiera describirme a mí mismo/a sin las etiquetas que otros me han puesto, ¿cómo lo haría?

Escribe tus respuestas y observarlas. Reconoce que tienes derecho a soltar lo que no te hace bien y a cultivar lo que te hace sentir pleno@. Este paso te ayudará a orientar tus decisiones y acciones hacia lo que realmente define tu esencia, en lugar de guiarte por las expectativas o miedos que has heredado de tu entorno.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe tu verdadero ser sin las etiquetas que otros te han puesto"
                    }
                ]
            }
        ])
    )
    db.add(exercise_2_1)
    db.flush()
    exercises_created.append(f"Ejercicio 2.1 (ID: {exercise_2_1.id})")
    print(f"  ✅ Ejercicio 2.1: Mi ser créé (ID: {exercise_2_1.id})")
    
    # EJERCICIO 2.2: Autoconciencia
    exercise_2_2 = Exercise(
        title="Ejercicio 2.2: Cultivando la autoconciencia",
        parent_title="Ejercicio #2: Ser",
        instructions="""<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Cultivando la Autoconciencia</h2>

<p style="margin-bottom: 16px;"><strong>Tiempo estimado:</strong> 30 minutos</p>
</div>""",
        order_number=2,
        theme_id=THEME_2_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Observa tu autenticidad",
                "instructions": """Siéntate en un lugar tranquilo, cierra los ojos y respira profundamente. Lleva tu atención a tu interior.

Pregúntate:
• ¿Cuándo fue la última vez que sentí que estaba actuando desde mi autenticidad?
• ¿Qué tanto de lo que hago en mi día a día refleja lo que realmente quiero y no solo lo que se espera de mí?
• ¿En qué momentos me he sentido desconectado/a de mí mismo/a?

Escribe tus respuestas sin filtros, observando si hay patrones en tu forma de actuar.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cuándo actúas desde tu autenticidad y cuándo te sientes desconectado/a?"
                    }
                ]
            },
            {
                "title": "Paso 2: Identifica patrones limitantes",
                "instructions": """Piensa en situaciones en las que sentiste que no estabas actuando desde tu verdadero ser. Pregúntate:

• ¿En qué momentos he tomado decisiones basadas en lo que los demás esperan de mí?
• ¿He sentido que necesito la validación de otros para sentirme valioso@?
• ¿Qué miedos aparecen cuando intento ser más auténtico@?

Anota ejemplos específicos en los que sentiste que no estabas alineado@ con tu esencia.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe situaciones donde no actuaste desde tu verdadero ser"
                    }
                ]
            },
            {
                "title": "Paso 3: Diferencia lo que deseas de lo aprendido",
                "instructions": """A veces, perseguimos metas que en el fondo no nos llenan. Es momento de reflexionar sobre qué realmente deseas y qué has aprendido a desear por presión social.

Pregúntate:
• Si no tuviera miedo al juicio de los demás, ¿qué haría diferente en mi vida?
• ¿Cuáles son los sueños o deseos que he ignorado porque no se alinean con lo que otros esperan de mí?
• ¿Cómo puedo empezar a tomar decisiones más alineadas con mi verdad interna?

Haz una lista de las cosas que realmente te hacen feliz y que deseas para ti mismo@, sin importar la opinión externa.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Lista las cosas que realmente deseas, sin importar la opinión externa"
                    }
                ]
            },
            {
                "title": "Paso 4: Compromiso con la autoconciencia",
                "instructions": """Para fortalecer la autoconciencia, es importante aprender a observar sin juzgar. A partir de hoy, comprométete a practicar lo siguiente:

💡 Observar sin etiquetar: Durante el día, detente unos segundos y pregúntate: ¿Estoy actuando desde mi esencia o desde el miedo a decepcionar a otros?

💡 Validar tu propia voz: Cuando surja una decisión importante, en lugar de buscar aprobación externa, reflexiona: ¿Esto realmente me hace feliz a mí?

💡 Escribir una afirmación de autenticidad: Crea una frase que refuerce tu compromiso con tu verdadero ser.

📌 Ejemplo de afirmación: "Hoy elijo actuar desde mi autenticidad. Mi valor no depende de la aprobación de los demás, sino de ser fiel a lo que soy."""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu afirmación de autenticidad"
                    }
                ]
            }
        ])
    )
    db.add(exercise_2_2)
    db.flush()
    exercises_created.append(f"Ejercicio 2.2 (ID: {exercise_2_2.id})")
    print(f"  ✅ Ejercicio 2.2: Autoconciencia créé (ID: {exercise_2_2.id})")
    
    # EJERCICIO 2.3: Vulnerabilidad
    exercise_2_3 = Exercise(
        title="Ejercicio 2.3: Abrazando la vulnerabilidad",
        parent_title="Ejercicio #2: Ser",
        instructions="""<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Abrazando la Vulnerabilidad</h2>

<p style="margin-bottom: 16px;"><strong>Tiempo estimado:</strong> 30 minutos</p>
</div>""",
        order_number=3,
        theme_id=THEME_2_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Reconoce cómo ocultas tu vulnerabilidad",
                "instructions": """Antes de poder abrazar nuestra vulnerabilidad, debemos reconocer cómo la hemos estado ocultando.

Pregúntate:
¿Cómo suelo protegerme para que los demás no vean mi vulnerabilidad?

• Me muestro fuerte y no dejo que los demás vean lo que me afecta
• Evito hablar de mis sentimientos y me guardo todo
• Trato de ser perfecto/a para que nadie me critique
• Me distancio emocionalmente de los demás para no ser herido/a

Escribe cuál de estas estrategias usas con más frecuencia y cómo ha afectado tu manera de relacionarte con los demás.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo ocultas tu vulnerabilidad y cómo te ha afectado?"
                    }
                ]
            },
            {
                "title": "Paso 2: Explora una situación vulnerable",
                "instructions": """Piensa en una situación reciente donde sentiste vulnerabilidad pero intentaste ocultarlo.

Pregúntate:
• ¿Qué te habría gustado decir en ese momento si no tuvieras miedo al juicio?
• ¿Qué pasaría si permitieras que alguien de confianza conociera esa parte de ti?

Escribe las respuestas y luego crea un mensaje dirigido a ti mismo@ desde la compasión, recordándote que está bien sentir y mostrarse tal como eres.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe una situación vulnerable y qué te habría gustado expresar"
                    },
                    {
                        "type": "text",
                        "question": "Escribe un mensaje de compasión para ti mismo/a"
                    }
                ]
            },
            {
                "title": "Paso 3: Acción concreta",
                "instructions": """Para empezar a abrazar tu vulnerabilidad, elige una acción concreta que puedas hacer hoy:

✅ Compartir un pensamiento o emoción real con alguien de confianza
✅ Admitir que necesitas ayuda en algo en lugar de tratar de hacerlo sol@
✅ Dejar de esconder una parte de ti que te hace único@

💡 Ejemplo: En lugar de decir "Estoy bien" cuando no lo estás, intenta decir "Hoy ha sido un día difícil, pero estoy intentando afrontarlo."

Escribe tu compromiso y cómo crees que esto puede ayudarte a sentirte más libre y auténtic@.

**Meditación complementaria:**
CONSTELACIÓN FAMILIAR para SANAR tu ENERGÍA y la de tu FAMILIA - Meditación Guiada Vivencial
https://www.youtube.com/watch?v=ZuTyYBDl82k

☝ Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (SER) para saber que has completado esta parte.

¡Te veo pronto!""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu compromiso para abrazar tu vulnerabilidad"
                    }
                ]
            }
        ])
    )
    db.add(exercise_2_3)
    db.flush()
    exercises_created.append(f"Ejercicio 2.3 (ID: {exercise_2_3.id})")
    print(f"  ✅ Ejercicio 2.3: Vulnerabilidad créé (ID: {exercise_2_3.id})")
    
    # ========================================================================================
    # EJERCICIO #3: REALIDAD (Thème 3)
    # ========================================================================================
    print("\n📝 Création de l'Ejercicio #3: Realidad...")
    
    exercise_3_1 = Exercise(
        title="Ejercicio 3.1: La vida que sí quiero",
        parent_title="Ejercicio #3: Realidad",
        instructions="""<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Construir la Vida que Sí Quiero</h2>

<p style="font-size: 1.1em; margin-bottom: 16px;">Este ejercicio tiene como propósito ayudarte a tomar consciencia de cómo has construido tu vida hasta ahora y cómo puedes comenzar a moldearla de manera más alineada con tu autenticidad y deseos reales.</p>

<p style="margin-bottom: 16px;">Este ejercicio no se trata de rechazar todo lo aprendido, sino de mirarlo con consciencia y preguntarnos: <strong>¿Esto realmente es lo que quiero? ¿O es lo que aprendí a querer?</strong></p>

<p style="margin-bottom: 16px;"><strong>Tiempo estimado:</strong> 30 minutos</p>
</div>""",
        order_number=1,
        theme_id=THEME_3_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Observa tu vida actual",
                "instructions": """Antes de construir la vida que sí quieres, primero observa la vida que tienes ahora. Sin juzgarte, responde con honestidad:

• ¿Qué aspectos de mi vida actual disfruto y quiero mantener?
• ¿Qué partes de mi vida siento que no reflejan mi verdadero ser?
• ¿En qué momentos siento que me desconecto de lo que realmente quiero?

✍️ Escribe lo que descubras. Esto te ayudará a ver qué áreas necesitan más atención.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué disfrutas de tu vida actual y qué no refleja tu verdadero ser?"
                    }
                ]
            },
            {
                "title": "Paso 2: Define tu visión",
                "instructions": """Para construir una vida auténtica, necesitas saber qué es importante para ti. En este paso, reflexiona sobre:

• Tus valores esenciales – ¿Qué principios guían tu vida? (Ejemplo: libertad, honestidad, creatividad, amor, crecimiento)
• Tus verdaderos deseos – ¿Qué te gustaría hacer si no tuvieras miedo al juicio o al fracaso?
• Las emociones que quieres sentir en tu día a día – ¿Cómo quieres vivir y sentirte en tu rutina?

✍️ Haz una lista con tus respuestas. Esto será tu guía para tomar decisiones alineadas con lo que realmente quieres.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Define tus valores, deseos y las emociones que quieres sentir"
                    }
                ]
            },
            {
                "title": "Paso 3: Identifica obstáculos",
                "instructions": """Muchas veces, no avanzamos porque hay miedos, creencias limitantes o patrones que nos mantienen en la misma rutina. Pregúntate:

• ¿Qué pensamientos o creencias me han impedido avanzar?
• ¿De dónde vienen esas creencias? ¿Son realmente mías o las aprendí de alguien más?
• ¿Qué puedo decirme a mí mismo/a en lugar de esas creencias para avanzar con más seguridad?

✍️ Ejemplo:
Si piensas "No soy lo suficientemente bueno para hacer esto", puedes reemplazarlo por:
"Estoy en proceso de crecimiento y cada paso que doy me acerca a la vida que quiero.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué creencias te frenan y cómo las transformarás?"
                    }
                ]
            },
            {
                "title": "Paso 4: Define acciones concretas",
                "instructions": """Ahora que tienes más claridad sobre lo que quieres y lo que te frena, es momento de pasar a la acción. Define 3 pequeñas acciones que puedas hacer esta semana para acercarte a la vida que quieres.

💡 Ejemplo de acciones concretas:
✅ Si quiero cambiar de trabajo → Buscar información sobre lo que me interesa
✅ Si quiero rodearme de personas más alineadas conmigo → Empezar a poner límites con relaciones que me desgastan
✅ Si quiero más bienestar → Crear un pequeño hábito de autocuidado diario

✍️ Escribe tus 3 acciones y comprométete a hacer al menos una esta semana.

(Te sugiero que hagas una lista de cómo deseas que se vea tu vida y elijas por mes solo 3 acciones que puedes modificar, son solo 3 cambios para 30 días, a largo plazo tendrás grandes resultados)""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Lista tus 3 acciones concretas para esta semana"
                    }
                ]
            },
            {
                "title": "Paso 5: Crea tu afirmación",
                "instructions": """Para mantener el rumbo, necesitas recordarte a ti mismo@ por qué elegiste este camino. Cierra este ejercicio con una afirmación que te motive a seguir avanzando.

Ejemplo de afirmaciones:
• "Cada paso que doy me acerca a la vida que realmente quiero y merezco."
• "Mi autenticidad es mi mayor poder, y cada día elijo vivir desde ella."
• "No tengo que hacerlo todo de golpe, pero puedo avanzar un poco cada día."

✍️ Escribe tu afirmación en un lugar visible y léela cada día como recordatorio de tu camino.

**Meditación complementaria:**
MANIFIESTA tu FUTURO DESEADO | CONECTA con tu YO FUTURO - Meditación Guiada Vivencial
https://www.youtube.com/watch?v=WB7zsan7WYs

☝ Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (REALIDAD) para saber que has completado esta parte y pases a agendar tu octava sesión 1:1.

¡Te veo pronto!""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu afirmación personal"
                    }
                ]
            }
        ])
    )
    db.add(exercise_3_1)
    db.flush()
    exercises_created.append(f"Ejercicio 3.1 (ID: {exercise_3_1.id})")
    print(f"  ✅ Ejercicio 3.1: La vida que sí quiero créé (ID: {exercise_3_1.id})")
    
    db.commit()
    
    print("\n" + "=" * 70)
    print("✅ TOUS LES EXERCICES DU MODULE 4 CRÉÉS AVEC SUCCÈS!")
    print("=" * 70)
    print(f"📚 Thème 1 (Rompiendo barreras): 2 exercices")
    print(f"📚 Thème 2 (Despertar auténtico): 3 exercices")
    print(f"📚 Thème 3 (Mapa de acción): 1 exercice")
    print(f"\n✨ Total: 6 exercices créés!")
    print("\n🎉 Module 4 est maintenant COMPLET (21 cartes + 6 exercices)!")

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        create_all_exercises_module4(db)
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

