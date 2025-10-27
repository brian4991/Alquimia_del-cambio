import React, { useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';

const RetiroAmateStyle = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className="min-h-screen bg-white">
      {/* Hero Section */}
      <section className="relative py-16 px-4 min-h-screen flex items-center justify-center">
        <div className="absolute inset-0 z-0">
          <img 
            src="/jardin-hero.jpg" 
            alt="Hero background" 
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-black/20" />
        </div>
        
        <div className="relative z-10 text-center max-w-5xl mx-auto">
          <div className="mb-6 sm:mb-8">
            <img 
              src="/logo-transparent.png" 
              alt="Logo" 
              className="h-20 w-20 sm:h-28 sm:w-28 md:h-32 md:w-32 mx-auto mb-4 sm:mb-6 drop-shadow-2xl"
            />
          </div>
          <h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl xl:text-7xl font-bold text-white mb-4 sm:mb-6 leading-tight drop-shadow-lg px-2">
            Rompe tus creencias, libera tus bloqueos y vuelve a confiar en ti
          </h1>
          <p className="text-lg sm:text-xl md:text-2xl lg:text-3xl text-white mb-8 sm:mb-10 drop-shadow-lg px-2">
            Sana tu historia, gana claridad y aprende a construir la vida que realmente deseas, en un espacio único y seguro
          </p>
          <Button 
            size="lg"
            className="bg-[#8B7355] hover:bg-[#6d5a43] text-white text-base sm:text-lg md:text-xl px-8 sm:px-10 md:px-12 py-6 sm:py-7 md:py-8 font-bold shadow-2xl"
            onClick={() => window.open('https://checkout.mailerlite.com/checkout/6005', '_blank')}
          >
            RESERVA TU LUGAR
          </Button>
        </div>
      </section>

      {/* Date & Location Banner */}
      <section className="py-8 sm:py-12 px-4" style={{backgroundColor: '#F5F5F0'}}>
        <div className="container mx-auto max-w-5xl text-center">
          <h2 className="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold text-gray-800">
            14 de diciembre
          </h2>
          <p className="text-lg sm:text-xl md:text-2xl lg:text-3xl text-gray-700 mt-2">
            El Jardín Secreto – París, Francia
          </p>
        </div>
      </section>

      {/* Experience Description */}
      <section className="py-12 sm:py-16 md:py-20 px-4 bg-white">
        <div className="container mx-auto max-w-4xl text-center">
          <h2 className="text-2xl sm:text-3xl md:text-4xl font-bold text-gray-800 mb-4 sm:mb-6 leading-tight">
            Vive una experiencia de <span className="text-[#8B7355]">transformación interior</span> para cerrar el año con claridad y propósito
          </h2>
          <p className="text-base sm:text-lg md:text-xl lg:text-2xl text-gray-700 leading-relaxed">
            Descubre cómo reprogramar tu mente, liberar la confusión emocional y recuperar la seguridad en tus decisiones y en ti misma
          </p>
        </div>
      </section>

      {/* Why This Retreat */}
      <section className="py-20 px-4" style={{backgroundColor: '#FDFCFB'}}>
        <div className="container mx-auto max-w-4xl">
          <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16">
            ¿POR QUÉ EL RETIRO RENACER ES PARA TI?
          </h2>
          <div className="space-y-6">
            {[
              'Porque en tus relaciones das más de lo que recibes. Te cuesta poner límites, decir "no" sin sentir culpa o pedir lo que necesitas sin miedo a perder el cariño del otro. Y aunque parezcas fuerte, muchas veces te sientes sola, no vista o emocionalmente cansada',
              'Porque hay momentos en los que dudas de ti misma, incluso cuando los demás te ven capaz. Esa voz interna que te exige más, que te compara o que te hace sentir que "no estás haciendo lo suficiente", se ha vuelto demasiado ruidosa',
              'Porque si bien has logrado mucho —has migrado, te has reinventado, empezado de cero— a veces te sientes desconectada de ti, de tu esencia, de tu propósito. No sabes si el camino que estás siguiendo realmente te representa o si solo estás sobreviviendo',
              'Porque llevas tiempo sintiendo que necesitas una pausa. Salir de la rutina, soltar el control y darte el permiso de escucharte, sin tener que sostener a todos los demás',
              'Porque sabes que este cierre de año no puede ser igual. Sientes el llamado de dejar atrás lo viejo, ordenar tus emociones y poner claridad en tus metas para 2026. Quieres aprender cómo transformar tu mente y accionar con confianza, sin miedo ni autoexigencia',
              'Y porque quieres rodearte de mujeres como tú: valientes, sensibles, auténticas. Mujeres que entienden el peso de empezar de nuevo, que buscan paz, propósito y expansión. Una tribu donde no tengas que fingir fortaleza, solo permitirte ser'
            ].map((text, index) => (
              <div key={index} className="flex items-start space-x-4 bg-white p-6 shadow-md">
                <div className="flex-shrink-0 text-2xl text-[#8B7355]">•</div>
                <p className="text-lg text-gray-700 leading-relaxed">{text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Image Banner */}
      <section className="py-0">
        <div className="w-full h-64 sm:h-80 md:h-96 lg:h-[500px]">
          <img 
            src="/groupe.png" 
            alt="Groupe de femmes" 
            className="w-full h-full object-cover"
          />
        </div>
      </section>

      {/* Pricing Section */}
      <section className="py-12 sm:py-16 md:py-20 px-4" style={{backgroundColor: '#DDE6D7'}}>
        <div className="container mx-auto max-w-4xl">
          <div className="text-center mb-8 sm:mb-12">
            <div className="inline-block bg-white px-6 sm:px-8 py-2 sm:py-3 mb-4 sm:mb-6 shadow-lg">
              <span className="font-bold text-base sm:text-lg md:text-xl text-[#8B7355]">¡Sólo para mujeres!</span>
            </div>
            <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-gray-900 mb-2 sm:mb-3">
              DESCUENTO DE
            </h2>
            <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-gray-900 mb-1 sm:mb-2">
              PREVENTA
            </h2>
            <p className="text-lg sm:text-xl text-gray-700">(Por tiempo limitado)</p>
          </div>

          <div className="bg-white shadow-xl p-6 sm:p-8 md:p-10 mb-6 sm:mb-8">
            <div className="text-center mb-8 sm:mb-10">
              <p className="text-base sm:text-lg text-gray-600 mb-2 sm:mb-3">Residentes en Francia o fuera</p>
              <p className="text-2xl sm:text-3xl text-gray-400 line-through mb-1 sm:mb-2">€199 EUR</p>
              <p className="text-5xl sm:text-6xl md:text-7xl font-bold text-[#8B7355] mb-4 sm:mb-6">
                €149 EUR
              </p>
            </div>

            <div className="bg-gray-50 p-4 sm:p-6 mb-6 sm:mb-8 text-center">
              <p className="text-lg sm:text-xl font-bold text-gray-900 mb-2 sm:mb-3">Pago completo o pago a cuotas</p>
              <p className="text-sm sm:text-base text-gray-700 leading-relaxed">
                En cuotas, el primer pago (€50) se realiza al momento de la inscripción, el segundo (€50) en noviembre y el último (€49) antes del retiro, en diciembre
              </p>
            </div>

            <div className="text-center">
              <Button 
                size="lg"
                className="bg-[#8B7355] hover:bg-[#6d5a43] text-white text-base sm:text-lg md:text-xl px-8 sm:px-10 md:px-12 py-5 sm:py-6 font-bold mb-4 sm:mb-6 w-full md:w-auto"
                onClick={() => window.open('https://checkout.mailerlite.com/checkout/6005', '_blank')}
              >
                QUIERO REALIZAR MI PAGO
              </Button>
              <p className="text-xs sm:text-sm text-gray-600 mt-4 sm:mt-6 leading-relaxed">
                <strong>Opciones de pago:</strong> Contamos con diferentes métodos de pago: Transferencia o Wero (para residentes en Francia). Tarjeta de crédito o débito (para residentes en Europa o fuera de ella)
              </p>
              <div className="mt-4 sm:mt-6 inline-block bg-[#DDE6D7] px-6 sm:px-8 py-3 sm:py-4 border-2 border-[#8B7355]">
                <p className="font-bold text-base sm:text-lg text-gray-800">
                  % Descuento para grupos a partir de 4 mujeres %
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* What Includes & What to Expect */}
      <section className="py-12 sm:py-16 md:py-20 px-4 bg-white">
        <div className="container mx-auto max-w-6xl">
          <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-center text-gray-800 mb-10 sm:mb-12 md:mb-16">
            ¡1 DÍA QUE LO CAMBIARÁN TODO!
          </h2>
          <div className="grid md:grid-cols-2 gap-6 sm:gap-8">
            {/* Que Incluye */}
            <div>
              <h3 className="text-2xl sm:text-3xl font-bold text-center text-white bg-[#8B7355] py-4 sm:py-6 mb-0">
                ¿QUÉ INCLUYE?
              </h3>
              <div className="bg-gray-50 p-5 sm:p-6 md:p-8 space-y-3 sm:space-y-4">
                {[
                  'Un día completo de transformación (8h30 a 18h30) en El Jardín Secreto de París',
                  'Desayuno, almuerzo con postre y merienda saludable',
                  'Bienvenida especial con ritual de apertura',
                  'Kit de bienvenida: Incluye materiales de trabajo, herramientas prácticas para los talleres y un regalo sorpresa',
                  'Fogata y experiencia de cierre',
                  'Taller "Point of You" – Coaching de creencias',
                  'Movimiento consciente',
                  'Participación en todos los talleres del programa Renacer',
                  'Actividades de recreación y conexión grupal'
                ].map((item, index) => (
                  <div key={index} className="flex items-start space-x-2 sm:space-x-3">
                    <div className="flex-shrink-0 text-lg sm:text-xl text-[#8B7355] font-bold">•</div>
                    <p className="text-sm sm:text-base text-gray-700 leading-relaxed">{item}</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Que Esperar */}
            <div>
              <h3 className="text-2xl sm:text-3xl font-bold text-center text-white bg-[#6d5a43] py-4 sm:py-6 mb-0">
                ¿QUÉ ESPERAR?
              </h3>
              <div className="bg-gray-50 p-5 sm:p-6 md:p-8 space-y-3 sm:space-y-4">
                {[
                  'Un espacio seguro y amoroso para conectar contigo y con mujeres que comparten tu deseo de crecimiento',
                  'Actividades que integran cuerpo, mente y alma',
                  'Herramientas prácticas y psicológicas para tu día a día',
                  'Meditaciones, mindfulness y bioenergética',
                  'Taller de coaching transformacional "Point of You"',
                  'Momentos de introspección y expansión',
                  'Espacios de recreación, música, movimiento y risas',
                  'Una comprensión más profunda de ti misma',
                  'Un nuevo enfoque para tu vida y relaciones',
                  'Un cierre de año poderoso con metas claras para 2026'
                ].map((item, index) => (
                  <div key={index} className="flex items-start space-x-2 sm:space-x-3">
                    <div className="flex-shrink-0 text-lg sm:text-xl text-[#6d5a43] font-bold">•</div>
                    <p className="text-sm sm:text-base text-gray-700 leading-relaxed">{item}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <div className="text-center mt-8 sm:mt-10 md:mt-12">
            <Button 
              size="lg"
              className="bg-[#8B7355] hover:bg-[#6d5a43] text-white text-base sm:text-lg md:text-xl px-8 sm:px-10 md:px-12 py-5 sm:py-6 font-bold w-full sm:w-auto"
              onClick={() => window.open('https://checkout.mailerlite.com/checkout/6005', '_blank')}
            >
              RESERVA TU LUGAR
            </Button>
          </div>
        </div>
      </section>

      {/* Location */}
      <section className="py-12 sm:py-16 md:py-20 px-4" style={{backgroundColor: '#F5F5F0'}}>
        <div className="container mx-auto max-w-5xl">
          <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-center text-gray-800 mb-8 sm:mb-10 md:mb-12">
            El Jardín Secreto – París, Francia
          </h2>
          <div className="mb-6 sm:mb-8">
            <img 
              src="/jardin-piscine-v2.jpg" 
              alt="El Jardín Secreto" 
              className="w-full h-64 sm:h-80 md:h-96 lg:h-[500px] object-cover shadow-xl"
            />
          </div>
          <div className="space-y-3 sm:space-y-4 text-base sm:text-lg text-gray-700 leading-relaxed">
            <p>
              En el corazón del histórico <strong>Barrio Latino de París</strong> se encuentra El Jardín Secreto, una joya escondida donde el silencio, la belleza y la historia se entrelazan.
            </p>
            <p>
              Una casa del siglo XVIII completamente restaurada, rodeada de un jardín privado lleno de luz, calma y armonía. Este refugio ofrece una atmósfera íntima y serena, perfecta para desconectar del ruido exterior y reconectar contigo misma.
            </p>
            <p>
              Cada rincón invita a la introspección: la calidez de la luz natural, los árboles centenarios, el sonido suave de las campanas… un entorno que abraza el alma y la mente.
            </p>
            <p>
              Aquí viviremos el <strong>Retiro Renacer</strong>, un día diseñado para cerrar el año y abrir un nuevo ciclo con propósito y claridad.
            </p>
            <p className="font-semibold">
              El Jardín Secreto no es solo el lugar del retiro, es parte de la experiencia: un escenario donde el alma se expande y la mente se transforma.
            </p>
          </div>
        </div>
      </section>

      {/* Retreat Space */}
      <section className="py-12 sm:py-16 md:py-20 px-4 bg-white">
        <div className="container mx-auto max-w-6xl">
          <h2 className="text-3xl sm:text-4xl font-bold text-center text-gray-800 mb-8 sm:mb-10 md:mb-12">
            Alojamiento
          </h2>
          <div className="grid md:grid-cols-2 gap-6 sm:gap-8">
            <div className="space-y-4">
              <img 
                src="/salon-cheminee.jpg" 
                alt="Espacio del retiro" 
                className="w-full h-48 sm:h-64 md:h-72 lg:h-80 object-cover shadow-lg"
              />
              <img 
                src="/salle-manger.jpg" 
                alt="Comedor" 
                className="w-full h-48 sm:h-64 md:h-72 lg:h-80 object-cover shadow-lg"
              />
            </div>
            <div className="flex flex-col justify-center space-y-4 sm:space-y-6">
              <p className="text-lg sm:text-xl md:text-2xl text-gray-700 leading-relaxed">
                Un espacio exclusivo con espacios luminosos y acogedores, rodeados de naturaleza y detalles parisinos
              </p>
              <p className="text-base sm:text-lg md:text-xl text-gray-700 leading-relaxed">
                Un entorno privado y lleno de calma donde cada rincón invita a reconectar contigo
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Why Different */}
      <section className="py-12 sm:py-16 md:py-20 px-4" style={{backgroundColor: '#FDFCFB'}}>
        <div className="container mx-auto max-w-6xl">
          <h2 className="text-2xl sm:text-3xl md:text-4xl font-bold text-center text-gray-800 mb-10 sm:mb-12 md:mb-16">
            ¿POR QUÉ NUESTROS RETIROS SON DIFERENTES Y ÚNICOS?
          </h2>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
            {[
              {
                img: '/jardin-hero.jpg',
                title: 'EXPERIENCIA DE LUJO',
                text: 'Cada detalle ha sido cuidadosamente diseñado para ofrecerte una experiencia elegante, íntima y transformadora.'
              },
              {
                img: '/femme-transformation.jpg',
                title: 'LA RÁPIDA TRANSFORMACIÓN',
                text: 'Vive una profunda transformación en tus retos y desafíos más difíciles. Descubrirás que cualquier dolor puede ser sanado.'
              },
              {
                img: '/femme-meditation.jpg',
                title: 'EL PODER DE LA AUTENTICIDAD',
                text: 'Nuestros retiros se centran en la transformación real, sin distracciones, llevándote de vuelta a lo esencial.'
              },
              {
                img: '/groupe.png',
                title: 'LAS SESIONES GRUPALES',
                text: 'Podrás trabajar en tus problemas más apremiantes. Estas sesiones mueven una energía muy poderosa.'
              },
              {
                img: '/groupe.png',
                title: 'LAS AMISTADES ETERNAS',
                text: 'Conocerás a mujeres que te cambiarán la vida. Tendrás la oportunidad de compartir experiencias únicas.'
              },
              {
                img: '/jardin-piscine-v2.jpg',
                title: 'CONEXIÓN CON LA NATURALEZA',
                text: 'Nuestros retiros se realizan en lugares de profunda conexión con la naturaleza como fuente de bienestar.'
              },
              {
                img: '/salon-cheminee.jpg',
                title: 'ESPIRITUALIDAD',
                text: 'Te sumergirás en prácticas espirituales cotidianas, incluyendo mindfulness, meditación y afirmaciones.'
              },
              {
                img: '/dianix-portrait.jpg',
                title: 'NUESTRO EQUIPO',
                text: 'La calidad humana y el amor de nuestro equipo hace que nuestro retiro sea excepcional.'
              }
            ].map((item, index) => (
              <div key={index} className="bg-white shadow-lg overflow-hidden">
                <div className="h-40 sm:h-48 overflow-hidden">
                  <img 
                    src={item.img} 
                    alt={item.title}
                    className="w-full h-full object-cover"
                  />
                </div>
                <div className="p-4 sm:p-6">
                  <h3 className="text-base sm:text-lg font-bold text-[#8B7355] mb-2 sm:mb-3 uppercase">
                    {item.title}
                  </h3>
                  <p className="text-xs sm:text-sm text-gray-700 leading-relaxed">
                    {item.text}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Founders */}
      <section className="py-12 sm:py-16 md:py-20 px-4 bg-white">
        <div className="container mx-auto max-w-6xl">
          <div className="text-center mb-8 sm:mb-12">
            <h3 className="text-lg sm:text-xl text-gray-600 mb-2">Fundadoras del retiro</h3>
          </div>
          
          {/* Nicole Ramírez */}
          <div className="mb-12 sm:mb-16 md:mb-20">
            <div className="text-center mb-6 sm:mb-8">
              <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-gray-800 mb-3 sm:mb-4">
                Hola, Hermosa
              </h2>
              <h3 className="text-2xl sm:text-3xl md:text-4xl font-bold text-[#8B7355]">
                Soy Nicole Ramírez
              </h3>
            </div>
            
            <div className="grid md:grid-cols-2 gap-8 sm:gap-10 md:gap-12 items-center">
              <div>
                <img 
                  src="/victoria-portrait.jpg" 
                  alt="Nicole Ramírez" 
                  className="w-full h-80 sm:h-96 md:h-[500px] lg:h-[600px] object-cover shadow-2xl"
                />
              </div>
              <div className="space-y-3 sm:space-y-4 text-gray-700 leading-relaxed text-sm sm:text-base">
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
                <p className="font-semibold text-[#8B7355] text-lg">
                  Cuando transformas tus pensamientos, transformas tu realidad.
                </p>
                <p className="bg-[#F5F5F0] p-6 border-l-4 border-[#8B7355] font-semibold">
                  En el retiro Renacer voy a compartir contigo las herramientas, experiencias y prácticas que me ayudaron a pasar de tener cero posibilidades en mi país, a crear una vida alineada a mis deseos, viviendo con plenitud, confianza y serenidad. Te acompañaré paso a paso para que tú también puedas cerrar un ciclo, liberar lo que pesa y construir desde adentro la vida que mereces vivir.
                </p>
              </div>
            </div>
          </div>

          {/* Dianix Bermúdez */}
          <div>
            <div className="text-center mb-6 sm:mb-8">
              <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-gray-800 mb-3 sm:mb-4">
                Hola, soy Dianix Bermúdez
              </h2>
              <p className="text-lg sm:text-xl text-gray-600">(Facilitadora)</p>
            </div>
            
            <div className="grid md:grid-cols-2 gap-8 sm:gap-10 md:gap-12 items-center">
              <div className="order-2 md:order-1 space-y-3 sm:space-y-4 text-gray-700 leading-relaxed text-sm sm:text-base">
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
                <p className="bg-[#F5F5F0] p-6 border-l-4 border-[#8B7355] font-semibold">
                  En este retiro quiero acompañarte a recordar tu poder interior, reconectarte con tu energía más auténtica y abrir espacio para que la abundancia llegue a tu vida con facilidad y propósito.
                </p>
              </div>
              <div className="order-1 md:order-2">
                <img 
                  src="/dianix-portrait.jpg" 
                  alt="Dianix Bermúdez" 
                  className="w-full h-80 sm:h-96 md:h-[500px] lg:h-[600px] object-cover shadow-2xl"
                />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-12 sm:py-16 md:py-20 px-4" style={{backgroundColor: '#F5F5F0'}}>
        <div className="container mx-auto max-w-6xl">
          <h2 className="text-3xl sm:text-4xl font-bold text-center text-gray-800 mb-10 sm:mb-12 md:mb-16">
            Testimonios
          </h2>
          <div className="space-y-6 sm:space-y-8">
            {[
              {
                text: 'Ayer viví un mini retiro transformador. Entré sin expectativas, sin saber nada, solo con la intención de conectar y abrirme a lo que viniera. Lo que encontré fue eso y mucho más: claridad, fuerza interior y un conocimiento profundo de mí misma que necesitaba en este momento de mi vida.',
                author: '- Karla'
              },
              {
                text: 'Me traje tranquilidad. Varias de las actividades y las experiencias que compartieron otras mujeres me ayudaron a ver una luz en el camino. Hoy me siento más en paz y con esperanza.',
                author: '- Vanessa'
              },
              {
                text: 'Sentí mucho valor y un profundo reencuentro conmigo. Me permití ser vulnerable, abrirme y compartir desde el corazón. Fue un día de liberación y conexión real.',
                author: '- Carolina'
              },
              {
                text: 'Me encantó compartir y escuchar a otras compañeras con historias parecidas a la mía. La guía psicológica y espiritual durante todo el día fue increíble. Me voy con claridad, calma y motivación.',
                author: '- Fabiana'
              },
              {
                text: 'El retiro fue una experiencia profundamente sanadora. Llegué con muchas preguntas y me fui con claridad, serenidad y una nueva visión de mí misma.',
                author: '- Marcela'
              },
              {
                text: 'Me sentí acompañada, vista y contenida. Fue un espacio lleno de amor donde pude reconectar con mi poder y mi fe en la vida.',
                author: '- Luz'
              }
            ].map((testimonial, index) => (
              <div key={index} className="bg-white p-5 sm:p-6 md:p-8 shadow-lg border-l-4 border-[#8B7355]">
                <p className="text-base sm:text-lg md:text-xl text-gray-700 italic mb-3 sm:mb-4 leading-relaxed">
                  "{testimonial.text}"
                </p>
                <p className="text-base sm:text-lg font-semibold text-[#8B7355]">
                  {testimonial.author}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-12 sm:py-16 md:py-20 px-4 bg-white">
        <div className="container mx-auto max-w-4xl">
          <h2 className="text-3xl sm:text-4xl font-bold text-center text-gray-800 mb-10 sm:mb-12 md:mb-16">
            Preguntas frecuentes
          </h2>
          <Accordion type="single" collapsible className="space-y-3 sm:space-y-4">
            {[
              {
                question: '¿Puedo ir sola?',
                answer: '¡Claro que sí! De hecho, la mayoría de las mujeres que asisten vienen solas. Renacer está pensado para que desde el primer momento te sientas acompañada y segura.'
              },
              {
                question: '¿Qué pasa después de hacer mi pago?',
                answer: 'Una vez que realices tu pago, recibirás un correo de confirmación con todos los detalles. Te enviaremos información práctica y estarás invitada a un grupo privado de WhatsApp.'
              },
              {
                question: '¿El vuelo o transporte están incluidos?',
                answer: 'No. El valor del retiro no incluye el vuelo ni el transporte. Te enviaremos una guía con las mejores rutas y opciones de transporte dentro de París.'
              },
              {
                question: '¿Qué pasa si nunca he ido a un retiro?',
                answer: 'No necesitas tener experiencia previa. Renacer fue creado para mujeres que simplemente sienten el llamado a un cambio. Estarás acompañada todo el tiempo.'
              },
              {
                question: '¿Si vivo en otro país, puedo asistir?',
                answer: 'Sí, por supuesto. Renacer es una experiencia internacional. París es muy accesible y el retiro se realiza en una ubicación céntrica y segura.'
              }
            ].map((faq, index) => (
              <AccordionItem key={index} value={`item-${index}`} className="bg-gray-50 border-2 border-gray-200">
                <AccordionTrigger className="px-4 sm:px-6 py-4 sm:py-5 text-base sm:text-lg md:text-xl font-bold text-gray-800 hover:no-underline hover:bg-gray-100 text-left">
                  {faq.question}
                </AccordionTrigger>
                <AccordionContent className="px-4 sm:px-6 pb-5 sm:pb-6 text-sm sm:text-base md:text-lg text-gray-700 leading-relaxed">
                  {faq.answer}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </section>

      {/* CTA Final */}
      <section className="py-12 sm:py-16 md:py-20 px-4 bg-[#8B7355]">
        <div className="container mx-auto max-w-4xl text-center">
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4 sm:mb-6">
            ¿Tienes dudas?
          </h2>
          <div className="space-y-2 sm:space-y-3 mb-8 sm:mb-10">
            <p className="text-xl sm:text-2xl text-white">
              ¿No sabes si es para ti?
            </p>
            <p className="text-xl sm:text-2xl text-white">
              ¿No has ido nunca de retiro?
            </p>
          </div>
          <p className="text-base sm:text-lg md:text-xl text-white mb-8 sm:mb-10 max-w-2xl mx-auto leading-relaxed px-2">
            Escríbeme y estaré lista con todo mi equipo para brindarte toda la ayuda que necesites.
          </p>
          <Button 
            size="lg"
            className="bg-white text-[#8B7355] hover:bg-gray-100 text-base sm:text-lg md:text-xl px-8 sm:px-10 md:px-12 py-5 sm:py-6 font-bold shadow-2xl w-full sm:w-auto"
            onClick={() => window.open('https://wa.me/33667596062', '_blank')}
          >
            HABLAR CON SOPORTE
          </Button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8 sm:py-10 md:py-12 px-4">
        <div className="container mx-auto max-w-6xl">
          <div className="flex flex-col md:flex-row justify-between items-center mb-6 sm:mb-8">
            <div className="flex items-center space-x-2 sm:space-x-3 mb-4 md:mb-0">
              <img 
                src="/logo-transparent.png" 
                alt="Logo" 
                className="h-10 w-10 sm:h-12 sm:w-12 object-contain"
              />
              <span className="text-lg sm:text-xl font-semibold">Cambio de Paradigma</span>
            </div>
            <div className="flex space-x-4 sm:space-x-6 text-sm sm:text-base">
              <a href="https://www.instagram.com/cambio.de.paradigma/" target="_blank" rel="noopener noreferrer" className="hover:text-[#8B7355] transition-colors">Instagram</a>
              <a href="https://www.tiktok.com/@cambio.de.paradigma" target="_blank" rel="noopener noreferrer" className="hover:text-[#8B7355] transition-colors">TikTok</a>
              <a href="https://wa.me/33667596062" target="_blank" rel="noopener noreferrer" className="hover:text-[#8B7355] transition-colors">Whatsapp</a>
            </div>
          </div>
          <div className="text-center text-xs sm:text-sm text-gray-400 border-t border-gray-700 pt-6 sm:pt-8">
            <p>Cambio de Paradigma - Copyright© 2024. Todos los derechos reservados.</p>
            <p className="mt-2 text-xs">
              DESCARGOS DE RESPONSABILIDAD IMPORTANTES: Este sitio no es parte del sitio web de Facebook o Facebook, Inc.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default RetiroAmateStyle;

