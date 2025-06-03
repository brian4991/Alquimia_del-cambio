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
      title: "Accompagnement Individuel",
      duration: "Sessions 1h",
      price: "89€",
      features: [
        "Séances personnalisées",
        "Écoute active et bienveillante", 
        "Techniques d'accompagnement modernes",
        "Suivi entre les séances",
        "Espace confidentiel et sécurisé"
      ],
      popular: false
    },
    {
      title: "Programme Transformation",
      duration: "3 mois",
      price: "350€",
      features: [
        "6 séances d'accompagnement",
        "Méthodes d'introspection guidée",
        "Outils de développement personnel",
        "Exercices pratiques quotidiens",
        "Support WhatsApp inclus",
        "Suivi personnalisé complet"
      ],
      popular: true
    },
    {
      title: "Accompagnement Premium", 
      duration: "6 mois",
      price: "650€",
      features: [
        "12 séances individuelles",
        "Programme de transformation complète",
        "Accès prioritaire",
        "Techniques avancées d'épanouissement",
        "Support illimité",
        "Bilan de progression mensuel"
      ],
      popular: false
    }
  ];

  const testimonials = [
    {
      name: "Emma L.",
      role: "Étudiante",
      content: "Grâce à son accompagnement, j'ai retrouvé confiance en moi et la sérénité. Une approche humaine et professionnelle exceptionnelle.",
      rating: 5
    },
    {
      name: "Marc R.",
      role: "Cadre",
      content: "Un parcours transformateur qui m'a aidé à gérer mon stress et à retrouver l'équilibre. Je recommande vivement.",
      rating: 5
    },
    {
      name: "Sofia M.",
      role: "Entrepreneur",
      content: "Une écoute extraordinaire et des outils concrets. Elle m'a accompagnée avec beaucoup de douceur vers ma transformation.",
      rating: 5
    }
  ];

  const faqs = [
    {
      question: "Comment se déroule une première séance ?",
      answer: "La première séance est un moment privilégié de découverte mutuelle. Nous prenons le temps d'échanger sur vos besoins, vos attentes et nous définissons ensemble vos objectifs d'accompagnement."
    },
    {
      question: "Quelle est la durée recommandée d'un accompagnement ?",
      answer: "Chaque parcours est unique. Certaines personnes ressentent des bienfaits dès les premières séances, d'autres préfèrent un accompagnement plus long pour un changement en profondeur."
    },
    {
      question: "Les séances se déroulent-elles en présentiel ou à distance ?",
      answer: "Je propose les deux modalités selon vos préférences et contraintes. Les séances en visioconférence sont tout aussi efficaces que celles en présentiel."
    },
    {
      question: "Quel est votre approche thérapeutique ?",
      answer: "Mon approche est intégrative, combinant l'écoute active, la psychologie positive, et des techniques de développement personnel adaptées à chaque personne."
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
              <h1 className="text-2xl font-inter font-bold text-sage-800">Accompagnement Psychologique</h1>
            </div>
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#about" className="text-sage-600 hover:text-sage-800 transition-colors font-medium">À propos</a>
              <a href="#services" className="text-sage-600 hover:text-sage-800 transition-colors font-medium">Services</a>
              <a href="#testimonials" className="text-sage-600 hover:text-sage-800 transition-colors font-medium">Témoignages</a>
              <a href="#contact" className="text-sage-600 hover:text-sage-800 transition-colors font-medium">Contact</a>
              <button
                onClick={() => navigate('/login')}
                className="bg-gradient-sage text-white px-6 py-2 rounded-full hover:shadow-sage transition-all duration-300 font-medium transform hover:scale-105"
              >
                Espace client
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
                Retrouvez votre 
                <span className="text-taupe-600 font-medium block relative">
                  équilibre intérieur
                  <div className="absolute -bottom-2 left-0 w-24 h-1 bg-gradient-taupe rounded-full" />
                </span>
              </h1>
              <p className="text-xl text-sage-600 mb-8 leading-relaxed font-inter">
                Un accompagnement psychologique bienveillant et personnalisé pour vous aider à 
                surmonter vos difficultés et révéler votre plein potentiel.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <button 
                  onClick={() => navigate('/login')}
                  className="bg-gradient-sage text-white px-8 py-4 rounded-full text-lg font-medium hover:shadow-sage hover:scale-105 transition-all duration-300 transform"
                >
                  Prendre rendez-vous
                </button>
                <button className="border-2 border-sage-300 text-sage-700 px-8 py-4 rounded-full text-lg font-medium hover:bg-sage-50 hover:border-sage-400 transition-all duration-300 transform hover:scale-105">
                  En savoir plus
                </button>
              </div>
            </div>
            <div className="relative">
              <div className="relative z-10">
                <img 
                  src="/portrait5.jpg" 
                  alt="Psychologue"
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
                  alt="À propos"
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
                Une approche <span className="text-taupe-600 font-medium">humaine</span> et bienveillante
              </h2>
              <p className="text-lg text-sage-600 mb-6 leading-relaxed font-inter">
                Psychologue diplômée, je vous accompagne avec empathie et professionnalisme 
                dans votre parcours de développement personnel et de mieux-être.
              </p>
              <div className="space-y-4">
                <div className="flex items-center group">
                  <div className="w-3 h-3 bg-gradient-sage rounded-full mr-4 group-hover:scale-125 transition-transform duration-300" />
                  <span className="text-sage-700 font-inter">Écoute active et sans jugement</span>
                </div>
                <div className="flex items-center group">
                  <div className="w-3 h-3 bg-gradient-taupe rounded-full mr-4 group-hover:scale-125 transition-transform duration-300" />
                  <span className="text-sage-700 font-inter">Méthodes adaptées à chaque personne</span>
                </div>
                <div className="flex items-center group">
                  <div className="w-3 h-3 bg-gradient-sage rounded-full mr-4 group-hover:scale-125 transition-transform duration-300" />
                  <span className="text-sage-700 font-inter">Accompagnement respectueux et confidentiel</span>
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
            <h2 className="text-4xl font-inter font-light text-sage-800 mb-4">Mes services d'accompagnement</h2>
            <p className="text-xl text-sage-600 font-inter">Des solutions personnalisées pour votre bien-être</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            {services.map((service, index) => (
              <div key={index} className={`relative p-8 rounded-3xl shadow-elegant hover:shadow-sage transition-all duration-500 transform hover:scale-105 hover:-translate-y-2 ${service.popular ? 'bg-gradient-sage text-white' : 'bg-white border border-sage-100'}`}>
                {service.popular && (
                  <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 bg-gradient-taupe text-white px-4 py-1 rounded-full text-sm font-medium shadow-taupe">
                    Le plus demandé
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
                  Prendre rendez-vous
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Approach Section with circular images and animations */}
      <section className="py-20 bg-white/60 backdrop-blur-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-inter font-light text-sage-800 mb-4">Mon approche thérapeutique</h2>
            <p className="text-xl text-sage-600 font-inter">Un accompagnement adapté à vos besoins</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center group">
              <div className="relative mb-6">
                <div className="absolute inset-0 bg-gradient-sage rounded-full opacity-20 group-hover:opacity-30 transition-opacity duration-300 transform group-hover:scale-110" />
                <img 
                  src="/portrait1.jpg" 
                  alt="Écoute active"
                  className="w-64 h-64 object-cover rounded-full mx-auto shadow-elegant border-4 border-white/80 relative z-10 group-hover:scale-105 transition-transform duration-500"
                  style={{
                    filter: 'brightness(1.05) contrast(1.08) saturate(1.1)'
                  }}
                />
                <div className="absolute -bottom-4 -right-4 w-12 h-12 bg-gradient-sage rounded-full opacity-80 group-hover:scale-125 transition-transform duration-300" />
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Écoute Active</h3>
              <p className="text-sage-600 font-inter">Un espace de parole libre et bienveillant pour exprimer vos émotions</p>
            </div>
            <div className="text-center group">
              <div className="relative mb-6">
                <div className="absolute inset-0 bg-gradient-taupe rounded-full opacity-20 group-hover:opacity-30 transition-opacity duration-300 transform group-hover:scale-110" />
                <img 
                  src="/portrait2.jpg" 
                  alt="Accompagnement personnalisé"
                  className="w-64 h-64 object-cover rounded-full mx-auto shadow-elegant border-4 border-white/80 relative z-10 group-hover:scale-105 transition-transform duration-500"
                  style={{
                    filter: 'brightness(1.05) contrast(1.08) saturate(1.1)'
                  }}
                />
                <div className="absolute -bottom-4 -right-4 w-12 h-12 bg-gradient-taupe rounded-full opacity-80 group-hover:scale-125 transition-transform duration-300" />
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Approche Personnalisée</h3>
              <p className="text-sage-600 font-inter">Des méthodes adaptées à votre personnalité et vos objectifs</p>
            </div>
            <div className="text-center group">
              <div className="relative mb-6">
                <div className="absolute inset-0 bg-gradient-sage rounded-full opacity-20 group-hover:opacity-30 transition-opacity duration-300 transform group-hover:scale-110" />
                <img 
                  src="/portrait4.jpg" 
                  alt="Transformation"
                  className="w-64 h-64 object-cover rounded-full mx-auto shadow-elegant border-4 border-white/80 relative z-10 group-hover:scale-105 transition-transform duration-500"
                  style={{
                    filter: 'brightness(1.05) contrast(1.08) saturate(1.1)'
                  }}
                />
                <div className="absolute -bottom-4 -right-4 w-12 h-12 bg-gradient-sage rounded-full opacity-80 group-hover:scale-125 transition-transform duration-300" />
              </div>
              <h3 className="text-xl font-inter font-medium text-sage-800 mb-3">Transformation Durable</h3>
              <p className="text-sage-600 font-inter">Un accompagnement vers un changement positif et durable</p>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Section with enhanced cards */}
      <section id="testimonials" className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-inter font-light text-sage-800 mb-4">Témoignages</h2>
            <p className="text-xl text-sage-600 font-inter">L'expérience de ceux qui ont franchi le pas</p>
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
            <h2 className="text-4xl font-inter font-light text-sage-800 mb-4">Questions fréquentes</h2>
            <p className="text-xl text-sage-600 font-inter">Les réponses à vos interrogations</p>
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
          <h2 className="text-4xl font-inter font-light mb-6">Prêt(e) à commencer votre transformation ?</h2>
          <p className="text-xl mb-8 opacity-90 font-inter">
            Je vous accompagne avec bienveillance vers un mieux-être durable.
          </p>
          <button 
            onClick={() => navigate('/login')}
            className="bg-white text-sage-700 px-8 py-4 rounded-full text-lg font-medium hover:bg-sage-50 transition-all duration-300 shadow-elegant hover:shadow-taupe transform hover:scale-105"
          >
            Prendre rendez-vous maintenant
          </button>
          <p className="text-sm mt-4 opacity-75 font-inter">Premier échange gratuit • Confidentialité garantie</p>
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
                <h3 className="text-xl font-inter font-medium">Accompagnement Psychologique</h3>
              </div>
              <p className="text-sage-300 font-inter">Pour un mieux-être authentique et durable.</p>
            </div>
            <div>
              <h4 className="font-inter font-medium mb-4">Services</h4>
              <ul className="space-y-2 text-sage-300 font-inter">
                <li><a href="#" className="hover:text-white transition-colors">Séances individuelles</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Programmes d'accompagnement</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Suivi personnalisé</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-inter font-medium mb-4">Contact</h4>
              <ul className="space-y-2 text-sage-300 font-inter">
                <li><a href="#" className="hover:text-white transition-colors">Prendre RDV</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Email</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Téléphone</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-inter font-medium mb-4">Informations</h4>
              <ul className="space-y-2 text-sage-300 font-inter">
                <li><a href="#" className="hover:text-white transition-colors">Mentions légales</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Confidentialité</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Déontologie</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-sage-700 mt-8 pt-8 text-center text-sage-300">
            <p className="font-inter">&copy; 2024 Accompagnement Psychologique. Tous droits réservés.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default PsychologyLanding; 