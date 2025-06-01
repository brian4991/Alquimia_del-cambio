import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';

const ThemeView = () => {
  const { themeId } = useParams();
  const navigate = useNavigate();
  const [theme, setTheme] = useState(null);
  const [exercises, setExercises] = useState([]);
  const [currentExercise, setCurrentExercise] = useState(0);
  const [responses, setResponses] = useState({});
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');
  const [themeCompleted, setThemeCompleted] = useState(false);
  const [showContent, setShowContent] = useState(true);

  useEffect(() => {
    const fetchThemeData = async () => {
      try {
        // Get theme exercises
        const exercisesResponse = await fetch(`http://localhost:8000/themes/${themeId}/exercises`, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        const exercisesData = await exercisesResponse.json();
        setExercises(exercisesData);
        
        // Get theme info from modules endpoint
        const modulesResponse = await fetch('http://localhost:8000/modules', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        const modules = await modulesResponse.json();
        
        // Find the theme by checking all modules
        let foundTheme = null;
        let moduleId = null;
        for (const module of modules) {
          const themesResponse = await fetch(`http://localhost:8000/modules/${module.id}/themes`, {
            headers: {
              'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
          });
          const themes = await themesResponse.json();
          foundTheme = themes.find(t => t.id === parseInt(themeId));
          if (foundTheme) {
            moduleId = module.id;
            break;
          }
        }
        
        if (!foundTheme) {
          setError('Tema non trouvé');
          return;
        }
        
        setTheme({...foundTheme, moduleId});

        // Initialize responses with existing user responses
        const initialResponses = {};
        exercisesData.forEach(exercise => {
          initialResponses[exercise.id] = exercise.user_response || '';
        });
        setResponses(initialResponses);

      } catch (err) {
        setError('Erreur lors du chargement du thème');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchThemeData();
  }, [themeId]);

  const handleResponseChange = (exerciseId, value) => {
    setResponses(prev => ({
      ...prev,
      [exerciseId]: value
    }));
  };

  const handleSubmitExercise = async () => {
    const exercise = exercises[currentExercise];
    const response = responses[exercise.id];
    
    if (!response.trim()) {
      alert('Veuillez répondre à l\'exercice avant de continuer.');
      return;
    }

    setSubmitting(true);
    try {
      await fetch('http://localhost:8000/submit-response', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify({
          exercise_id: exercise.id,
          response_text: response
        })
      });
      
      if (currentExercise < exercises.length - 1) {
        setCurrentExercise(currentExercise + 1);
      } else {
        // Complete the theme
        await fetch(`http://localhost:8000/complete-theme/${themeId}`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        setThemeCompleted(true);
      }
    } catch (err) {
      setError('Erreur lors de la soumission');
      console.error(err);
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="flex items-center space-x-3">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-500"></div>
          <span className="text-sage-600">Chargement du thème...</span>
        </div>
      </div>
    );
  }

  if (error || !theme) {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="bg-red-50 border border-red-200 rounded-lg p-4">
          <p className="text-red-700">{error || 'Thème non trouvé'}</p>
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

  if (themeCompleted) {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl p-8 border border-sage-200 text-center relative overflow-hidden">
          <div className="absolute top-0 right-0 opacity-10">
            <div className="text-8xl">🎉</div>
          </div>
          <div className="relative z-10">
            <div className="text-6xl mb-6">✨</div>
            <h1 className="text-3xl font-serif font-bold text-sage-800 mb-4">
              ¡Felicidades! 🌟
            </h1>
            <p className="text-lg text-sage-600 mb-6">
              Has completado el tema "{theme.title}"
            </p>
            <div className="bg-gradient-nature rounded-2xl p-6 mb-8">
              <p className="text-sage-700">
                Tómate un momento para integrar lo que acabas de explorar. 
                Cada reflexión te acerca más a tu autenticidad.
              </p>
            </div>
            <div className="space-y-4">
              <Link
                to={`/module/${theme.moduleId}`}
                className="inline-block bg-gradient-to-r from-primary-500 to-primary-600 text-white px-8 py-3 rounded-lg font-medium hover:from-primary-600 hover:to-primary-700 transition-colors shadow-lg mr-4"
              >
                Volver al módulo
              </Link>
              <Link
                to="/dashboard"
                className="inline-block bg-sage-100 text-sage-700 px-8 py-3 rounded-lg font-medium hover:bg-sage-200 transition-colors"
              >
                Ir al panel principal
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (showContent) {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8">
          <nav className="mb-6">
            <div className="flex items-center space-x-2 text-sm text-sage-600">
              <Link to="/dashboard" className="hover:text-primary-600 transition-colors">Panel</Link>
              <span>›</span>
              <Link to={`/module/${theme.moduleId}`} className="hover:text-primary-600 transition-colors">Módulo</Link>
              <span>›</span>
              <span className="text-sage-800 font-medium">{theme.title}</span>
            </div>
          </nav>

          <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-8 border border-sage-200">
            <h1 className="text-3xl font-serif font-bold text-sage-800 mb-4">
              {theme.title}
            </h1>
            <p className="text-sage-600 mb-6">
              {exercises.length} ejercicios • Tema {theme.order_number}
            </p>
          </div>
        </div>

        {/* Theme Content */}
        <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-8 border border-sage-200 mb-8">
          <h2 className="text-2xl font-serif font-bold text-sage-800 mb-6">
            Contenido del Tema
          </h2>
          <div className="prose prose-sage max-w-none">
            <div className="text-sage-700 leading-relaxed whitespace-pre-line">
              {theme.content}
            </div>
          </div>
        </div>

        {/* Start Exercises Button */}
        <div className="text-center">
          <button
            onClick={() => setShowContent(false)}
            className="bg-gradient-to-r from-primary-500 to-primary-600 text-white px-8 py-4 rounded-lg font-medium hover:from-primary-600 hover:to-primary-700 transition-colors shadow-lg text-lg"
          >
            Comenzar ejercicios
          </button>
        </div>
      </div>
    );
  }

  const currentExerciseData = exercises[currentExercise];
  const progress = ((currentExercise + 1) / exercises.length) * 100;

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="mb-8">
        <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-6 border border-sage-200">
          <div className="flex items-center justify-between mb-4">
            <button 
              onClick={() => setShowContent(true)}
              className="flex items-center text-sage-600 hover:text-primary-600 transition-colors"
            >
              <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
              Volver al contenido
            </button>
            <span className="bg-sage-100 text-sage-700 text-sm px-3 py-1 rounded-full">
              {theme.title}
            </span>
          </div>
          
          <div className="flex items-center space-x-4 mb-4">
            <div className="text-3xl">📝</div>
            <div>
              <h1 className="text-2xl font-serif font-bold text-sage-800">
                {currentExerciseData?.title}
              </h1>
              <p className="text-sage-600">
                Ejercicio {currentExercise + 1} de {exercises.length}
              </p>
            </div>
          </div>

          {/* Progress Bar */}
          <div className="w-full bg-sage-200 rounded-full h-2">
            <div 
              className="h-2 bg-gradient-to-r from-primary-400 to-primary-600 rounded-full transition-all duration-500 ease-out"
              style={{ width: `${progress}%` }}
            ></div>
          </div>
        </div>
      </div>

      {/* Exercise Content */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Main Exercise */}
        <div className="lg:col-span-2">
          <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-8 border border-sage-200 relative overflow-hidden">
            <div className="absolute top-0 right-0 opacity-5">
              <div className="text-7xl">🌸</div>
            </div>
            
            <div className="relative z-10">
              <h2 className="text-xl font-serif font-bold text-sage-800 mb-4">
                {currentExerciseData?.question}
              </h2>

              {currentExerciseData?.instructions && (
                <div className="bg-gradient-nature rounded-lg p-4 mb-6">
                  <p className="text-sage-700 text-sm">
                    <span className="font-medium">Instrucciones:</span> {currentExerciseData.instructions}
                  </p>
                </div>
              )}
              
              <div className="space-y-6">
                <textarea
                  value={responses[currentExerciseData?.id] || ''}
                  onChange={(e) => handleResponseChange(currentExerciseData.id, e.target.value)}
                  placeholder="Expresa tus pensamientos y sentimientos aquí... Tómate tu tiempo, deja que tus palabras fluyan naturalmente."
                  className="w-full h-48 p-4 border border-sage-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-primary-500 bg-white/80 backdrop-blur-sm resize-none text-sage-800 placeholder-sage-400"
                />
                
                <div className="flex justify-between items-center">
                  <div className="flex items-center space-x-2 text-sm text-sage-500">
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <span>Tómate el tiempo necesario para tu reflexión</span>
                  </div>
                  
                  <button
                    onClick={handleSubmitExercise}
                    disabled={submitting || !responses[currentExerciseData?.id]?.trim()}
                    className="px-6 py-3 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-lg font-medium hover:from-primary-600 hover:to-primary-700 focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 shadow-lg"
                  >
                    {submitting ? (
                      <div className="flex items-center">
                        <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                        </svg>
                        Enviando...
                      </div>
                    ) : currentExercise === exercises.length - 1 ? (
                      'Finalizar tema'
                    ) : (
                      'Siguiente ejercicio'
                    )}
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          {/* Exercise Navigation */}
          <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-6 border border-sage-200">
            <h3 className="text-lg font-semibold text-sage-800 mb-4 flex items-center">
              <span className="mr-2">📋</span>
              Ejercicios del tema
            </h3>
            <div className="space-y-2">
              {exercises.map((exercise, index) => (
                <div
                  key={exercise.id}
                  className={`p-3 rounded-lg transition-colors ${
                    index === currentExercise
                      ? 'bg-primary-100 border border-primary-300'
                      : index < currentExercise
                      ? 'bg-green-50 border border-green-200'
                      : 'bg-sage-50 border border-sage-200'
                  }`}
                >
                  <div className="flex items-center space-x-3">
                    <div className={`w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold ${
                      index === currentExercise
                        ? 'bg-primary-500 text-white'
                        : index < currentExercise
                        ? 'bg-green-500 text-white'
                        : 'bg-sage-300 text-sage-600'
                    }`}>
                      {index < currentExercise ? '✓' : index + 1}
                    </div>
                    <span className={`text-sm ${
                      index === currentExercise
                        ? 'text-primary-800 font-medium'
                        : index < currentExercise
                        ? 'text-green-800'
                        : 'text-sage-600'
                    }`}>
                      {exercise.title}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Motivation Card */}
          <div className="bg-gradient-calm rounded-2xl shadow-xl p-6 border border-sage-200">
            <h3 className="text-lg font-semibold text-sage-800 mb-4 flex items-center">
              <span className="mr-2">💫</span>
              Inspiración
            </h3>
            <div className="space-y-4">
              <blockquote className="text-sage-700 italic">
                "La transformación personal comienza con la observación amorosa de uno mismo."
              </blockquote>
              <div className="flex justify-center space-x-2 text-2xl">
                <span>🌱</span>
                <span>🦋</span>
                <span>✨</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ThemeView; 