import React, { useState, useEffect, useRef } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getModules } from '../services/api';
import { config } from '../config';
import { 
  Music, 
  Target, 
  Lightbulb, 
  Sparkles, 
  BookOpen,
  Play,
  Pause,
  ClipboardList,
  Check,
  Lock,
  BarChart3
} from 'lucide-react';

const ModuleView = () => {
  const { moduleId } = useParams();
  const [module, setModule] = useState(null);
  const [themes, setThemes] = useState([]);
  const [recursos, setRecursos] = useState([]);
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
        
        // Separate themes and recursos
        const normalThemes = themesData.filter(t => !t.theme_type || t.theme_type === 'theme');
        const recursosData = themesData.filter(t => t.theme_type === 'resource');
        
        setThemes(normalThemes);
        setRecursos(recursosData);

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
        setIsAudioPlaying(false);
      } else {
        const playPromise = audioRef.current.play();
        if (playPromise !== undefined) {
          playPromise
            .then(() => {
              setIsAudioPlaying(true);
            })
            .catch(error => {
              console.error('Error playing audio:', error);
              alert(`Error al reproducir el audio: ${error.message}`);
              setIsAudioPlaying(false);
            });
        }
      }
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
              <div className="rounded-2xl p-6 mb-6" style={{ 
                background: 'linear-gradient(135deg, rgba(107, 116, 90, 0.3) 0%, rgba(107, 116, 90, 0.2) 100%)' 
              }}>
                <h3 className="text-lg font-semibold text-sage-800 mb-4 flex items-center">
                  <Music className="w-5 h-5 mr-2 text-sage-700" />
                  Audio de Introducción
                </h3>
                <div className="flex items-center space-x-4">
                  <button
                    onClick={toggleAudio}
                    className="w-12 h-12 rounded-full flex items-center justify-center text-white transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105"
                    style={{ 
                      backgroundColor: '#6b745a'
                    }}
                    onMouseEnter={(e) => e.target.style.backgroundColor = '#5a6349'}
                    onMouseLeave={(e) => e.target.style.backgroundColor = '#6b745a'}
                  >
                    {isAudioPlaying ? (
                      <Pause className="w-5 h-5" />
                    ) : (
                      <Play className="w-5 h-5 ml-0.5" />
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
                  src={`/audio/${module.audio_file}`}
                  onEnded={handleAudioEnded}
                  className="hidden"
                >
                  Tu navegador no soporta la reproducción de audio.
                </audio>
              </div>
            )}

            {/* Module Details */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {module.objective && (
                <div className="bg-white/50 rounded-xl p-4">
                  <h4 className="font-semibold text-sage-800 mb-2 flex items-center">
                    <Target className="w-5 h-5 mr-2 text-sage-700" />
                    Objetivo
                  </h4>
                  <p className="text-sage-700 text-sm">{module.objective}</p>
                </div>
              )}

              {module.belief_to_transform && (
                <div className="bg-white/50 rounded-xl p-4">
                  <h4 className="font-semibold text-sage-800 mb-2 flex items-center">
                    <Lightbulb className="w-5 h-5 mr-2 text-sage-700" />
                    Creencia a Transformar
                  </h4>
                  <p className="text-sage-700 text-sm italic">"{module.belief_to_transform}"</p>
                </div>
              )}

              {module.expected_results && (
                <div className="bg-white/50 rounded-xl p-4 md:col-span-2">
                  <h4 className="font-semibold text-sage-800 mb-2 flex items-center">
                    <Sparkles className="w-5 h-5 mr-2 text-sage-700" />
                    Resultados Esperados
                  </h4>
                  <p className="text-sage-700 text-sm">{module.expected_results}</p>
                </div>
              )}

              {module.recommended_book && (
                <div className="bg-white/50 rounded-xl p-4 md:col-span-2">
                  <h4 className="font-semibold text-sage-800 mb-2 flex items-center">
                    <BookOpen className="w-5 h-5 mr-2 text-sage-700" />
                    Libro Recomendado
                  </h4>
                  <p className="text-sage-700 text-sm">{module.recommended_book}</p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Themes and Recursos Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
        {/* Themes Column (left, 2/3) */}
        <div className="lg:col-span-2">
          <h2 className="text-2xl font-inter font-bold text-sage-800 mb-6 flex items-center">
            <ClipboardList className="w-6 h-6 mr-3 text-sage-700" />
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
                  <div 
                    className="w-12 h-12 rounded-full flex items-center justify-center text-white font-bold"
                    style={{
                      backgroundColor: theme.is_completed 
                        ? '#6b745a' 
                        : theme.is_unlocked 
                          ? '#6b745a' 
                          : '#9ca3af'
                    }}
                  >
                    {theme.is_completed ? (
                      <Check className="w-5 h-5" />
                    ) : theme.is_unlocked ? (
                      <span>{theme.order_number}</span>
                    ) : (
                      <Lock className="w-5 h-5" />
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
                    className="px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200 text-white hover:shadow-lg transform hover:scale-105"
                    style={{ 
                      backgroundColor: '#6b745a'
                    }}
                    onMouseEnter={(e) => e.target.style.backgroundColor = '#5a6349'}
                    onMouseLeave={(e) => e.target.style.backgroundColor = '#6b745a'}
                  >
                    {theme.is_completed ? 'Revisar' : 'Comenzar'}
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

        {/* Recursos Column (right, 1/3) */}
        <div>
          <h2 className="text-2xl font-inter font-bold text-sage-800 mb-6 flex items-center">
            <Lightbulb className="w-6 h-6 mr-3 text-sage-700" />
            Recursos
          </h2>
          
          {recursos.length > 0 ? (
            <div className="space-y-6">
              {recursos.map((recurso) => (
                <Link
                  key={recurso.id}
                  to={`/theme/${recurso.id}`}
                  className="block rounded-2xl shadow-xl p-6 transition-all duration-300 hover:shadow-2xl min-h-[152px]"
                  style={{ backgroundColor: '#6b745a' }}
                >
                  <div className="flex items-start space-x-4 mb-4">
                    <div className="w-12 h-12 rounded-full flex items-center justify-center bg-white/20 backdrop-blur-sm flex-shrink-0">
                      <BookOpen className="w-5 h-5 text-white" />
                    </div>
                    <div className="flex-1">
                      <h3 className="text-xl font-semibold text-white mb-2">
                        {recurso.title}
                      </h3>
                    </div>
                  </div>
                  <div className="text-white/90 text-sm leading-relaxed">
                    {recurso.content.substring(0, 200)}...
                  </div>
                </Link>
              ))}
            </div>
          ) : (
            <div className="bg-gradient-calm border-2 border-dashed border-sage-300 rounded-xl p-6 text-center">
              <BookOpen className="w-12 h-12 text-sage-400 mx-auto mb-3" />
              <p className="text-sage-600 text-sm">
                No hay recursos adicionales disponibles para este módulo todavía.
              </p>
            </div>
          )}
        </div>
      </div>

      {/* Progress Summary */}
      <div className="bg-gradient-calm rounded-2xl shadow-xl p-6 border border-sage-200">
        <h3 className="text-lg font-semibold text-sage-800 mb-4 flex items-center">
          <BarChart3 className="w-5 h-5 mr-2 text-sage-700" />
          Progreso del Módulo
        </h3>
        <div className="flex items-center space-x-4">
          <div className="flex-1">
            <div className="bg-white/60 rounded-full h-3 overflow-hidden">
              <div 
                className="h-full transition-all duration-500 ease-out"
                style={{ 
                  width: `${themes.length > 0 ? (themes.filter(t => t.is_completed).length / themes.length) * 100 : 0}%`,
                  background: 'linear-gradient(to right, #6b745a, #8a9373)'
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
