import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  ChevronLeft, 
  ChevronRight, 
  Pencil, 
  Check, 
  X,
  Target,
  BookOpen,
  Settings,
  FolderOpen,
  Sparkles,
  FileText,
  Play
} from 'lucide-react';
import {
  XMarkIcon
} from '@heroicons/react/24/outline';
import api from '../services/api';
import RichTextEditor from './RichTextEditor';

const CardsView = ({ themeId, themeName, onBack, onGoToExercises }) => {
  const navigate = useNavigate();

  // Decode JWT token to get user info
  const decodeToken = (token) => {
    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      return payload;
    } catch (error) {
      console.error('Error decoding token:', error);
      return null;
    }
  };

  // Check if current user is admin
  const userInfo = (() => {
    const token = localStorage.getItem('token');
    if (!token) return null;
    return decodeToken(token);
  })();

  const isAdmin = userInfo && userInfo.role === 'admin';
  const [cards, setCards] = useState([]);
  const [theme, setTheme] = useState(null);
  const [currentCardIndex, setCurrentCardIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingCard, setEditingCard] = useState(null);
  const [editTitle, setEditTitle] = useState('');
  const [editContent, setEditContent] = useState('');
  const [saving, setSaving] = useState(false);
  
  // Exercise-specific states
  const [exerciseResponses, setExerciseResponses] = useState({});
  const [submittingResponse, setSubmittingResponse] = useState(false);

  useEffect(() => {
    fetchThemeAndCards();
  }, [themeId]);

  const fetchThemeAndCards = async () => {
    try {
      setLoading(true);
      // Fetch theme info first to get module_id
      const themeResponse = await api.get(`/themes/${themeId}`);
      setTheme(themeResponse.data);
      
      // Then fetch cards
      const cardsResponse = await api.get(`/themes/${themeId}/cards`);
      setCards(cardsResponse.data);
      
      // Initialize exercise responses from cards data
      const responses = {};
      cardsResponse.data.forEach(card => {
        if (card.card_type === 'exercise' && card.user_responses) {
          responses[card.id] = card.user_responses;
        }
      });
      setExerciseResponses(responses);
      
      setCurrentCardIndex(0);
    } catch (err) {
      setError('Error loading theme and cards');
      console.error('Error fetching theme and cards:', err);
    } finally {
      setLoading(false);
    }
  };

  const goToPrevCard = () => {
    if (currentCardIndex > 0) {
      setCurrentCardIndex(currentCardIndex - 1);
      cancelEditing();
    }
  };

  const goToNextCard = () => {
    if (currentCardIndex < cards.length - 1) {
      setCurrentCardIndex(currentCardIndex + 1);
      cancelEditing();
    }
  };

  const goToCard = (index) => {
    setCurrentCardIndex(index);
    cancelEditing();
  };

  const startEditing = (card) => {
    setEditingCard(card.id);
    setEditTitle(card.title);
    setEditContent(card.content);
  };

  const cancelEditing = () => {
    setEditingCard(null);
    setEditTitle('');
    setEditContent('');
  };

  const saveCard = async (cardId) => {
    try {
      setSaving(true);
      
      // Garder le contenu tel quel pour préserver l'apparence
      const cleanContent = editContent;
      
      await api.put(`/cards/${cardId}`, {
        title: editTitle,
        content: cleanContent
      });
      
      setCards(cards.map(card => 
        card.id === cardId 
          ? { ...card, title: editTitle, content: cleanContent }
          : card
      ));
      
      setEditingCard(null);
      setEditTitle('');
      setEditContent('');
    } catch (err) {
      console.error('Error saving card:', err);
      alert('Error saving card');
    } finally {
      setSaving(false);
    }
  };

  const getCardIcon = (cardType) => {
    switch (cardType) {
      case 'intro': return Target;
      case 'theory': return BookOpen;
      case 'practical': return Settings;
      case 'resources': return FolderOpen;
      case 'conclusion': return Sparkles;
      case 'exercise': return FileText; // We can import a better icon later
      default: return FileText;
    }
  };

  const getCardColors = (cardType) => {
    switch (cardType) {
      case 'intro': return {
        bg: 'rgba(107, 116, 90, 0.1)',
        border: 'rgba(107, 116, 90, 0.3)',
        text: '#6b745a',
        accent: 'rgba(107, 116, 90, 0.2)'
      };
      case 'theory': return {
        bg: 'bg-sage',
        border: 'border-sage',
        text: 'text-white',
        accent: 'bg-sage-light'
      };
      case 'practical': return {
        bg: 'bg-taupe',
        border: 'border-taupe',
        text: 'text-white',
        accent: 'bg-taupe-light'
      };
      case 'resources': return {
        bg: 'bg-amber-50',
        border: 'border-amber-200',
        text: 'text-amber-800',
        accent: 'bg-amber-100'
      };
      case 'conclusion': return {
        bg: 'gradient-elegant',
        border: 'border-gray-200',
        text: 'text-gray-800',
        accent: 'bg-gray-100'
      };
      case 'exercise': return {
        bg: 'bg-orange-50',
        border: 'border-orange-200',
        text: 'text-orange-800',
        accent: 'bg-orange-100'
      };
      default: return {
        bg: 'bg-white',
        border: 'border-gray-200',
        text: 'text-gray-800',
        accent: 'bg-gray-100'
      };
    }
  };

  // Exercise response functions
  const handleResponseChange = (cardId, questionIndex, value) => {
    setExerciseResponses(prev => ({
      ...prev,
      [cardId]: {
        ...prev[cardId],
        [questionIndex]: value
      }
    }));
  };

  const submitExerciseResponse = async (cardId, questionIndex, responseText) => {
    try {
      setSubmittingResponse(true);
      
      await api.post(`/cards/${cardId}/responses`, {
        card_id: cardId,
        question_index: questionIndex,
        response_text: responseText
      });
      
      // Update local state
      setExerciseResponses(prev => ({
        ...prev,
        [cardId]: {
          ...prev[cardId],
          [questionIndex]: responseText
        }
      }));
      
    } catch (err) {
      console.error('Error submitting response:', err);
      alert('Error submitting response');
    } finally {
      setSubmittingResponse(false);
    }
  };

  const saveAllExerciseResponses = async (cardId) => {
    try {
      setSubmittingResponse(true);
      const cardResponses = exerciseResponses[cardId] || {};
      
      // Submit all responses for this card
      const promises = Object.entries(cardResponses).map(([questionIndex, responseText]) => {
        if (responseText && responseText.trim()) {
          return api.post(`/cards/${cardId}/responses`, {
            card_id: cardId,
            question_index: parseInt(questionIndex),
            response_text: responseText.trim()
          });
        }
      }).filter(Boolean);
      
      await Promise.all(promises);
      alert('Réponses sauvegardées avec succès !');
      
    } catch (err) {
      console.error('Error saving responses:', err);
      alert('Erreur lors de la sauvegarde');
    } finally {
      setSubmittingResponse(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen gradient-elegant flex items-center justify-center">
        <div className="modern-card text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-4 border-sage border-t-transparent mx-auto mb-4"></div>
          <p className="text-sage font-inter text-lg">Cargando contenido...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen gradient-elegant flex items-center justify-center">
        <div className="modern-card text-center">
          <XMarkIcon className="w-16 h-16 text-red-500 mx-auto mb-4" />
          <p className="text-red-600 mb-4 font-inter">{error}</p>
          <button 
            onClick={fetchCards}
            className="btn-sage font-inter"
          >
            Reintentar
          </button>
        </div>
      </div>
    );
  }

  if (cards.length === 0) {
    return (
      <div className="min-h-screen gradient-elegant flex items-center justify-center">
        <div className="modern-card text-center">
          <DocumentTextIcon className="w-16 h-16 text-taupe mx-auto mb-4" />
                      <p className="text-taupe-dark mb-4 font-inter text-lg">Ningún contenido disponible para este tema.</p>
            <button 
              onClick={onBack}
              className="btn-taupe font-inter"
            >
              Volver
            </button>
        </div>
      </div>
    );
  }

  const currentCard = cards[currentCardIndex];
  const cardColors = getCardColors(currentCard.card_type);
  const IconComponent = getCardIcon(currentCard.card_type);

  return (
    <div className="min-h-screen gradient-elegant">
      {/* Header moderne */}
      <div className="glass-effect border-b border-gray-200">
        <div className="max-w-5xl mx-auto px-6 py-8">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-6">
              <button
                onClick={onBack}
                className="flex items-center text-sage hover:text-sage-dark transition-elegant group"
              >
                <ChevronLeft className="w-6 h-6 mr-2 group-hover:-translate-x-1 transition-transform" />
                <span className="font-inter text-lg">Volver</span>
              </button>
              <div>
                <h1 className="font-inter text-3xl font-semibold text-black mb-2">{themeName}</h1>
                <p className="font-inter text-taupe text-lg">
                  Contenido {currentCardIndex + 1} de {cards.length}
                </p>
              </div>
            </div>
            <div className="text-right">
              {theme && (
                <button
                  onClick={() => onGoToExercises()}
                  className="flex items-center space-x-3 px-6 py-3 gradient-sage hover:shadow-sage text-white rounded-xl font-medium transition-elegant transform hover:scale-105"
                >
                  <Play className="w-5 h-5" />
                  <span className="font-inter">Ir a ejercicios</span>
                </button>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Barre de progression moderne */}
      <div className="bg-white border-b border-gray-100">
        <div className="max-w-5xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between mb-3">
            <span className="font-inter text-sm font-medium text-taupe-dark">Progreso</span>
            <span className="font-inter text-sm text-taupe">
              {Math.round(((currentCardIndex + 1) / cards.length) * 100)}% completado
            </span>
          </div>
          <div className="progress-modern">
            <div 
              className="progress-bar" 
              style={{ width: `${((currentCardIndex + 1) / cards.length) * 100}%` }}
            ></div>
          </div>
        </div>
      </div>

      {/* Navigation par points */}
      <div className="bg-white border-b border-gray-100">
        <div className="max-w-5xl mx-auto px-6 py-6">
          <div className="flex justify-center items-center space-x-3">
            {cards.map((card, index) => {
              const isActive = index === currentCardIndex;
              const cardIcon = getCardIcon(card.card_type);
              return (
                <button
                  key={card.id}
                  onClick={() => goToCard(index)}
                  className={`nav-dot relative group ${isActive ? 'active' : ''}`}
                  title={card.title}
                >
                  {isActive && (
                    <div className="absolute -top-8 left-1/2 transform -translate-x-1/2 bg-black text-white px-2 py-1 rounded text-xs font-inter whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity">
                      {card.title}
                    </div>
                  )}
                </button>
              );
            })}
          </div>
        </div>
      </div>

      {/* Carte actuelle */}
      <div className="max-w-4xl mx-auto px-6 py-12">
        <div 
          className="modern-card border-2 relative overflow-hidden"
          style={{
            backgroundColor: cardColors.bg,
            borderColor: cardColors.border
          }}
        >
          {/* En-tête de carte */}
          <div className="flex items-center justify-between mb-8">
            <div className="flex items-center space-x-4">
              <div 
                className="p-3 rounded-xl"
                style={{ backgroundColor: cardColors.accent }}
              >
                <IconComponent 
                  className="w-8 h-8" 
                  style={{ color: cardColors.text }}
                />
              </div>
              <div>
                {editingCard === currentCard.id ? (
                  <input
                    type="text"
                    value={editTitle}
                    onChange={(e) => setEditTitle(e.target.value)}
                    className="font-inter text-2xl font-semibold bg-white border-2 border-sage px-4 py-2 rounded-lg focus:outline-none focus:border-sage-dark"
                    autoFocus
                  />
                ) : (
                  <h3 
                    className="font-inter text-2xl font-semibold mb-1"
                    style={{ color: cardColors.text }}
                  >
                    {currentCard.title}
                  </h3>
                )}
                <p 
                  className="font-inter text-sm opacity-75 capitalize"
                  style={{ color: cardColors.text }}
                >
                  {currentCard.card_type.replace('_', ' ')} • {currentCardIndex + 1} / {cards.length}
                </p>
              </div>
            </div>
            
            <div className="flex items-center space-x-2">
              {editingCard !== currentCard.id && isAdmin && (
                <button
                  onClick={() => startEditing(currentCard)}
                  className="p-3 text-taupe hover:bg-taupe hover:text-white rounded-xl transition-elegant"
                  title="Editar contenido"
                >
                  <Pencil className="w-5 h-5" />
                </button>
              )}
            </div>
          </div>

          {/* Contenu de la carte */}
          <div className="space-y-6">
            {editingCard === currentCard.id ? (
              <RichTextEditor
                value={editContent}
                onChange={setEditContent}
                placeholder="Écrivez le contenu de cette section..."
                height={400}
                onSave={() => saveCard(currentCard.id)}
                onCancel={cancelEditing}
                saving={saving}
              />
            ) : (
              <div 
                className="rich-content max-w-none font-inter text-lg"
                dangerouslySetInnerHTML={{ __html: currentCard.content }}
              />
            )}
          </div>

          {/* Exercise Section */}
          {currentCard.card_type === 'exercise' && currentCard.exercise_questions && (
            <div className="mt-8 border-t pt-8">
              <div className="space-y-6">
                {/* Exercise Instructions */}
                {currentCard.exercise_instructions && (
                  <div className="glass-effect-sage rounded-xl p-6">
                    <h4 className="font-inter text-lg font-semibold text-sage-dark mb-3 flex items-center">
                      <span className="mr-2">💡</span>
                      Instrucciones
                    </h4>
                    <p className="font-inter text-sage-dark leading-relaxed">
                      {currentCard.exercise_instructions}
                    </p>
                  </div>
                )}

                {/* Exercise Questions */}
                <div className="space-y-4">
                  <h4 className="font-inter text-xl font-semibold text-orange-800 flex items-center">
                    <span className="mr-2">📝</span>
                    Preguntas del ejercicio
                  </h4>
                  
                  {currentCard.exercise_questions.map((question, index) => {
                    const responseValue = exerciseResponses[currentCard.id]?.[index] || '';
                    
                    return (
                      <div key={index} className="bg-white rounded-xl border-2 border-orange-200 p-6">
                        <div className="mb-4">
                          <label className="block font-inter text-sm font-medium text-orange-800 mb-2">
                            <span className="inline-flex items-center justify-center w-6 h-6 bg-orange-500 text-white rounded-full text-xs font-bold mr-2">
                              {index + 1}
                            </span>
                            {question}
                          </label>
                        </div>
                        
                        <textarea
                          value={responseValue}
                          onChange={(e) => handleResponseChange(currentCard.id, index, e.target.value)}
                          className="w-full border border-orange-200 rounded-lg px-4 py-3 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 font-inter min-h-[120px] resize-vertical"
                          placeholder="Escribe tu respuesta aquí..."
                        />
                        
                        {/* Individual save button */}
                        <div className="mt-3 flex justify-end">
                          <button
                            onClick={() => submitExerciseResponse(currentCard.id, index, responseValue)}
                            disabled={submittingResponse || !responseValue.trim()}
                            className={`px-4 py-2 rounded-lg font-inter text-sm font-medium transition-elegant ${
                              responseValue.trim() 
                                ? 'bg-orange-500 hover:bg-orange-600 text-white'
                                : 'bg-gray-200 text-gray-400 cursor-not-allowed'
                            }`}
                          >
                            {submittingResponse ? 'Guardando...' : 'Guardar respuesta'}
                          </button>
                        </div>
                      </div>
                    );
                  })}
                  
                  {/* Save all responses button */}
                  <div className="mt-6 text-center">
                    <button
                      onClick={() => saveAllExerciseResponses(currentCard.id)}
                      disabled={submittingResponse}
                      className="bg-orange-600 hover:bg-orange-700 text-white px-8 py-3 rounded-xl font-inter font-medium transition-elegant disabled:opacity-50"
                    >
                      {submittingResponse ? 'Guardando...' : 'Guardar todas las respuestas'}
                    </button>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Navigation flèches */}
        <div className="flex justify-between items-center mt-12">
          <button
            onClick={goToPrevCard}
            disabled={currentCardIndex === 0}
            className={`flex items-center px-8 py-4 rounded-xl font-inter font-medium transition-elegant ${
              currentCardIndex === 0
                ? 'bg-gray-200 text-gray-400 cursor-not-allowed'
                : 'glass-effect hover:shadow-elegant text-sage hover:text-sage-dark'
            }`}
          >
            <ChevronLeft className="w-6 h-6 mr-3" />
            Anterior
          </button>

          <div className="text-center px-6">
            <p className="font-inter text-sm text-taupe mb-2">Navegación</p>
            <p className="font-inter text-2xl font-semibold text-black">
              {currentCardIndex + 1} / {cards.length}
            </p>
          </div>

          <button
            onClick={goToNextCard}
            disabled={currentCardIndex === cards.length - 1}
            className={`flex items-center px-8 py-4 rounded-xl font-inter font-medium transition-elegant ${
              currentCardIndex === cards.length - 1
                ? 'bg-gray-200 text-gray-400 cursor-not-allowed'
                : 'gradient-sage text-white hover:shadow-sage'
            }`}
          >
            Siguiente
            <ChevronRight className="w-6 h-6 ml-3" />
          </button>
        </div>

        {/* Message de fin élégant */}
        {currentCardIndex === cards.length - 1 && (
          <div className="mt-16 text-center">
            <div className="modern-card bg-gradient-to-r from-sage to-taupe text-white">
              <Sparkles className="w-16 h-16 mx-auto mb-6 opacity-90" />
              <h3 className="font-inter text-2xl font-semibold mb-4">
                ¡Felicidades!
              </h3>
              <p className="font-inter text-lg mb-8 opacity-90 leading-relaxed">
                Has terminado la exploración de este contenido.<br />
                Continúa tu recorrido con los ejercicios prácticos.
              </p>
              <button
                onClick={onBack}
                className="bg-white text-sage px-10 py-4 rounded-xl font-inter font-medium hover:shadow-elegant transition-elegant"
              >
                Continuar con ejercicios
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default CardsView; 
