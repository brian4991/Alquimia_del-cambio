import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const PsychologyLanding = () => {
  const navigate = useNavigate();
  const [openFaq, setOpenFaq] = useState(null);
  const [scrollY, setScrollY] = useState(0);

  const toggleFaq = (index) => {
    setOpenFaq(openFaq === index ? null : index);
  };

  useEffect(() => {
    const handleScroll = () => setScrollY(window.scrollY);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const services = [
    {
      title: "Acompañamiento Individual",
      duration: "Sesiones 1h",
      price: "89€",
      features: [
        "Sesiones personalizadas",
        "Escucha activa y afectuosa", 
        "Técnicas de acompañamiento modernas",
        "Seguimiento entre sesiones",
        "Espacio confidencial y seguro"
      ],
      popular: false
    },
    {
      title: "Programa Transformación",
      duration: "3 meses",
      price: "350€",
      features: [
        "6 sesiones de acompañamiento",
        "Métodos de introspección guiada",
        "Herramientas de desarrollo personal",
        "Ejercicios prácticos diarios",
        "Soporte WhatsApp incluido",
        "Seguimiento personalizado completo"
      ],
      popular: true
    },
    {
      title: "Acompañamiento Premium", 
      duration: "6 meses",
      price: "650€",
      features: [
        "12 sesiones individuales",
        "Programa de transformación completa",
        "Acceso prioritario",
        "Técnicas avanzadas de crecimiento",
        "Soporte ilimitado",
        "Balance de progreso mensual"
      ],
      popular: false
    }
  ];

  const scientificFoundations = [
    { name: "Paul Ekman", field: "Emociones y microexpresiones", university: "UC San Francisco", book: "Emotions Revealed" },
    { name: "Brené Brown", field: "Vulnerabilidad y conexión", university: "University of Houston", book: "Daring Greatly" },
    { name: "Carl Rogers", field: "Psicología humanista", university: "University of Chicago", book: "On Becoming a Person" },
    { name: "John Bowlby", field: "Teoría del apego", university: "Tavistock Clinic", book: "Attachment and Loss" },
    { name: "Daniel Goleman", field: "Inteligencia emocional", university: "Harvard University", book: "Emotional Intelligence" },
    { name: "Kristin Neff", field: "Autocompasión", university: "University of Texas", book: "Self-Compassion" }
  ];

  const testimonials = [
    {
      name: "Emma L.",
      role: "Estudiante",
      content: "Gracias a su acompañamiento, recuperé la confianza en mí misma y la serenidad. Un enfoque humano y profesional excepcional.",
      rating: 5
    },
    {
      name: "Marc R.",
      role: "Ejecutivo",
      content: "Un recorrido transformador que me ayudó a gestionar mi estrés y recuperar el equilibrio. Lo recomiendo encarecidamente.",
      rating: 5
    },
    {
      name: "Sofia M.",
      role: "Emprendedora",
      content: "Una escucha extraordinaria y herramientas concretas. Me acompañó con mucha dulzura hacia mi transformación.",
      rating: 5
    }
  ];

  const faqs = [
    {
      question: "¿Cómo se desarrolla una primera sesión?",
      answer: "La primera sesión es un momento privilegiado de descubrimiento mutuo. Nos tomamos el tiempo para intercambiar sobre tus necesidades, expectativas y definimos juntos tus objetivos de acompañamiento."
    },
    {
      question: "¿Cuál es la duración recomendada de un acompañamiento?",
      answer: "Cada recorrido es único. Algunas personas sienten beneficios desde las primeras sesiones, otras prefieren un acompañamiento más largo para un cambio profundo."
    },
    {
      question: "¿Las sesiones se realizan presencialmente o a distancia?",
      answer: "Propongo ambas modalidades según tus preferencias y limitaciones. Las sesiones por videoconferencia son tan efectivas como las presenciales."
    },
    {
      question: "¿Cuál es tu enfoque terapéutico?",
      answer: "Mi enfoque es integrativo, combinando la escucha activa, la psicología positiva, y técnicas de desarrollo personal adaptadas a cada persona."
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-elegant relative overflow-x-hidden">
      
      {/* Enhanced floating elements with more variety */}
      <div className="fixed inset-0 pointer-events-none z-5">
        {/* Floating circles */}
        {[...Array(12)].map((_, i) => (
          <div
            key={i}
            className={`absolute rounded-full opacity-20 ${
              i % 3 === 0 ? 'bg-sage-300' : i % 3 === 1 ? 'bg-taupe-300' : 'bg-sage-200'
            }`}
            style={{
              width: `${8 + (i % 4) * 4}px`,
              height: `${8 + (i % 4) * 4}px`,
              left: `${10 + i * 8}%`,
              top: `${20 + i * 6}%`,
              transform: `translateY(${scrollY * (0.02 + i * 0.005)}px) translateX(${Math.sin(scrollY * 0.001 + i) * 20}px)`,
              animation: `gentle-float ${5 + i * 0.5}s ease-in-out infinite ${i * 0.2}s`
            }}
          />
        ))}
        
        {/* Decorative plant silhouettes */}
        <div 
          className="absolute top-20 left-10 opacity-10 text-6xl"
          style={{
            transform: `translateY(${scrollY * 0.1}px) rotate(${scrollY * 0.02}deg)`
          }}
        >
          🌿
        </div>
        <div 
          className="absolute top-60 right-20 opacity-8 text-5xl"
          style={{
            transform: `translateY(${scrollY * 0.08}px) rotate(${-scrollY * 0.015}deg)`
          }}
        >
          🍃
        </div>
        <div 
          className="absolute bottom-40 left-20 opacity-12 text-7xl"
          style={{
            transform: `translateY(${scrollY * -0.05}px) rotate(${scrollY * 0.01}deg)`
          }}
        >
          🌱
        </div>
        
        {/* Gradient orbs */}
        <div 
          className="absolute top-32 right-32 w-64 h-64 bg-gradient-to-br from-sage-200 to-transparent rounded-full opacity-30 blur-3xl"
          style={{
            transform: `translateY(${scrollY * 0.15}px) scale(${1 + scrollY * 0.0005})`
          }}
        />
        <div 
          className="absolute bottom-32 left-32 w-80 h-80 bg-gradient-to-tr from-taupe-200 to-transparent rounded-full opacity-20 blur-3xl"
          style={{
            transform: `translateY(${scrollY * -0.1}px) scale(${1 + scrollY * 0.0003})`
          }}
        />
      </div>

      <style jsx>{`
        @keyframes gentle-float {
          0%, 100% { transform: translateY(0px) rotate(0deg); }
          25% { transform: translateY(-8px) rotate(2deg); }
          50% { transform: translateY(-12px) rotate(0deg); }
          75% { transform: translateY(-8px) rotate(-2deg); }
        }
        
        @keyframes pulse-glow {
          0%, 100% { box-shadow: 0 0 20px rgba(107, 116, 90, 0.3); }
          50% { box-shadow: 0 0 40px rgba(107, 116, 90, 0.5); }
        }
        
        .animate-pulse-glow {
          animation: pulse-glow 3s ease-in-out infinite;
        }
      `}</style>

      {/* Header with glass effect */}
      <header className="bg-white/95 backdrop-blur-md shadow-elegant sticky top-0 z-50 relative border-b border-sage-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-sage rounded-full flex items-center justify-center shadow-sage animate-pulse-glow">
                <span className="text-white font-bold text-xl">✨</span>
              </div>
              <h1 className="text-2xl font-inter font-bold text-sage-800">Acompañamiento Psicológico</h1>
            </div>
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#about" className="text-sage-600 hover:text-sage-800 transition-colors font-medium">Acerca de</a>
              <a href="#services" className="text-sage-600 hover:text-sage-800 transition-colors font-medium">Servicios</a>
              <a href="#testimonials" className="text-sage-600 hover:text-sage-800 transition-colors font-medium">Testimonios</a>
              <a href="#contact" className="text-sage-600 hover:text-sage-800 transition-colors font-medium">Contacto</a>
              <button
                onClick={() => navigate('/login')}
                className="bg-gradient-sage text-white px-6 py-2 rounded-full hover:shadow-sage transition-all duration-300 font-medium transform hover:scale-105"
              >
                Espacio cliente
              </button>
            </nav>
          </div>
        </div>
      </header>

      {/* Hero Section with enhanced visual effects */}
      <section className="relative py-20 overflow-hidden">
        {/* Background gradient overlay */}
        <div className="absolute inset-0 bg-gradient-to-br from-sage-50/50 via-transparent to-taupe-50/30" />
        
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div className="text-left">
              <h1 className="text-5xl md:text-6xl font-inter font-light text-sage-800 mb-6 leading-tight">
                Encuentra tu 
                <span className="text-taupe-600 font-medium block relative">
                  equilibrio interior
                  <div className="absolute -bottom-2 left-0 w-24 h-1 bg-gradient-taupe rounded-full" />
                </span>
              </h1>
              <p className="text-xl text-sage-600 mb-8 leading-relaxed font-inter">
                Un acompañamiento psicológico afectuoso y personalizado para ayudarte a 
                superar tus dificultades y revelar tu pleno potencial.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <button 
                  onClick={() => navigate('/login')}
                  className="bg-gradient-sage text-white px-8 py-4 rounded-full text-lg font-medium hover:shadow-sage hover:scale-105 transition-all duration-300 transform"
                >
                  Reservar cita
                </button>
                <button className="border-2 border-sage-300 text-sage-700 px-8 py-4 rounded-full text-lg font-medium hover:bg-sage-50 hover:border-sage-400 transition-all duration-300 transform hover:scale-105">
                  Saber más
                </button>
              </div>
            </div>
            <div className="relative">
              <div className="relative z-10">
                <img 
                  src="/portrait5.jpg" 
                  alt="Psicóloga"
                  className="w-full h-auto rounded-3xl shadow-elegant border-4 border-white/50 transition-transform duration-100 ease-out"
                  style={{
                    filter: 'brightness(1.05) contrast(1.1) saturate(1.1)',
                    transform: `translateY(${Math.max(-30, Math.min(30, scrollY * 0.03))}px)`
                  }}
                />
                {/* Floating elements around the image */}
                <div 
                  className="absolute -top-8 -right-8 w-20 h-20 bg-gradient-sage rounded-full opacity-60 blur-sm"
                  style={{ animation: 'gentle-float 6s ease-in-out infinite 1s' }}
                />
                <div 
                  className="absolute -bottom-6 -left-6 w-16 h-16 bg-gradient-taupe rounded-full opacity-50 blur-sm"
                  style={{ animation: 'gentle-float 7s ease-in-out infinite 3s' }}
                />
              </div>
              {/* Enhanced decorative elements */}
              <div className="absolute -top-4 -right-4 w-72 h-72 bg-gradient-to-br from-sage-200/30 to-taupe-200/20 rounded-full opacity-60 -z-10 blur-2xl" />
              <div className="absolute -bottom-6 -left-6 w-48 h-48 bg-gradient-to-br from-taupe-200/40 to-sage-200/30 rounded-full opacity-50 -z-10 blur-xl" />
            </div>
          </div>
        </div>
      </section>

      {/* About Section with glass cards */}
      <section id="about" className="py-20 bg-white/60 backdrop-blur-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div className="relative">
              <div className="glass-effect-sage rounded-3xl p-2">
                <img 
                  src="/portrait3.jpg" 
                  alt="Acerca de"
                  className="w-full h-auto rounded-2xl shadow-elegant"
                  style={{
                    filter: 'brightness(1.08) contrast(1.05) saturate(1.15)'
                  }}
                />
              </div>
              {/* Floating accent */}
              <div 
                className="absolute top-8 -left-8 w-24 h-24 bg-gradient-to-br from-sage-300 to-taupe-300 rounded-full opacity-40 blur-lg"
                style={{ animation: 'gentle-float 6s ease-in-out infinite' }}
              />
            </div>
            <div>
              <h2 className="text-4xl font-inter font-light text-sage-800 mb-6">
                Un enfoque <span className="text-taupe-600 font-medium">humano</span> y afectuoso
              </h2>
              <p className="text-lg text-sage-600 mb-6 leading-relaxed font-inter">
                Psicóloga titulada, te acompaño con empatía y profesionalismo 
                en tu camino de desarrollo personal y bienestar.
              </p>
              <div className="space-y-4">
                <div className="flex items-center group">
                  <div className="w-3 h-3 bg-gradient-sage rounded-full mr-4 group-hover:scale-125 transition-transform duration-300" />
                  <span className="text-sage-700 font-inter">Escucha activa y sin juicio</span>
                </div>
                <div className="flex items-center group">
                  <div className="w-3 h-3 bg-gradient-taupe rounded-full mr-4 group-hover:scale-125 transition-transform duration-300" />
                  <span className="text-sage-700 font-inter">Métodos adaptados a cada persona</span>
                </div>
                <div className="flex items-center group">
                  <div className="w-3 h-3 bg-gradient-sage rounded-full mr-4 group-hover:scale-125 transition-transform duration-300" />
                  <span className="text-sage-700 font-inter">Acompañamiento respetuoso y confidencial</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Services Section with enhanced cards */}
      <section id="services" className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-inter font-light text-sage-800 mb-4">Mis servicios de acompañamiento</h2>
            <p className="text-xl text-sage-600 font-inter">Soluciones personalizadas para tu bienestar</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            {services.map((service, index) => (
              <div key={index} className={`relative p-8 rounded-3xl shadow-elegant hover:shadow-sage transition-all duration-500 transform hover:scale-105 hover:-translate-y-2 ${service.popular ? 'bg-gradient-sage text-white' : 'bg-white border border-sage-100'}`}>
                {service.popular && (
                  <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 bg-gradient-taupe text-white px-4 py-1 rounded-full text-sm font-medium shadow-taupe">
                    Más solicitado
                  </div>
                )}
                <div className="text-center mb-6">
                  <h3 className={`text-2xl font-inter font-medium mb-2 ${service.popular ? 'text-white' : 'text-sage-800'}`}>
                    {service.title}
                  </h3>
                  <p className={`text-sm mb-4 font-inter ${service.popular ? 'text-sage-100' : 'text-sage-600'}`}>
                    {service.duration}
                  </p>
                  <div className={`text-4xl font-inter font-light ${service.popular ? 'text-white' : 'text-sage-800'}`}>
                    {service.price}
                  </div>
                </div>
                <ul className="space-y-3 mb-8">
                  {service.features.map((feature, fIndex) => (
                    <li key={fIndex} className={`flex items-center font-inter ${service.popular ? 'text-sage-100' : 'text-sage-600'}`}>
                      <span className={`mr-3 ${service.popular ? 'text-white' : 'text-taupe-500'}`}>✓</span>
                      {feature}
                    </li>
                  ))}
                </ul>
                <button 
                  onClick={() => navigate('/login')}
                  className={`w-full py-3 rounded-full font-medium transition-all duration-300 transform hover:scale-105 ${
                    service.popular 
                      ? 'bg-white text-sage-700 hover:bg-sage-50 shadow-lg' 
                      : 'bg-gradient-sage text-white hover:shadow-sage'
                  }`}
                >
                  Reservar cita
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Program Overview - Subtle addition about the program */}
      <section className="py-20 bg-white/60 backdrop-blur-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-inter font-light text-sage-800 mb-4">
              Programa <span className="text-taupe-600 font-medium">"Alquimia del Cambio"</span>
            </h2>
            <p className="text-xl text-sage-600 font-inter max-w-3xl mx-auto">
              Un recorrido transformador de 4 etapas, basado en neurociencia y psicología positiva
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div className="text-center group">
              <div className="w-16 h-16 bg-gradient-sage rounded-2xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform duration-300">
                <span className="text-white text-2xl">🗺️</span>
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Gestión Emocional</h3>
              <p className="text-sage-600 font-inter">Herramientas para navegar tus emociones con serenidad y claridad</p>
            </div>
            
            <div className="text-center group">
              <div className="w-16 h-16 bg-gradient-taupe rounded-2xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform duration-300">
                <span className="text-white text-2xl">🎉</span>
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Amor Propio</h3>
              <p className="text-sage-600 font-inter">Cultiva una relación sana y compasiva contigo mismo/a</p>
            </div>
            
            <div className="text-center group">
              <div className="w-16 h-16 bg-gradient-sage rounded-2xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform duration-300">
                <span className="text-white text-2xl">💕</span>
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Relaciones Sanas</h3>
              <p className="text-sage-600 font-inter">Construye vínculos equilibrados y auténticos</p>
            </div>
            
            <div className="text-center group">
              <div className="w-16 h-16 bg-gradient-taupe rounded-2xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform duration-300">
                <span className="text-white text-2xl">⭐</span>
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Autenticidad</h3>
              <p className="text-sage-600 font-inter">Vive en coherencia con tus valores más profundos</p>
            </div>
          </div>
          
          <div className="text-center mt-12">
            <div className="glass-effect rounded-2xl p-6 max-w-2xl mx-auto border border-sage-100">
              <p className="text-sage-600 font-inter mb-4">
                <span className="text-taupe-600 font-medium">Metodología validada</span> por la psicología científica moderna
              </p>
              <div className="flex justify-center space-x-8 text-sm text-sage-500">
                <span>• Neuroplasticidad</span>
                <span>• Psicología Positiva</span>
                <span>• Mindfulness</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Scientific Foundations Section */}
      <section className="py-20 bg-gradient-to-br from-sage-50 to-taupe-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-inter font-light text-sage-800 mb-4">
              Fundamentos <span className="text-taupe-600 font-medium">científicos</span>
            </h2>
            <p className="text-xl text-sage-600 font-inter max-w-3xl mx-auto">
              Nuestro enfoque se basa en décadas de investigación de los psicólogos más reconocidos mundialmente
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
            {scientificFoundations.map((researcher, index) => (
              <div key={index} className="glass-effect rounded-3xl p-6 shadow-elegant hover:shadow-sage transition-all duration-500 transform hover:scale-105 hover:-translate-y-2 border border-sage-100 group">
                <div className="flex items-center gap-4 mb-4">
                  <div className="w-14 h-14 bg-gradient-sage rounded-2xl flex items-center justify-center font-inter font-bold text-white text-xl shadow-sage group-hover:scale-110 transition-transform duration-300">
                    {researcher.name.split(' ').map(n => n[0]).join('')}
                  </div>
                  <div>
                    <h3 className="font-inter font-medium text-sage-800 group-hover:text-sage-900">{researcher.name}</h3>
                    <p className="text-sm text-sage-500 font-inter">{researcher.university}</p>
                  </div>
                </div>
                <p className="text-sage-600 font-inter mb-3 leading-relaxed">{researcher.field}</p>
                <div className="inline-flex items-center bg-taupe-100 rounded-full px-3 py-1">
                  <span className="text-xs font-inter text-taupe-700">📚 {researcher.book}</span>
                </div>
              </div>
            ))}
          </div>

          <div className="glass-effect rounded-3xl p-8 shadow-elegant border border-sage-100 max-w-4xl mx-auto">
            <div className="flex items-center gap-4 mb-6">
              <div className="w-16 h-16 bg-gradient-taupe rounded-2xl flex items-center justify-center">
                <span className="text-white text-2xl">🧠</span>
              </div>
              <h3 className="text-2xl font-inter font-medium text-sage-800">Neuroplasticidad: Tu cerebro puede transformarse</h3>
            </div>
            <p className="text-lg text-sage-600 leading-relaxed font-inter">
              La neurociencia moderna demuestra que nuestro cerebro mantiene su capacidad de crear nuevas conexiones 
              hasta edades avanzadas. Los métodos de nuestro programa aprovechan esta <span className="text-taupe-600 font-medium">plasticidad cerebral</span> 
              para facilitar cambios duraderos en tus patrones emocionales, relacionales y de autoestima.
            </p>
          </div>
        </div>
      </section>

      <section className="py-20 bg-white/60 backdrop-blur-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-inter font-light text-sage-800 mb-4">Mi enfoque terapéutico</h2>
            <p className="text-xl text-sage-600 font-inter">Un acompañamiento adaptado a tus necesidades</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center group">
              <div className="relative mb-6">
                <div className="absolute inset-0 bg-gradient-sage rounded-full opacity-20 group-hover:opacity-30 transition-opacity duration-300 transform group-hover:scale-110" />
                <img 
                  src="/portrait1.jpg" 
                  alt="Escucha activa"
                  className="w-64 h-64 object-cover rounded-full mx-auto shadow-elegant border-4 border-white/80 relative z-10 group-hover:scale-105 transition-transform duration-500"
                  style={{
                    filter: 'brightness(1.05) contrast(1.08) saturate(1.1)'
                  }}
                />
                <div className="absolute -bottom-4 -right-4 w-12 h-12 bg-gradient-sage rounded-full opacity-80 group-hover:scale-125 transition-transform duration-300" />
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Escucha Activa</h3>
              <p className="text-sage-600 font-inter">Un espacio de expresión libre y afectuoso para expresar tus emociones</p>
            </div>
            <div className="text-center group">
              <div className="relative mb-6">
                <div className="absolute inset-0 bg-gradient-taupe rounded-full opacity-20 group-hover:opacity-30 transition-opacity duration-300 transform group-hover:scale-110" />
                <img 
                  src="/portrait2.jpg" 
                  alt="Acompañamiento personalizado"
                  className="w-64 h-64 object-cover rounded-full mx-auto shadow-elegant border-4 border-white/80 relative z-10 group-hover:scale-105 transition-transform duration-500"
                  style={{
                    filter: 'brightness(1.05) contrast(1.08) saturate(1.1)'
                  }}
                />
                <div className="absolute -bottom-4 -right-4 w-12 h-12 bg-gradient-taupe rounded-full opacity-80 group-hover:scale-125 transition-transform duration-300" />
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Enfoque Personalizado</h3>
              <p className="text-sage-600 font-inter">Métodos adaptados a tu personalidad y objetivos</p>
            </div>
            <div className="text-center group">
              <div className="relative mb-6">
                <div className="absolute inset-0 bg-gradient-sage rounded-full opacity-20 group-hover:opacity-30 transition-opacity duration-300 transform group-hover:scale-110" />
                <img 
                  src="/portrait4.jpg" 
                  alt="Transformación"
                  className="w-64 h-64 object-cover rounded-full mx-auto shadow-elegant border-4 border-white/80 relative z-10 group-hover:scale-105 transition-transform duration-500"
                  style={{
                    filter: 'brightness(1.05) contrast(1.08) saturate(1.1)'
                  }}
                />
                <div className="absolute -bottom-4 -right-4 w-12 h-12 bg-gradient-sage rounded-full opacity-80 group-hover:scale-125 transition-transform duration-300" />
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Transformación Duradera</h3>
              <p className="text-sage-600 font-inter">Un acompañamiento hacia un cambio positivo y duradero</p>
            </div>
          </div>
        </div>
      </section>

      {/* Program Section with Screenshots */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-inter font-light text-sage-800 mb-4">
              Descubre tu <span className="text-taupe-600 font-medium">plataforma personal</span>
            </h2>
            <p className="text-xl text-sage-600 font-inter max-w-3xl mx-auto">
              Un programa interactivo diseñado para acompañarte a tu ritmo en tu transformación personal
            </p>
          </div>

          {/* Program Benefits */}
          <div className="grid md:grid-cols-3 gap-8 mb-16">
            <div className="text-center group">
              <div className="w-16 h-16 bg-gradient-sage rounded-2xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform duration-300">
                <span className="text-white text-2xl">🎯</span>
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Recorrido Estructurado</h3>
              <p className="text-sage-600 font-inter">4 módulos progresivos para una transformación profunda</p>
            </div>
            <div className="text-center group">
              <div className="w-16 h-16 bg-gradient-taupe rounded-2xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform duration-300">
                <span className="text-white text-2xl">📝</span>
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Ejercicios Prácticos</h3>
              <p className="text-sage-600 font-inter">Herramientas concretas para anclar tus aprendizajes</p>
            </div>
            <div className="text-center group">
              <div className="w-16 h-16 bg-gradient-sage rounded-2xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform duration-300">
                <span className="text-white text-2xl">📊</span>
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Seguimiento Personalizado</h3>
              <p className="text-sage-600 font-inter">Visualiza tu progreso y celebra tus avances</p>
            </div>
          </div>

          {/* Screenshots Showcase */}
          <div className="space-y-16">
            
            {/* Dashboard Preview */}
            <div className="grid md:grid-cols-2 gap-12 items-center">
              <div className="relative group">
                <div className="absolute inset-0 bg-gradient-sage rounded-3xl opacity-20 group-hover:opacity-30 transition-opacity duration-300 transform rotate-3 group-hover:rotate-6" />
                <div className="relative bg-white rounded-3xl shadow-elegant overflow-hidden border border-sage-100 group-hover:shadow-sage transition-all duration-500 transform group-hover:scale-105">
                  <img 
                    src="/panel.png" 
                    alt="Panel de control"
                    className="w-full h-auto"
                  />
                </div>
              </div>
              <div>
                <h3 className="text-3xl font-inter font-light text-sage-800 mb-6">
                  Tu <span className="text-taupe-600 font-medium">panel de control</span> personal
                </h3>
                <p className="text-lg text-sage-600 mb-6 leading-relaxed font-inter">
                  Accede a tus módulos, sigue tu progreso y mantén una visión general de tu recorrido de transformación.
                </p>
                <div className="space-y-3">
                  <div className="flex items-center">
                    <div className="w-2 h-2 bg-gradient-sage rounded-full mr-3" />
                    <span className="text-sage-700 font-inter">Visión general de tu progreso</span>
                  </div>
                  <div className="flex items-center">
                    <div className="w-2 h-2 bg-gradient-taupe rounded-full mr-3" />
                    <span className="text-sage-700 font-inter">Acceso directo a todos tus módulos</span>
                  </div>
                  <div className="flex items-center">
                    <div className="w-2 h-2 bg-gradient-sage rounded-full mr-3" />
                    <span className="text-sage-700 font-inter">Interfaz intuitiva y tranquilizante</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Module Preview */}
            <div className="grid md:grid-cols-2 gap-12 items-center">
              <div className="order-2 md:order-1">
                <h3 className="text-3xl font-inter font-light text-sage-800 mb-6">
                  <span className="text-taupe-600 font-medium">Módulos interactivos</span> y atractivos
                </h3>
                <p className="text-lg text-sage-600 mb-6 leading-relaxed font-inter">
                  Cada módulo te guía paso a paso con contenido rico, ejercicios prácticos y seguimiento de tu evolución.
                </p>
                <div className="space-y-3">
                  <div className="flex items-center">
                    <div className="w-2 h-2 bg-gradient-taupe rounded-full mr-3" />
                    <span className="text-sage-700 font-inter">Contenido teórico y práctico equilibrado</span>
                  </div>
                  <div className="flex items-center">
                    <div className="w-2 h-2 bg-gradient-sage rounded-full mr-3" />
                    <span className="text-sage-700 font-inter">Progresión adaptada a tu ritmo</span>
                  </div>
                  <div className="flex items-center">
                    <div className="w-2 h-2 bg-gradient-taupe rounded-full mr-3" />
                    <span className="text-sage-700 font-inter">Recursos de audio y escritos</span>
                  </div>
                </div>
              </div>
              <div className="relative group order-1 md:order-2">
                <div className="absolute inset-0 bg-gradient-taupe rounded-3xl opacity-20 group-hover:opacity-30 transition-opacity duration-300 transform -rotate-3 group-hover:-rotate-6" />
                <div className="relative bg-white rounded-3xl shadow-elegant overflow-hidden border border-sage-100 group-hover:shadow-sage transition-all duration-500 transform group-hover:scale-105">
                  <img 
                    src="/module.png" 
                    alt="Módulo interactivo"
                    className="w-full h-auto"
                  />
                </div>
              </div>
            </div>

            {/* Exercises Preview */}
            <div className="grid md:grid-cols-2 gap-12 items-center">
              <div className="relative group">
                <div className="absolute inset-0 bg-gradient-sage rounded-3xl opacity-20 group-hover:opacity-30 transition-opacity duration-300 transform rotate-2 group-hover:rotate-4" />
                <div className="relative bg-white rounded-3xl shadow-elegant overflow-hidden border border-sage-100 group-hover:shadow-sage transition-all duration-500 transform group-hover:scale-105">
                  <img 
                    src="/exercices.png" 
                    alt="Ejercicios prácticos"
                    className="w-full h-auto"
                  />
                </div>
              </div>
              <div>
                <h3 className="text-3xl font-inter font-light text-sage-800 mb-6">
                  <span className="text-taupe-600 font-medium">Ejercicios prácticos</span> personalizados
                </h3>
                <p className="text-lg text-sage-600 mb-6 leading-relaxed font-inter">
                  Pon en práctica tus aprendizajes con ejercicios de reflexión personalizados que te ayudan a anclar tu transformación.
                </p>
                <div className="space-y-3">
                  <div className="flex items-center">
                    <div className="w-2 h-2 bg-gradient-sage rounded-full mr-3" />
                    <span className="text-sage-700 font-inter">Preguntas guiadas para la introspección</span>
                  </div>
                  <div className="flex items-center">
                    <div className="w-2 h-2 bg-gradient-taupe rounded-full mr-3" />
                    <span className="text-sage-700 font-inter">Espacio seguro para tus reflexiones</span>
                  </div>
                  <div className="flex items-center">
                    <div className="w-2 h-2 bg-gradient-sage rounded-full mr-3" />
                    <span className="text-sage-700 font-inter">Progreso seguido y alentado</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Call to Action */}
          <div className="text-center mt-16">
            <div className="glass-effect rounded-3xl p-8 shadow-elegant border border-sage-100 max-w-2xl mx-auto">
              <h3 className="text-2xl font-inter font-medium text-sage-800 mb-4">
                ¿Lista/o para descubrir tu plataforma?
              </h3>
              <p className="text-sage-600 font-inter mb-6">
                Comienza tu transformación hoy mismo con un acompañamiento personalizado y herramientas concretas.
              </p>
              <button 
                onClick={() => navigate('/login')}
                className="bg-gradient-sage text-white px-8 py-4 rounded-full text-lg font-medium hover:shadow-sage transition-all duration-300 transform hover:scale-105"
              >
                Acceder a la plataforma
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Section with enhanced cards */}
      <section id="testimonials" className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-inter font-light text-sage-800 mb-4">Testimonios</h2>
            <p className="text-xl text-sage-600 font-inter">La experiencia de quienes dieron el paso</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <div key={index} className="glass-effect rounded-3xl p-8 shadow-elegant hover:shadow-sage transition-all duration-500 transform hover:scale-105 hover:-translate-y-2 border border-sage-100">
                <div className="flex mb-4">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <span key={i} className="text-taupe-400 text-xl">★</span>
                  ))}
                </div>
                <p className="text-sage-700 italic mb-6 font-inter leading-relaxed">"{testimonial.content}"</p>
                <div>
                  <h4 className="font-inter font-medium text-sage-800">{testimonial.name}</h4>
                  <p className="text-sage-600 text-sm font-inter">{testimonial.role}</p>
                </div>
                {/* Decorative element */}
                <div className="w-12 h-1 bg-gradient-taupe rounded-full mt-4" />
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ Section with enhanced interactions */}
      <section id="faq" className="py-20 bg-white/60 backdrop-blur-sm">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-inter font-light text-sage-800 mb-4">Preguntas frecuentes</h2>
            <p className="text-xl text-sage-600 font-inter">Las respuestas a tus dudas</p>
          </div>
          <div className="space-y-4">
            {faqs.map((faq, index) => (
              <div key={index} className="glass-effect rounded-3xl shadow-elegant overflow-hidden border border-sage-100 hover:shadow-sage transition-all duration-300">
                <button
                  onClick={() => toggleFaq(index)}
                  className="w-full p-6 text-left flex justify-between items-center hover:bg-sage-50/50 transition-colors group"
                >
                  <h3 className="font-inter font-medium text-sage-800 group-hover:text-sage-900">{faq.question}</h3>
                  <span className={`text-2xl text-taupe-500 transition-all duration-300 group-hover:text-taupe-600 ${openFaq === index ? 'rotate-45 scale-110' : 'hover:scale-110'}`}>
                    +
                  </span>
                </button>
                {openFaq === index && (
                  <div className="px-6 pb-6 transform transition-all duration-500 ease-out">
                    <div className="w-full h-0.5 bg-gradient-taupe rounded-full mb-4 opacity-50" />
                    <p className="text-sage-600 leading-relaxed font-inter">{faq.answer}</p>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section with enhanced gradients */}
      <section className="py-20 bg-gradient-sage text-white relative overflow-hidden">
        {/* Animated background elements */}
        <div className="absolute inset-0">
          <div 
            className="absolute top-10 left-10 w-32 h-32 bg-white/10 rounded-full blur-2xl"
            style={{ animation: 'gentle-float 8s ease-in-out infinite' }}
          />
          <div 
            className="absolute bottom-10 right-10 w-40 h-40 bg-taupe-300/20 rounded-full blur-3xl"
            style={{ animation: 'gentle-float 10s ease-in-out infinite 2s' }}
          />
        </div>
        
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
          <h2 className="text-4xl font-inter font-light mb-6">¿Lista/o para comenzar tu transformación?</h2>
          <p className="text-xl mb-8 opacity-90 font-inter">
            Te acompaño con cariño hacia un bienestar duradero.
          </p>
          <button 
            onClick={() => navigate('/login')}
            className="bg-white text-sage-700 px-8 py-4 rounded-full text-lg font-medium hover:bg-sage-50 transition-all duration-300 shadow-elegant hover:shadow-taupe transform hover:scale-105"
          >
            Reservar cita ahora
          </button>
          <p className="text-sm mt-4 opacity-75 font-inter">Primera consulta gratuita • Confidencialidad garantizada</p>
        </div>
      </section>

      {/* Footer with sage colors */}
      <footer className="bg-sage-800 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-3 mb-4">
                <div className="w-8 h-8 bg-gradient-taupe rounded-full flex items-center justify-center shadow-taupe">
                  <span className="text-white font-bold">✨</span>
                </div>
                <h3 className="text-xl font-inter font-medium">Acompañamiento Psicológico</h3>
              </div>
              <p className="text-sage-300 font-inter">Para un bienestar auténtico y duradero.</p>
            </div>
            <div>
              <h4 className="font-inter font-medium mb-4">Servicios</h4>
              <ul className="space-y-2 text-sage-300 font-inter">
                <li><a href="#" className="hover:text-white transition-colors">Sesiones individuales</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Programas de acompañamiento</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Seguimiento personalizado</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-inter font-medium mb-4">Contacto</h4>
              <ul className="space-y-2 text-sage-300 font-inter">
                <li><a href="#" className="hover:text-white transition-colors">Reservar cita</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Email</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Teléfono</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-inter font-medium mb-4">Información</h4>
              <ul className="space-y-2 text-sage-300 font-inter">
                <li><a href="#" className="hover:text-white transition-colors">Términos legales</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Privacidad</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Deontología</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-sage-700 mt-8 pt-8 text-center text-sage-300">
            <p className="font-inter">&copy; 2024 Acompañamiento Psicológico. Todos los derechos reservados.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default PsychologyLanding; 