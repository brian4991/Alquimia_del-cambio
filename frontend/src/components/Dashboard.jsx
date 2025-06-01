import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { 
  ArrowRightIcon, 
  PlayIcon, 
  CheckCircleIcon,
  BookOpenIcon,
  ClockIcon,
  TrophyIcon,
  SparklesIcon,
  ChartBarIcon,
  AcademicCapIcon
} from '@heroicons/react/24/outline';

const Dashboard = () => {
  const [modules, setModules] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchModules = async () => {
      try {
        const response = await fetch('http://localhost:8000/modules', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        
        if (!response.ok) {
          throw new Error('Erreur lors du chargement des modules');
        }
        
        const data = await response.json();
        setModules(data);
      } catch (err) {
        setError('Impossible de charger les modules');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchModules();
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
    <div className="max-w-7xl mx-auto px-6 py-12">
      {/* En-tête de bienvenue */}
      <div className="mb-16">
        <div className="modern-card gradient-elegant text-center relative overflow-hidden">
          <div className="absolute top-0 right-0 opacity-10">
            <SparklesIcon className="w-32 h-32 text-sage" />
          </div>
          <div className="relative z-10">
            <div className="flex justify-center mb-6">
              <div className="p-4 gradient-sage rounded-full">
                <AcademicCapIcon className="w-12 h-12 text-white" />
              </div>
            </div>
            <h1 className="font-inter text-4xl font-semibold text-black mb-4">
              Bienvenido a tu recorrido
            </h1>
            <p className="font-inter text-xl text-taupe-dark leading-relaxed max-w-2xl mx-auto">
              Descubre tu potencial a través de un viaje de transformación personal guiado y amoroso
            </p>
          </div>
        </div>
      </div>

      {/* Statistiques rapides */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
        <div className="modern-card text-center">
          <div className="flex justify-center mb-4">
            <div className="p-3 bg-gray-100 rounded-xl">
              <BookOpenIcon className="w-8 h-8 text-gray-700" />
            </div>
          </div>
          <h3 className="font-inter text-xl font-semibold text-black mb-2">
            {modules.length}
          </h3>
          <p className="font-inter text-taupe">
            Módulos disponibles
          </p>
        </div>
        
        <div className="modern-card text-center">
          <div className="flex justify-center mb-4">
            <div className="p-3 bg-gray-100 rounded-xl">
              <CheckCircleIcon className="w-8 h-8 text-gray-700" />
            </div>
          </div>
          <h3 className="font-inter text-xl font-semibold text-black mb-2">
            {modules.filter(m => m.completed).length}
          </h3>
          <p className="font-inter text-taupe">
            Módulos completados
          </p>
        </div>
        
        <div className="modern-card text-center">
          <div className="flex justify-center mb-4">
            <div className="p-3 bg-gray-100 rounded-xl">
              <TrophyIcon className="w-8 h-8 text-gray-700" />
            </div>
          </div>
          <h3 className="font-inter text-xl font-semibold text-black mb-2">
            {Math.round((modules.filter(m => m.completed).length / Math.max(modules.length, 1)) * 100)}%
          </h3>
          <p className="font-inter text-taupe">
            Progreso general
          </p>
        </div>
      </div>

      {/* Liste des modules */}
      <div className="mb-12">
        <div className="flex items-center space-x-3 mb-8">
          <div className="p-3 gradient-taupe rounded-xl">
            <ChartBarIcon className="w-8 h-8 text-white" />
          </div>
          <h2 className="font-inter text-3xl font-semibold text-black">
            Tus módulos de formación
          </h2>
        </div>
        
        {modules.length === 0 ? (
          <div className="modern-card text-center">
            <BookOpenIcon className="w-16 h-16 text-taupe mx-auto mb-6" />
            <h3 className="font-inter text-2xl font-semibold text-black mb-4">
              Ningún módulo disponible
            </h3>
            <p className="font-inter text-taupe-dark mb-8 leading-relaxed">
              Los módulos de formación estarán disponibles pronto. Mantente conectado para descubrir tu camino de transformación.
            </p>
            <Link 
              to="/admin" 
              className="btn-sage font-inter inline-flex items-center"
            >
              <ArrowRightIcon className="w-5 h-5 mr-2" />
              Acceder a la administración
            </Link>
          </div>
        ) : (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {modules.map(module => (
              <div key={module.id} className="modern-card group hover:shadow-sage transition-elegant">
                <div className="flex items-start justify-between mb-6">
                  <div className="flex items-center space-x-4">
                    <div className={`p-4 rounded-xl ${
                      module.completed 
                        ? 'bg-green-100' 
                        : 'gradient-sage'
                    }`}>
                      {module.completed ? (
                        <CheckCircleIcon className="w-10 h-10 text-green-600" />
                      ) : (
                        <PlayIcon className="w-10 h-10 text-white" />
                      )}
                    </div>
                    <div>
                      <h3 className="font-inter text-xl font-semibold text-black mb-1">
                        {module.title}
                      </h3>
                      <div className="flex items-center space-x-4 text-sm font-inter text-taupe">
                        <div className="flex items-center space-x-1">
                          <BookOpenIcon className="w-4 h-4" />
                          <span>Módulo {module.order_number}</span>
                        </div>
                        <div className="flex items-center space-x-1">
                          <ClockIcon className="w-4 h-4" />
                          <span>~45 min</span>
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  {module.completed && (
                    <div className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-xs font-inter font-medium">
                      Completado
                    </div>
                  )}
                </div>

                <div className="mb-6">
                  <p className="font-inter text-taupe-dark leading-relaxed">
                    {module.description}
                  </p>
                </div>

                {/* Barre de progression */}
                <div className="mb-6">
                  <div className="flex justify-between items-center mb-2">
                    <span className="font-inter text-sm font-medium text-taupe-dark">
                      Progreso
                    </span>
                    <span className="font-inter text-sm text-taupe">
                      {module.progress || 0}%
                    </span>
                  </div>
                  <div className="progress-modern">
                    <div 
                      className="progress-bar"
                      style={{ width: `${module.progress || 0}%` }}
                    ></div>
                  </div>
                </div>

                <div className="flex items-center justify-between">
                  <div className="font-inter text-sm text-taupe">
                    {module.themes_count || 0} temas disponibles
                  </div>
                  
                  <Link
                    to={`/module/${module.id}`}
                    className={`inline-flex items-center px-6 py-3 rounded-xl font-inter font-medium transition-elegant group-hover:translate-x-1 ${
                      module.completed
                        ? 'bg-green-100 text-green-700 hover:bg-green-200'
                        : 'gradient-sage text-white hover:shadow-sage'
                    }`}
                  >
                    {module.completed ? 'Revisar' : 'Comenzar'}
                    <ArrowRightIcon className="w-5 h-5 ml-2" />
                  </Link>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Section motivation */}
      <div className="modern-card gradient-elegant text-center">
        <div className="flex justify-center mb-6">
          <div className="p-4 gradient-taupe rounded-full">
            <SparklesIcon className="w-12 h-12 text-white" />
          </div>
        </div>
        <h3 className="font-inter text-2xl font-semibold text-black mb-6">
          Tu transformación comienza hoy
        </h3>
        <blockquote className="font-inter text-lg text-taupe-dark leading-relaxed max-w-2xl mx-auto mb-8 italic">
          "Cada paso de tu recorrido es una oportunidad de descubrir quién eres realmente y florecer plenamente."
        </blockquote>
        <div className="flex justify-center space-x-6 text-4xl opacity-70">
          <div className="p-3 bg-sage rounded-full">
            <BookOpenIcon className="w-8 h-8 text-white" />
          </div>
          <div className="p-3 bg-taupe rounded-full">
            <SparklesIcon className="w-8 h-8 text-white" />
          </div>
          <div className="p-3 bg-sage-light rounded-full">
            <TrophyIcon className="w-8 h-8 text-white" />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard; 
