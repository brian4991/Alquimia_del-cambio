import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getModules } from '../services/api';
import { 
  ArrowRightIcon, 
  PlayIcon, 
  CheckCircleIcon,
  BookOpenIcon,
  ClockIcon,
  TrophyIcon,
  SparklesIcon,
  ChartBarIcon,
  AcademicCapIcon,
  LockClosedIcon,
  ArrowPathIcon,
  QuestionMarkCircleIcon,
  ChevronDownIcon,
  ChevronUpIcon,
  MusicalNoteIcon
} from '@heroicons/react/24/outline';

const Dashboard = () => {
  const [modules, setModules] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [showIntroVideo, setShowIntroVideo] = useState(false);

  const fetchModules = async () => {
    try {
      setLoading(true);
      const data = await getModules();
      setModules(data);
      setError('');
    } catch (err) {
      setError('Impossible de charger les modules');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchModules();
  }, []);

  // Listen for storage changes (e.g., when user is validated in another tab)
  useEffect(() => {
    const handleStorageChange = (e) => {
      if (e.key === 'userValidationChanged') {
        fetchModules();
        localStorage.removeItem('userValidationChanged');
      }
    };

    window.addEventListener('storage', handleStorageChange);
    
    // Also listen for custom events in the same tab
    const handleValidationChange = () => {
      fetchModules();
    };
    
    window.addEventListener('userValidationChanged', handleValidationChange);

    return () => {
      window.removeEventListener('storage', handleStorageChange);
      window.removeEventListener('userValidationChanged', handleValidationChange);
    };
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen gradient-elegant flex items-center justify-center">
        <div className="modern-card text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-4 border-sage border-t-transparent mx-auto mb-4"></div>
          <p className="text-sage font-inter text-lg">Cargando tu recorrido...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-4xl mx-auto px-6 py-12">
        <div className="modern-card bg-red-50 border-red-200 border-2 text-center">
          <p className="text-red-700 font-inter text-lg mb-4">{error}</p>
          <button 
            onClick={() => window.location.reload()}
            className="btn-sage font-inter"
          >
            Reintentar
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 py-6 sm:py-12">
      {/* En-tête de bienvenue */}
      <div className="mb-8 sm:mb-16">
        <div className="modern-card text-center relative overflow-hidden" style={{
          backgroundImage: 'url(/portrait5.jpg)',
          backgroundSize: 'cover',
          backgroundPosition: 'center 70%',
          backgroundRepeat: 'no-repeat',
          animation: 'slowPan 30s ease-in-out infinite alternate'
        }}>
          <style jsx>{`
            @keyframes slowPan {
              0% { background-position: center 0%; }
              100% { background-position: center 100%; }
            }
          `}</style>
          {/* Overlay grisé */}
          <div className="absolute inset-0 bg-black bg-opacity-60"></div>

          <div className="relative z-10">
            <div className="flex justify-center mb-4 sm:mb-6">
              <div className="p-3 sm:p-4 gradient-sage rounded-full">
                <AcademicCapIcon className="w-8 h-8 sm:w-12 sm:h-12 text-white" />
              </div>
            </div>
            <h1 className="font-inter text-2xl sm:text-3xl md:text-4xl font-semibold text-white mb-3 sm:mb-4 px-4">
              Bienvenido(a) a tu recorrido
            </h1>
            <p className="font-inter text-base sm:text-lg md:text-xl text-white leading-relaxed max-w-2xl mx-auto px-4">
              Descubre tu potencial a través de un viaje de transformación personal guiado y profundo
            </p>
          </div>
        </div>
      </div>

      {/* Bandeau vidéo d'introduction */}
      <div className="mb-8 sm:mb-12">
        <button
          onClick={() => setShowIntroVideo(!showIntroVideo)}
          className="w-full modern-card p-4 sm:p-5 flex items-center justify-between group hover:shadow-sage transition-elegant cursor-pointer bg-gradient-to-r from-sage/5 to-taupe/5 border-2 border-sage/20 hover:border-sage/40"
        >
          <div className="flex items-center space-x-3 sm:space-x-4">
            <div className="p-2 sm:p-3 gradient-sage rounded-full">
              <QuestionMarkCircleIcon className="w-5 h-5 sm:w-6 sm:h-6 text-white" />
            </div>
            <div className="text-left">
              <p className="font-inter text-sm sm:text-base md:text-lg font-medium text-black">
                ¿Es tu primera vez aquí o necesitas ayuda?
              </p>
              <p className="font-inter text-xs sm:text-sm text-taupe hidden sm:block">
                Video para saber como utilizar la plataforma y lo que vas hacer cada semana
              </p>
            </div>
          </div>
          <div className={`p-2 rounded-full bg-sage/10 transition-transform duration-300 ${showIntroVideo ? 'rotate-180' : ''}`}>
            <ChevronDownIcon className="w-5 h-5 sm:w-6 sm:h-6 text-sage" />
          </div>
        </button>

        <div 
          className={`overflow-hidden transition-all duration-500 ease-in-out ${
            showIntroVideo ? 'max-h-[800px] opacity-100 mt-4' : 'max-h-0 opacity-0'
          }`}
        >
          <div className="modern-card p-4 sm:p-6">
            <div className="relative w-full" style={{ paddingBottom: '56.25%' }}>
              <iframe
                className="absolute inset-0 w-full h-full rounded-xl"
                src="https://www.youtube.com/embed/XNQzifUHuCQ"
                title="Video de introducción a la plataforma"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              ></iframe>
            </div>
            <p className="font-inter text-sm text-taupe text-center mt-4">
              Este video te guiará en tus primeros pasos en la plataforma
            </p>
          </div>
        </div>
      </div>

      {/* Statistiques rapides */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 sm:gap-6 mb-8 sm:mb-16">
        <div className="modern-card text-center p-4 sm:p-8">
          <div className="flex justify-center mb-3 sm:mb-4">
            <div className="p-2 sm:p-3 bg-gray-100 rounded-xl">
              <BookOpenIcon className="w-6 h-6 sm:w-8 sm:h-8 text-gray-700" />
            </div>
          </div>
          <h3 className="font-inter text-lg sm:text-xl font-semibold text-black mb-1 sm:mb-2">
            {modules.length}
          </h3>
          <p className="font-inter text-sm sm:text-base text-taupe">
            Módulos disponibles
          </p>
        </div>
        
        <div className="modern-card text-center p-4 sm:p-8">
          <div className="flex justify-center mb-3 sm:mb-4">
            <div className="p-2 sm:p-3 bg-gray-100 rounded-xl">
              <CheckCircleIcon className="w-6 h-6 sm:w-8 sm:h-8 text-gray-700" />
            </div>
          </div>
          <h3 className="font-inter text-lg sm:text-xl font-semibold text-black mb-1 sm:mb-2">
            {modules.filter(m => m.completed).length}
          </h3>
          <p className="font-inter text-sm sm:text-base text-taupe">
            Módulos completados
          </p>
        </div>
        
        <div className="modern-card text-center p-4 sm:p-8">
          <div className="flex justify-center mb-3 sm:mb-4">
            <div className="p-2 sm:p-3 bg-gray-100 rounded-xl">
              <TrophyIcon className="w-6 h-6 sm:w-8 sm:h-8 text-gray-700" />
            </div>
          </div>
          <h3 className="font-inter text-lg sm:text-xl font-semibold text-black mb-1 sm:mb-2">
            {Math.round((modules.filter(m => m.completed).length / Math.max(modules.length, 1)) * 100)}%
          </h3>
          <p className="font-inter text-sm sm:text-base text-taupe">
            Progreso general
          </p>
        </div>
      </div>

      {/* Liste des modules */}
      <div className="mb-8 sm:mb-12">
        <div className="flex items-center space-x-2 sm:space-x-3 mb-6 sm:mb-8">
          <div className="p-2 sm:p-3 gradient-taupe rounded-xl">
            <ChartBarIcon className="w-6 h-6 sm:w-8 sm:h-8 text-white" />
          </div>
          <h2 className="font-inter text-xl sm:text-2xl md:text-3xl font-semibold text-black">
            Tus módulos de formación
          </h2>
        </div>
        
        {modules.length === 0 ? (
          <div className="modern-card text-center p-6 sm:p-8">
            <BookOpenIcon className="w-12 h-12 sm:w-16 sm:h-16 text-taupe mx-auto mb-4 sm:mb-6" />
            <h3 className="font-inter text-xl sm:text-2xl font-semibold text-black mb-3 sm:mb-4">
              Ningún módulo disponible
            </h3>
            <p className="font-inter text-sm sm:text-base text-taupe-dark mb-6 sm:mb-8 leading-relaxed">
              Los módulos de formación estarán disponibles pronto. Mantente conectado para descubrir tu camino de transformación.
            </p>
            <Link 
              to="/admin" 
              className="btn-sage font-inter inline-flex items-center text-sm sm:text-base"
            >
              <ArrowRightIcon className="w-4 h-4 sm:w-5 sm:h-5 mr-2" />
              Acceder a la administración
            </Link>
          </div>
        ) : (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 sm:gap-6 lg:gap-8">
            {modules.map(module => (
              <div key={module.id} className={`modern-card group transition-elegant p-4 sm:p-6 lg:p-8 ${
                module.is_accessible === false 
                  ? 'opacity-60 cursor-not-allowed' 
                  : 'hover:shadow-sage cursor-pointer'
              }`}>
                <div className="flex items-start justify-between mb-4 sm:mb-6 flex-wrap gap-3">
                  <div className="flex items-center space-x-3 sm:space-x-4 flex-1 min-w-0">
                    <div className={`p-3 sm:p-4 rounded-xl flex-shrink-0 ${
                      !module.is_accessible 
                        ? 'bg-gray-200'
                        : module.completed 
                          ? 'bg-green-100' 
                          : 'gradient-sage'
                    }`}>
                      {!module.is_accessible ? (
                        <LockClosedIcon className="w-8 h-8 sm:w-10 sm:h-10 text-gray-500" />
                      ) : module.completed ? (
                        <CheckCircleIcon className="w-8 h-8 sm:w-10 sm:h-10 text-green-600" />
                      ) : (
                        <PlayIcon className="w-8 h-8 sm:w-10 sm:h-10 text-white" />
                      )}
                    </div>
                    <div className="min-w-0">
                      <h3 className="font-inter text-lg sm:text-xl font-semibold text-black mb-1 break-words">
                        {module.title}
                      </h3>
                      <div className="flex items-center space-x-2 sm:space-x-4 text-xs sm:text-sm font-inter text-taupe">
                        <div className="flex items-center space-x-1">
                          <BookOpenIcon className="w-3 h-3 sm:w-4 sm:h-4" />
                          <span>Módulo {module.order_number}</span>
                        </div>

                      </div>
                    </div>
                  </div>
                  
                  {!module.is_accessible ? (
                    <div className="px-3 py-1 bg-gray-200 text-gray-600 rounded-full text-xs font-inter font-medium flex items-center space-x-1">
                      <LockClosedIcon className="w-3 h-3" />
                      <span>Bloqueado</span>
                    </div>
                  ) : module.completed ? (
                    <div className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-xs font-inter font-medium">
                      Completado
                    </div>
                  ) : null}
                </div>

                <div className="mb-4 sm:mb-6">
                  <p className="font-inter text-sm sm:text-base text-taupe-dark leading-relaxed">
                    {module.description}
                  </p>
                </div>

                <div className="flex items-center justify-between flex-wrap gap-3">
                  <div className="font-inter text-xs sm:text-sm text-taupe">
                    {module.themes_count || 0} temas disponibles
                  </div>
                  
                  {!module.is_accessible ? (
                    <div className="inline-flex items-center px-4 sm:px-6 py-2 sm:py-3 rounded-xl font-inter text-sm sm:text-base font-medium bg-gray-200 text-gray-500 cursor-not-allowed">
                      <LockClosedIcon className="w-4 h-4 sm:w-5 sm:h-5 mr-2" />
                      Bloqueado
                    </div>
                  ) : (
                    <Link
                      to={`/module/${module.id}`}
                      className={`inline-flex items-center px-4 sm:px-6 py-2 sm:py-3 rounded-xl font-inter text-sm sm:text-base font-medium transition-elegant group-hover:translate-x-1 ${
                        module.completed
                          ? 'bg-green-100 text-green-700 hover:bg-green-200'
                          : 'gradient-sage text-white hover:shadow-sage'
                      }`}
                    >
                      {module.completed ? 'Revisar' : 'Comenzar'}
                      <ArrowRightIcon className="w-4 h-4 sm:w-5 sm:h-5 ml-2" />
                    </Link>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Meditations Section */}
      <div className="mb-8 sm:mb-12">
        <div className="flex items-center space-x-2 sm:space-x-3 mb-6 sm:mb-8">
          <div className="p-2 sm:p-3 gradient-taupe rounded-xl">
            <MusicalNoteIcon className="w-6 h-6 sm:w-8 sm:h-8 text-white" />
          </div>
          <h2 className="font-inter text-xl sm:text-2xl md:text-3xl font-semibold text-black">
            Meditaciones Guiadas
          </h2>
        </div>
        
        <Link 
          to="/meditaciones" 
          className="block modern-card group transition-elegant p-4 sm:p-6 lg:p-8 hover:shadow-sage cursor-pointer"
        >
          <div className="flex items-start justify-between mb-4 sm:mb-6 flex-wrap gap-3">
            <div className="flex items-center space-x-3 sm:space-x-4 flex-1 min-w-0">
              <div className="p-3 sm:p-4 rounded-xl flex-shrink-0 gradient-sage">
                <SparklesIcon className="w-8 h-8 sm:w-10 sm:h-10 text-white" />
              </div>
              <div className="min-w-0">
                <h3 className="font-inter text-lg sm:text-xl font-semibold text-black mb-1 break-words">
                  Meditaciones
                </h3>
                <div className="flex items-center space-x-2 sm:space-x-4 text-xs sm:text-sm font-inter text-taupe">
                  <div className="flex items-center space-x-1">
                    <MusicalNoteIcon className="w-3 h-3 sm:w-4 sm:h-4" />
                    <span>Espacio de paz interior</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="mb-4 sm:mb-6">
            <p className="font-inter text-sm sm:text-base text-taupe-dark leading-relaxed">
              Un espacio dedicado a tu bienestar interior. Meditaciones guiadas para acompañarte en cada etapa de tu transformación personal.
            </p>
          </div>

          <div className="flex items-center justify-between flex-wrap gap-3">
            <div className="font-inter text-xs sm:text-sm text-taupe">
              5 meditaciones disponibles
            </div>
            
            <div className="inline-flex items-center px-4 sm:px-6 py-2 sm:py-3 rounded-xl font-inter text-sm sm:text-base font-medium transition-elegant group-hover:translate-x-1 gradient-sage text-white hover:shadow-sage">
              Comenzar
              <ArrowRightIcon className="w-4 h-4 sm:w-5 sm:h-5 ml-2" />
            </div>
          </div>
        </Link>
      </div>

      {/* Section motivation */}
      <div className="modern-card text-center p-6 sm:p-8">
        <h3 className="font-inter text-xl sm:text-2xl font-semibold text-black mb-4 sm:mb-6">
          Tu transformación comienza hoy
        </h3>
        <blockquote className="font-inter text-base sm:text-lg text-taupe-dark leading-relaxed max-w-2xl mx-auto italic px-4">
          "Cada paso de tu recorrido es una oportunidad de descubrir quién eres realmente."
        </blockquote>
      </div>
    </div>
  );
};

export default Dashboard; 
