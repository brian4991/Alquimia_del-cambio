import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import EditableSection from './EditableSection';
import { config } from '../config';

const LandingPage = () => {
  const navigate = useNavigate();
  const [openFaq, setOpenFaq] = useState(null);
  const [pageContent, setPageContent] = useState({});
  const [loading, setLoading] = useState(true);

  // Load page content
  useEffect(() => {
    loadPageContent();
  }, []);

  const loadPageContent = async () => {
    try {
      const response = await fetch(`${config.apiUrl}/api/page-content/retiro`);
      if (response.ok) {
        const data = await response.json();
        setPageContent(data.sections || {});
      }
    } catch (error) {
      console.error('Error loading page content:', error);
    } finally {
      setLoading(false);
    }
  };

  const saveSection = async (sectionKey, content) => {
    const updatedContent = {
      ...pageContent,
      [sectionKey]: content
    };

    try {
      const response = await fetch(`${config.apiUrl}/api/page-content/retiro`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ sections: updatedContent })
      });

      if (response.ok) {
        setPageContent(updatedContent);
        alert('Contenido guardado correctamente');
      } else {
        throw new Error('Failed to save content');
      }
    } catch (error) {
      console.error('Error saving content:', error);
      throw error;
    }
  };

  const toggleFaq = (index) => {
    setOpenFaq(openFaq === index ? null : index);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="fixed top-0 w-full bg-stone-50/95 backdrop-blur-sm shadow-sm z-50 border-b border-stone-200">
        <div className="container mx-auto px-6 py-4 flex justify-between items-center">
          <div className="flex items-center space-x-4">
            <img 
              src="/Logo nr.png" 
              alt="Cambio de Paradigma" 
              className="w-12 h-12 object-contain"
              onError={(e) => {
                e.target.style.display = 'none';
              }}
            />
            <div>
              <h1 className="text-2xl font-bold text-gray-800">Cambio de Paradigma</h1>
              <p className="text-xs text-taupe-600">Retiro Ámate</p>
            </div>
          </div>
          <button
            onClick={() => navigate('/login')}
            style={{borderColor: '#6b745a', color: '#6b745a'}}
            className="bg-transparent border-2 px-6 py-2 rounded-full hover:text-white transition-all font-semibold"
            onMouseEnter={(e) => e.target.style.backgroundColor = '#6b745a'}
            onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}
          >
            Iniciar sesión
          </button>
        </div>
      </header>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-6 bg-white">
        <div className="container mx-auto max-w-4xl text-center">
          <div className="w-32 h-32 bg-gray-200 rounded-full mx-auto mb-8 flex items-center justify-center text-xs text-gray-600">
            [LOGO-002]
          </div>
          <EditableSection
            sectionKey="hero_title"
            content={pageContent.hero_title}
            onSave={saveSection}
          >
            <h1 className="text-4xl md:text-6xl font-bold text-gray-800 mb-8 leading-tight">
              Despierta la luz que habita en ti, eleva tu autoestima y sana desde adentro en un lugar seguro y único.
            </h1>
          </EditableSection>
          <EditableSection
            sectionKey="hero_subtitle"
            content={pageContent.hero_subtitle}
            onSave={saveSection}
          >
            <p className="text-xl md:text-2xl text-gray-600 mb-10">
              Vive una experiencia transformadora de amor propio, sanidad y bienestar emocional.
            </p>
          </EditableSection>
          <button 
            style={{backgroundColor: '#6b745a'}}
            className="text-white px-12 py-4 rounded-full text-lg font-semibold hover:opacity-90 transition-all shadow-lg hover:shadow-xl transform hover:scale-105"
          >
            RESERVA TU LUGAR
          </button>
        </div>
      </section>

      {/* Date & Location */}
      <section className="py-16" style={{backgroundColor: '#F5F5F0'}}>
        <div className="container mx-auto max-w-4xl text-center px-6">
          <EditableSection
            sectionKey="date_location"
            content={pageContent.date_location}
            onSave={saveSection}
          >
            <div>
              <h2 className="text-3xl md:text-5xl font-bold text-gray-800 mb-4">
                27, 28 de Febrero y 1 de Marzo 2026
              </h2>
              <p className="text-2xl text-gray-600">
                Isla de Barú, Cartagena - Colombia
              </p>
            </div>
          </EditableSection>
        </div>
      </section>

      {/* Experience Description */}
      <section className="py-20 bg-white">
        <div className="container mx-auto max-w-5xl text-center px-6">
          <EditableSection
            sectionKey="experience_description"
            content={pageContent.experience_description}
            onSave={saveSection}
          >
            <h2 className="text-3xl md:text-4xl font-bold text-gray-800 mb-8 leading-relaxed">
              Vive una experiencia única y transformadora durante 3 días, en un paraíso rodeado de mar donde viviremos una fusión de sanidad emocional, espiritualidad, conexión y plenitud
            </h2>
          </EditableSection>
        </div>
      </section>

      {/* Why This Retreat */}
      <section className="py-20" style={{backgroundColor: '#F9F6F3'}}>
        <div className="container mx-auto max-w-6xl px-6">
          <EditableSection
            sectionKey="why_retreat_title"
            content={pageContent.why_retreat_title}
            onSave={saveSection}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16">
              ¿POR QUÉ EL RETIRO ÁMATE ES PARA TI?
            </h2>
          </EditableSection>
          <div className="grid md:grid-cols-2 gap-8">
            {[
              'Sabes que necesitas soltar y sanar heridas del pasado y crear una vida consciente, saludable, donde reine el bienestar, el que tú necesites y elijas para ti.',
              'Sientes un deseo profundo de activar y fortalecer tu poder interior, llevándote a un nivel más alto de autoestima y confianza.',
              'Mereces sentirte amada, respetada y digna de milagros y bendiciones.',
              'Deseas profundizar en tu autoconocimiento, conectar contigo misma y descubrir tu propósito.',
              'Entiendes que la sanación personal es la clave para mejorar todas tus relaciones, fomentando conexiones más saludables.',
              'Necesitas una tribu de mujeres, donde te traten con amor y respeto, conocer mujeres que buscan lo mismo que tú y que sus vidas y vivencias transformen la tuya.',
              'Anhelas desconectar de la rutina diaria y conectar con tu ser, con otras mujeres y con la naturaleza, lista para dar un paso decisivo hacia una vida más transformadora.'
            ].map((text, index) => (
              <div key={index} className="flex items-start space-x-4">
                <div 
                  style={{backgroundColor: '#6b745a'}}
                  className="flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center text-white font-bold shadow-md"
                >
                  •
                </div>
                <p className="text-gray-700 text-lg leading-relaxed">{text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Image Banner 1 */}
      <section className="py-12 bg-white">
        <div className="container mx-auto px-6">
          <div className="w-full h-96 bg-gray-200 flex items-center justify-center text-gray-600">
            [IMG-HERO-001: Image principale du retiro - femmes en méditation au bord de la mer]
          </div>
        </div>
      </section>

      {/* Logo Section */}
      <section className="py-12 bg-white">
        <div className="container mx-auto max-w-sm px-6">
          <div className="w-full h-32 bg-gray-200 flex items-center justify-center text-gray-600 text-xs">
            [LOGO-003: Logo secondaire]
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section className="py-20" style={{backgroundColor: '#eef2ec'}}>
        <div className="container mx-auto max-w-4xl px-6">
          <EditableSection
            sectionKey="pricing_header"
            content={pageContent.pricing_header}
            onSave={saveSection}
          >
            <div className="text-center mb-12">
              <div className="inline-block bg-white px-6 py-3 rounded-full mb-6 shadow-md border-2" style={{borderColor: '#6b745a'}}>
                <span style={{color: '#6b745a'}} className="font-bold text-lg">¡Sólo para mujeres!</span>
              </div>
              <h2 className="text-4xl md:text-5xl font-bold text-gray-800 mb-4">
                DESCUENTO DE PREVENTA
              </h2>
              <p className="text-gray-600 text-lg mb-2">(Por tiempo limitado)</p>
            </div>
          </EditableSection>

          <div className="bg-white rounded-3xl shadow-2xl p-10 mb-8 border border-stone-200">
            <EditableSection
              sectionKey="pricing_details"
              content={pageContent.pricing_details}
              onSave={saveSection}
            >
              <div>
                <div className="grid md:grid-cols-2 gap-8 mb-8">
                  <div className="text-center border-r border-gray-200">
                    <p className="text-gray-600 mb-2">Residentes fuera de Colombia</p>
                    <p className="text-2xl text-gray-400 line-through mb-2">$1,299 USD</p>
                    <p style={{color: '#6b745a'}} className="text-5xl font-bold">$1,099 USD</p>
                  </div>
                  <div className="text-center">
                    <p className="text-gray-600 mb-2">Residentes en Colombia</p>
                    <p className="text-2xl text-gray-400 line-through mb-2">$4,299,000 COP</p>
                    <p style={{color: '#6b745a'}} className="text-5xl font-bold">$3,999,000 COP</p>
                  </div>
                </div>

                <div className="text-center mb-8">
                  <p className="text-gray-700 mb-4">Pago completo o pago a cuotas</p>
                  <p className="text-sm text-gray-600 mb-6">
                    En cuotas el primer pago se hace a la hora de la inscripción, y las siguientes cuotas se cobran cada 30 días.
                  </p>
                </div>
              </div>
            </EditableSection>

            <div className="text-center">
              <button 
                style={{backgroundColor: '#6b745a'}}
                className="text-white px-12 py-4 rounded-full text-lg font-semibold hover:opacity-90 transition-all shadow-lg hover:shadow-xl transform hover:scale-105 mb-4"
              >
                QUIERO REALIZAR MI PAGO
              </button>
              <p className="text-sm text-gray-600 mt-4">
                Opciones de pago: Contamos con diferentes métodos de pago (cuotas) y el pago se puede realizar por tarjeta de crédito o débito.
              </p>
              <p style={{color: '#6b745a'}} className="font-semibold mt-4">
                % Descuento para grupos a partir de 4 personas %
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* What's Included & What to Expect - 2 colonnes */}
      <section className="py-20 bg-white">
        <div className="container mx-auto max-w-7xl px-6">
          <EditableSection
            sectionKey="three_days_title"
            content={pageContent.three_days_title}
            onSave={saveSection}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16">
              ¡3 DÍAS QUE LO CAMBIARÁN TODO!
            </h2>
          </EditableSection>
          <div className="grid md:grid-cols-2 gap-0">
            {/* Colonne 1: Que Incluye - Background sage-100 */}
            <div className="p-12" style={{backgroundColor: '#eef2ec'}}>
              <h3 className="text-3xl font-bold text-center mb-8" style={{
                backgroundColor: '#6b745a',
                color: 'white',
                padding: '12px 24px',
                display: 'inline-block',
                width: '100%',
                textAlign: 'center'
              }}>
                ¿QUÉ INCLUYE?
              </h3>
              <div className="space-y-4">
                {[
                  '3 días de hospedaje.',
                  'Transporte acuático desde Cartagena al hotel de retiro ida y regreso.',
                  'Cóctel de bienvenida.',
                  '3 comidas al día: desayuno, almuerzo y cena.',
                  'Kit de bienvenida: sorpresas y regalos que harán mágicos tus días. PD: recuerda dejar un espacio en tu maleta para todas las cosas increíbles que llevarás de regreso a casa.',
                  'Servicio diario de limpieza.',
                  'Baño de mar (experiencia).',
                  'Arte terapia.',
                  'Sesión de Zumba.',
                  'Participación en todos los talleres enfocados en sanidad interior y el fortalecimiento de la autoestima y confianza. (no se desglosan porque hacen parte de la privacidad y experiencia exclusiva del retiro).',
                  'Participación en cada una de las actividades de recreación que el retiro ha preparado para hacer inolvidable esta experiencia.'
                ].map((item, index) => (
                  <div key={index} className="flex items-start space-x-3">
                    <div 
                      style={{backgroundColor: '#6b745a'}}
                      className="flex-shrink-0 w-6 h-6 rounded-full flex items-center justify-center text-white text-sm font-bold shadow-md"
                    >
                      ✓
                    </div>
                    <p className="text-gray-800 leading-relaxed">{item}</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Colonne 2: Que Esperar - Background taupe-100 */}
            <div className="p-12" style={{backgroundColor: '#f4f2ed'}}>
              <h3 className="text-3xl font-bold text-center mb-8" style={{
                backgroundColor: '#a28d72',
                color: 'white',
                padding: '12px 24px',
                display: 'inline-block',
                width: '100%',
                textAlign: 'center'
              }}>
                ¿QUÉ ESPERAR?
              </h3>
              <div className="space-y-4">
                {[
                  'Un espacio seguro para conectar con otras mujeres con el mismo propósito de crecer en su mejor versión.',
                  'Actividades de conexión con tu cuerpo - alma - espíritu.',
                  'Herramientas prácticas para aplicar en la vida diaria para mantener la sanidad emocional y vivir en plenitud.',
                  'Arte Terapia para sanar el alma.',
                  'Meditación, mindfulness y bioenergética.',
                  'Conectar con tu esencia, autenticidad y propósito de vida.',
                  'Tiempos de sanidad, renovación y crecimiento.',
                  'Espacios de recreación, risas, zumba, música y juegos.',
                  'Una comprensión más profunda de ti misma, de tus necesidades y tus deseos, lo que te permitirá tomar decisiones más alineadas con tus valores y metas.',
                  'Un cambio radical de perspectiva en la forma en que ves tu vida, relaciones y desafíos, permitiéndote una actitud más positiva y resiliente.',
                  'Un empoderamiento genuino de reconocer tu fuerza interior que te llevará a tomar el control de tu vida.',
                  'Un tiempo para desconectar con tu exterior y rutina diaria para conectar contigo y con tu propósito de vida.',
                  'Sanar, soltar y transformar tu vida.'
                ].map((item, index) => (
                  <div key={index} className="flex items-start space-x-3">
                    <div 
                      style={{backgroundColor: '#a28d72'}}
                      className="flex-shrink-0 w-6 h-6 rounded-full flex items-center justify-center text-white text-sm font-bold shadow-md"
                    >
                      •
                    </div>
                    <p className="text-gray-800 leading-relaxed">{item}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <div className="text-center mt-12">
            <button 
              style={{backgroundColor: '#6b745a'}}
              className="text-white px-12 py-4 rounded-full text-lg font-semibold hover:opacity-90 transition-all shadow-lg hover:shadow-xl transform hover:scale-105"
            >
              RESERVA TU LUGAR
            </button>
          </div>
        </div>
      </section>

      {/* Location - Barú - Image + Texte avec background */}
      <section className="py-20 bg-white">
        <div className="container mx-auto max-w-7xl px-6">
          <EditableSection
            sectionKey="location_title"
            content={pageContent.location_title}
            onSave={saveSection}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-12">
              Barú, Cartagena - Colombia
            </h2>
          </EditableSection>
          <div className="grid md:grid-cols-2 gap-0">
            {/* Image à gauche */}
            <div className="h-full min-h-[500px]">
              <div className="w-full h-full bg-gray-200 flex items-center justify-center text-gray-600">
                [IMG-LOCATION-001: Vue aérienne de l'île de Barú avec plage paradisiaque]
              </div>
            </div>
            {/* Texte avec background à droite */}
            <div className="p-12" style={{backgroundColor: '#dde6d7'}}>
              <EditableSection
                sectionKey="location_description"
                content={pageContent.location_description}
                onSave={saveSection}
              >
                <div className="space-y-6">
                  <p className="text-lg leading-relaxed" style={{color: '#59614c'}}>
                    <strong>La Isla Barú en Cartagena</strong>, Colombia, es un refugio mágico en la costa del Caribe. Este lugar es reconocido por sus playas de arena blanca, aguas cristalinas y una atmósfera de paz y tranquilidad que invita a la sanidad y bienestar. La serenidad del entorno, los paisajes tropicales y las aguas turquesas del mar Caribe te sumergen en una experiencia única. La Isla Barú de Cartagena es un destino verdaderamente maravilloso y memorable.
                  </p>
                  <p className="text-lg leading-relaxed" style={{color: '#59614c'}}>
                    El lugar donde viviremos esta experiencia transformadora está ubicado a solo 1 hora de Cartagena. <strong>Es el escenario donde encontrarás el maravilloso hotel de lujo donde se llevará a cabo nuestro retiro Ámate</strong>, y donde disfrutaremos en paz y plenitud este encuentro que nos cambiará la vida.
                  </p>
                </div>
              </EditableSection>
            </div>
          </div>
        </div>
      </section>

      {/* Accommodation */}
      <section className="py-20" style={{backgroundColor: '#F9F6F3'}}>
        <div className="container mx-auto max-w-6xl px-6">
          <h2 className="text-4xl font-bold text-center text-gray-800 mb-12">
            Alojamiento
          </h2>
          <div className="bg-white rounded-2xl shadow-xl p-8">
            <div className="grid md:grid-cols-2 gap-8 items-center">
              <div>
                <h3 className="text-2xl font-semibold text-gray-800 mb-4">
                  Habitaciones compartidas para dos personas con dos camas queen.
                </h3>
                <p className="text-gray-700 text-lg">
                  Provistas de hermosos espacios y una maravillosa vista al mar.
                </p>
              </div>
              <div className="space-y-4">
                <div className="w-full h-64 bg-gray-200 rounded-xl flex items-center justify-center text-gray-600">
                  [IMG-ROOM-001: Chambre d'hôtel avec vue mer]
                </div>
                <div className="w-full h-64 bg-gray-200 rounded-xl flex items-center justify-center text-gray-600">
                  [IMG-ROOM-002: Intérieur de chambre luxueuse]
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Why We're Different */}
      <section className="py-20" style={{backgroundColor: '#f4f2ed'}}>
        <div className="container mx-auto max-w-6xl px-6">
          <EditableSection
            sectionKey="why_different_title"
            content={pageContent.why_different_title}
            onSave={saveSection}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16">
              ¿POR QUÉ NUESTROS RETIROS SON DIFERENTES Y ÚNICOS?
            </h2>
          </EditableSection>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                title: 'EXPERIENCIA DE LUJO',
                description: 'Dedicamos una atención detallada a cada elemento para garantizar que la experiencia sea un auténtico deleite y lujo completo en cada rincón y momento de tu vivencia en el retiro.',
                img: 'IMG-DIFF-001'
              },
              {
                title: 'LA RÁPIDA TRANSFORMACIÓN',
                description: 'Vive una profunda transformación y sanidad en tus retos, desafíos y heridas más difíciles. Descubrirás que cualquier dolor o bloqueo que te limita, puede ser sanado, abrirás tu corazón y avanzarás con una mayor claridad hacia tu propósito de vida.',
                img: 'IMG-DIFF-002'
              },
              {
                title: 'EL PODER DE LA AUTENTICIDAD',
                description: 'Nuestros retiros se centran en la transformación real, sin las distracciones de los retiros "convencionales" para llevarte de vuelta a lo esencial: un viaje hacia tu interior, resignificar tu historia y sanidad profunda.',
                img: 'IMG-DIFF-003'
              },
              {
                title: 'LAS SESIONES GRUPALES A DIARIO',
                description: 'Podrás trabajar en tus problemas más apremiantes y recibir claridad en el acto. Estas sesiones mueven una energía de grupo muy poderosa lo que hace que la experiencia sea muy efectiva y transformadora.',
                img: 'IMG-DIFF-004'
              },
              {
                title: 'LAS AMISTADES ETERNAS',
                description: 'Conocerás a muchas mujeres que te cambiarán la vida. Tendrás la oportunidad de compartir experiencias únicas junto a muchas otras mujeres que también experimentan un bienestar emocional, y que te entenderán mejor que nadie, algo que a muchos de nosotros nos falta cuando nos embarcamos en este viaje.',
                img: 'IMG-DIFF-005'
              },
              {
                title: 'CONEXIÓN CON LA NATURALEZA',
                description: 'Pasamos poco tiempo en contacto con la naturaleza, en espacios "verdes y azules", a los que se atribuye un efecto positivo sobre la salud física y mental. Nuestros retiros se realizan en lugares de profunda conexión con la naturaleza, incluyendo caminatas y baños de bosque o mar, como fuente de bienestar y práctica terapéutica.',
                img: 'IMG-DIFF-006'
              },
              {
                title: 'ESPIRITUALIDAD',
                description: 'Te sumergirás en el desarrollo y enriquecimiento de tus prácticas espirituales cotidianas, incluyendo el mindfulness, meditación, afirmaciones y la oración. Consideramos que Dios es la clave para una sanidad absoluta, llevándote hacia estados de conciencia de serenidad, tranquilidad, sabiduría interior, así como un mayor propósito y significado en la vida.',
                img: 'IMG-DIFF-007'
              },
              {
                title: 'NUESTRO EQUIPO',
                description: 'Sin lugar a dudas, uno de los pilares fundamentales que hace que nuestro retiro sea excepcional es la calidad humana y el amor de nuestro equipo. Cada miembro del equipo está profundamente comprometido con tu bienestar y crecimiento personal. Son personas apasionadas y compasivas que están aquí para brindarte apoyo en cada paso de tu viaje.',
                img: 'IMG-DIFF-008'
              }
            ].map((item, index) => (
              <div key={index} className="bg-white rounded-xl overflow-hidden shadow-lg hover:shadow-xl transition-all">
                <div className="w-full h-48 bg-gray-200 flex items-center justify-center text-gray-600 text-xs">
                  [{item.img}: {item.title}]
                </div>
                <div className="p-6" style={{backgroundColor: '#6b745a'}}>
                  <h3 className="text-xl font-bold text-white mb-3 uppercase">{item.title}</h3>
                </div>
                <div className="p-6">
                  <p className="text-gray-700 leading-relaxed">{item.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Founder Section */}
      <section className="py-20" style={{backgroundColor: '#F5F5F0'}}>
        <div className="container mx-auto max-w-6xl px-6">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <div className="w-full h-[500px] bg-gray-200 rounded-2xl flex items-center justify-center text-gray-600">
                [IMG-FOUNDER-001: Photo professionnelle de Victoria Novoa]
              </div>
            </div>
            <EditableSection
              sectionKey="founder_bio"
              content={pageContent.founder_bio}
              onSave={saveSection}
            >
              <div>
                <h2 className="text-4xl font-bold text-gray-800 mb-6">
                  Hola, Hermosa
                </h2>
                <h3 style={{color: '#6b745a'}} className="text-3xl font-semibold mb-6">
                  Soy Victoria Novoa
                </h3>
                <div className="space-y-4 text-gray-700 leading-relaxed">
                  <p>
                    Mujer apasionada por el bienestar emocional y la salud mental, lo cual me ha llevado hoy en día a formarme como Psicóloga Clínica y de Salud, Líder Coach y Life Coach, experta en Inteligencia Emocional, diplomada en Neuropsicología del desarrollo, Magister en Psicoterapia Cognitivo Conductual y Magister en Terapia del Bienestar emocional y Terapias de la Tercera Generación en la Práctica Psicológica.
                  </p>
                  <p>
                    Hace más de 9 años me he dedicado a ayudar a miles de mujeres alrededor del mundo, a las que he acompañado en su proceso de autoconocimiento y amor propio; les ayudo a reconstruir su seguridad y a romper creencias, pensamientos, malos hábitos e ideales que las han limitado por años.
                  </p>
                  <p>
                    Creo en el poder de la mente, creo en el potencial que hay en ti, creo en el propósito dado por Dios a tu vida, y por eso he creado este retiro para ti. Tengo la firme convicción de que este tiempo llevará tu vida a un nuevo nivel.
                  </p>
                  <p className="font-semibold">
                    En este retiro voy a compartir contigo todas las herramientas y conocimientos que me han ayudado para recuperar mi esencia de mujer, reafirmar mi valor y vivir en plenitud.
                  </p>
                </div>
              </div>
            </EditableSection>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-20" style={{backgroundColor: '#FDFCFB'}}>
        <div className="container mx-auto max-w-6xl px-6">
          <EditableSection
            sectionKey="testimonials_title"
            content={pageContent.testimonials_title}
            onSave={saveSection}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16">
              Testimonios
            </h2>
          </EditableSection>
          <div className="grid md:grid-cols-2 gap-8">
            {[
              {
                text: 'Este retiro llegó a sacar todos esos secretos que dolían y que no me permitían ser la mamá y esposa que deseaba ser. Ahora me amo y amo lo que veo en el espejo, me siento hermosa y valiosa. Este retiro marcó mi vida, me siento viva y feliz.',
                img: 'TESTIMONIAL-001'
              },
              {
                text: 'Gracias a que Dios me puso en este retiro liberé y solté todo lo que me cargaba y pude sanar y entender la vida de mis papás. Definitivamente hoy no soy la misma que llegó aquí.',
                img: 'TESTIMONIAL-002'
              },
              {
                text: 'Venir aquí fue reconocer que estaba con una cantidad de candados, de bloqueos, miedos e inseguridades, sintiendo que no era merecedora de absolutamente nada, necesitaba sanar mi niña interior y en este retiro empecé a abrir cada uno de esos candados, empecé visualizar, a creer y a sanar, esta experiencia fue extraordinaria y valió toda la pena del mundo.',
                img: 'TESTIMONIAL-003'
              },
              {
                text: 'Jamás pensé que me fuera a remover tanto pero fue lo que definitivamente cambió mi vida y no solo transformó a mí sino a través de mí, a mi matrimonio y familia. Me voy del retiro renovada, cambiada y transformada.',
                img: 'TESTIMONIAL-004'
              },
              {
                text: 'Perder a una madre es un dolor muy grande y hoy doy gracias a Dios por los años que me permitió tenerla, hoy me siento libre, hoy puedo tomar decisiones que antes no podía, hoy me voy con la convicción que este retiro era lo que necesitaba.',
                img: 'TESTIMONIAL-005'
              },
              {
                text: 'Llegué aquí con muchas expectativas pero la verdad han sido superadas, no pensé desbloquear tantas cosas en mi vida, yo decía: "a mí se me repite el mismo patrón siempre" pero ahora me siento libre y segura.',
                img: 'TESTIMONIAL-006'
              }
            ].map((testimonial, index) => (
              <div key={index} className="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all border border-stone-200">
                <div className="w-full h-48 bg-gray-200 rounded-xl flex items-center justify-center text-gray-600 text-xs mb-6">
                  [IMG-{testimonial.img}: Photo de la participante]
                </div>
                <p className="text-gray-700 italic leading-relaxed text-lg">
                  "{testimonial.text}"
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Promo Image */}
      <section className="py-12 bg-white">
        <div className="container mx-auto px-6">
          <div className="w-full h-96 bg-gray-200 flex items-center justify-center text-gray-600">
            [IMG-PROMO-001: Image promotionnelle du retiro avec groupe de femmes heureuses]
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section className="py-20" style={{backgroundColor: '#F5F5F0'}}>
        <div className="container mx-auto max-w-4xl px-6">
          <EditableSection
            sectionKey="faq_title"
            content={pageContent.faq_title}
            onSave={saveSection}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16">
              Preguntas frecuentes
            </h2>
          </EditableSection>
          <div className="space-y-4">
            {[
              {
                question: '¿Puedo ir sola?',
                answer: '¡Por supuesto! Más del 80% de las mujeres que participan en nuestros retiros vienen solas. Es una magnífica oportunidad para conocer gente nueva que tiene tus mismos intereses y propósitos. Harás amigas para toda la vida.'
              },
              {
                question: '¿Qué pasa después de hacer mi pago?',
                answer: 'Una vez hagas tu proceso de inscripción harás parte de nuestro grupo de WhatsApp del Retiro Ámate en el cual tendrás nuestro acompañamiento durante todos estos meses hasta que llegue el día del retiro. En este grupo te iremos enviando guías de cómo prepararnos para el retiro, de lo que necesitas llevar, del lugar donde estaremos y recomendaciones de todo tipo para que esta experiencia del retiro sea inolvidable para ti.'
              },
              {
                question: '¿El vuelo (tiquete de avión) está incluido?',
                answer: 'No, el vuelo no está incluido ya que este dependerá del lugar donde residas, sin embargo, con el equipo estamos dispuestas a asesorarte y darte recomendaciones.'
              },
              {
                question: '¿Qué pasa si nunca he ido a un retiro o vivido una experiencia parecida?',
                answer: 'Tranquila, esta será tu primera experiencia y la más transformadora, no necesitas haber vivido alguna experiencia similar antes, no necesitas saber sobre meditación, mindfulness ni nada relacionado. Solo necesitas tener un corazón dispuesto a vivir tu mayor tiempo de sanidad y transformación de todos los años de tu vida.'
              },
              {
                question: '¿Si vivo en otro país, puedo asistir?',
                answer: 'Siiii, en cada retiro tenemos mujeres que vienen de todas partes del mundo.'
              }
            ].map((faq, index) => (
              <div key={index} className="bg-white rounded-xl shadow-md overflow-hidden">
                <button
                  onClick={() => toggleFaq(index)}
                  className="w-full px-6 py-5 text-left flex justify-between items-center hover:bg-gray-50 transition-all"
                >
                  <h3 className="text-lg font-semibold text-gray-800">{faq.question}</h3>
                  <svg
                    style={{color: '#6b745a'}}
                    className={`w-6 h-6 transform transition-transform ${
                      openFaq === index ? 'rotate-180' : ''
                    }`}
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                  </svg>
                </button>
                {openFaq === index && (
                  <div className="px-6 py-4 bg-gray-50 border-t border-gray-200">
                    <p className="text-gray-700 leading-relaxed">{faq.answer}</p>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20" style={{backgroundColor: '#6b745a'}}>
        <div className="container mx-auto max-w-4xl px-6 text-center">
          <EditableSection
            sectionKey="cta_final"
            content={pageContent.cta_final}
            onSave={saveSection}
            editClassName="p-4 bg-white/20 border-2 border-white/50 rounded-lg"
          >
            <div>
              <h2 className="text-4xl font-bold text-white mb-6">
                ¿Tienes dudas?
              </h2>
              <p className="text-xl text-white mb-4">
                ¿No sabes si es para ti?
              </p>
              <p className="text-xl text-white mb-8">
                ¿No has ido nunca de retiro?
              </p>
              <p className="text-white text-lg mb-8">
                Escríbeme y estaré lista con todo mi equipo para brindarte toda la ayuda que necesites.
              </p>
            </div>
          </EditableSection>
          <button 
            style={{color: '#6b745a'}}
            className="bg-white px-12 py-4 rounded-full text-lg font-semibold hover:bg-gray-100 transition-all shadow-lg hover:shadow-xl transform hover:scale-105"
          >
            HABLAR CON SOPORTE
          </button>
        </div>
      </section>
    </div>
  );
};

export default LandingPage;

