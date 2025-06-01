import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { 
  ChevronLeftIcon, 
  BookOpenIcon, 
  CheckCircleIcon, 
  LockClosedIcon,
  PlayIcon,
  CardStackIcon
} from '@heroicons/react/24/outline';
import api from '../services/api';
import CardsView from './CardsView';

const ModuleDetail = () => {
  const { moduleId } = useParams();
  const navigate = useNavigate();
  const [module, setModule] = useState(null);
  const [themes, setThemes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedTheme, setSelectedTheme] = useState(null);
  const [viewMode, setViewMode] = useState('themes'); // 'themes', 'cards', 'exercises'

  useEffect(() => {
    fetchModuleData();
  }, [moduleId]);

  const fetchModuleData = async () => {
    try {
      setLoading(true);
      const [moduleResponse, themesResponse] = await Promise.all([
        api.get(`/modules`), // We'll filter by ID
        api.get(`/modules/${moduleId}/themes`)
      ]);
      
      const moduleData = moduleResponse.data.find(m => m.id === parseInt(moduleId));
      setModule(moduleData);
      setThemes(themesResponse.data);
    } catch (err) {
      setError('Error loading module');
      console.error('Error fetching module data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleThemeClick = (theme) => {
    if (!theme.is_unlocked) {
      return;
    }
    setSelectedTheme(theme);
    setViewMode('cards');
  };

  const handleBackToThemes = () => {
    setSelectedTheme(null);
    setViewMode('themes');
  };

  const handleGoToExercises = () => {
    setViewMode('exercises');
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-indigo-600"></div>
          <p className="mt-4 text-gray-600">Cargando módulo...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600 mb-4">{error}</p>
          <button 
            onClick={fetchModuleData}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          >
            Reintentar
          </button>
        </div>
      </div>
    );
  }

  // Show CardsView if a theme is selected
  if (viewMode === 'cards' && selectedTheme) {
    return (
      <CardsView 
        themeId={selectedTheme.id}
        themeName={selectedTheme.title}
        onBack={handleBackToThemes}
      />
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <div className="bg-white shadow-lg">
        <div className="max-w-6xl mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <button
                onClick={() => navigate('/dashboard')}
                className="flex items-center text-gray-600 hover:text-gray-800 transition-colors"
              >
                <ChevronLeftIcon className="w-5 h-5 mr-2" />
                Volver al Dashboard
              </button>
              <div>
                <h1 className="text-3xl font-bold text-gray-900">{module?.title}</h1>
                <p className="text-gray-600 mt-1">{module?.description}</p>
              </div>
            </div>
            {module?.audio_file && (
              <button className="flex items-center bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">
                <PlayIcon className="w-4 h-4 mr-2" />
                Audio del Módulo
              </button>
            )}
          </div>
        </div>
      </div>

      <div className="max-w-6xl mx-auto px-4 py-8">
        {/* Module Info */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-8">
          <div className="grid md:grid-cols-2 gap-6">
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-3">Objetivo del Módulo</h3>
              <p className="text-gray-700 leading-relaxed">{module?.objective}</p>
              
              <h3 className="text-lg font-semibold text-gray-900 mb-3 mt-6">Creencia a Transformar</h3>
              <p className="text-red-600 italic">"{module?.belief_to_transform}"</p>
            </div>
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-3">Resultados Esperados</h3>
              <p className="text-gray-700 leading-relaxed">{module?.expected_results}</p>
              
              {module?.recommended_book && (
                <>
                  <h3 className="text-lg font-semibold text-gray-900 mb-3 mt-6">Libro Recomendado</h3>
                  <p className="text-blue-600">{module.recommended_book}</p>
                </>
              )}
            </div>
          </div>
        </div>

        {/* Themes */}
        <div className="space-y-6">
          <h2 className="text-2xl font-bold text-gray-900">Temas del Módulo</h2>
          
          <div className="grid gap-6">
            {themes.map((theme, index) => (
              <div 
                key={theme.id}
                className={`theme-card bg-white rounded-lg shadow-md overflow-hidden transition-all duration-300 ${
                  theme.is_unlocked 
                    ? 'hover:shadow-lg cursor-pointer border-l-4 border-blue-500' 
                    : 'opacity-60 border-l-4 border-gray-300'
                }`}
                onClick={() => handleThemeClick(theme)}
              >
                <div className="p-6">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-4">
                      <div className="flex-shrink-0">
                        {theme.is_completed ? (
                          <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center">
                            <CheckCircleIcon className="w-6 h-6 text-green-600" />
                          </div>
                        ) : theme.is_unlocked ? (
                          <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                            <BookOpenIcon className="w-6 h-6 text-blue-600" />
                          </div>
                        ) : (
                          <div className="w-12 h-12 bg-gray-100 rounded-full flex items-center justify-center">
                            <LockClosedIcon className="w-6 h-6 text-gray-400" />
                          </div>
                        )}
                      </div>
                      <div className="flex-grow">
                        <h3 className="text-xl font-semibold text-gray-900">
                          Tema {index + 1}: {theme.title}
                        </h3>
                        <p className="text-gray-600 mt-1">{theme.content}</p>
                        <div className="flex items-center space-x-4 mt-3">
                          <div className="flex items-center text-sm text-gray-500">
                            <CardStackIcon className="w-4 h-4 mr-1" />
                            {theme.total_cards} contenidos
                          </div>
                          {theme.is_completed && (
                            <span className="text-green-600 text-sm font-medium">
                              ✓ Completado
                            </span>
                          )}
                        </div>
                      </div>
                    </div>
                    <div className="flex-shrink-0">
                      {theme.is_unlocked ? (
                        <div className="text-blue-600">
                          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                          </svg>
                        </div>
                      ) : (
                        <div className="text-gray-400">
                          <LockClosedIcon className="w-6 h-6" />
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Instructions */}
        <div className="mt-12 bg-blue-50 border border-blue-200 rounded-lg p-6">
          <h3 className="text-lg font-semibold text-blue-900 mb-3">
            📖 Cómo usar este módulo
          </h3>
          <div className="text-blue-800 space-y-2">
            <p>• <strong>Lee todo el contenido</strong> de cada tema usando el nuevo sistema de cards</p>
            <p>• <strong>Completa todos los ejercicios</strong> de reflexión personal</p>
            <p>• <strong>Tómate tu tiempo</strong> para procesar y aplicar los conceptos</p>
            <p>• <strong>Cada tema se desbloquea</strong> al completar el anterior</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ModuleDetail; 
