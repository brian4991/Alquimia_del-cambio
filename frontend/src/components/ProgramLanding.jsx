import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import EditableSection from './EditableSection';
import { config } from '../config';

const ProgramLanding = () => {
  const navigate = useNavigate();
  const [pageContent, setPageContent] = useState({});
  const [loading, setLoading] = useState(true);

  // Load page content
  useEffect(() => {
    loadPageContent();
  }, []);

  const loadPageContent = async () => {
    try {
      const response = await fetch(`${config.apiUrl}/api/page-content/program`);
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
      const response = await fetch(`${config.apiUrl}/api/page-content/program`, {
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
              <p className="text-xs text-taupe-600">Programa de Transformación Personal</p>
            </div>
          </div>
          <button
            onClick={() => navigate('/login')}
            style={{borderColor: '#6b745a', color: '#6b745a'}}
            className="bg-transparent border-2 px-6 py-2 rounded-full hover:text-white transition-all font-semibold"
            onMouseEnter={(e) => e.target.style.backgroundColor = '#6b745a'}
            onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}
          >
            Acceder al Portal
          </button>
        </div>
      </header>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-6 bg-white">
        <div className="container mx-auto max-w-6xl text-center">
          <div className="w-32 h-32 bg-gray-200 rounded-full mx-auto mb-8 flex items-center justify-center text-xs text-gray-600">
            [LOGO-PROGRAMA]
          </div>
          <EditableSection
            sectionKey="hero_title"
            content={pageContent.hero_title}
            onSave={saveSection}
          >
            <h1 className="text-4xl md:text-6xl font-bold text-gray-800 mb-8 leading-tight">
              Transforma tu vida con Cambio de Paradigma
            </h1>
          </EditableSection>
          <EditableSection
            sectionKey="hero_subtitle"
            content={pageContent.hero_subtitle}
            onSave={saveSection}
          >
            <p className="text-xl md:text-2xl text-gray-600 mb-10">
              Un programa completo de 5 módulos para tu desarrollo personal y bienestar emocional
            </p>
          </EditableSection>
          <button 
            onClick={() => navigate('/login')}
            style={{backgroundColor: '#6b745a'}}
            className="text-white px-12 py-4 rounded-full text-lg font-semibold hover:opacity-90 transition-all shadow-lg hover:shadow-xl transform hover:scale-105"
          >
            COMENZAR MI TRANSFORMACIÓN
          </button>
        </div>
      </section>

      {/* Program Overview */}
      <section className="py-20" style={{backgroundColor: '#F5F5F0'}}>
        <div className="container mx-auto max-w-6xl px-6">
          <EditableSection
            sectionKey="overview_title"
            content={pageContent.overview_title}
            onSave={saveSection}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16">
              ¿QUÉ ES ALQUIMIA DEL CAMBIO?
            </h2>
          </EditableSection>
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <div className="w-full h-96 bg-gray-200 rounded-2xl flex items-center justify-center text-gray-600">
                [IMG-PROGRAMA-001: Mujer en transformación personal]
              </div>
            </div>
            <EditableSection
              sectionKey="overview_description"
              content={pageContent.overview_description}
              onSave={saveSection}
            >
              <div className="space-y-6">
                <p className="text-lg text-gray-700 leading-relaxed">
                  Cambio de Paradigma es un programa de transformación personal diseñado para guiarte en un viaje profundo de autoconocimiento, sanación emocional y desarrollo personal.
                </p>
                <p className="text-lg text-gray-700 leading-relaxed">
                  A través de 5 módulos cuidadosamente estructurados, te acompañaremos paso a paso en tu proceso de crecimiento personal, ayudándote a fortalecer tu autoestima, sanar heridas del pasado y construir la vida que mereces.
                </p>
                <p className="text-lg text-gray-700 leading-relaxed">
                  Cada módulo incluye contenido teórico, ejercicios prácticos de reflexión y herramientas aplicables a tu vida diaria.
                </p>
              </div>
            </EditableSection>
          </div>
        </div>
      </section>

      {/* 5 Modules */}
      <section className="py-20 bg-white">
        <div className="container mx-auto max-w-6xl px-6">
          <EditableSection
            sectionKey="modules_title"
            content={pageContent.modules_title}
            onSave={saveSection}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16">
              LOS 5 MÓDULOS DEL PROGRAMA
            </h2>
          </EditableSection>
          <div className="space-y-8">
            {[
              {
                number: 1,
                title: 'El Mapa de tus Emociones',
                description: 'Aprende a identificar, comprender y gestionar tus emociones de manera saludable.',
                color: '#8B9D83'
              },
              {
                number: 2,
                title: 'Celebra tu Ser',
                description: 'Reconecta con tu valor único, acepta tu imperfección y fortalece tu autoestima.',
                color: '#A8957D'
              },
              {
                number: 3,
                title: 'El Arte de Amar',
                description: 'Descubre cómo construir relaciones saludables basadas en el respeto y la comunicación.',
                color: '#B8A69E'
              },
              {
                number: 4,
                title: 'De la Expectativa a la Realidad',
                description: 'Libérate de expectativas limitantes y conecta con tu esencia auténtica.',
                color: '#9CAF88'
              },
              {
                number: 5,
                title: 'Libertad en Acción',
                description: 'Define tus objetivos, supera creencias limitantes y actúa hacia tu mejor versión.',
                color: '#D4C5B0'
              }
            ].map((module, index) => (
              <div 
                key={index}
                className="bg-white rounded-2xl shadow-lg hover:shadow-xl transition-all p-8 border-l-8"
                style={{borderColor: module.color}}
              >
                <div className="flex items-start space-x-6">
                  <div 
                    className="flex-shrink-0 w-16 h-16 rounded-full flex items-center justify-center text-white text-2xl font-bold shadow-lg"
                    style={{backgroundColor: module.color}}
                  >
                    {module.number}
                  </div>
                  <div className="flex-1">
                    <h3 className="text-2xl font-bold text-gray-800 mb-3">
                      {module.title}
                    </h3>
                    <p className="text-gray-700 text-lg leading-relaxed">
                      {module.description}
                    </p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Benefits */}
      <section className="py-20" style={{backgroundColor: '#F9F6F3'}}>
        <div className="container mx-auto max-w-6xl px-6">
          <EditableSection
            sectionKey="benefits_title"
            content={pageContent.benefits_title}
            onSave={saveSection}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16">
              ¿POR QUÉ ELEGIR ALQUIMIA DEL CAMBIO?
            </h2>
          </EditableSection>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                icon: '🎯',
                title: 'Contenido Estructurado',
                description: 'Un programa completo y progresivo diseñado por profesionales de la psicología y el coaching.'
              },
              {
                icon: '💪',
                title: 'Ejercicios Prácticos',
                description: 'Cada módulo incluye ejercicios de reflexión y herramientas aplicables inmediatamente.'
              },
              {
                icon: '🌱',
                title: 'A Tu Ritmo',
                description: 'Avanza según tu propio tiempo y necesidades, respetando tu proceso personal.'
              },
              {
                icon: '📱',
                title: 'Acceso Digital',
                description: 'Accede desde cualquier lugar y en cualquier momento a través de nuestro portal web.'
              },
              {
                icon: '✨',
                title: 'Transformación Profunda',
                description: 'Herramientas comprobadas para generar cambios reales y duraderos en tu vida.'
              },
              {
                icon: '❤️',
                title: 'Acompañamiento',
                description: 'Un espacio seguro para tu crecimiento personal y desarrollo emocional.'
              }
            ].map((benefit, index) => (
              <div 
                key={index}
                className="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all text-center"
              >
                <div className="text-5xl mb-4">{benefit.icon}</div>
                <h3 className="text-xl font-bold text-gray-800 mb-3">
                  {benefit.title}
                </h3>
                <p className="text-gray-700 leading-relaxed">
                  {benefit.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-20 bg-white">
        <div className="container mx-auto max-w-5xl px-6">
          <EditableSection
            sectionKey="how_it_works_title"
            content={pageContent.how_it_works_title}
            onSave={saveSection}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16">
              ¿CÓMO FUNCIONA?
            </h2>
          </EditableSection>
          <div className="space-y-6">
            {[
              {
                step: 1,
                title: 'Regístrate en el Portal',
                description: 'Crea tu cuenta en nuestro portal digital de forma rápida y sencilla.'
              },
              {
                step: 2,
                title: 'Accede a los Módulos',
                description: 'Explora el contenido de cada módulo: videos, textos y recursos descargables.'
              },
              {
                step: 3,
                title: 'Realiza los Ejercicios',
                description: 'Completa los ejercicios de reflexión personal que te ayudarán a integrar los aprendizajes.'
              },
              {
                step: 4,
                title: 'Avanza a Tu Ritmo',
                description: 'Progresa según tu disponibilidad, respetando tu proceso único de transformación.'
              },
              {
                step: 5,
                title: 'Transforma tu Vida',
                description: 'Aplica las herramientas aprendidas y observa los cambios positivos en tu vida diaria.'
              }
            ].map((item, index) => (
              <div 
                key={index}
                className="flex items-start space-x-6 bg-gradient-to-r from-stone-50 to-white p-6 rounded-xl border-l-4"
                style={{borderColor: '#6b745a'}}
              >
                <div 
                  className="flex-shrink-0 w-12 h-12 rounded-full flex items-center justify-center text-white text-xl font-bold shadow-lg"
                  style={{backgroundColor: '#6b745a'}}
                >
                  {item.step}
                </div>
                <div>
                  <h3 className="text-xl font-bold text-gray-800 mb-2">
                    {item.title}
                  </h3>
                  <p className="text-gray-700 leading-relaxed">
                    {item.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-20" style={{backgroundColor: '#eef2ec'}}>
        <div className="container mx-auto max-w-6xl px-6">
          <EditableSection
            sectionKey="testimonials_title"
            content={pageContent.testimonials_title}
            onSave={saveSection}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-center text-gray-800 mb-16">
              Lo que dicen nuestras participantes
            </h2>
          </EditableSection>
          <div className="grid md:grid-cols-2 gap-8">
            {[
              {
                text: 'Este programa me ayudó a entender mis emociones y a manejarlas de manera saludable. Ahora me siento más en paz conmigo misma.',
                name: 'María G.',
                img: 'TESTIMONIO-PROGRAMA-001'
              },
              {
                text: 'Los ejercicios de cada módulo me permitieron reflexionar profundamente sobre mi vida. Fue un viaje transformador.',
                name: 'Laura S.',
                img: 'TESTIMONIO-PROGRAMA-002'
              },
              {
                text: 'La estructura del programa es excelente. Cada módulo se construye sobre el anterior, creando un camino claro hacia el crecimiento personal.',
                name: 'Ana M.',
                img: 'TESTIMONIO-PROGRAMA-003'
              },
              {
                text: 'Poder hacerlo a mi ritmo fue fundamental. Este programa me dio las herramientas para cambiar mi vida.',
                name: 'Carmen P.',
                img: 'TESTIMONIO-PROGRAMA-004'
              }
            ].map((testimonial, index) => (
              <div 
                key={index}
                className="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all"
              >
                <div className="w-full h-48 bg-gray-200 rounded-xl flex items-center justify-center text-gray-600 text-xs mb-6">
                  [IMG-{testimonial.img}]
                </div>
                <p className="text-gray-700 italic leading-relaxed text-lg mb-4">
                  "{testimonial.text}"
                </p>
                <p className="font-semibold text-gray-800">
                  - {testimonial.name}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Founder */}
      <section className="py-20 bg-white">
        <div className="container mx-auto max-w-6xl px-6">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <div className="w-full h-[500px] bg-gray-200 rounded-2xl flex items-center justify-center text-gray-600">
                [IMG-VICTORIA-PROGRAMA: Victoria Novoa profesional]
              </div>
            </div>
            <EditableSection
              sectionKey="founder_bio"
              content={pageContent.founder_bio}
              onSave={saveSection}
            >
              <div>
                <h2 className="text-4xl font-bold text-gray-800 mb-6">
                  Creado por Victoria Novoa
                </h2>
                <h3 style={{color: '#6b745a'}} className="text-2xl font-semibold mb-6">
                  Psicóloga Clínica y Coach de Vida
                </h3>
                <div className="space-y-4 text-gray-700 leading-relaxed">
                  <p>
                    Psicóloga Clínica y de Salud, Líder Coach y Life Coach, experta en Inteligencia Emocional, diplomada en Neuropsicología del desarrollo, Magister en Psicoterapia Cognitivo Conductual y Magister en Terapia del Bienestar emocional.
                  </p>
                  <p>
                    Con más de 9 años de experiencia ayudando a miles de mujeres alrededor del mundo en su proceso de autoconocimiento y amor propio, he diseñado este programa para acompañarte en tu camino de transformación personal.
                  </p>
                  <p className="font-semibold" style={{color: '#6b745a'}}>
                    Mi misión es ayudarte a reconectar con tu esencia, fortalecer tu autoestima y construir la vida plena que mereces.
                  </p>
                </div>
              </div>
            </EditableSection>
          </div>
        </div>
      </section>

      {/* CTA Final */}
      <section className="py-20" style={{backgroundColor: '#6b745a'}}>
        <div className="container mx-auto max-w-4xl px-6 text-center">
          <EditableSection
            sectionKey="cta_final"
            content={pageContent.cta_final}
            onSave={saveSection}
            editClassName="p-4 bg-white/20 border-2 border-white/50 rounded-lg"
          >
            <div>
              <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
                ¿Lista para transformar tu vida?
              </h2>
              <p className="text-xl text-white mb-10 leading-relaxed">
                Únete a miles de mujeres que ya están viviendo su transformación personal con Cambio de Paradigma.
              </p>
            </div>
          </EditableSection>
          <button 
            onClick={() => navigate('/login')}
            style={{color: '#6b745a'}}
            className="bg-white px-12 py-4 rounded-full text-lg font-semibold hover:bg-gray-100 transition-all shadow-lg hover:shadow-xl transform hover:scale-105"
          >
            ACCEDER AL PORTAL AHORA
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-stone-100 border-t border-stone-200 py-12">
        <div className="container mx-auto max-w-6xl px-6">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center space-x-3 mb-4 md:mb-0">
              <img 
                src="/Logo nr.png" 
                alt="Cambio de Paradigma" 
                className="w-10 h-10 object-contain"
                onError={(e) => {
                  e.target.style.display = 'none';
                }}
              />
              <span className="text-lg font-semibold text-gray-800">
                Cambio de Paradigma
              </span>
            </div>
            <div className="flex space-x-6 text-gray-600">
              <button 
                onClick={() => navigate('/retiro-renacer')}
                className="hover:text-gray-800 transition-colors"
              >
                Retiro Renacer
              </button>
              <button className="hover:text-gray-800 transition-colors">
                Contacto
              </button>
            </div>
          </div>
          <div className="mt-8 text-center text-sm text-gray-600">
            © 2024 Cambio de Paradigma. Todos los derechos reservados.
          </div>
        </div>
      </footer>
    </div>
  );
};

export default ProgramLanding;

