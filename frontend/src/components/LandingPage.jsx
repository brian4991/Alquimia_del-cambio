import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const LandingPage = () => {
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

  const programs = [
    {
      title: "Programme Découverte",
      duration: "4 semaines",
      price: "97€",
      features: [
        "Introduction aux bases de l'alchimie du changement",
        "3 modules fondamentaux",
        "Exercices pratiques quotidiens",
        "Accès communauté Discord",
        "Support email"
      ],
      popular: false
    },
    {
      title: "Programme Transformation",
      duration: "12 semaines",
      price: "297€",
      features: [
        "Programme complet de transformation",
        "12 modules approfondis",
        "Sessions de coaching de groupe",
        "Suivi personnalisé",
        "Ressources audio et vidéo",
        "Certificat de completion",
        "Accès à vie"
      ],
      popular: true
    },
    {
      title: "Accompagnement Premium",
      duration: "6 mois",
      price: "897€",
      features: [
        "Coaching individuel personnalisé",
        "Tous les modules + contenu exclusif",
        "Sessions 1-on-1 mensuelles",
        "Plan d'action sur mesure",
        "Support prioritaire 24/7",
        "Accès VIP aux nouveautés",
        "Garantie résultats"
      ],
      popular: false
    }
  ];

  const testimonials = [
    {
      name: "Marie Dubois",
      role: "Entrepreneur",
      content: "Ce programme a complètement transformé ma façon de voir les défis. J'ai appris à utiliser chaque obstacle comme un tremplin vers la croissance.",
      rating: 5,
      image: "👩‍💼"
    },
    {
      name: "Thomas Martin",
      role: "Coach de vie",
      content: "L'approche de l'alchimie du changement est révolutionnaire. Mes clients ont des résultats exceptionnels depuis que j'applique ces méthodes.",
      rating: 5,
      image: "👨‍💼"
    },
    {
      name: "Sophie Laurent",
      role: "Manager",
      content: "En 3 mois, j'ai développé une résilience que je n'imaginais pas possible. Le contenu est riche et les exercices très pratiques.",
      rating: 5,
      image: "👩‍💻"
    }
  ];

  const faqs = [
    {
      question: "Qu'est-ce que l'Alchimie du Changement exactement ?",
      answer: "L'Alchimie du Changement est une méthode innovante qui transforme les défis en opportunités de croissance. Elle combine psychologie positive, neurosciences et techniques de développement personnel pour créer des transformations durables."
    },
    {
      question: "Combien de temps faut-il pour voir des résultats ?",
      answer: "La plupart de nos participants commencent à observer des changements dès les premières semaines. Les transformations profondes se manifestent généralement après 4-8 semaines de pratique régulière."
    },
    {
      question: "Le programme convient-il aux débutants ?",
      answer: "Absolument ! Nos programmes sont conçus pour tous les niveaux. Nous commençons par les bases et progressons graduellement vers des concepts plus avancés."
    },
    {
      question: "Y a-t-il une garantie de satisfaction ?",
      answer: "Oui, nous offrons une garantie de satisfaction de 30 jours. Si vous n'êtes pas entièrement satisfait, nous vous remboursons intégralement."
    },
    {
      question: "Comment fonctionne l'accès aux modules ?",
      answer: "Une fois inscrit, vous accédez à votre portail personnel où tous les modules sont organisés de manière progressive. Vous pouvez avancer à votre rythme tout en suivant la structure recommandée."
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-sage-50 via-white to-nature-50 relative overflow-x-hidden">
      {/* Decorative Plants - Left Side */}
      <div className="fixed left-0 top-0 h-full w-96 pointer-events-none z-10">
        {/* Large Ficus Leaf - Top */}
        <div 
          className="absolute top-16 -left-8 transform transition-all duration-1000 ease-out"
          style={{
            transform: `translateY(${scrollY * 0.08}px) translateX(${Math.min(scrollY * 0.06, 90)}px) rotateZ(${scrollY * 0.015}deg)`,
            opacity: Math.min(scrollY * 0.002, 0.85)
          }}
        >
          <img 
            src="/plant1.jpg" 
            alt="Ficus leaves"
            className="w-56 h-auto transform rotate-15 drop-shadow-2xl"
            style={{
              filter: 'contrast(1.1) saturate(1.25) brightness(1.08)'
            }}
          />
        </div>

        {/* Eucalyptus Branch - Middle */}
        <div 
          className="absolute top-80 left-2 transform transition-all duration-1000 ease-out"
          style={{
            transform: `translateY(${scrollY * 0.12}px) translateX(${Math.min(scrollY * 0.04, 70)}px) rotateZ(${-scrollY * 0.02}deg)`,
            opacity: Math.min(scrollY * 0.003, 0.9)
          }}
        >
          <img 
            src="/plant2.jpg" 
            alt="Eucalyptus branch"
            className="w-44 h-auto transform -rotate-25 drop-shadow-xl"
            style={{
              filter: 'contrast(1.15) saturate(1.2) brightness(1.05)'
            }}
          />
        </div>

        {/* Vertical Eucalyptus - Bottom */}
        <div 
          className="absolute bottom-32 left-8 transform transition-all duration-1000 ease-out"
          style={{
            transform: `translateY(${scrollY * -0.06}px) translateX(${Math.min(scrollY * 0.05, 60)}px) rotateZ(${scrollY * 0.018}deg)`,
            opacity: Math.min(scrollY * 0.004, 0.8)
          }}
        >
          <img 
            src="/plant5.jpg" 
            alt="Eucalyptus vertical"
            className="w-40 h-auto transform rotate-35 drop-shadow-lg"
            style={{
              filter: 'contrast(1.2) saturate(1.3) brightness(1.1)'
            }}
          />
        </div>
      </div>

      {/* Decorative Plants - Right Side */}
      <div className="fixed right-0 top-0 h-full w-96 pointer-events-none z-10">
        {/* Large Single Ficus Leaf - Top */}
        <div 
          className="absolute top-24 -right-12 transform transition-all duration-1000 ease-out"
          style={{
            transform: `translateY(${scrollY * 0.1}px) translateX(${Math.max(-scrollY * 0.05, -85)}px) rotateZ(${-scrollY * 0.02}deg)`,
            opacity: Math.min(scrollY * 0.0025, 0.9)
          }}
        >
          <img 
            src="/plant3.jpg" 
            alt="Large ficus leaf"
            className="w-64 h-auto transform -rotate-20 drop-shadow-2xl"
            style={{
              filter: 'contrast(1.12) saturate(1.3) brightness(1.06)'
            }}
          />
        </div>

        {/* Detailed Ficus Leaf - Middle */}
        <div 
          className="absolute top-96 -right-8 transform transition-all duration-1000 ease-out"
          style={{
            transform: `translateY(${scrollY * 0.14}px) translateX(${Math.max(-scrollY * 0.06, -75)}px) rotateZ(${scrollY * 0.025}deg)`,
            opacity: Math.min(scrollY * 0.003, 0.85)
          }}
        >
          <img 
            src="/plant4.jpg" 
            alt="Detailed ficus leaf"
            className="w-52 h-auto transform rotate-30 drop-shadow-xl"
            style={{
              filter: 'contrast(1.18) saturate(1.35) brightness(1.08)'
            }}
          />
        </div>

        {/* Small Eucalyptus Branch - Bottom */}
        <div 
          className="absolute bottom-28 -right-6 transform transition-all duration-1000 ease-out"
          style={{
            transform: `translateY(${scrollY * -0.08}px) translateX(${Math.max(-scrollY * 0.04, -65)}px) rotateZ(${-scrollY * 0.015}deg)`,
            opacity: Math.min(scrollY * 0.0035, 0.8)
          }}
        >
          <img 
            src="/plant2.jpg" 
            alt="Small eucalyptus"
            className="w-38 h-auto transform -rotate-15 drop-shadow-lg"
            style={{
              filter: 'contrast(1.1) saturate(1.25) brightness(1.12)'
            }}
          />
        </div>
      </div>

      {/* Floating Particles */}
      <div className="fixed inset-0 pointer-events-none z-5">
        {[...Array(6)].map((_, i) => (
          <div
            key={i}
            className="absolute w-2 h-2 bg-green-200 rounded-full opacity-30"
            style={{
              left: `${20 + i * 15}%`,
              top: `${30 + i * 10}%`,
              transform: `translateY(${scrollY * (0.02 + i * 0.01)}px) translateX(${Math.sin(scrollY * 0.001 + i) * 10}px)`,
              animation: `float ${3 + i}s ease-in-out infinite`
            }}
          />
        ))}
      </div>

      <style jsx>{`
        @keyframes float {
          0%, 100% { transform: translateY(0px); }
          50% { transform: translateY(-10px); }
        }
      `}</style>
      {/* Header */}
      <header className="bg-white/90 backdrop-blur-sm shadow-lg sticky top-0 z-50 relative">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-nature rounded-full flex items-center justify-center">
                <span className="text-white font-bold text-xl">🧪</span>
              </div>
              <h1 className="text-2xl font-bold text-sage-800">Alchimie du Changement</h1>
            </div>
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#program" className="text-sage-600 hover:text-sage-800 transition-colors">Programme</a>
              <a href="#pricing" className="text-sage-600 hover:text-sage-800 transition-colors">Tarifs</a>
              <a href="#testimonials" className="text-sage-600 hover:text-sage-800 transition-colors">Témoignages</a>
              <a href="#faq" className="text-sage-600 hover:text-sage-800 transition-colors">FAQ</a>
              <button
                onClick={() => navigate('/login')}
                className="bg-green-700 text-white px-6 py-2 rounded-full hover:bg-green-800 hover:shadow-lg transition-all duration-300 font-semibold"
              >
                Se connecter au portail
              </button>
            </nav>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative py-20 overflow-hidden">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-5xl md:text-6xl font-bold text-sage-800 mb-6">
              Transformez vos <span className="text-green-700 font-extrabold">défis</span> 
              <br />en opportunités
            </h1>
            <p className="text-xl text-sage-600 mb-8 max-w-3xl mx-auto">
              Découvrez l'art de l'Alchimie du Changement : une méthode révolutionnaire pour 
              transformer chaque obstacle en tremplin vers votre épanouissement personnel et professionnel.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button 
                onClick={() => navigate('/login')}
                className="bg-green-700 text-white px-8 py-4 rounded-full text-lg font-bold hover:bg-green-800 hover:shadow-xl transition-all duration-300"
              >
                Commencer maintenant
              </button>
              <button className="border-2 border-sage-300 text-sage-700 px-8 py-4 rounded-full text-lg font-semibold hover:bg-sage-50 transition-all duration-300">
                Découvrir le programme
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-white/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-sage-800 mb-4">Pourquoi l'Alchimie du Changement ?</h2>
            <p className="text-xl text-sage-600">Une approche unique basée sur la science et l'expérience</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center p-8 bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow">
              <div className="w-16 h-16 bg-green-700 rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg">
                <span className="text-2xl">🧠</span>
              </div>
              <h3 className="text-xl font-bold text-sage-800 mb-3">Approche Scientifique</h3>
              <p className="text-sage-600">Basée sur les dernières recherches en neurosciences et psychologie positive</p>
            </div>
            <div className="text-center p-8 bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow">
              <div className="w-16 h-16 bg-green-700 rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg">
                <span className="text-2xl">⚡</span>
              </div>
              <h3 className="text-xl font-bold text-sage-800 mb-3">Résultats Rapides</h3>
              <p className="text-sage-600">Des changements observables dès les premières semaines de pratique</p>
            </div>
            <div className="text-center p-8 bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow">
              <div className="w-16 h-16 bg-green-700 rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg">
                <span className="text-2xl">🌱</span>
              </div>
              <h3 className="text-xl font-bold text-sage-800 mb-3">Transformation Durable</h3>
              <p className="text-sage-600">Des outils pratiques pour une évolution continue et authentique</p>
            </div>
          </div>
        </div>
      </section>

      {/* Program Section */}
      <section id="program" className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-sage-800 mb-4">Notre Programme</h2>
            <p className="text-xl text-sage-600">Un parcours structuré en 4 phases de transformation</p>
          </div>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div className="text-center">
              <div className="w-20 h-20 bg-green-700 rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg">
                <span className="text-white font-bold text-2xl">1</span>
              </div>
              <h3 className="text-xl font-bold text-sage-800 mb-3">Prise de Conscience</h3>
              <p className="text-sage-600">Identifier vos patterns et blocages actuels</p>
            </div>
            <div className="text-center">
              <div className="w-20 h-20 bg-green-700 rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg">
                <span className="text-white font-bold text-2xl">2</span>
              </div>
              <h3 className="text-xl font-bold text-sage-800 mb-3">Déconstruction</h3>
              <p className="text-sage-600">Transformer les croyances limitantes</p>
            </div>
            <div className="text-center">
              <div className="w-20 h-20 bg-green-700 rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg">
                <span className="text-white font-bold text-2xl">3</span>
              </div>
              <h3 className="text-xl font-bold text-sage-800 mb-3">Reconstruction</h3>
              <p className="text-sage-600">Développer de nouveaux réflexes positifs</p>
            </div>
            <div className="text-center">
              <div className="w-20 h-20 bg-green-700 rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg">
                <span className="text-white font-bold text-2xl">4</span>
              </div>
              <h3 className="text-xl font-bold text-sage-800 mb-3">Intégration</h3>
              <p className="text-sage-600">Ancrer durablement vos nouvelles capacités</p>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section id="pricing" className="py-20 bg-white/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-sage-800 mb-4">Choisissez votre parcours</h2>
            <p className="text-xl text-sage-600">Des options adaptées à votre rythme et vos objectifs</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            {programs.map((program, index) => (
              <div key={index} className={`relative p-8 rounded-2xl shadow-lg hover:shadow-xl transition-shadow ${program.popular ? 'bg-gradient-nature text-white' : 'bg-white'}`}>
                {program.popular && (
                  <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 bg-yellow-400 text-sage-800 px-4 py-1 rounded-full text-sm font-bold">
                    Le plus populaire
                  </div>
                )}
                <div className="text-center mb-6">
                  <h3 className={`text-2xl font-bold mb-2 ${program.popular ? 'text-white' : 'text-sage-800'}`}>
                    {program.title}
                  </h3>
                  <p className={`text-sm mb-4 ${program.popular ? 'text-sage-100' : 'text-sage-600'}`}>
                    {program.duration}
                  </p>
                  <div className={`text-4xl font-bold ${program.popular ? 'text-white' : 'text-sage-800'}`}>
                    {program.price}
                  </div>
                </div>
                <ul className="space-y-3 mb-8">
                  {program.features.map((feature, fIndex) => (
                    <li key={fIndex} className={`flex items-center ${program.popular ? 'text-sage-100' : 'text-sage-600'}`}>
                      <span className={`mr-3 ${program.popular ? 'text-white' : 'text-green-500'}`}>✓</span>
                      {feature}
                    </li>
                  ))}
                </ul>
                <button 
                  onClick={() => navigate('/login')}
                  className={`w-full py-3 rounded-full font-semibold transition-all duration-300 ${
                    program.popular 
                      ? 'bg-white text-sage-800 hover:bg-sage-50' 
                      : 'bg-green-700 text-white hover:bg-green-800 hover:shadow-lg font-semibold'
                  }`}
                >
                  Commencer maintenant
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section id="testimonials" className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-sage-800 mb-4">Ce que disent nos participants</h2>
            <p className="text-xl text-sage-600">Des transformations authentiques et inspirantes</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <div key={index} className="bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition-shadow">
                <div className="flex items-center mb-4">
                  <div className="w-12 h-12 bg-green-700 rounded-full flex items-center justify-center mr-4 shadow-lg">
                    <span className="text-2xl">{testimonial.image}</span>
                  </div>
                  <div>
                    <h4 className="font-bold text-sage-800">{testimonial.name}</h4>
                    <p className="text-sage-600 text-sm">{testimonial.role}</p>
                  </div>
                </div>
                <div className="flex mb-4">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <span key={i} className="text-yellow-400 text-xl">★</span>
                  ))}
                </div>
                <p className="text-sage-700 italic">"{testimonial.content}"</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section id="faq" className="py-20 bg-white/50">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-sage-800 mb-4">Questions Fréquentes</h2>
            <p className="text-xl text-sage-600">Tout ce que vous devez savoir avant de commencer</p>
          </div>
          <div className="space-y-4">
            {faqs.map((faq, index) => (
              <div key={index} className="bg-white rounded-2xl shadow-lg overflow-hidden">
                <button
                  onClick={() => toggleFaq(index)}
                  className="w-full p-6 text-left flex justify-between items-center hover:bg-sage-50 transition-colors"
                >
                  <h3 className="font-bold text-sage-800">{faq.question}</h3>
                  <span className={`text-2xl transition-transform ${openFaq === index ? 'rotate-45' : ''}`}>
                    +
                  </span>
                </button>
                {openFaq === index && (
                  <div className="px-6 pb-6">
                    <p className="text-sage-600">{faq.answer}</p>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-nature text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-4xl font-bold mb-6">Prêt à transformer votre vie ?</h2>
          <p className="text-xl mb-8 opacity-90">
            Rejoignez des milliers de personnes qui ont déjà commencé leur transformation avec l'Alchimie du Changement.
          </p>
          <button 
            onClick={() => navigate('/login')}
            className="bg-white text-green-800 px-8 py-4 rounded-full text-lg font-bold hover:bg-green-50 transition-all duration-300 shadow-lg hover:shadow-xl"
          >
            Accéder au portail maintenant
          </button>
          <p className="text-sm mt-4 opacity-75">Garantie de satisfaction • Support 24/7 • Accès immédiat</p>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-sage-800 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-3 mb-4">
                <div className="w-8 h-8 bg-gradient-nature rounded-full flex items-center justify-center">
                  <span className="text-white font-bold">🧪</span>
                </div>
                <h3 className="text-xl font-bold">Alchimie du Changement</h3>
              </div>
              <p className="text-sage-300">Transformez vos défis en opportunités de croissance.</p>
            </div>
            <div>
              <h4 className="font-bold mb-4">Programme</h4>
              <ul className="space-y-2 text-sage-300">
                <li><a href="#" className="hover:text-white transition-colors">Modules</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Exercices</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Communauté</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold mb-4">Support</h4>
              <ul className="space-y-2 text-sage-300">
                <li><a href="#" className="hover:text-white transition-colors">FAQ</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Contact</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Aide</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold mb-4">Légal</h4>
              <ul className="space-y-2 text-sage-300">
                <li><a href="#" className="hover:text-white transition-colors">CGV</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Confidentialité</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Mentions légales</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-sage-700 mt-8 pt-8 text-center text-sage-300">
            <p>&copy; 2024 Alchimie du Changement. Tous droits réservés.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage; 