import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { getStepExercises, submitResponse, completeStep } from '../services/api';

const StepView = () => {
  const { stepId } = useParams();
  const navigate = useNavigate();
  const [exercises, setExercises] = useState([]);
  const [currentExercise, setCurrentExercise] = useState(0);
  const [responses, setResponses] = useState({});
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');
  const [stepCompleted, setStepCompleted] = useState(false);

  useEffect(() => {
    const fetchExercises = async () => {
      try {
        const exercisesData = await getStepExercises(stepId);
        setExercises(exercisesData);
        
        // Initialize responses
        const initialResponses = {};
        exercisesData.forEach(exercise => {
          initialResponses[exercise.id] = '';
        });
        setResponses(initialResponses);
      } catch (err) {
        setError('Erreur lors du chargement des exercices');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchExercises();
  }, [stepId]);

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
      await submitResponse(exercise.id, response);
      
      if (currentExercise < exercises.length - 1) {
        setCurrentExercise(currentExercise + 1);
      } else {
        // Complete the step
        await completeStep(stepId);
        setStepCompleted(true);
      }
    } catch (err) {
      setError('Erreur lors de la soumission');
      console.error(err);
    } finally {
      setSubmitting(false);
    }
  };

  const getStepInfo = (stepId) => {
    const stepMap = {
      1: { title: "El Mapa de tus Emociones - Session 1", module: "Módulo 1", emoji: "🗺️", color: "from-primary-400 to-primary-600" },
      2: { title: "El Mapa de tus Emociones - Session 2", module: "Módulo 1", emoji: "❤️", color: "from-primary-400 to-primary-600" },
      3: { title: "Celebra tu Ser - Session 1", module: "Módulo 2", emoji: "🎉", color: "from-secondary-400 to-secondary-600" },
      4: { title: "Celebra tu Ser - Session 2", module: "Módulo 2", emoji: "✨", color: "from-secondary-400 to-secondary-600" },
      5: { title: "El Arte de Amar - Session 1", module: "Módulo 3", emoji: "💖", color: "from-lavender-400 to-lavender-600" },
      6: { title: "El Arte de Amar - Session 2", module: "Módulo 3", emoji: "🌹", color: "from-lavender-400 to-lavender-600" },
      7: { title: "De la expectativa a la realidad - Session 1", module: "Módulo 4", emoji: "🎭", color: "from-sage-400 to-sage-600" },
      8: { title: "De la expectativa a la realidad - Session 2", module: "Módulo 4", emoji: "🌟", color: "from-sage-400 to-sage-600" },
      9: { title: "Libertad en Acción - Session 1", module: "Módulo 5", emoji: "🕊️", color: "from-cream-400 to-cream-600" },
    };
    return stepMap[parseInt(stepId)] || { title: "Session", module: "Module", emoji: "📚", color: "from-gray-400 to-gray-600" };
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="flex items-center space-x-3">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-500"></div>
          <span className="text-sage-600">Chargement de votre session...</span>
        </div>
      </div>
    );
  }

  if (error || exercises.length === 0) {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="bg-red-50 border border-red-200 rounded-lg p-4">
          <p className="text-red-700">{error || 'Aucun exercice trouvé pour cette session.'}</p>
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

  if (stepCompleted) {
    const stepInfo = getStepInfo(stepId);
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl p-8 border border-sage-200 text-center relative overflow-hidden">
          <div className="absolute top-0 right-0 opacity-10">
            <div className="text-8xl">🎉</div>
          </div>
          <div className="relative z-10">
            <div className="text-6xl mb-6">{stepInfo.emoji}</div>
            <h1 className="text-3xl font-inter font-bold text-sage-800 mb-4">
              Félicitations ! 🌟
            </h1>
            <p className="text-lg text-sage-600 mb-6">
              Vous avez terminé la session "{stepInfo.title}"
            </p>
            <div className="bg-gradient-nature rounded-2xl p-6 mb-8">
              <p className="text-sage-700">
                Prenez un moment pour intégrer ce que vous venez d'explorer. 
                Chaque réflexion vous rapproche de votre authenticité.
              </p>
            </div>
            <div className="space-y-4">
              <Link
                to="/dashboard"
                className="inline-block bg-gradient-to-r from-primary-500 to-primary-600 text-white px-8 py-3 rounded-lg font-medium hover:from-primary-600 hover:to-primary-700 transition-colors shadow-lg"
              >
                Retourner au tableau de bord
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }

  const currentExerciseData = exercises[currentExercise];
  const stepInfo = getStepInfo(stepId);
  const progress = ((currentExercise + 1) / exercises.length) * 100;

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="mb-8">
        <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-6 border border-sage-200">
          <div className="flex items-center justify-between mb-4">
            <Link 
              to="/dashboard" 
              className="flex items-center text-sage-600 hover:text-primary-600 transition-colors"
            >
              <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
              Retour au tableau de bord
            </Link>
            <span className="bg-sage-100 text-sage-700 text-sm px-3 py-1 rounded-full">
              {stepInfo.module}
            </span>
          </div>
          
          <div className="flex items-center space-x-4 mb-4">
            <div className="text-3xl">{stepInfo.emoji}</div>
            <div>
              <h1 className="text-2xl font-inter font-bold text-sage-800">
                {stepInfo.title}
              </h1>
              <p className="text-sage-600">
                Exercice {currentExercise + 1} sur {exercises.length}
              </p>
            </div>
          </div>

          {/* Progress Bar */}
          <div className="w-full bg-sage-200 rounded-full h-2">
            <div 
              className={`h-2 bg-gradient-to-r ${stepInfo.color} rounded-full transition-all duration-500 ease-out`}
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
              <h2 className="text-xl font-inter font-bold text-sage-800 mb-6">
                {currentExerciseData.question}
              </h2>
              
              <div className="space-y-6">
                <textarea
                  value={responses[currentExerciseData.id] || ''}
                  onChange={(e) => handleResponseChange(currentExerciseData.id, e.target.value)}
                  placeholder="Exprimez vos pensées et ressentis ici... Prenez votre temps, laissez vos mots couler naturellement."
                  className="w-full h-48 p-4 border border-sage-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-primary-500 bg-white/80 backdrop-blur-sm resize-none text-sage-800 placeholder-sage-400"
                />
                
                <div className="flex justify-between items-center">
                  <div className="flex items-center space-x-2 text-sm text-sage-500">
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <span>Prenez le temps nécessaire pour votre réflexion</span>
                  </div>
                  
                  <button
                    onClick={handleSubmitExercise}
                    disabled={submitting || !responses[currentExerciseData.id]?.trim()}
                    className="px-6 py-3 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-lg font-medium hover:from-primary-600 hover:to-primary-700 focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 shadow-lg"
                  >
                    {submitting ? (
                      <div className="flex items-center">
                        <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                        </svg>
                        Envoi...
                      </div>
                    ) : currentExercise === exercises.length - 1 ? (
                      'Terminer la session'
                    ) : (
                      'Exercice suivant'
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
              Exercices de la session
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
                      Exercice {index + 1}
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
              Inspiration
            </h3>
            <div className="space-y-4">
              <blockquote className="text-sage-700 italic">
                "La transformation personnelle commence par l'observation bienveillante de soi-même."
              </blockquote>
              <div className="flex justify-center space-x-2 text-2xl">
                <span>🌱</span>
                <span>🦋</span>
                <span>✨</span>
              </div>
            </div>
          </div>

          {/* Tips Card */}
          <div className="bg-gradient-nature rounded-2xl shadow-xl p-6 border border-sage-200">
            <h3 className="text-lg font-semibold text-sage-800 mb-4 flex items-center">
              <span className="mr-2">💡</span>
              Conseils
            </h3>
            <ul className="space-y-2 text-sm text-sage-700">
              <li className="flex items-start">
                <span className="mr-2">•</span>
                Prenez votre temps pour réfléchir
              </li>
              <li className="flex items-start">
                <span className="mr-2">•</span>
                Soyez authentique dans vos réponses
              </li>
              <li className="flex items-start">
                <span className="mr-2">•</span>
                Il n'y a pas de "bonne" ou "mauvaise" réponse
              </li>
              <li className="flex items-start">
                <span className="mr-2">•</span>
                Écoutez votre intuition
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StepView; 
