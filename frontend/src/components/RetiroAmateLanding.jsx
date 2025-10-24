import React, { useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';

const LandingPage = () => {
  const navigate = useNavigate();
  const videoRef1 = useRef(null);
  const videoRef2 = useRef(null);
  const videoRef3 = useRef(null);

  useEffect(() => {
    const handleVideoEnd = (videoElement) => {
      // Fade out
      videoElement.style.transition = 'opacity 0.6s ease-out';
      videoElement.style.opacity = '0';
      
      setTimeout(() => {
        if (videoElement && videoElement.paused) {
          videoElement.currentTime = 0;
          videoElement.play();
          // Fade in
          setTimeout(() => {
            videoElement.style.transition = 'opacity 0.6s ease-in';
            videoElement.style.opacity = '1';
          }, 50);
        }
      }, 800); // Délai réduit à 0.8 seconde
    };

    const setupVideo = (videoRef, playbackSpeed = 0.8) => {
      const video = videoRef.current;
      if (video) {
        video.playbackRate = playbackSpeed;
        // Fade in initial
        video.style.opacity = '0';
        video.addEventListener('loadeddata', () => {
          video.style.transition = 'opacity 0.6s ease-in';
          video.style.opacity = '1';
        });
        video.addEventListener('ended', () => handleVideoEnd(video));
        return () => {
          video.removeEventListener('ended', () => handleVideoEnd(video));
        };
      }
    };

    const cleanup1 = setupVideo(videoRef1, 0.8); // Ralentir de 20%
    const cleanup2 = setupVideo(videoRef2, 1.0); // Vitesse normale
    const cleanup3 = setupVideo(videoRef3, 0.8); // Ralentir de 20%

    return () => {
      cleanup1 && cleanup1();
      cleanup2 && cleanup2();
      cleanup3 && cleanup3();
    };
  }, []);


  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="fixed top-0 w-full bg-white/80 backdrop-blur-lg shadow-elegant z-50 border-b border-stone-200/50 transition-all duration-300">
        <div className="container mx-auto px-6 py-4 flex justify-between items-center">
          <div className="flex items-center space-x-4 animate-fade-in">
            <img 
              src="/logo-renacer.png" 
              alt="Cambio de Paradigma" 
              className="w-12 h-12 object-contain transition-transform hover:scale-110"
              onError={(e) => {
                e.target.style.display = 'none';
              }}
            />
            <div>
              <h1 className="text-2xl font-bold bg-gradient-to-r from-sage-600 to-sage-700 bg-clip-text text-transparent">
                Cambio de Paradigma
              </h1>
              <p className="text-xs text-taupe-600 font-medium">Retiro Renacer</p>
            </div>
          </div>
          <Button
            onClick={() => navigate('/login')}
            variant="outline"
            className="border-2 border-sage-600 text-sage-700 hover:bg-sage-600 hover:text-white transition-all duration-300 font-semibold rounded-full shadow-sm hover:shadow-sage"
          >
            Iniciar sesión
          </Button>
        </div>
      </header>

      {/* Hero Section */}
      <section className="pt-32 pb-24 px-6 relative overflow-hidden">
        <div className="absolute inset-0">
          <img 
            src="/jardin-hero.jpg" 
            alt="El Jardín Secreto - París" 
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-white/60 via-white/70 to-white/75" />
        </div>
        <div className="container mx-auto max-w-5xl text-center relative z-10">
          <div className="w-32 h-32 mx-auto mb-10 animate-scale-in">
            <img 
              src="/logo-renacer.png" 
              alt="Logo Cambio de Paradigma" 
              className="w-full h-full object-contain drop-shadow-2xl hover:scale-110 transition-transform duration-300"
            />
          </div>
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6 leading-tight tracking-tight animate-slide-up">
            Rompe tus creencias, libera tus bloqueos y vuelve a confiar en ti
          </h1>
          <p className="text-xl md:text-2xl text-gray-700 mb-12 max-w-4xl mx-auto leading-relaxed animate-fade-in">
            Sana tu historia, gana claridad y aprende a construir la vida que realmente deseas, en un espacio único y seguro
          </p>
          <Button 
            size="lg"
            className="bg-sage-600 hover:bg-sage-700 text-white shadow-elegant hover:shadow-sage hover:scale-105 transition-all duration-300 text-lg px-8 py-6 rounded-full font-semibold"
            onClick={() => window.open('https://wa.me/33667596062', '_blank')}
          >
            HABLAR CON EL EQUIPO
          </Button>
        </div>
      </section>

      {/* Date & Location */}
      <section className="py-20 relative overflow-hidden" style={{backgroundColor: '#F5F5F0'}}>
        <div className="absolute inset-0 bg-gradient-to-b from-transparent via-sage-50/30 to-transparent" />
        <div className="container mx-auto max-w-5xl text-center px-6 relative z-10">
          <Card className="inline-block bg-white/90 backdrop-blur-sm shadow-elegant hover:shadow-sage border-2 border-sage-200 transition-all duration-300 hover:scale-102">
            <CardContent className="p-8 md:p-10">
              <h2 className="text-3xl md:text-5xl font-bold bg-gradient-to-r from-sage-700 via-sage-600 to-taupe-600 bg-clip-text text-transparent tracking-tight">
                14 de diciembre | El Jardín Secreto – París, Francia
              </h2>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Experience Description */}
      <section className="py-24 relative overflow-hidden">
        <div className="absolute inset-0">
          <img 
            src="/femme-transformation.jpg" 
            alt="Transformation intérieure" 
            className="w-full h-full object-cover"
            style={{ objectPosition: 'center 70%' }}
          />
          <div className="absolute inset-0 bg-gradient-to-b from-white/60 via-white/70 to-white/75" />
        </div>
        <div className="container mx-auto max-w-5xl text-center px-6 relative z-10">
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 mb-8 leading-tight tracking-tight animate-fade-in">
            Vive una experiencia de <span className="bg-gradient-sage bg-clip-text text-transparent">transformación interior</span> para cerrar el año con claridad y propósito
          </h2>
          <p className="text-xl md:text-2xl text-gray-700 leading-relaxed max-w-4xl mx-auto">
            Descubre cómo reprogramar tu mente, liberar la confusión emocional y recuperar la seguridad en tus decisiones y en ti misma
          </p>
        </div>
      </section>

      {/* Why This Retreat */}
      <section className="py-24" style={{backgroundColor: '#F9F6F3'}}>
        <div className="container mx-auto max-w-7xl px-6">
          <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-20 tracking-tight">
            ¿Por qué el Retiro Renacer es para ti?
          </h2>
          <div className="grid lg:grid-cols-3 gap-8">
            {/* 2/3 largeur - Toutes les cartes empilées */}
            <div className="lg:col-span-2 space-y-6">
              {[
                'Porque en tus relaciones das más de lo que recibes. Te cuesta poner límites, decir "no" sin sentir culpa o pedir lo que necesitas sin miedo a perder el cariño del otro. Y aunque parezcas fuerte, muchas veces te sientes sola, no vista o emocionalmente cansada',
                'Porque hay momentos en los que dudas de ti misma, incluso cuando los demás te ven capaz. Esa voz interna que te exige más, que te compara o que te hace sentir que "no estás haciendo lo suficiente", se ha vuelto demasiado ruidosa',
                'Porque si bien has logrado mucho —has migrado, te has reinventado, empezado de cero— a veces te sientes desconectada de ti, de tu esencia, de tu propósito. No sabes si el camino que estás siguiendo realmente te representa o si solo estás sobreviviendo',
                'Porque llevas tiempo sintiendo que necesitas una pausa. Salir de la rutina, soltar el control y darte el permiso de escucharte, sin tener que sostener a todos los demás',
                'Porque sabes que este cierre de año no puede ser igual. Sientes el llamado de dejar atrás lo viejo, ordenar tus emociones y poner claridad en tus metas para 2026. Quieres aprender cómo transformar tu mente y accionar con confianza, sin miedo ni autoexigencia',
                'Y porque quieres rodearte de mujeres como tú: valientes, sensibles, auténticas. Mujeres que entienden el peso de empezar de nuevo, que buscan paz, propósito y expansión. Una tribu donde no tengas que fingir fortaleza, solo permitirte ser'
              ].map((text, index) => (
                <Card key={index} className="group hover:shadow-elegant hover:scale-102 transition-all duration-300 border-2 border-stone-200 hover:border-sage-300 bg-white overflow-hidden">
                  <CardContent className="flex items-start space-x-4 p-6">
                    <div className="flex-shrink-0 w-12 h-12 bg-gradient-sage rounded-xl flex items-center justify-center text-white font-bold shadow-sage group-hover:scale-110 transition-transform duration-300">
                      ✓
                    </div>
                    <p className="text-gray-700 text-lg leading-relaxed">{text}</p>
                  </CardContent>
                </Card>
              ))}
            </div>

            {/* 1/3 largeur - Vidéo verticale */}
            <div className="flex items-start justify-center lg:sticky lg:top-24">
              <div className="w-full rounded-3xl overflow-hidden shadow-2xl hover:shadow-sage transition-all duration-500 border-4 border-white">
                <video 
                  ref={videoRef1}
                  className="w-full h-auto"
                  autoPlay 
                  muted 
                  playsInline
                >
                  <source src="/video-para-ti.mov" type="video/mp4" />
                </video>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Image Banner 1 */}
      <section className="py-12 bg-white">
        <div className="container mx-auto px-6">
          <div className="w-full h-96 rounded-3xl overflow-hidden shadow-elegant relative">
            <img 
              src="/groupe-retiro.jpg" 
              alt="Groupe de femmes - Retiro Renacer" 
              className="w-full h-full object-cover"
            />
            <div className="absolute inset-0 bg-gradient-to-b from-white/60 via-white/70 to-white/75" />
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section className="py-24 relative overflow-hidden" style={{backgroundColor: '#eef2ec'}}>
        <div className="absolute inset-0 bg-gradient-to-br from-sage-100/50 to-transparent" />
        <div className="container mx-auto max-w-4xl px-6 relative z-10">
          <div className="text-center mb-16 animate-fade-in">
            <div className="inline-block bg-white px-8 py-4 rounded-full mb-8 shadow-sage border-2 border-sage-400 hover:scale-105 transition-transform duration-300">
              <span className="font-bold text-xl bg-gradient-sage bg-clip-text text-transparent">¡Sólo para mujeres!</span>
            </div>
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4 tracking-tight">
              DESCUENTO DE PREVENTA
            </h2>
            <p className="text-sage-700 text-xl mb-2 font-medium">(Por tiempo limitado)</p>
          </div>

          <Card className="bg-white rounded-3xl shadow-elegant hover:shadow-sage border-2 border-sage-200 overflow-hidden transition-all duration-300">
            <CardContent className="p-12">
              <div>
                <div className="text-center mb-10">
                  <p className="text-gray-600 mb-4 text-lg font-medium">Residentes en Francia o fuera</p>
                  <p className="text-3xl text-gray-400 line-through mb-3">€199 EUR</p>
                  <div className="relative inline-block">
                    <p className="text-6xl md:text-7xl font-bold bg-gradient-sage bg-clip-text text-transparent mb-8 animate-scale-in">
                      €149 EUR
                    </p>
                    <div className="absolute -top-4 -right-20 bg-lavender-600 text-white text-sm font-bold px-4 py-2 rounded-full rotate-12 shadow-lg">
                      -25%
                    </div>
                  </div>
                </div>

                <Card className="text-center mb-10 bg-gradient-to-br from-sage-50 to-taupe-50 border-2 border-sage-200">
                  <CardContent className="p-6">
                    <p className="text-gray-900 mb-4 font-bold text-xl">Pago completo o pago en cuotas</p>
                    <p className="text-base text-gray-700 leading-relaxed">
                      En cuotas, el primer pago (€50) se realiza al momento de la inscripción, el segundo (€50) en noviembre y el último (€49) antes del retiro, en diciembre
                    </p>
                  </CardContent>
                </Card>
              </div>

              <div className="text-center">
                <Button 
                  size="lg"
                  className="bg-gradient-sage hover:opacity-90 text-white shadow-sage hover:shadow-elegant hover:scale-105 transition-all duration-300 text-lg px-10 py-6 rounded-full font-bold mb-6"
                  onClick={() => window.open('https://checkout.mailerlite.com/checkout/6005', '_blank')}
                >
                  QUIERO REALIZAR MI PAGO
                </Button>
                <p className="text-base text-gray-600 mt-6 leading-relaxed max-w-2xl mx-auto">
                  Opciones de pago: Contamos con diferentes métodos de pago: Transferencia o Wero (para residentes en Francia). Tarjeta de crédito o débito (para residentes en Europa o fuera de ella)
                </p>
                <div className="mt-6 inline-block bg-gradient-to-r from-lavender-100 to-lavender-50 px-8 py-4 rounded-full border-2 border-lavender-300 shadow-md">
                  <p className="font-bold text-lg text-lavender-800">
                    🎁 Descuento para grupos a partir de 4 mujeres
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* What's Included & What to Expect - 2 colonnes */}
      <section className="py-24 bg-gradient-to-b from-stone-50 to-white">
        <div className="container mx-auto max-w-7xl px-6">
          <h2 className="text-4xl md:text-6xl font-bold text-center text-gray-800 mb-20 tracking-tight">
            1 DÍA QUE PUEDE CAMBIARLO TODO
          </h2>
          <div className="grid md:grid-cols-2 gap-8">
            {/* Colonne 1: Que Incluye */}
            <Card className="overflow-hidden shadow-2xl hover:shadow-sage transition-all duration-300 border-0">
              <CardHeader className="bg-gradient-to-br from-sage-600 to-sage-700 text-white pb-8">
                <CardTitle className="text-3xl font-bold text-center">
                ¿QUÉ INCLUYE?
                </CardTitle>
              </CardHeader>
              <CardContent className="p-8 bg-gradient-to-b from-sage-50/30 to-white">
                <div className="space-y-5">
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
                ].map((item, index) => (
                    <div key={index} className="flex items-start space-x-4 group">
                      <div className="flex-shrink-0 w-8 h-8 bg-gradient-to-br from-sage-500 to-sage-600 rounded-full flex items-center justify-center text-white font-bold shadow-lg group-hover:scale-110 transition-transform duration-300">
                      ✓
                    </div>
                      <p className="text-gray-800 leading-relaxed text-base pt-1">{item}</p>
                  </div>
                ))}
              </div>
              </CardContent>
            </Card>

            {/* Colonne 2: Que Esperar */}
            <Card className="overflow-hidden shadow-2xl hover:shadow-elegant transition-all duration-300 border-0">
              <CardHeader className="bg-gradient-to-br from-taupe-600 to-taupe-700 text-white pb-8">
                <CardTitle className="text-3xl font-bold text-center">
                ¿QUÉ ESPERAR?
                </CardTitle>
              </CardHeader>
              <CardContent className="p-8 bg-gradient-to-b from-taupe-50/30 to-white">
                <div className="space-y-5">
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
                ].map((item, index) => (
                    <div key={index} className="flex items-start space-x-4 group">
                      <div className="flex-shrink-0 w-8 h-8 bg-gradient-to-br from-taupe-500 to-taupe-600 rounded-full flex items-center justify-center text-white font-bold shadow-lg group-hover:scale-110 transition-transform duration-300">
                      •
                    </div>
                      <p className="text-gray-800 leading-relaxed text-base pt-1">{item}</p>
                  </div>
                ))}
              </div>
              </CardContent>
            </Card>
          </div>

          <div className="text-center mt-16">
            <Button 
              size="lg"
              style={{backgroundColor: '#6b745a'}}
              className="shadow-xl hover:shadow-2xl hover:-translate-y-1"
              onClick={() => window.open('https://wa.me/33667596062', '_blank')}
            >
              HABLAR CON EL EQUIPO
            </Button>
          </div>
        </div>
      </section>

      {/* Location - Paris - Image + Texte avec background */}
      <section className="py-24" style={{backgroundColor: '#e8e4df'}}>
        <div className="container mx-auto max-w-7xl px-6">
          <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16 tracking-tight">
            El Jardín Secreto – París, Francia
          </h2>
          <div className="grid md:grid-cols-2 gap-0">
            {/* Image à gauche */}
            <div className="h-full min-h-[500px] rounded-l-3xl overflow-hidden shadow-elegant">
              <img 
                src="/jardin-piscine.png" 
                alt="El Jardín Secreto de París - Vue extérieure" 
                className="w-full h-full object-cover hover:scale-105 transition-transform duration-700"
              />
            </div>
            {/* Texte avec background à droite */}
            <div className="p-12" style={{backgroundColor: '#dde6d7'}}>
              <div className="space-y-6">
              <p className="text-lg leading-relaxed" style={{color: '#59614c'}}>
                En el corazón del histórico <strong>Barrio Latino de París</strong> se encuentra El Jardín Secreto, una joya escondida donde el silencio, la belleza y la historia se entrelazan.
              </p>
              <p className="text-lg leading-relaxed" style={{color: '#59614c'}}>
                Una casa del siglo XVIII completamente restaurada, rodeada de un jardín privado lleno de luz, calma y armonía. Este refugio ofrece una atmósfera íntima y serena, perfecta para desconectar del ruido exterior y reconectar contigo misma.
              </p>
              <p className="text-lg leading-relaxed" style={{color: '#59614c'}}>
                Cada rincón invita a la introspección: la calidez de la luz natural, los árboles centenarios, el sonido suave de las campanas… un entorno que abraza el alma y la mente.
              </p>
              <p className="text-lg leading-relaxed" style={{color: '#59614c'}}>
                Aquí viviremos el <strong>Retiro Renacer</strong>, un día diseñado para cerrar el año y abrir un nuevo ciclo con propósito y claridad. En este espacio exclusivo y lleno de energía, aprenderás a liberar lo viejo, reencontrarte contigo y activar tu poder interior.
              </p>
              <p className="text-lg leading-relaxed font-semibold" style={{color: '#59614c'}}>
                El Jardín Secreto no es solo el lugar del retiro, es parte de la experiencia: un escenario donde el alma se expande y la mente se transforma.
              </p>
            </div>
            </div>
          </div>
        </div>
      </section>

      {/* Retreat Space */}
      <section className="py-24" style={{backgroundColor: '#F9F6F3'}}>
        <div className="container mx-auto max-w-6xl px-6">
          <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16 tracking-tight">
            El espacio del retiro
          </h2>
          <div className="bg-white rounded-2xl shadow-xl p-8">
            <div className="grid md:grid-cols-2 gap-8 items-center">
              <div>
                <p className="text-gray-700 text-xl leading-relaxed mb-4">
                  Un espacio exclusivo con espacios luminosos y acogedores, rodeados de naturaleza y detalles parisinos
                </p>
                <p className="text-gray-700 text-lg leading-relaxed">
                  Un entorno privado y lleno de calma donde cada rincón invita a reconectar contigo
                </p>
              </div>
              <div className="space-y-4">
                <div className="w-full h-64 rounded-xl overflow-hidden shadow-lg hover:shadow-elegant transition-shadow">
                  <img 
                    src="/salon-cheminee.jpg" 
                    alt="Espace lumineux du Jardin Secret" 
                    className="w-full h-full object-cover hover:scale-105 transition-transform duration-500"
                  />
                </div>
                <div className="w-full h-64 rounded-xl overflow-hidden shadow-lg hover:shadow-elegant transition-shadow">
                  <img 
                    src="/salle-manger.jpg" 
                    alt="Salle à manger élégante du retiro" 
                    className="w-full h-full object-cover hover:scale-105 transition-transform duration-500"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Why We're Different */}
      <section className="py-24" style={{backgroundColor: '#f4f2ed'}}>
        <div className="container mx-auto max-w-7xl px-6">
          <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-20 tracking-tight">
            ¿Por qué el Retiro Renacer es diferente y único?
          </h2>
          
          <div className="grid lg:grid-cols-3 gap-8">
            {/* Colonne gauche - Points 1-3 */}
            <div className="space-y-6">
            {[
              {
                title: 'EXPERIENCIA DE LUJO',
                  description: 'Cada detalle ha sido cuidadosamente diseñado para ofrecerte una experiencia elegante, íntima y transformadora. Desde el entorno parisino hasta cada momento del programa, todo está pensado para que te sientas contenida, inspirada y en armonía. El verdadero lujo de Renacer está en vivir un proceso profundo en un espacio que refleja belleza, calma y propósito.'
                },
                {
                  title: 'TRANSFORMACIÓN CONSCIENTE',
                  description: 'A través de herramientas de coaching, psicología y espiritualidad práctica, aprenderás a identificar y transformar las creencias que te bloquean. En un solo día podrás liberar patrones que llevas años repitiendo y ganar claridad, confianza y dirección para avanzar hacia lo que realmente deseas.'
                },
                {
                  title: 'PODER DE LA EXCLUSIVIDAD',
                  description: 'Renacer es un retiro íntimo, con cupos limitados, pensado para mujeres que buscan un proceso profundo y personalizado. Cada experiencia está cuidadosamente guiada, lo que permite atención cercana, acompañamiento profesional y una conexión genuina contigo misma. Un espacio reducido para grandes transformaciones.'
                }
              ].map((item, index) => (
                <Card key={index} className="bg-white/80 backdrop-blur-sm border-2 border-sage-200 hover:border-sage-400 hover:shadow-sage transition-all duration-300">
                  <CardContent className="p-6">
                    <h3 className="text-xl font-bold text-sage-800 mb-3 uppercase">{item.title}</h3>
                    <p className="text-gray-700 leading-relaxed text-sm">{item.description}</p>
                  </CardContent>
                </Card>
              ))}
            </div>

            {/* Colonne centrale - Vidéos verticales */}
            <div className="flex flex-col gap-6 items-center">
              <div className="w-full max-w-xs rounded-3xl overflow-hidden shadow-2xl hover:shadow-sage transition-all duration-500 border-4 border-white">
                <video 
                  ref={videoRef2}
                  className="w-full h-auto"
                  autoPlay 
                  muted 
                  playsInline
                >
                  <source src="/video-retiro-2.mov" type="video/mp4" />
                </video>
              </div>
              <div className="w-full max-w-xs rounded-3xl overflow-hidden shadow-2xl hover:shadow-sage transition-all duration-500 border-4 border-white">
                <video 
                  ref={videoRef3}
                  className="w-full h-auto"
                  autoPlay 
                  muted 
                  playsInline
                >
                  <source src="/video-retiro-1.mov" type="video/mp4" />
                </video>
              </div>
            </div>

            {/* Colonne droite - Points 4-7 */}
            <div className="space-y-6">
              {[
                {
                  title: 'CONEXIÓN Y TRIBU',
                  description: 'En las dinámicas grupales experimentarás el poder del círculo femenino. Conocerás mujeres auténticas, valientes y sensibles que, como tú, están eligiendo cambiar su historia. De estos encuentros nacen amistades reales, redes de apoyo y vínculos que trascienden el retiro.'
                },
                {
                  title: 'ENTORNO QUE INSPIRA',
                  description: 'El retiro se realiza en El Jardín Secreto, un oasis oculto en el corazón de París. La armonía entre naturaleza, arte y silencio crea un ambiente ideal para pausar, respirar y reconectar con tu esencia. Cada rincón está impregnado de calma y propósito.'
                },
                {
                  title: 'ESPIRITUALIDAD APLICADA',
                  description: 'Renacer integra la espiritualidad desde lo cotidiano: mindfulness, meditación y prácticas de reconexión interior. Aprenderás a mantener esa conexión incluso después del retiro, viviendo con más conciencia, fe y coherencia emocional.'
                },
                {
                  title: 'ACOMPAÑAMIENTO PROFESIONAL',
                  description: 'Sin lugar a dudas, uno de los pilares fundamentales que hace que nuestro retiro sea excepcional es la calidad humana y el amor de nuestro equipo. Cada miembro está profundamente comprometido con tu bienestar y crecimiento personal.'
                }
              ].map((item, index) => (
                <Card key={index} className="bg-white/80 backdrop-blur-sm border-2 border-taupe-200 hover:border-taupe-400 hover:shadow-elegant transition-all duration-300">
                  <CardContent className="p-6">
                    <h3 className="text-xl font-bold text-taupe-800 mb-3 uppercase">{item.title}</h3>
                    <p className="text-gray-700 leading-relaxed text-sm">{item.description}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Founder Section */}
      <section className="py-24 relative overflow-hidden" style={{backgroundColor: '#F5F5F0'}}>
        <div className="absolute inset-0 bg-gradient-to-br from-taupe-100/40 to-sage-100/40" />
        <div className="container mx-auto max-w-6xl px-6 relative z-10">
          <div className="space-y-16">
            {/* Nicole Ramírez */}
          <div className="grid md:grid-cols-2 gap-16 items-center">
            <div className="relative group">
              <div className="absolute -inset-4 bg-gradient-sage rounded-3xl opacity-20 blur-2xl group-hover:opacity-30 transition-opacity" />
              <div className="relative w-full h-[500px] rounded-3xl shadow-elegant hover:shadow-sage transition-shadow overflow-hidden">
                <img 
                  src="/victoria-portrait.jpg" 
                    alt="Nicole Ramírez - Fundadora y Facilitadora" 
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                />
              </div>
            </div>
            <Card className="bg-white/95 backdrop-blur-sm shadow-elegant hover:shadow-sage border-2 border-sage-200 transition-all duration-300">
              <CardContent className="p-8">
                <div className="mb-6">
                  <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-3">
                    Hola, hermosa
                  </h2>
                  <h3 className="text-3xl md:text-4xl font-semibold bg-gradient-sage bg-clip-text text-transparent">
                    Soy Nicole Ramírez
                  </h3>
                  <p className="text-lg text-gray-600 mt-2">(Fundadora y Facilitadora)</p>
                </div>
                <div className="space-y-4 text-gray-700 leading-relaxed text-base">
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
                  <p className="font-semibold text-sage-800">
                    Cuando transformas tus pensamientos, transformas tu realidad.
                  </p>
                  <p className="font-semibold text-sage-800 bg-sage-50 p-4 rounded-lg border-l-4 border-sage-600">
                    En el retiro Renacer voy a compartir contigo las herramientas, experiencias y prácticas que me ayudaron a pasar de tener cero posibilidades en mi país, a crear una vida alineada a mis deseos, viviendo con plenitud, confianza y serenidad. Te acompañaré paso a paso para que tú también puedas cerrar un ciclo, liberar lo que pesa y construir desde adentro la vida que mereces vivir.
                  </p>
                </div>
              </CardContent>
            </Card>
            </div>

            {/* Dianix Bermúdez */}
            <div className="grid md:grid-cols-2 gap-16 items-center">
              <Card className="bg-white/95 backdrop-blur-sm shadow-elegant hover:shadow-sage border-2 border-sage-200 transition-all duration-300">
                <CardContent className="p-8">
                  <div className="mb-6">
                    <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-3">
                      Hola, soy Dianix Bermúdez
                    </h2>
                    <p className="text-lg text-gray-600">(Facilitadora)</p>
                  </div>
                  <div className="space-y-4 text-gray-700 leading-relaxed text-base">
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
                    <p className="font-semibold text-sage-800 bg-sage-50 p-4 rounded-lg border-l-4 border-sage-600">
                      En este retiro quiero acompañarte a recordar tu poder interior, reconectarte con tu energía más auténtica y abrir espacio para que la abundancia llegue a tu vida con facilidad y propósito.
                    </p>
                  </div>
                </CardContent>
              </Card>
              <div className="relative group">
                <div className="absolute -inset-4 bg-gradient-sage rounded-3xl opacity-20 blur-2xl group-hover:opacity-30 transition-opacity" />
                <div className="relative w-full h-[500px] rounded-3xl shadow-elegant hover:shadow-sage transition-shadow overflow-hidden">
                  <img 
                    src="/dianix-portrait.jpg" 
                    alt="Dianix Bermúdez - Facilitadora" 
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-24 relative overflow-hidden" style={{backgroundColor: '#FDFCFB'}}>
        <div className="absolute inset-0 bg-gradient-to-br from-lavender-50/30 via-transparent to-sage-50/30" />
        <div className="container mx-auto max-w-6xl px-6 relative z-10">
          <div className="text-center mb-20">
            <h2 className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-sage-700 to-taupe-600 bg-clip-text text-transparent mb-4 tracking-tight">
              Testimonios
            </h2>
            <p className="text-xl text-gray-600">Lo que ellas vivieron</p>
          </div>
          <div className="grid md:grid-cols-2 gap-8">
            {[
              {
                name: 'Karla',
                text: 'Ayer viví un mini retiro transformador. Entré sin expectativas, sin saber nada, ni de qué se trataban muchas herramientas, solo con la intención de conectar y abrirme a lo que viniera. Lo que encontré fue eso y mucho más: claridad, fuerza interior y un conocimiento profundo de mí misma que necesitaba en este momento de mi vida. Gracias infinitas al equipo, tan humanas y de gran corazón, por guiarnos en esta experiencia mágica.',
                color: 'from-sage-400 to-sage-600'
              },
              {
                name: 'Vanessa',
                text: 'Me traje tranquilidad. Varias de las actividades y las experiencias que compartieron otras mujeres me ayudaron a ver una luz en el camino. Hoy me siento más en paz y con esperanza.',
                color: 'from-lavender-400 to-lavender-600'
              },
              {
                name: 'Carolina',
                text: 'Sentí mucho valor y un profundo reencuentro conmigo. Me permití ser vulnerable, abrirme y compartir desde el corazón. Fue un día de liberación y conexión real.',
                color: 'from-taupe-400 to-taupe-600'
              },
              {
                name: 'Fabiana',
                text: 'Me encantó compartir y escuchar a otras compañeras con historias parecidas a la mía. La guía psicológica y espiritual durante todo el día fue increíble. Me voy con claridad, calma y motivación para seguir mi proceso.',
                color: 'from-rose-400 to-rose-600'
              },
              {
                name: 'Laura',
                text: 'Me gustó el ambiente y la energía. Hubo material valioso y dinámicas que realmente te hacen pensar y sanar. Me fui con más claridad y con herramientas prácticas para aplicar en mi vida.',
                color: 'from-sage-400 to-sage-600'
              },
              {
                name: 'Marcela',
                text: 'El retiro fue una experiencia profundamente sanadora. Llegué con muchas preguntas y me fui con claridad, serenidad y una nueva visión de mí misma.',
                color: 'from-lavender-400 to-lavender-600'
              },
              {
                name: 'Luz',
                text: 'Me sentí acompañada, vista y contenida. Fue un espacio lleno de amor donde pude reconectar con mi poder y mi fe en la vida. Me voy con el corazón liviano y la mente en calma.',
                color: 'from-taupe-400 to-taupe-600'
              }
            ].map((testimonial, index) => {
              const initials = testimonial.name.split(' ').map(n => n[0]).join('');
              
              return (
                <Card key={index} className="group bg-white hover:shadow-elegant hover:scale-102 transition-all duration-300 border-2 border-stone-200 hover:border-lavender-300 overflow-hidden">
                  <CardContent className="p-8">
                    <div className="flex items-center space-x-4 mb-6">
                      <div className={`w-16 h-16 rounded-full bg-gradient-to-br ${testimonial.color} shadow-lg flex items-center justify-center group-hover:scale-110 transition-transform duration-300`}>
                        <span className="text-white text-2xl font-bold">{initials}</span>
                      </div>
                      <h3 className="text-2xl font-bold text-gray-900">{testimonial.name}</h3>
                    </div>
                    <div className="relative">
                      <span className="absolute -top-2 -left-2 text-4xl text-lavender-300 opacity-50">"</span>
                      <p className="text-gray-700 italic leading-relaxed text-base pl-6">
                        {testimonial.text}
                      </p>
                      <span className="absolute -bottom-6 -right-2 text-4xl text-lavender-300 opacity-50">"</span>
                    </div>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section className="py-24" style={{backgroundColor: '#F5F5F0'}}>
        <div className="container mx-auto max-w-4xl px-6">
          <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-20 tracking-tight">
            Preguntas frecuentes
          </h2>
          <Accordion type="single" collapsible className="space-y-4">
            {[
              {
                question: '¿Puedo ir sola?',
                answer: '¡Claro que sí! De hecho, la mayoría de las mujeres que asisten vienen solas. Renacer está pensado para que desde el primer momento te sientas acompañada y segura. Vivir esta experiencia sin compañía te permite conectarte contigo misma y abrirte a nuevas amistades. No llegas sola… llegas a una tribu de mujeres auténticas que están transitando caminos similares al tuyo.'
              },
              {
                question: '¿Qué pasa después de hacer mi pago?',
                answer: 'Una vez que realices tu pago o reserva, recibirás un correo de confirmación automática con todos los detalles de como unirte a la comunidad. En las semanas previas al evento, te enviaremos información práctica (horarios, recomendaciones, qué llevar y cómo prepararte). Además, estarás invitada a un grupo privado de WhatsApp, donde compartiremos recordatorios, tips previos y podrás empezar a conectar con las demás participantes.'
              },
              {
                question: '¿El vuelo o transporte están incluidos?',
                answer: 'No. El valor del retiro no incluye el vuelo ni el transporte hasta el lugar. Sin embargo, te enviaremos una guía con las mejores rutas y opciones de transporte dentro de París, si lo necesitas, para que llegues fácilmente al Jardín Secreto, el espacio donde se realizará la experiencia. Si viajas desde otra ciudad o país, también podremos orientarte con recomendaciones de alojamiento cercano y con posibles descuentos.'
              },
              {
                question: '¿Qué pasa si nunca he ido a un retiro o vivido una experiencia parecida?',
                answer: 'No necesitas tener experiencia previa. Renacer fue creado para mujeres que simplemente sienten el llamado a un cambio y desean reconectarse con ellas mismas. Durante todo el proceso estarás acompañada por Nicole Ramírez y un equipo profesional, que te guiarán paso a paso para que te sientas cómoda, sostenida y comprendida. Solo necesitas abrirte a la experiencia y permitirte recibir.'
              },
              {
                question: '¿Si vivo en otro país, puedo asistir?',
                answer: 'Sí, por supuesto. Renacer es una experiencia internacional, han asistido chicas que estaban de viaje en Paris o viven en Europa. París es una ciudad muy accesible y el retiro se realiza en una ubicación céntrica, segura y fácil de llegar. Solo asegúrate de reservar con tiempo tu cupo, ya que los espacios son limitados y se agotan rápido.'
              }
            ].map((faq, index) => (
              <AccordionItem key={index} value={`item-${index}`} className="bg-white rounded-2xl shadow-lg border-2 overflow-hidden px-2">
                <AccordionTrigger className="px-6 py-6 text-xl font-bold text-gray-800 hover:no-underline hover:bg-stone-50">
                  {faq.question}
                </AccordionTrigger>
                <AccordionContent className="px-6 pb-6 text-gray-700 leading-relaxed text-lg">
                  {faq.answer}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-24 relative overflow-hidden bg-gradient-sage">
        <div className="absolute inset-0">
          <div className="absolute top-0 left-0 w-96 h-96 bg-white/10 rounded-full blur-3xl" />
          <div className="absolute bottom-0 right-0 w-96 h-96 bg-white/10 rounded-full blur-3xl" />
        </div>
        <div className="container mx-auto max-w-4xl px-6 text-center relative z-10">
          <div className="animate-fade-in">
            <div className="inline-block mb-8">
              <span className="text-7xl">💬</span>
            </div>
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-8 tracking-tight">
              ¿Tienes dudas?
            </h2>
            <div className="space-y-3 mb-10">
              <p className="text-2xl text-white/95">
                ¿No sabes si este retiro es para ti?
              </p>
              <p className="text-2xl text-white/95">
                ¿Nunca has asistido a una experiencia como esta?
              </p>
            </div>
            <Card className="inline-block bg-white/10 backdrop-blur-md border-2 border-white/30 mb-10">
              <CardContent className="p-6">
                <p className="text-white text-xl max-w-2xl leading-relaxed">
                  No te preocupes. Estamos aquí para acompañarte y resolver todas tus preguntas. Queremos que te sientas segura. Escríbeme y con gusto te ayudaremos a encontrar la mejor opción para ti.
                </p>
              </CardContent>
            </Card>
          </div>
          <Button 
            size="lg"
            variant="outline"
            className="bg-white text-sage-700 border-2 border-white hover:bg-sage-50 hover:text-sage-800 shadow-elegant hover:shadow-2xl hover:scale-105 transition-all duration-300 text-lg px-10 py-6 rounded-full font-bold"
            onClick={() => window.open('https://wa.me/33667596062', '_blank')}
          >
            HABLAR CON EL EQUIPO
          </Button>
        </div>
      </section>
    </div>
  );
};

export default LandingPage;

