import React, { useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';

const RetiroAmateStyle = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className="min-h-screen bg-white font-inter">
      {/* Hero Section */}
      <section className="relative py-0 min-h-screen flex items-center justify-center bg-beige">
        <div className="absolute inset-0 z-0">
          <img 
            src="/jardin-hero.jpg" 
            alt="Hero background" 
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-white/50 via-white/40 to-white/60" />
        </div>
        
        <div className="relative z-10 text-center max-w-4xl mx-auto px-4 py-20">
          <img 
            src="/logo-transparent.png" 
            alt="Logo" 
            className="h-24 w-24 sm:h-32 sm:w-32 mx-auto mb-8 drop-shadow-xl"
          />
          <h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-semibold text-gray-800 mb-6 leading-tight px-2">
            Rompe tus creencias, libera tus bloqueos y vuelve a confiar en ti
          </h1>
          <p className="text-lg sm:text-xl md:text-2xl text-gray-700 mb-8 leading-relaxed px-2 font-normal">
            Sana tu historia, gana claridad y aprende a construir la vida que realmente deseas, en un espacio único y seguro
          </p>
          <Button 
            size="lg"
            className="bg-sage-600 hover:bg-sage-700 text-white text-base sm:text-lg px-10 sm:px-14 py-6 sm:py-7 font-medium rounded-xl shadow-sage transition-all"
            onClick={() => window.open('https://checkout.mailerlite.com/checkout/6005', '_blank')}
          >
            RESERVA TU LUGAR
          </Button>
        </div>
      </section>

      {/* Small Images Section */}
      <section className="py-8 bg-stone-50">
        <div className="container mx-auto max-w-5xl px-4">
          <div className="grid grid-cols-3 gap-4">
            <img src="/salon-cheminee.jpg" alt="" className="w-full h-32 sm:h-40 object-cover rounded-lg shadow-md" />
            <img src="/jardin-piscine-v2.jpg" alt="" className="w-full h-32 sm:h-40 object-cover rounded-lg shadow-md" />
            <img src="/salle-manger.jpg" alt="" className="w-full h-32 sm:h-40 object-cover rounded-lg shadow-md" />
          </div>
        </div>
      </section>

      {/* Date Section */}
      <section className="py-12 bg-white">
        <div className="container mx-auto max-w-3xl text-center px-4">
          <p className="text-2xl sm:text-3xl font-medium text-gray-800 mb-2">
            14 de diciembre 2025
          </p>
          <p className="text-lg sm:text-xl text-taupe-600">
            El Jardín Secreto – París, Francia
          </p>
        </div>
      </section>

      {/* Info Section with Sage background */}
      <section className="py-16 bg-beige">
        <div className="container mx-auto max-w-6xl px-4">
          <div className="grid md:grid-cols-2 gap-8 items-center">
            <div className="order-2 md:order-1">
              <img 
                src="/groupe.png" 
                alt="Groupe" 
                className="w-full h-80 object-cover rounded-xl shadow-elegant"
              />
            </div>
            <div className="order-1 md:order-2 bg-gradient-sage text-white p-10 sm:p-14 rounded-2xl shadow-sage">
              <h2 className="text-2xl sm:text-3xl font-semibold mb-6 leading-tight">
                ¿POR QUÉ EL RETIRO RENACER ES PARA TI?
              </h2>
              <div className="space-y-4 text-sm sm:text-base leading-relaxed">
                <p>• Porque en tus relaciones das más de lo que recibes. Te cuesta poner límites, decir "no" sin sentir culpa o pedir lo que necesitas sin miedo a perder el cariño del otro. Y aunque parezcas fuerte, muchas veces te sientes sola, no vista o emocionalmente cansada</p>
                <p>• Porque hay momentos en los que dudas de ti misma, incluso cuando los demás te ven capaz. Esa voz interna que te exige más, que te compara o que te hace sentir que "no estás haciendo lo suficiente", se ha vuelto demasiado ruidosa</p>
                <p>• Porque si bien has logrado mucho —has migrado, te has reinventado, empezado de cero— a veces te sientes desconectada de ti, de tu esencia, de tu propósito. No sabes si el camino que estás siguiendo realmente te representa o si solo estás sobreviviendo</p>
                <p>• Porque llevas tiempo sintiendo que necesitas una pausa. Salir de la rutina, soltar el control y darte el permiso de escucharte, sin tener que sostener a todos los demás</p>
                <p>• Porque sabes que este cierre de año no puede ser igual. Sientes el llamado de dejar atrás lo viejo, ordenar tus emociones y poner claridad en tus metas para 2026. Quieres aprender cómo transformar tu mente y accionar con confianza, sin miedo ni autoexigencia</p>
                <p>• Y porque quieres rodearte de mujeres como tú: valientes, sensibles, auténticas. Mujeres que entienden el peso de empezar de nuevo, que buscan paz, propósito y expansión. Una tribu donde no tengas que fingir fortaleza, solo permitirte ser</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Logo Central */}
      <section className="py-16 bg-stone-50">
        <div className="container mx-auto max-w-2xl text-center px-4">
          <img 
            src="/logo-transparent.png" 
            alt="Logo" 
            className="h-20 w-20 mx-auto mb-6"
          />
          <p className="text-xl sm:text-2xl font-medium text-gray-700 mb-4 leading-relaxed">
            Vive una experiencia de <strong className="text-sage-700">transformación interior</strong>
          </p>
          <p className="text-base sm:text-lg text-gray-600 leading-relaxed">
            para cerrar el año con claridad y propósito
          </p>
        </div>
      </section>

      {/* Pricing Section */}
      <section className="py-16 bg-gradient-sage text-white">
        <div className="container mx-auto max-w-5xl px-4 text-center">
          <p className="text-xl mb-4 font-medium">¡Sólo para mujeres!</p>
          <h2 className="text-4xl sm:text-5xl md:text-6xl font-bold mb-8">
            DESCUENTO DE<br/>PREVENTA
          </h2>
          <p className="text-lg mb-10">(Por tiempo limitado)</p>
          
          <div className="bg-white text-gray-800 rounded-2xl p-10 sm:p-14 max-w-3xl mx-auto shadow-elegant">
            <p className="text-gray-600 mb-3">Residentes en Francia o fuera</p>
            <p className="text-3xl text-gray-400 line-through mb-3">€199 EUR</p>
            <p className="text-6xl sm:text-7xl font-bold text-sage-600 mb-8">€149 EUR</p>
            
            <div className="bg-beige p-6 rounded-xl mb-8">
              <p className="font-semibold text-lg mb-3 text-gray-800">Pago completo o pago a cuotas</p>
              <p className="text-sm text-gray-600 leading-relaxed">
                En cuotas, el primer pago (€50) se realiza al momento de la inscripción, el segundo (€50) en noviembre y el último (€49) antes del retiro
              </p>
            </div>
            
            <Button 
              size="lg"
              className="w-full bg-sage-600 hover:bg-sage-700 text-white text-lg py-6 font-medium rounded-xl shadow-sage"
              onClick={() => window.open('https://checkout.mailerlite.com/checkout/6005', '_blank')}
            >
              QUIERO REALIZAR MI PAGO
            </Button>
            
            <p className="text-xs text-gray-500 mt-6 leading-relaxed">
              Opciones de pago: Transferencia, Wero (Francia), tarjeta de crédito o débito
            </p>
            
            <div className="mt-6 inline-block bg-taupe-100 px-6 py-3 rounded-lg border-2 border-taupe-300">
              <p className="font-semibold text-base text-taupe-800">
                Descuento para grupos a partir de 4 mujeres
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* What Includes */}
      <section className="py-16 bg-white">
        <div className="container mx-auto max-w-6xl px-4">
          <h2 className="text-3xl sm:text-4xl font-semibold text-center text-gray-800 mb-12">
            ¡1 DÍA QUE LO CAMBIARÁ TODO!
          </h2>
          <div className="grid md:grid-cols-2 gap-8">
            {/* Incluye */}
            <div className="bg-gradient-sage text-white p-8 sm:p-10 rounded-2xl shadow-sage">
              <h3 className="text-2xl font-semibold mb-6 text-center">¿QUÉ INCLUYE?</h3>
              <div className="space-y-3 text-sm sm:text-base leading-relaxed">
                {[
                  'Un día completo de transformación (8h30 a 18h30) en El Jardín Secreto de París',
                  'Desayuno, almuerzo con postre y merienda saludable',
                  'Bienvenida especial con ritual de apertura',
                  'Kit de bienvenida: Incluye materiales de trabajo, herramientas prácticas para los talleres y un regalo sorpresa',
                  'Fogata y experiencia de cierre',
                  'Taller "Point of You" – Coaching de creencias',
                  'Movimiento consciente',
                  'Participación en todos los talleres del programa Renacer: Espacios enfocados en creencias, claridad emocional, autoestima, confianza y cumplimiento de metas',
                  'Actividades de recreación y conexión grupal'
                ].map((item, i) => (
                  <p key={i}>• {item}</p>
                ))}
              </div>
            </div>

            {/* Esperar */}
            <div className="bg-gradient-taupe text-white p-8 sm:p-10 rounded-2xl shadow-taupe">
              <h3 className="text-2xl font-semibold mb-6 text-center">¿QUÉ ESPERAR?</h3>
              <div className="space-y-3 text-sm sm:text-base leading-relaxed">
                {[
                  'Un espacio seguro y amoroso para conectar contigo y con mujeres que comparten tu deseo de crecimiento y autenticidad',
                  'Actividades que integran cuerpo, mente y alma, diseñadas para reconectar con tu poder interior',
                  'Herramientas prácticas y psicológicas para aplicar en tu día a día y mantener claridad emocional, dirección y equilibrio',
                  'Meditaciones, mindfulness y bioenergética para fortalecer tu conexión interna y liberar tensión acumulada',
                  'Taller de coaching transformacional "Point of You" para cambiar tu perspectiva y comprender tus creencias desde la raíz',
                  'Momentos de introspección y expansión, donde podrás redefinir tu historia y tu visión de futuro',
                  'Espacios de recreación, música, movimiento y risas, porque el crecimiento también se celebra',
                  'Una comprensión más profunda de ti misma, de lo que necesitas y de lo que realmente deseas, para tomar decisiones alineadas con tu propósito',
                  'Un nuevo enfoque para tu vida y tus relaciones, más consciente, resiliente y equilibrado',
                  'Un cierre de año poderoso, soltando lo viejo y estableciendo metas claras para accionar con confianza y dirección en 2026'
                ].map((item, i) => (
                  <p key={i}>• {item}</p>
                ))}
              </div>
            </div>
          </div>
          
          <div className="text-center mt-10">
            <Button 
              size="lg"
              className="bg-sage-600 hover:bg-sage-700 text-white px-12 py-6 rounded-xl shadow-sage"
              onClick={() => window.open('https://checkout.mailerlite.com/checkout/6005', '_blank')}
            >
              RESERVA TU LUGAR
            </Button>
          </div>
        </div>
      </section>

      {/* Location */}
      <section className="py-16 bg-beige">
        <div className="container mx-auto max-w-5xl px-4">
          <h2 className="text-3xl sm:text-4xl font-semibold text-center text-gray-800 mb-8">
            El Jardín Secreto – París, Francia
          </h2>
          <div className="mb-8">
            <img 
              src="/jardin-piscine-v2.jpg" 
              alt="El Jardín Secreto" 
              className="w-full h-96 object-cover rounded-2xl shadow-elegant"
            />
          </div>
          <div className="max-w-3xl mx-auto text-center space-y-4 text-gray-700 leading-relaxed">
            <p>
              En el corazón del histórico <strong className="text-sage-700">Barrio Latino de París</strong> se encuentra El Jardín Secreto, una joya escondida donde el silencio, la belleza y la historia se entrelazan.
            </p>
            <p>
              Una casa del siglo XVIII completamente restaurada, rodeada de un jardín privado lleno de luz, calma y armonía.
            </p>
            <p className="font-medium text-sage-700">
              El Jardín Secreto no es solo el lugar del retiro, es parte de la experiencia: un escenario donde el alma se expande y la mente se transforma.
            </p>
          </div>
        </div>
      </section>

      {/* Alojamiento */}
      <section className="py-16 bg-white">
        <div className="container mx-auto max-w-6xl px-4">
          <h2 className="text-3xl sm:text-4xl font-semibold text-center text-gray-800 mb-10">
            Alojamiento
          </h2>
          <div className="grid md:grid-cols-2 gap-6">
            <img 
              src="/salon-cheminee.jpg" 
              alt="Espacio" 
              className="w-full h-80 object-cover rounded-xl shadow-elegant"
            />
            <img 
              src="/salle-manger.jpg" 
              alt="Comedor" 
              className="w-full h-80 object-cover rounded-xl shadow-elegant"
            />
          </div>
          <p className="text-center text-xl text-gray-700 mt-8 max-w-3xl mx-auto font-medium">
            Un espacio exclusivo rodeado de naturaleza y detalles parisinos
          </p>
        </div>
      </section>

      {/* Why Different - 8 cards */}
      <section className="py-16 bg-stone-50">
        <div className="container mx-auto max-w-6xl px-4">
          <h2 className="text-3xl sm:text-4xl font-semibold text-center text-gray-800 mb-12">
            ¿POR QUÉ NUESTROS RETIROS SON DIFERENTES?
          </h2>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              { img: '/jardin-hero.jpg', title: 'EXPERIENCIA DE LUJO', text: 'Cada detalle cuidadosamente diseñado para tu transformación' },
              { img: '/femme-transformation.jpg', title: 'TRANSFORMACIÓN', text: 'Profunda sanación emocional y mental' },
              { img: '/femme-meditation.jpg', title: 'AUTENTICIDAD', text: 'Proceso profundo y real sin distracciones' },
              { img: '/groupe.png', title: 'SESIONES GRUPALES', text: 'Energía de grupo muy poderosa' },
              { img: '/groupe.png', title: 'AMISTADES', text: 'Conexiones auténticas que perduran' },
              { img: '/jardin-piscine-v2.jpg', title: 'NATURALEZA', text: 'Conexión profunda con lo natural' },
              { img: '/salon-cheminee.jpg', title: 'ESPIRITUALIDAD', text: 'Prácticas de mindfulness y meditación' },
              { img: '/victoria-portrait.jpg', title: 'EQUIPO', text: 'Calidad humana y amor excepcional' }
            ].map((item, i) => (
              <div key={i} className="bg-white rounded-xl overflow-hidden shadow-elegant hover:shadow-sage transition-all duration-300 hover:scale-102">
                <img src={item.img} alt={item.title} className="w-full h-40 object-cover" />
                <div className="p-5">
                  <h3 className="font-semibold text-sm mb-2 text-sage-700 uppercase">{item.title}</h3>
                  <p className="text-xs text-gray-600 leading-relaxed">{item.text}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Founder with sage background */}
      <section className="py-16 bg-white">
        <div className="container mx-auto max-w-6xl px-4">
          <div className="mb-12 text-center">
            <h2 className="text-3xl sm:text-4xl font-semibold text-gray-800 mb-4">
              Fundadoras del retiro
            </h2>
          </div>
          
          {/* Nicole */}
          <div className="grid md:grid-cols-2 gap-10 items-center mb-16">
            <div className="bg-gradient-sage text-white p-10 sm:p-14 rounded-2xl shadow-sage">
              <h2 className="text-3xl sm:text-4xl font-semibold mb-4">
                Hola, Hermosa
              </h2>
              <h3 className="text-2xl sm:text-3xl font-medium mb-6">
                Soy Nicole Ramírez
              </h3>
              <div className="space-y-4 text-sm sm:text-base leading-relaxed">
                <p>
                  Soy una mujer apasionada por el crecimiento personal, el bienestar emocional y la mente humana.
                </p>
                <p>
                  He vivido momentos de quiebre, de confusión y de reinvención… pero cada desafío se convirtió en una oportunidad para descubrir mi propósito y ayudar a otras personas a hacer lo mismo.
                </p>
                <p>
                  Esa búsqueda me llevó a formarme como Psicóloga y Coach de Vida, y a crear Cambio de Paradigma, un programa de 12 semanas que acompaña a profesionales y emprendedores a transformar el dolor en propósito, reconectando con su poder interno y construyendo una vida con claridad, confianza y paz.
                </p>
                <p>
                  Durante más de cinco años he acompañado a personas de todo el mundo en procesos de autoconocimiento profundo, liberación emocional y reprogramación mental.
                </p>
                <p>
                  He visto cómo, cuando una persona cambia su forma de pensar, cambia toda su realidad.
                </p>
                <p className="italic">
                  Creo profundamente en el poder interno que todos tenemos para reinventarnos, en la capacidad de empezar de nuevo y en el vínculo entre la mente y lo que proyectamos en el mundo.
                </p>
                <p className="font-semibold">
                  Cuando transformas tus pensamientos, transformas tu realidad.
                </p>
                <p className="font-medium bg-white/20 p-4 rounded-lg border-l-4 border-white">
                  En el retiro Renacer voy a compartir contigo las herramientas, experiencias y prácticas que me ayudaron a pasar de tener cero posibilidades en mi país, a crear una vida alineada a mis deseos, viviendo con plenitud, confianza y serenidad. Te acompañaré paso a paso para que tú también puedas cerrar un ciclo, liberar lo que pesa y construir desde adentro la vida que mereces vivir.
                </p>
              </div>
            </div>
            <div>
              <img 
                src="/victoria-portrait.jpg" 
                alt="Nicole Ramírez" 
                className="w-full h-[600px] object-cover rounded-2xl shadow-elegant"
              />
            </div>
          </div>
          
          {/* Dianix */}
          <div className="grid md:grid-cols-2 gap-10 items-center">
            <div className="order-2 md:order-1">
              <img 
                src="/dianix-portrait.jpg" 
                alt="Dianix Bermúdez" 
                className="w-full h-[600px] object-cover rounded-2xl shadow-elegant"
              />
            </div>
            <div className="order-1 md:order-2 bg-gradient-taupe text-white p-10 sm:p-14 rounded-2xl shadow-taupe">
              <h2 className="text-3xl sm:text-4xl font-semibold mb-4">
                Hola, soy Dianix Bermúdez
              </h2>
              <p className="text-lg mb-6">(Facilitadora)</p>
              <div className="space-y-4 text-sm sm:text-base leading-relaxed">
                <p>
                  Soy Mentora de Vida, experta en Energía, Manifestación y Negocios Conscientes, y autora del libro "La Energía es la Vida".
                </p>
                <p>
                  Mi propósito es recordarte que todo lo que deseas ya habita dentro de ti: la abundancia, la confianza, la alegría y el poder de crear la realidad que sueñas.
                </p>
                <p>
                  Vivo en París junto a mi familia, y cada día agradezco haber elegido este camino de expansión y propósito.
                </p>
                <p>
                  Mi propio proceso de transformación me llevó a crear el Movimiento EPAAAA, una comunidad dedicada a acompañar a mujeres a elevar su energía, liberar creencias limitantes y reprogramar su mente para vivir en abundancia y plenitud.
                </p>
                <p className="italic">
                  Creo profundamente que la energía es la vida, y que cuando alineas tu mente, tus emociones y tu intención, todo comienza a fluir.
                </p>
                <p className="font-medium bg-white/20 p-4 rounded-lg border-l-4 border-white">
                  En este retiro quiero acompañarte a recordar tu poder interior, reconectarte con tu energía más auténtica y abrir espacio para que la abundancia llegue a tu vida con facilidad y propósito.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-16 bg-beige">
        <div className="container mx-auto max-w-6xl px-4">
          <h2 className="text-3xl sm:text-4xl font-semibold text-center text-gray-800 mb-12">
            Testimonios
          </h2>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {[
              { name: 'Karla', text: 'Ayer viví un mini retiro transformador. Entré sin expectativas, sin saber nada, ni de qué se trataban muchas herramientas, solo con la intención de conectar y abrirme a lo que viniera. Lo que encontré fue eso y mucho más: claridad, fuerza interior y un conocimiento profundo de mí misma que necesitaba en este momento de mi vida. Gracias infinitas al equipo, tan humanas y de gran corazón, por guiarnos en esta experiencia mágica.' },
              { name: 'Vanessa', text: 'Me traje tranquilidad. Varias de las actividades y las experiencias que compartieron otras mujeres me ayudaron a ver una luz en el camino. Hoy me siento más en paz y con esperanza.' },
              { name: 'Carolina', text: 'Sentí mucho valor y un profundo reencuentro conmigo. Me permití ser vulnerable, abrirme y compartir desde el corazón. Fue un día de liberación y conexión real.' },
              { name: 'Fabiana', text: 'Me encantó compartir y escuchar a otras compañeras con historias parecidas a la mía. La guía psicológica y espiritual durante todo el día fue increíble. Me voy con claridad, calma y motivación para seguir mi proceso.' },
              { name: 'Laura', text: 'Me gustó el ambiente y la energía. Hubo material valioso y dinámicas que realmente te hacen pensar y sanar. Me fui con más claridad y con herramientas prácticas para aplicar en mi vida.' },
              { name: 'Marcela', text: 'El retiro fue una experiencia profundamente sanadora. Llegué con muchas preguntas y me fui con claridad, serenidad y una nueva visión de mí misma.' },
              { name: 'Luz', text: 'Me sentí acompañada, vista y contenida. Fue un espacio lleno de amor donde pude reconectar con mi poder y mi fe en la vida. Me voy con el corazón liviano y la mente en calma.' }
            ].map((item, i) => (
              <div key={i} className="bg-white p-6 rounded-xl shadow-elegant border-l-4 border-sage-500">
                <p className="text-gray-700 italic text-sm leading-relaxed mb-3">"{item.text}"</p>
                <p className="text-sage-700 font-semibold">- {item.name}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-16 bg-white">
        <div className="container mx-auto max-w-4xl px-4">
          <h2 className="text-3xl sm:text-4xl font-semibold text-center text-gray-800 mb-12">
            Preguntas frecuentes
          </h2>
          <Accordion type="single" collapsible className="space-y-4">
            {[
              { 
                q: '¿Puedo ir sola?', 
                a: '¡Claro que sí! De hecho, la mayoría de las mujeres que asisten vienen solas. Renacer está pensado para que desde el primer momento te sientas acompañada y segura. Vivir esta experiencia sin compañía te permite conectarte contigo misma y abrirte a nuevas amistades. No llegas sola… llegas a una tribu de mujeres auténticas que están transitando caminos similares al tuyo.' 
              },
              { 
                q: '¿Qué pasa después de hacer mi pago?', 
                a: 'Una vez que realices tu pago o reserva, recibirás un correo de confirmación automática con todos los detalles de como unirte a la comunidad. En las semanas previas al evento, te enviaremos información práctica (horarios, recomendaciones, qué llevar y cómo prepararte). Además, estarás invitada a un grupo privado de WhatsApp, donde compartiremos recordatorios, tips previos y podrás empezar a conectar con las demás participantes.' 
              },
              { 
                q: '¿El vuelo o transporte están incluidos?', 
                a: 'No. El valor del retiro no incluye el vuelo ni el transporte hasta el lugar. Sin embargo, te enviaremos una guía con las mejores rutas y opciones de transporte dentro de París, si lo necesitas, para que llegues fácilmente al Jardín Secreto, el espacio donde se realizará la experiencia. Si viajas desde otra ciudad o país, también podremos orientarte con recomendaciones de alojamiento cercano y con posibles descuentos.' 
              },
              { 
                q: '¿Qué pasa si nunca he ido a un retiro o vivido una experiencia parecida?', 
                a: 'No necesitas tener experiencia previa. Renacer fue creado para mujeres que simplemente sienten el llamado a un cambio y desean reconectarse con ellas mismas. Durante todo el proceso estarás acompañada por Nicole Ramírez y un equipo profesional, que te guiarán paso a paso para que te sientas cómoda, sostenida y comprendida. Solo necesitas abrirte a la experiencia y permitirte recibir.' 
              },
              { 
                q: '¿Si vivo en otro país, puedo asistir?', 
                a: 'Sí, por supuesto. Renacer es una experiencia internacional, han asistido chicas que estaban de viaje en Paris o viven en Europa. París es una ciudad muy accesible y el retiro se realiza en una ubicación céntrica, segura y fácil de llegar. Solo asegúrate de reservar con tiempo tu cupo, ya que los espacios son limitados y se agotan rápido.' 
              }
            ].map((faq, i) => (
              <AccordionItem key={i} value={`item-${i}`} className="bg-stone-50 border-2 border-stone-200 rounded-xl px-6">
                <AccordionTrigger className="text-lg font-semibold text-gray-800 hover:no-underline hover:text-sage-700 transition-colors">
                  {faq.q}
                </AccordionTrigger>
                <AccordionContent className="text-gray-600 leading-relaxed">
                  {faq.a}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-gradient-sage text-white text-center">
        <div className="container mx-auto max-w-3xl px-4">
          <h2 className="text-3xl sm:text-4xl font-semibold mb-6">
            ¿Tienes dudas?
          </h2>
          <div className="space-y-2 mb-8">
            <p className="text-xl">¿No sabes si es para ti?</p>
            <p className="text-xl">¿No has ido nunca de retiro?</p>
          </div>
          <p className="text-lg mb-8 leading-relaxed">
            Escríbeme y estaré lista con todo mi equipo para ayudarte
          </p>
          <Button 
            size="lg"
            className="bg-white text-sage-700 hover:bg-stone-50 px-12 py-6 font-semibold rounded-xl shadow-elegant"
            onClick={() => window.open('https://wa.me/33667596062', '_blank')}
          >
            HABLAR CON SOPORTE
          </Button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-sage-800 text-white py-12">
        <div className="container mx-auto max-w-6xl px-4">
          <div className="flex flex-col md:flex-row justify-between items-center mb-8">
            <div className="flex items-center space-x-3 mb-4 md:mb-0">
              <img src="/logo-transparent.png" alt="Logo" className="h-12 w-12" />
              <span className="text-lg font-semibold">Cambio de Paradigma</span>
            </div>
            <div className="flex space-x-6 text-sm">
              <a href="https://www.instagram.com/cambio.de.paradigma/" target="_blank" rel="noopener noreferrer" className="hover:text-sage-200 transition-colors">Instagram</a>
              <a href="https://www.tiktok.com/@cambio.de.paradigma" target="_blank" rel="noopener noreferrer" className="hover:text-sage-200 transition-colors">TikTok</a>
              <a href="https://wa.me/33667596062" target="_blank" rel="noopener noreferrer" className="hover:text-sage-200 transition-colors">Whatsapp</a>
            </div>
          </div>
          <div className="text-center text-sm text-white/80 border-t border-white/20 pt-6">
            <p>© 2024 Cambio de Paradigma. Todos los derechos reservados.</p>
            <p className="mt-2 text-xs">
              Este sitio no es parte de Facebook o Facebook, Inc.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default RetiroAmateStyle;
