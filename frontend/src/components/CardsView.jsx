import React, { useState, useEffect } from 'react';
import { 
  ChevronLeftIcon, 
  ChevronRightIcon, 
  PencilIcon, 
  CheckIcon, 
  XMarkIcon,
  BookOpenIcon,
  LightBulbIcon,
  WrenchScrewdriverIcon,
  DocumentTextIcon,
  SparklesIcon,
  AcademicCapIcon
} from '@heroicons/react/24/outline';
import api from '../services/api';

const CardsView = ({ themeId, themeName, onBack }) => {
  const [cards, setCards] = useState([]);
  const [currentCardIndex, setCurrentCardIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingCard, setEditingCard] = useState(null);
  const [editTitle, setEditTitle] = useState('');
  const [editContent, setEditContent] = useState('');
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    fetchCards();
  }, [themeId]);

  const fetchCards = async () => {
    try {
      setLoading(true);
      const response = await api.get(`/themes/${themeId}/cards`);
      setCards(response.data);
      setCurrentCardIndex(0);
    } catch (err) {
      setError('Error loading cards');
      console.error('Error fetching cards:', err);
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
      await api.put(`/cards/${cardId}`, {
        title: editTitle,
        content: editContent
      });
      
      setCards(cards.map(card => 
        card.id === cardId 
          ? { ...card, title: editTitle, content: editContent }
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
      case 'intro': return BookOpenIcon;
      case 'theory': return LightBulbIcon;
      case 'practical': return WrenchScrewdriverIcon;
      case 'resources': return DocumentTextIcon;
      case 'conclusion': return SparklesIcon;
      default: return AcademicCapIcon;
    }
  };

  const getCardColors = (cardType) => {
    switch (cardType) {
      case 'intro': return {
        bg: 'bg-blue-50',
        border: 'border-blue-200',
        text: 'text-blue-700',
        accent: 'bg-blue-100'
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
      default: return {
        bg: 'bg-white',
        border: 'border-gray-200',
        text: 'text-gray-800',
        accent: 'bg-gray-100'
      };
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
                <ChevronLeftIcon className="w-6 h-6 mr-2 group-hover:-translate-x-1 transition-transform" />
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
              <div className="px-4 py-2 bg-sage-light rounded-full">
                <span className="font-inter text-white text-sm font-medium">Navegación interactiva</span>
              </div>
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
        <div className={`modern-card ${cardColors.bg} ${cardColors.border} border-2 relative overflow-hidden`}>
          {/* En-tête de carte */}
          <div className="flex items-center justify-between mb-8">
            <div className="flex items-center space-x-4">
              <div className={`p-3 rounded-xl ${cardColors.accent}`}>
                <IconComponent className={`w-8 h-8 ${cardColors.text}`} />
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
                  <h3 className={`font-inter text-2xl font-semibold ${cardColors.text} mb-1`}>
                    {currentCard.title}
                  </h3>
                )}
                <p className={`font-inter text-sm ${cardColors.text} opacity-75 capitalize`}>
                  {currentCard.card_type.replace('_', ' ')} • {currentCardIndex + 1} / {cards.length}
                </p>
              </div>
            </div>
            
            <div className="flex items-center space-x-2">
              {editingCard === currentCard.id ? (
                <>
                  <button
                    onClick={() => saveCard(currentCard.id)}
                    disabled={saving}
                    className="p-3 text-green-600 hover:bg-green-100 rounded-xl transition-elegant disabled:opacity-50"
                    title="Guardar"
                  >
                    <CheckIcon className="w-5 h-5" />
                  </button>
                  <button
                    onClick={cancelEditing}
                    className="p-3 text-gray-600 hover:bg-gray-100 rounded-xl transition-elegant"
                    title="Cancelar"
                  >
                    <XMarkIcon className="w-5 h-5" />
                  </button>
                </>
              ) : (
                <button
                  onClick={() => startEditing(currentCard)}
                  className="p-3 text-taupe hover:bg-taupe hover:text-white rounded-xl transition-elegant"
                  title="Editar contenido"
                >
                  <PencilIcon className="w-5 h-5" />
                </button>
              )}
            </div>
          </div>

          {/* Contenu de la carte */}
          <div className="space-y-6">
            {editingCard === currentCard.id ? (
              <textarea
                value={editContent}
                onChange={(e) => setEditContent(e.target.value)}
                className="w-full h-80 p-6 border-2 border-sage rounded-xl focus:outline-none focus:border-sage-dark resize-none font-inter text-lg leading-relaxed"
                placeholder="Escribe el contenido de esta sección..."
              />
            ) : (
              <div 
                className={`prose prose-lg max-w-none ${cardColors.text} font-inter leading-relaxed text-lg`}
                dangerouslySetInnerHTML={{ 
                  __html: currentCard.content
                    .replace(/\n/g, '<br>')
                    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                    .replace(/\*(.*?)\*/g, '<em>$1</em>') 
                }}
              />
            )}
          </div>
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
            <ChevronLeftIcon className="w-6 h-6 mr-3" />
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
            <ChevronRightIcon className="w-6 h-6 ml-3" />
          </button>
        </div>

        {/* Message de fin élégant */}
        {currentCardIndex === cards.length - 1 && (
          <div className="mt-16 text-center">
            <div className="modern-card bg-gradient-to-r from-sage to-taupe text-white">
              <SparklesIcon className="w-16 h-16 mx-auto mb-6 opacity-90" />
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
