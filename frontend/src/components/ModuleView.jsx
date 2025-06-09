import React, { useState, useEffect, useRef } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getModules } from '../services/api';
import { config } from '../config';

const ModuleView = () => {
  const { moduleId } = useParams();
  const [module, setModule] = useState(null);
  const [themes, setThemes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [isAudioPlaying, setIsAudioPlaying] = useState(false);
  const audioRef = useRef(null);

  useEffect(() => {
    const fetchModuleData = async () => {
      try {
        // Get module data
        const modulesResponse = await fetch(`${config.apiUrl}/modules`, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        const modules = await modulesResponse.json();
        const currentModule = modules.find(m => m.id === parseInt(moduleId));
        
        if (!currentModule) {
          setError('Module non trouvé');
          return;
        }
        
        setModule(currentModule);

        // Get themes for this module
        const themesResponse = await fetch(`${config.apiUrl}/modules/${moduleId}/themes`, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        const themesData = await themesResponse.json();
        setThemes(themesData);

      } catch (err) {
        setError('Erreur lors du chargement du module');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchModuleData();
  }, [moduleId]);

  const toggleAudio = () => {
    if (audioRef.current) {
      if (isAudioPlaying) {
        audioRef.current.pause();
      } else {
        audioRef.current.play();
      }
      setIsAudioPlaying(!isAudioPlaying);
    }
  };

  const handleAudioEnded = () => {
    setIsAudioPlaying(false);
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="flex items-center space-x-3">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-500"></div>
          <span className="text-sage-600">Chargement du module...</span>
        </div>
      </div>
    );
  }

  if (error || !module) {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="bg-red-50 border border-red-200 rounded-lg p-4">
          <p className="text-red-700">{error || 'Module non trouvé'}</p>
          <Link 
            to="/dashboard" 
            className="mt-2 inline-block text-primary-600 hover:text-primary-700"
          >
            Retour au tableau de bord
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Module Header */}
      <div className="mb-8">
        <div className="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl p-8 border border-sage-200 relative overflow-hidden">
          {/* Background decoration */}
          <div className="absolute top-0 right-0 opacity-5">
            <div className="text-9xl">🧠</div>
          </div>
          
          <div className="relative z-10">
            {/* Breadcrumb */}
            <nav className="mb-6">
              <Link 
                to="/dashboard" 
                className="text-sage-600 hover:text-primary-600 transition-colors text-sm flex items-center"
              >
                <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                </svg>
                Retour au tableau de bord
              </Link>
            </nav>

            {/* Module Title */}
            <h1 className="text-4xl font-inter font-bold text-sage-800 mb-4">
              Módulo {module.order_number}: {module.title}
            </h1>
            
            {/* Module Description */}
            <p className="text-lg text-sage-600 mb-6 leading-relaxed">
              {module.description}
            </p>

            {/* Audio Introduction */}
            {module.audio_file && (
              <div className="bg-gradient-nature rounded-2xl p-6 mb-6">
                <h3 className="text-lg font-semibold text-sage-800 mb-4 flex items-center">
                  <span className="mr-2">🎵</span>
                  Audio de Introducción
                </h3>
                <div className="flex items-center space-x-4">
                  <button
                    onClick={toggleAudio}
                    className="w-12 h-12 bg-primary-500 hover:bg-primary-600 rounded-full flex items-center justify-center text-white transition-colors shadow-lg"
                  >
                    {isAudioPlaying ? (
                      <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 9v6m4-6v6" />
                      </svg>
                    ) : (
                      <svg className="w-6 h-6 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1.5a2.5 2.5 0 110 5H9V10z" />
                      </svg>
                    )}
                  </button>
                  <div className="flex-1">
                    <p className="text-sage-700 text-sm">
                      {isAudioPlaying ? 'Reproduciendo...' : 'Escucha la introducción del módulo'}
                    </p>
                  </div>
                </div>
                <audio
                  ref={audioRef}
                  onEnded={handleAudioEnded}
                  className="hidden"
                >
                  <source src={`/audio/${module.audio_file}`} type="audio/mpeg" />
                  Tu navegador no soporta la reproducción de audio.
                </audio>
              </div>
            )}

            {/* Module Details */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {module.objective && (
                <div className="bg-white/50 rounded-xl p-4">
                  <h4 className="font-semibold text-sage-800 mb-2 flex items-center">
                    <span className="mr-2">🎯</span>
                    Objetivo
                  </h4>
                  <p className="text-sage-700 text-sm">{module.objective}</p>
                </div>
              )}

              {module.belief_to_transform && (
                <div className="bg-white/50 rounded-xl p-4">
                  <h4 className="font-semibold text-sage-800 mb-2 flex items-center">
                    <span className="mr-2">💭</span>
                    Creencia a Transformar
                  </h4>
                  <p className="text-sage-700 text-sm italic">"{module.belief_to_transform}"</p>
                </div>
              )}

              {module.expected_results && (
                <div className="bg-white/50 rounded-xl p-4 md:col-span-2">
                  <h4 className="font-semibold text-sage-800 mb-2 flex items-center">
                    <span className="mr-2">✨</span>
                    Resultados Esperados
                  </h4>
                  <p className="text-sage-700 text-sm">{module.expected_results}</p>
                </div>
              )}

              {module.recommended_book && (
                <div className="bg-white/50 rounded-xl p-4 md:col-span-2">
                  <h4 className="font-semibold text-sage-800 mb-2 flex items-center">
                    <span className="mr-2">📚</span>
                    Libro Recomendado
                  </h4>
                  <p className="text-sage-700 text-sm">{module.recommended_book}</p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Themes Section */}
      <div className="mb-8">
        <h2 className="text-2xl font-inter font-bold text-sage-800 mb-6 flex items-center">
          <span className="mr-3">📋</span>
          Temas del Módulo
        </h2>
        
        <div className="space-y-6">
          {themes.map((theme, index) => (
            <div
              key={theme.id}
              className={`bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl border border-sage-200 p-6 transition-all duration-300 ${
                !theme.is_unlocked ? 'opacity-60' : 'hover:shadow-2xl'
              }`}
            >
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center space-x-4">
                  <div className={`w-12 h-12 rounded-full flex items-center justify-center text-white font-bold ${
                    theme.is_completed 
                      ? 'bg-green-500' 
                      : theme.is_unlocked 
                        ? 'bg-primary-500' 
                        : 'bg-sage-300'
                  }`}>
                    {theme.is_completed ? (
                      <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                    ) : theme.is_unlocked ? (
                      <span>{theme.order_number}</span>
                    ) : (
                      <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 2h12a2 2 0 002-2V7a2 2 0 00-2-2H6a2 2 0 00-2 2v10a2 2 0 002 2zM9 5a3 3 0 016 0v2H9V5z" />
                      </svg>
                    )}
                  </div>
                  <div>
                    <h3 className="text-xl font-semibold text-sage-800">
                      Tema {theme.order_number}: {theme.title}
                    </h3>
                    <p className="text-sage-600 text-sm mt-1">
                      {theme.is_completed ? 'Completado' : theme.is_unlocked ? 'Disponible' : 'Bloqueado'}
                    </p>
                  </div>
                </div>
                
                {theme.is_unlocked && (
                  <Link
                    to={`/theme/${theme.id}`}
                    className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                      theme.is_completed
                        ? 'bg-green-100 text-green-700 hover:bg-green-200'
                        : 'bg-primary-500 text-white hover:bg-primary-600'
                    }`}
                  >
                    {theme.is_completed ? 'Revoir' : 'Commencer'}
                  </Link>
                )}
              </div>
              
              <div className="text-sage-700 text-sm leading-relaxed">
                {theme.content.substring(0, 200)}...
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Progress Summary */}
      <div className="bg-gradient-calm rounded-2xl shadow-xl p-6 border border-sage-200">
        <h3 className="text-lg font-semibold text-sage-800 mb-4 flex items-center">
          <span className="mr-2">📊</span>
          Progreso del Módulo
        </h3>
        <div className="flex items-center space-x-4">
          <div className="flex-1">
            <div className="bg-white/60 rounded-full h-3 overflow-hidden">
              <div 
                className="h-full bg-gradient-to-r from-primary-400 to-primary-600 transition-all duration-500 ease-out"
                style={{ 
                  width: `${themes.length > 0 ? (themes.filter(t => t.is_completed).length / themes.length) * 100 : 0}%` 
                }}
              ></div>
            </div>
          </div>
          <div className="text-right">
            <span className="text-xl font-bold text-sage-800">
              {themes.filter(t => t.is_completed).length}
            </span>
            <span className="text-sage-600">/{themes.length}</span>
            <p className="text-sm text-sage-600">temas completados</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ModuleView; 
