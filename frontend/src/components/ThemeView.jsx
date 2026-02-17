import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { config } from '../config';
import ExerciseTable from './ExerciseTable';
import { 
  DocumentTextIcon, 
  PencilSquareIcon, 
  CheckCircleIcon, 
  SparklesIcon,
  ChevronLeftIcon,
  ArrowRightIcon,
  LightBulbIcon,
  HeartIcon,
  CloudArrowUpIcon,
  CheckIcon,
  ExclamationCircleIcon
} from '@heroicons/react/24/outline';
import CardsView from './CardsView';

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
  const [showCards, setShowCards] = useState(false);
  const [savingStates, setSavingStates] = useState({});
  const debounceTimers = useRef({});

  // Scroll to top when exercise changes
  useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [currentExercise]);

  useEffect(() => {
    const fetchThemeData = async () => {
      try {
        // Get theme exercises
        const exercisesResponse = await fetch(`${config.apiUrl}/themes/${themeId}/exercises`, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        const exercisesData = await exercisesResponse.json();
        setExercises(exercisesData);
        
        // Get theme info from modules endpoint
        const modulesResponse = await fetch(`${config.apiUrl}/modules`, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        const modules = await modulesResponse.json();
        
        // Find the theme by checking all modules
        let foundTheme = null;
        let moduleId = null;
        for (const module of modules) {
          const themesResponse = await fetch(`${config.apiUrl}/modules/${module.id}/themes`, {
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
          setError('Tema no encontrado');
          return;
        }
        
        setTheme({...foundTheme, moduleId});
        
        // If theme is a resource, go directly to cards view
        if (foundTheme.theme_type === 'resource') {
          setShowContent(false);
          setShowCards(true);
        }

        // Initialize responses with existing user responses
        const initialResponses = {};
        exercisesData.forEach(exercise => {
          // Main exercise response
          initialResponses[exercise.id] = exercise.user_response || '';
          
          // Legacy sub-question responses
          if (exercise.sub_question_responses) {
            Object.entries(exercise.sub_question_responses).forEach(([index, response]) => {
              initialResponses[`${exercise.id}_${index}`] = response || '';
            });
          }
          
          // New exercise sections responses
          if (exercise.exercise_sections) {
            exercise.exercise_sections.forEach((section, sectionIndex) => {
              if (section.questions) {
                section.questions.forEach((question, questionIndex) => {
                  const responseKey = `${exercise.id}_section_${sectionIndex}_question_${questionIndex}`;
                  const subQuestionKey = `section_${sectionIndex}_question_${questionIndex}`;
                  // Load existing response if available
                  initialResponses[responseKey] = exercise.sub_question_responses?.[subQuestionKey] || '';
                });
              }
            });
          }
        });
        
        // Load responses from localStorage first (for unsaved changes)
        const localStorageKey = `exercise_responses_${themeId}`;
        const savedResponses = localStorage.getItem(localStorageKey);
        if (savedResponses) {
          try {
            const parsedResponses = JSON.parse(savedResponses);
            // Merge with server responses, preferring localStorage if more recent
            Object.keys(parsedResponses).forEach(key => {
              if (parsedResponses[key] && parsedResponses[key].trim && parsedResponses[key].trim()) {
                initialResponses[key] = parsedResponses[key];
              }
            });
          } catch (e) {
            console.error('Error parsing localStorage responses:', e);
          }
        }
        
        setResponses(initialResponses);

      } catch (err) {
        setError('Error al cargar el tema');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchThemeData();
  }, [themeId]);

  const handleResponseChange = (exerciseId, value) => {
    setResponses(prev => {
      const newResponses = {
        ...prev,
        [exerciseId]: value
      };
      // Save to localStorage immediately
      localStorage.setItem(`exercise_responses_${themeId}`, JSON.stringify(newResponses));
      return newResponses;
    });
    
    // Debounced auto-save to server
    if (debounceTimers.current[exerciseId]) {
      clearTimeout(debounceTimers.current[exerciseId]);
    }
    
    debounceTimers.current[exerciseId] = setTimeout(() => {
      autoSaveResponse(exerciseId, value);
    }, 2000); // Auto-save after 2 seconds of inactivity
  };

  const handleTableDataChange = (responseKey, data) => {
    setResponses(prev => {
      const newResponses = {
        ...prev,
        [responseKey]: data
      };
      // Save to localStorage immediately
      localStorage.setItem(`exercise_responses_${themeId}`, JSON.stringify(newResponses));
      return newResponses;
    });
    
    // Debounced auto-save to server
    if (debounceTimers.current[responseKey]) {
      clearTimeout(debounceTimers.current[responseKey]);
    }
    
    debounceTimers.current[responseKey] = setTimeout(() => {
      autoSaveResponse(responseKey, data);
    }, 2000);
  };

  const autoSaveResponse = async (responseKey, responseData) => {
    // Parse the response key to determine the exercise and question
    const keyParts = String(responseKey).split('_');
    
    if (keyParts.length === 1) {
      // Legacy main response (not used in current implementation)
      return;
    }
    
    // Find the exercise ID
    const exerciseId = parseInt(keyParts[0]);
    const exercise = exercises.find(ex => ex.id === exerciseId);
    
    if (!exercise) return;
    
    // Determine sub-question index
    let subQuestionIndex;
    if (keyParts.includes('section')) {
      // New format: exerciseId_section_X_question_Y
      const sectionIdx = keyParts[keyParts.indexOf('section') + 1];
      const questionIdx = keyParts[keyParts.indexOf('question') + 1];
      subQuestionIndex = `section_${sectionIdx}_question_${questionIdx}`;
    } else {
      // Legacy format: exerciseId_questionIndex
      subQuestionIndex = parseInt(keyParts[1]);
    }
    
    // Silently save in background
    try {
      const responseText = typeof responseData === 'object' ? JSON.stringify(responseData) : responseData;
      
      if (responseText && responseText.trim()) {
        await fetch(`${config.apiUrl}/submit-sub-question-response`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          },
          body: JSON.stringify({
            exercise_id: exerciseId,
            sub_question_index: subQuestionIndex,
            response_text: responseText
          })
        });
      }
    } catch (err) {
      console.error('Auto-save error:', err);
    }
  };

  const saveIndividualResponse = async (responseKey, responseData) => {
    setSavingStates(prev => ({ ...prev, [responseKey]: 'saving' }));
    
    try {
      // Parse the response key to determine the exercise and question
      const keyParts = String(responseKey).split('_');
      const exerciseId = parseInt(keyParts[0]);
      
      // Determine sub-question index
      let subQuestionIndex;
      if (keyParts.includes('section')) {
        const sectionIdx = keyParts[keyParts.indexOf('section') + 1];
        const questionIdx = keyParts[keyParts.indexOf('question') + 1];
        subQuestionIndex = `section_${sectionIdx}_question_${questionIdx}`;
      } else {
        subQuestionIndex = parseInt(keyParts[1]);
      }
      
      const responseText = typeof responseData === 'object' ? JSON.stringify(responseData) : responseData;
      
      if (!responseText || !responseText.trim()) {
        setSavingStates(prev => ({ ...prev, [responseKey]: 'error' }));
        setTimeout(() => {
          setSavingStates(prev => ({ ...prev, [responseKey]: null }));
        }, 2000);
        return;
      }
      
      await fetch(`${config.apiUrl}/submit-sub-question-response`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify({
          exercise_id: exerciseId,
          sub_question_index: subQuestionIndex,
          response_text: responseText
        })
      });
      
      setSavingStates(prev => ({ ...prev, [responseKey]: 'saved' }));
      setTimeout(() => {
        setSavingStates(prev => ({ ...prev, [responseKey]: null }));
      }, 2000);
    } catch (err) {
      console.error('Error saving response:', err);
      setSavingStates(prev => ({ ...prev, [responseKey]: 'error' }));
      setTimeout(() => {
        setSavingStates(prev => ({ ...prev, [responseKey]: null }));
      }, 3000);
    }
  };

  const areAllQuestionsAnswered = () => {
    const currentExerciseData = exercises[currentExercise];
    
    // Check legacy sub-questions
    if (currentExerciseData?.sub_questions && currentExerciseData.sub_questions.length > 0) {
      const allLegacyAnswered = currentExerciseData.sub_questions.every((_, questionIndex) => {
        const responseKey = `${currentExerciseData.id}_${questionIndex}`;
        return responses[responseKey]?.trim();
      });
      if (!allLegacyAnswered) return false;
    }
    
    // Check new exercise sections
    if (currentExerciseData?.exercise_sections && currentExerciseData.exercise_sections.length > 0) {
      for (let sectionIndex = 0; sectionIndex < currentExerciseData.exercise_sections.length; sectionIndex++) {
        const section = currentExerciseData.exercise_sections[sectionIndex];
        if (section.questions && section.questions.length > 0) {
          for (let questionIndex = 0; questionIndex < section.questions.length; questionIndex++) {
            const responseKey = `${currentExerciseData.id}_section_${sectionIndex}_question_${questionIndex}`;
            const response = responses[responseKey];
            
            // For table questions, check if it has data
            if (section.questions[questionIndex].type === 'table') {
              if (!response || (typeof response === 'object' && Object.keys(response).length === 0)) {
                return false;
              }
            } else {
              // For text questions, check if it's not empty
              if (!response || !response.trim()) {
                return false;
              }
            }
          }
        }
      }
    }
    
    return true;
  };

  const handleSubmitExercise = async () => {
    const exercise = exercises[currentExercise];
    
    if (!areAllQuestionsAnswered()) {
      alert('Por favor responde a todas las preguntas antes de continuar.');
      return;
    }

    setSubmitting(true);
    try {
      // Submit legacy sub-question responses
      if (exercise.sub_questions) {
        for (let questionIndex = 0; questionIndex < exercise.sub_questions.length; questionIndex++) {
          const responseKey = `${exercise.id}_${questionIndex}`;
          const responseText = responses[responseKey];
          
          if (responseText?.trim()) {
            await fetch(`${config.apiUrl}/submit-sub-question-response`, {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
              },
              body: JSON.stringify({
                exercise_id: exercise.id,
                sub_question_index: questionIndex,
                response_text: responseText
              })
            });
          }
        }
      }

      // Submit new exercise sections responses
      if (exercise.exercise_sections) {
        for (let sectionIndex = 0; sectionIndex < exercise.exercise_sections.length; sectionIndex++) {
          const section = exercise.exercise_sections[sectionIndex];
          if (section.questions) {
            for (let questionIndex = 0; questionIndex < section.questions.length; questionIndex++) {
              const responseKey = `${exercise.id}_section_${sectionIndex}_question_${questionIndex}`;
              const responseData = responses[responseKey];
              
              if (responseData) {
                const responseText = typeof responseData === 'object' ? JSON.stringify(responseData) : responseData;
                
                if (responseText && responseText.trim()) {
                  await fetch(`${config.apiUrl}/submit-sub-question-response`, {
                    method: 'POST',
                    headers: {
                      'Content-Type': 'application/json',
                      'Authorization': `Bearer ${localStorage.getItem('token')}`
                    },
                    body: JSON.stringify({
                      exercise_id: exercise.id,
                      sub_question_index: `section_${sectionIndex}_question_${questionIndex}`,
                      response_text: responseText
                    })
                  });
                }
              }
            }
          }
        }
      }
      
      if (currentExercise < exercises.length - 1) {
        setCurrentExercise(currentExercise + 1);
      } else {
        // Complete the theme
        await fetch(`${config.apiUrl}/complete-theme/${themeId}`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        
        // Clear localStorage after successful completion
        localStorage.removeItem(`exercise_responses_${themeId}`);
        
        setThemeCompleted(true);
      }
    } catch (err) {
      setError('Error al enviar');
      console.error(err);
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen gradient-elegant flex items-center justify-center">
        <div className="modern-card text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-4 border-sage border-t-transparent mx-auto mb-4"></div>
          <span className="text-sage font-inter text-lg">Cargando tema...</span>
        </div>
      </div>
    );
  }

  if (error || !theme) {
    return (
      <div className="max-w-4xl mx-auto px-6 py-12">
        <div className="modern-card bg-red-50 border-red-200 border-2">
          <p className="text-red-700 font-inter text-lg mb-4">{error || 'Thème non trouvé'}</p>
          <Link 
            to="/dashboard" 
            className="btn-sage font-inter inline-flex items-center"
          >
            <ChevronLeftIcon className="w-5 h-5 mr-2" />
            Volver al panel de control
          </Link>
        </div>
      </div>
    );
  }

  if (themeCompleted) {
    return (
      <div className="max-w-4xl mx-auto px-6 py-12">
        <div className="modern-card text-center gradient-elegant relative overflow-hidden">
          <div className="absolute top-0 right-0 opacity-10">
            <SparklesIcon className="w-32 h-32 text-sage" />
          </div>
          <div className="relative z-10">
            <SparklesIcon className="w-20 h-20 text-sage mx-auto mb-6" />
            <h1 className="font-inter text-4xl font-semibold text-black mb-4">
              ¡Felicidades!
            </h1>
            <p className="font-inter text-xl text-taupe-dark mb-6">
              Has completado el tema "{theme.title}"
            </p>
            <div className="glass-effect-sage rounded-2xl p-8 mb-8">
              <p className="font-inter text-sage-dark text-lg leading-relaxed">
                Tómate un momento para integrar lo que acabas de explorar. 
                Cada reflexión te acerca más a tu autenticidad.
              </p>
            </div>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                to={`/module/${theme.moduleId}`}
                className="btn-sage font-inter inline-flex items-center justify-center"
              >
                <ChevronLeftIcon className="w-5 h-5 mr-2" />
                Volver al módulo
              </Link>
              <Link
                to="/dashboard"
                className="btn-taupe font-inter inline-flex items-center justify-center"
              >
                Panel de Control
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }

  // Add cards view handling
  if (showCards) {
    return (
      <CardsView 
        themeId={parseInt(themeId)}
        themeName={theme.title}
        onBack={() => {
          // If it's a resource, go back to module instead of showing content page
          if (theme.theme_type === 'resource') {
            navigate(`/module/${theme.moduleId}`);
          } else {
            setShowCards(false);
            setShowContent(true);
          }
        }}
        onGoToExercises={() => {
          setShowContent(false);
          setShowCards(false);
        }}
      />
    );
  }

  if (showContent) {
    return (
      <div className="max-w-4xl mx-auto px-6 py-12">
        {/* Header élégant */}
        <div className="mb-12">
          <nav className="mb-8">
            <div className="flex items-center space-x-3 text-sm font-inter text-taupe">
              <Link to="/dashboard" className="hover:text-sage transition-elegant">Panel de Control</Link>
              <ChevronLeftIcon className="w-4 h-4" />
              <Link to={`/module/${theme.moduleId}`} className="hover:text-sage transition-elegant">Módulo</Link>
              <ChevronLeftIcon className="w-4 h-4" />
              <span className="text-black font-medium">{theme.title}</span>
            </div>
          </nav>

          <div className="modern-card gradient-elegant border-2 border-gray-200">
            <p className="font-inter text-sm font-medium text-taupe mb-1">Semana {theme.order_number}</p>
            <h1 className="font-inter text-4xl font-semibold text-black mb-4">
              {theme.title}
            </h1>
            <div className="flex items-center space-x-6 text-taupe font-inter">
              <div className="flex items-center space-x-2">
                <PencilSquareIcon className="w-5 h-5" />
                <span>{exercises.length} ejercicios</span>
              </div>
            </div>
          </div>
        </div>

        {/* Contenu du thème */}
        <div className="modern-card mb-12">
          <div className="flex items-center space-x-3 mb-6">
            <div className="p-3 bg-sage rounded-xl">
              <DocumentTextIcon className="w-8 h-8 text-white" />
            </div>
            <h2 className="font-inter text-2xl font-semibold text-black">
              Contenido del tema
            </h2>
          </div>
          <div className="prose prose-lg max-w-none">
            <div className="font-inter text-lg text-taupe-dark leading-relaxed whitespace-pre-line">
              {theme.content}
            </div>
          </div>
        </div>

        {/* Boutons de navigation modernes */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <button
            onClick={() => setShowCards(true)}
            className="modern-card hover:shadow-sage transition-elegant group text-left p-8 bg-gradient-to-br from-sage to-sage-dark text-white border-sage border-2"
          >
            <div className="flex items-center justify-between mb-4">
              <DocumentTextIcon className="w-12 h-12 opacity-90" />
              <ArrowRightIcon className="w-6 h-6 group-hover:translate-x-1 transition-transform" />
            </div>
            <h3 className="font-inter text-xl font-semibold mb-2">
              Contenido interactivo
            </h3>
            <p className="font-inter opacity-90 leading-relaxed">
              Explora el contenido con una navegación moderna e intuitiva
            </p>
          </button>
          
          <button
            onClick={() => setShowContent(false)}
            className="modern-card hover:shadow-elegant transition-elegant group text-left p-8 bg-gradient-to-br from-taupe to-taupe-dark text-white border-taupe border-2"
          >
            <div className="flex items-center justify-between mb-4">
              <PencilSquareIcon className="w-12 h-12 opacity-90" />
              <ArrowRightIcon className="w-6 h-6 group-hover:translate-x-1 transition-transform" />
            </div>
            <h3 className="font-inter text-xl font-semibold mb-2">
              Ejercicios prácticos
            </h3>
            <p className="font-inter opacity-90 leading-relaxed">
              Pon en práctica a través de ejercicios de reflexión
            </p>
          </button>
        </div>
      </div>
    );
  }

  const currentExerciseData = exercises[currentExercise];
  const progress = ((currentExercise + 1) / exercises.length) * 100;

  return (
    <div className="max-w-6xl mx-auto px-6 py-12">
      {/* Header exercices */}
      <div className="mb-12">
        <div className="modern-card">
          <div className="flex items-center justify-between mb-6">
            <button 
              onClick={() => {
                setShowContent(true);
                setShowCards(false);
              }}
              className="flex items-center text-sage hover:text-sage-dark transition-elegant group"
            >
              <ChevronLeftIcon className="w-6 h-6 mr-2 group-hover:-translate-x-1 transition-transform" />
              <span className="font-inter text-lg">Volver al contenido</span>
            </button>
            <div className="px-4 py-2 bg-sage-light rounded-full">
              <span className="font-inter text-white text-sm font-medium">{theme.title}</span>
            </div>
          </div>
          
          <div className="flex items-center space-x-6 mb-6">
            <div className="p-4 bg-taupe rounded-xl">
              <PencilSquareIcon className="w-10 h-10 text-white" />
            </div>
            <div>
              <h1 className="font-inter text-3xl font-semibold text-black mb-2">
                {currentExerciseData?.parent_title || currentExerciseData?.title}
              </h1>
              <p className="font-inter text-taupe text-lg">
                Ejercicio {currentExercise + 1} de {exercises.length}
              </p>
            </div>
          </div>

          {/* Barre de progression */}
          <div className="progress-modern">
            <div 
              className="progress-bar"
              style={{ width: `${progress}%` }}
            ></div>
          </div>
        </div>
      </div>

      {/* Contenu exercice */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Exercice principal */}
        <div className="lg:col-span-2">
          <div className="modern-card relative overflow-hidden">
            <div className="absolute top-0 right-0 opacity-5">
              <HeartIcon className="w-32 h-32 text-sage" />
            </div>
            
            <div className="relative z-10">
              <h2 className="font-inter text-2xl font-semibold text-black mb-6">
                {currentExerciseData?.title}
              </h2>

              {currentExerciseData?.instructions && (
                <div className="glass-effect-sage rounded-xl p-6 mb-8">
                  <span className="font-medium font-inter text-sage-dark block mb-2">Instrucciones:</span>
                  <div 
                    className="font-inter text-sage-dark leading-relaxed rich-content"
                    dangerouslySetInnerHTML={{ __html: currentExerciseData.instructions }}
                  />
                </div>
              )}
              
              <div className="space-y-8">
                {/* Legacy sub-questions */}
                {currentExerciseData?.sub_questions && currentExerciseData.sub_questions.length > 0 && (
                  <div className="space-y-6">
                    <h3 className="font-inter text-xl font-semibold text-black mb-4">Preguntas</h3>
                    {currentExerciseData.sub_questions.map((question, questionIndex) => {
                      const responseKey = `${currentExerciseData.id}_${questionIndex}`;
                      
                      return (
                        <div key={questionIndex} className="space-y-4">
                          <div className="glass-effect-sage rounded-xl p-4">
                            <div 
                              className="font-inter text-lg font-medium text-sage-dark rich-content"
                              dangerouslySetInnerHTML={{ __html: question }}
                            />
                          </div>
                          
                          <textarea
                            value={responses[responseKey] || ''}
                            onChange={(e) => handleResponseChange(responseKey, e.target.value)}
                            placeholder="Expresa tus pensamientos y sentimientos aquí... Tómate tu tiempo."
                            className="w-full h-40 p-6 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-sage focus:border-sage glass-effect resize-none font-inter text-base leading-relaxed text-black placeholder-taupe"
                          />
                        </div>
                      );
                    })}
                  </div>
                )}

                {/* New exercise sections */}
                {currentExerciseData?.exercise_sections && currentExerciseData.exercise_sections.length > 0 && (
                  <div className="space-y-8">
                    {currentExerciseData.exercise_sections.map((section, sectionIndex) => (
                      <div key={sectionIndex} className="bg-gradient-to-r from-sage-50 to-sage-100 rounded-xl border-2 border-sage-200 p-6">
                        <div className="mb-6">
                          <h3 className="font-inter text-xl font-bold text-sage-800 mb-3 flex items-center">
                            <span className="mr-2">📋</span>
                            {section.title}
                          </h3>
                          {section.instructions && (
                            <div className="bg-white/80 rounded-lg p-4 border border-sage-200 mb-4">
                              <span className="font-medium font-inter text-sage-900 block mb-2">Instrucciones:</span>
                              <div 
                                className="font-inter text-sage-900 leading-relaxed rich-content"
                                dangerouslySetInnerHTML={{ __html: section.instructions }}
                              />
                            </div>
                          )}
                        </div>

                        {section.questions && section.questions.length > 0 && (
                          <div className="space-y-6">
                            {section.questions.map((question, questionIndex) => {
                              const responseKey = `${currentExerciseData.id}_section_${sectionIndex}_question_${questionIndex}`;
                              const responseValue = responses[responseKey];
                              
                              return (
                                <div key={questionIndex} className="bg-white rounded-lg border border-sage-200 p-5">
                                  <div className="mb-4">
                                    <div className="flex items-start mb-3">
                                      <span className="bg-sage-100 text-sage-800 text-sm font-medium px-3 py-1 rounded-full mr-3 mt-1">
                                        Pregunta {questionIndex + 1}
                                      </span>
                                      <div 
                                        className="font-inter text-lg font-medium text-gray-800 flex-1 rich-content"
                                        dangerouslySetInnerHTML={{ __html: question.question }}
                                      />
                                    </div>
                                  </div>
                                  
                                  {/* Render different input types based on question type */}
                                  {question.type === 'table' && question.table_config ? (
                                    <div className="space-y-4">
                                      <ExerciseTable
                                        tableConfig={question.table_config}
                                        questionIndex={questionIndex}
                                        cardId={currentExerciseData.id}
                                        initialData={responseValue ? (() => {
                                          try {
                                            return typeof responseValue === 'string' ? JSON.parse(responseValue) : responseValue;
                                          } catch {
                                            return {};
                                          }
                                        })() : {}}
                                        onDataChange={(data) => handleTableDataChange(responseKey, data)}
                                        readOnly={false}
                                      />
                                    </div>
                                  ) : (
                                    <textarea
                                      value={typeof responseValue === 'string' ? responseValue : ''}
                                      onChange={(e) => handleResponseChange(responseKey, e.target.value)}
                                      placeholder="Expresa tus pensamientos y sentimientos aquí... Tómate tu tiempo."
                                      className="w-full h-40 p-6 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-green-500 focus:border-green-500 glass-effect resize-none font-inter text-base leading-relaxed text-black placeholder-taupe"
                                    />
                                  )}
                                </div>
                              );
                            })}
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                )}

                {/* Show message if no questions available */}
                {(!currentExerciseData?.sub_questions || currentExerciseData.sub_questions.length === 0) && 
                 (!currentExerciseData?.exercise_sections || currentExerciseData.exercise_sections.length === 0) && (
                  <div className="text-center py-8 text-gray-500">
                    <p>No hay preguntas disponibles para este ejercicio.</p>
                  </div>
                )}
                
                <div className="flex justify-between items-center">
                  <div className="flex items-center space-x-3 text-sm font-inter text-taupe">
                    <LightBulbIcon className="w-5 h-5" />
                    <span>Tómate el tiempo necesario para tu reflexión</span>
                  </div>
                  
                  <button
                    onClick={handleSubmitExercise}
                    disabled={submitting || !areAllQuestionsAnswered()}
                    className="px-8 py-4 gradient-sage text-white rounded-xl font-inter font-medium hover:shadow-sage focus:ring-2 focus:ring-sage focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-elegant"
                  >
                    {submitting ? (
                      <div className="flex items-center">
                        <div className="animate-spin rounded-full h-5 w-5 border-2 border-white border-t-transparent mr-3"></div>
                        Guardando...
                      </div>
                    ) : currentExercise === exercises.length - 1 ? (
                      'Guardar y finalizar tema'
                    ) : (
                      'Guardar respuesta y siguiente ejercicio'
                    )}
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Barre latérale */}
        <div className="space-y-6">
          {/* Navigation exercices */}
          <div className="modern-card">
            <h3 className="font-inter text-xl font-semibold text-black mb-6 flex items-center">
              <DocumentTextIcon className="w-6 h-6 mr-3 text-sage" />
              Ejercicios del tema
            </h3>
            <div className="space-y-3">
              {exercises.map((exercise, index) => (
                <div
                  key={exercise.id}
                  className={`p-4 rounded-xl transition-elegant ${
                    index === currentExercise
                      ? 'bg-sage text-white'
                      : index < currentExercise
                      ? 'bg-green-50 border border-green-200'
                      : 'bg-gray-50 border border-gray-200'
                  }`}
                >
                  <div className="flex items-center space-x-3">
                    <div className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold font-inter ${
                      index === currentExercise
                        ? 'bg-white text-sage'
                        : index < currentExercise
                        ? 'bg-green-500 text-white'
                        : 'bg-gray-300 text-gray-600'
                    }`}>
                      {index < currentExercise ? <CheckCircleIcon className="w-5 h-5" /> : index + 1}
                    </div>
                    <span className={`text-sm font-inter ${
                      index === currentExercise
                        ? 'text-white font-medium'
                        : index < currentExercise
                        ? 'text-green-800'
                        : 'text-gray-600'
                    }`}>
                      {exercise.title}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Carte inspiration */}
          <div className="modern-card gradient-elegant">
            <h3 className="font-inter text-xl font-semibold text-black mb-6 flex items-center">
              <SparklesIcon className="w-6 h-6 mr-3 text-taupe" />
              Inspiración
            </h3>
            <div className="space-y-4">
              <blockquote className="font-inter text-taupe-dark italic text-lg leading-relaxed">
                "La transformación personal comienza con la observación amorosa de uno mismo."
              </blockquote>
              <div className="flex justify-center space-x-3 text-3xl opacity-60">
                <HeartIcon className="w-8 h-8 text-sage" />
                <LightBulbIcon className="w-8 h-8 text-taupe" />
                <SparklesIcon className="w-8 h-8 text-sage" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ThemeView; 
