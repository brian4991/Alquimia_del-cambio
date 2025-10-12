"""
Script pour ajouter les 3 derniers subtemas du Thème 2 Module 3 - fidèle au texte
Subtemas 3-5: Negociando necesidades + Mi persona equilibrio + Fundamentos de bienestar
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sqlalchemy.orm import Session
from database import SessionLocal
from models import ThemeCard

# Styles
FONT = "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
C_TEXT = "#2d2d2d"
C_TITLE = "#6b745a"
C_ACCENT = "#a28d72"
C_BG_LIGHT = "#f5f5f0"
C_BG_GRAY = "#cbcbcc"

def css():
    return f'color: {C_TEXT}; font-family: {FONT}; line-height: 1.8; max-width: 800px;'

def add_remaining_subtemas(db: Session, theme_id: int, starting_order: int):
    """Ajouter les 3 derniers subtemas"""
    print("\n🎴 Ajout des subtemas 3-5 au Thème 2...")
    
    cards = []
    order = starting_order
    
    # Subtema 3: Negociando necesidades (cards 14-17)
    cards.extend([
        {
            "title": "Subtema 3: Negociando Necesidades - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 3: Negociando Necesidades</h1>

<p style="margin-bottom: 16px;">En todas nuestras relaciones, ya sean amorosas, familiares o de amistad, uno de los aspectos más fundamentales para construir conexiones saludables es aprender a negociar nuestras necesidades.</p>

<p style="margin-bottom: 16px;">Negociar no significa ceder en todo, ni hacer que nuestras necesidades sean menos importantes. Más bien, se trata de aprender a comunicarlas de manera efectiva, encontrar puntos de acuerdo con los demás y, al mismo tiempo, mantener nuestro bienestar emocional.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Un Aspecto Esencial</h3>
<p style="margin-bottom: 0;">Las necesidades son parte esencial de lo que somos. Todos tenemos deseos, expectativas y deseos fundamentales que necesitamos satisfacer para sentirnos felices, cómodos y seguros. Sin embargo, muchas veces no somos conscientes de qué tan importante es comunicar nuestras necesidades de forma clara y asertiva.</p>
</div>

<p style="margin-bottom: 16px;">Por otro lado, también podemos temer que, al expresar lo que necesitamos, estemos siendo demasiado demandantes o que el otro no nos entienda. Esto puede generar conflictos internos y con los demás.</p>
</div>""",
            "card_type": "theory",
            "order_number": order
        },
        {
            "title": "Negociando Necesidades - Parte 2",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Qué Son Nuestras Necesidades y Cómo Identificarlas?</h2>

<p style="margin-bottom: 16px;">Las necesidades pueden ser emocionales, físicas, psicológicas y sociales. A veces, lo que necesitamos en una relación es simplemente sentirnos escuchados, apoyados emocionalmente o que se nos dé espacio para ser nosotros mismos.</p>

<p style="margin-bottom: 16px;">En otras ocasiones, podemos necesitar tiempo para nosotros, respeto por nuestras decisiones o simplemente que la otra persona sea más comprometida con ciertos aspectos de la relación.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Autoconocimiento</h3>
<p style="margin-bottom: 0;">Es importante que antes de aprender a negociar nuestras necesidades, nos conozcamos a nosotros mismos. ¿Qué es lo que realmente necesito de una relación? ¿Qué aspectos no estoy dispuesto a comprometer porque son esenciales para mi bienestar? Este proceso de autoconocimiento nos permite identificar nuestras necesidades no negociables, esas que son fundamentales para nuestra salud emocional y las que nos hacen sentir bien en la relación.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "Negociando Necesidades - Parte 3",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Negociables vs. No Negociables</h2>

<p style="margin-bottom: 16px;">Dentro de nuestras necesidades, es clave diferenciar entre lo que es negociable y lo que no lo es.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">Necesidades No Negociables</h4>
<p style="margin-bottom: 0;">Las necesidades no negociables son aquellas que son fundamentales para el bienestar emocional y psicológico. Estas pueden incluir el respeto mutuo, la honestidad, la fidelidad, la comunicación abierta o la seguridad emocional. Si alguna de estas necesidades no se satisface, la relación probablemente sufrirá.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">Necesidades Negociables</h4>
<p style="margin-bottom: 12px;">Por otro lado, las necesidades negociables son aquellas que no comprometen nuestra salud emocional ni nuestro bienestar, pero que pueden ser más flexibles.</p>
<p style="margin-bottom: 0;">Por ejemplo, tal vez prefieras pasar más tiempo juntos, pero si la otra persona no puede hacerlo por razones laborales, en muchos casos puedes negociar este aspecto sin que afecte la relación. Es importante ser realista y saber cuándo ceder y cuándo mantenerse firme.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 2
        },
        {
            "title": "Negociando Necesidades - Parte 4",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">La Importancia de la Comunicación Efectiva</h2>

<p style="margin-bottom: 16px;">La comunicación es uno de los pilares de cualquier negociación exitosa. Para que nuestras necesidades sean escuchadas y respetadas, necesitamos expresarlas de manera clara, honesta y sin miedo.</p>

<p style="margin-bottom: 16px;">Es vital que evitemos suposiciones y, en su lugar, utilicemos un lenguaje asertivo que permita al otro comprender lo que necesitamos sin hacerlos sentir atacados ni criticados.</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 24px 0;">
<h4 style="color: {C_TITLE}; margin-top: 0;">Un ejemplo práctico</h4>
<p style="margin-bottom: 12px;">Tal vez sientas que necesitas más tiempo de calidad con tu pareja, pero si no comunicas esa necesidad de forma abierta, la otra persona puede no entender la importancia que tiene para ti.</p>
<p style="margin-bottom: 0;">En lugar de reprochar o culpar, explica cómo te sientes y lo que realmente necesitas: "Me he dado cuenta de que me siento más feliz y conectado cuando pasamos tiempo juntos sin distracciones, ¿podemos encontrar tiempo para eso esta semana?" Este tipo de enfoque permite una conversación constructiva y sin presiones.</p>
</div>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Recomendaciones para una negociación efectiva:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 12px; border-radius: 5px;">
<p style="margin: 0;"><strong>1. Escucha activa:</strong> Antes de expresar tus propias necesidades, escucha las del otro. La negociación es un proceso de dos vías.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 12px; border-radius: 5px;">
<p style="margin: 0;"><strong>2. Mantén la calma:</strong> Las discusiones sobre necesidades pueden ser intensas. Mantén la calma, evita los gritos o acusaciones, y utiliza un tono sereno y respetuoso.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 12px; border-radius: 5px;">
<p style="margin: 0;"><strong>3. Sé flexible pero firme:</strong> Reconoce cuándo una necesidad puede ser negociable, pero no tengas miedo de ser firme cuando se trata de lo que realmente importa.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 12px; border-radius: 5px;">
<p style="margin: 0;"><strong>4. Crea un espacio seguro:</strong> Fomenta un ambiente en el que ambas personas se sientan cómodas expresando sus necesidades.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 12px; border-radius: 5px;">
<p style="margin: 0;"><strong>5. Establece acuerdos claros:</strong> Una vez que hayas negociado tus necesidades, asegúrate de acordar lo que ambas partes están dispuestas a hacer.</p>
</div>

<p style="margin-top: 24px; margin-bottom: 16px;">Negociar nuestras necesidades no solo se trata de conseguir lo que queremos, sino de crear relaciones más equilibradas, respetuosas y sanas, donde ambas partes se sientan valoradas y escuchadas. Es un proceso que requiere paciencia, práctica y, sobre todo, el deseo genuino de fortalecer la relación de manera equitativa.</p>
</div>""",
            "card_type": "practical",
            "order_number": order + 3
        },
        {
            "title": "Ejercicio: Negociando Necesidades",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Conoce tus Negociables vs No Negociables</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a conocer tus negociables vs no negociables.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2: Fundamentos</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.3: Negociando necesidades</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 4
        }
    ])
    
    order += 5
    
    # Subtema 4: Mi persona equilibrio - Ce subtema est TRÈS long, je vais le diviser en plusieurs cards
    # Continuera dans le prochain message...
    
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
    print(f"✅ {len(cards)} cards ajoutées (Subtema 3)")
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 AJOUT DES SUBTEMAS 3-5 AU THÈME 2 MODULE 3")
        print("=" * 70)
        
        # ID du thème 2 créé précédemment
        THEME_ID = 11  # Thème 2 créé par le script précédent
        STARTING_ORDER = 14  # Commencer après les 13 cards existantes
        
        num_cards = add_remaining_subtemas(db, THEME_ID, STARTING_ORDER)
        
        print("\n" + "=" * 70)
        print("✅ SUBTEMA 3 AJOUTÉ")
        print("=" * 70)
        print(f"📚 {num_cards} cards ajoutées")
        print(f"\n⚠️  Il manque encore 2 subtemas (Mi persona equilibrio, Fundamentos de bienestar)")
        print("🎯 Je vais créer un 3ème script pour finir")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

