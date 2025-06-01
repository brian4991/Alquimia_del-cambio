import React, { useState, useEffect } from 'react';
import { ChevronLeftIcon, ChevronRightIcon, PencilIcon, EyeIcon, CheckIcon, XMarkIcon } from '@heroicons/react/24/outline';
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
      setCurrentCardIndex(0); // Reset to first card
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
      cancelEditing(); // Cancel editing when navigating
    }
  };

  const goToNextCard = () => {
    if (currentCardIndex < cards.length - 1) {
      setCurrentCardIndex(currentCardIndex + 1);
      cancelEditing(); // Cancel editing when navigating
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
      
      // Update local state
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
      case 'intro': return '🎯';
      case 'theory': return '📚';
      case 'practical': return '🛠️';
      case 'resources': return '📖';
      case 'conclusion': return '✨';
      default: return '📄';
    }
  };

  const getCardBorderColor = (cardType) => {
    switch (cardType) {
      case 'intro': return 'border-blue-200 bg-blue-50';
      case 'theory': return 'border-purple-200 bg-purple-50';
      case 'practical': return 'border-green-200 bg-green-50';
      case 'resources': return 'border-orange-200 bg-orange-50';
      case 'conclusion': return 'border-pink-200 bg-pink-50';
      default: return 'border-gray-200 bg-gray-50';
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-indigo-600"></div>
          <p className="mt-4 text-gray-600">Cargando contenido...</p>
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
            onClick={fetchCards}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          >
            Reintentar
          </button>
        </div>
      </div>
    );
  }

  if (cards.length === 0) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <p className="text-gray-600 mb-4">No hay contenido disponible para este tema.</p>
          <button 
            onClick={onBack}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          >
            Volver
          </button>
        </div>
      </div>
    );
  }

  const currentCard = cards[currentCardIndex];

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <div className="bg-white shadow-lg">
        <div className="max-w-4xl mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <button
                onClick={onBack}
                className="flex items-center text-gray-600 hover:text-gray-800 transition-colors"
              >
                <ChevronLeftIcon className="w-5 h-5 mr-2" />
                Volver
              </button>
              <div>
                <h1 className="text-2xl font-bold text-gray-900">{themeName}</h1>
                <p className="text-gray-600">
                  Carta {currentCardIndex + 1} de {cards.length}
                </p>
              </div>
            </div>
            <div className="text-sm text-gray-500">
              Sistema de Cards Editable
            </div>
          </div>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="bg-white border-b">
        <div className="max-w-4xl mx-auto px-4 py-3">
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm font-medium text-gray-700">Progreso</span>
            <span className="text-sm text-gray-500">
              {Math.round(((currentCardIndex + 1) / cards.length) * 100)}%
            </span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div 
              className="bg-blue-600 h-2 rounded-full transition-all duration-300" 
              style={{ width: `${((currentCardIndex + 1) / cards.length) * 100}%` }}
            ></div>
          </div>
        </div>
      </div>

      {/* Card Navigation Dots */}
      <div className="bg-white border-b">
        <div className="max-w-4xl mx-auto px-4 py-4">
          <div className="flex justify-center space-x-2 overflow-x-auto">
            {cards.map((card, index) => (
              <button
                key={card.id}
                onClick={() => goToCard(index)}
                className={`w-3 h-3 rounded-full transition-all duration-200 ${
                  index === currentCardIndex 
                    ? 'bg-blue-600 scale-125' 
                    : 'bg-gray-300 hover:bg-gray-400'
                }`}
                title={`Ir a: ${card.title}`}
              />
            ))}
          </div>
        </div>
      </div>

      {/* Current Card */}
      <div className="max-w-4xl mx-auto px-4 py-8">
        <div 
          className={`card-container ${getCardBorderColor(currentCard.card_type)} border-2 rounded-lg overflow-hidden transition-all duration-300 shadow-lg`}
        >
          {/* Card Header */}
          <div className="bg-white border-b px-6 py-4 flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <span className="text-2xl">{getCardIcon(currentCard.card_type)}</span>
              <div>
                {editingCard === currentCard.id ? (
                  <input
                    type="text"
                    value={editTitle}
                    onChange={(e) => setEditTitle(e.target.value)}
                    className="text-lg font-semibold text-gray-900 bg-gray-100 px-2 py-1 rounded border-2 border-blue-300 focus:outline-none focus:border-blue-500"
                    autoFocus
                  />
                ) : (
                  <h3 className="text-lg font-semibold text-gray-900">{currentCard.title}</h3>
                )}
                <p className="text-sm text-gray-500 capitalize">
                  {currentCard.card_type.replace('_', ' ')} • Carta {currentCardIndex + 1} de {cards.length}
                </p>
              </div>
            </div>
            
            <div className="flex items-center space-x-2">
              {editingCard === currentCard.id ? (
                <>
                  <button
                    onClick={() => saveCard(currentCard.id)}
                    disabled={saving}
                    className="p-2 text-green-600 hover:bg-green-100 rounded-lg transition-colors disabled:opacity-50"
                    title="Guardar cambios"
                  >
                    <CheckIcon className="w-4 h-4" />
                  </button>
                  <button
                    onClick={cancelEditing}
                    className="p-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
                    title="Cancelar"
                  >
                    <XMarkIcon className="w-4 h-4" />
                  </button>
                </>
              ) : (
                <button
                  onClick={() => startEditing(currentCard)}
                  className="p-2 text-blue-600 hover:bg-blue-100 rounded-lg transition-colors"
                  title="Editar contenido"
                >
                  <PencilIcon className="w-4 h-4" />
                </button>
              )}
            </div>
          </div>

          {/* Card Content */}
          <div className="p-8">
            {editingCard === currentCard.id ? (
              <textarea
                value={editContent}
                onChange={(e) => setEditContent(e.target.value)}
                className="w-full h-64 p-4 border-2 border-blue-300 rounded-lg focus:outline-none focus:border-blue-500 resize-none"
                placeholder="Escribe el contenido de la card..."
              />
            ) : (
              <div 
                className="prose prose-lg max-w-none text-gray-700 leading-relaxed"
                dangerouslySetInnerHTML={{ 
                  __html: currentCard.content.replace(/\n/g, '<br>').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\*(.*?)\*/g, '<em>$1</em>') 
                }}
              />
            )}
          </div>
        </div>

        {/* Navigation Arrows */}
        <div className="flex justify-between items-center mt-8">
          <button
            onClick={goToPrevCard}
            disabled={currentCardIndex === 0}
            className={`flex items-center px-6 py-3 rounded-lg font-medium transition-all ${
              currentCardIndex === 0
                ? 'bg-gray-200 text-gray-400 cursor-not-allowed'
                : 'bg-white text-gray-700 hover:bg-gray-50 shadow-md hover:shadow-lg'
            }`}
          >
            <ChevronLeftIcon className="w-5 h-5 mr-2" />
            Anterior
          </button>

          <div className="text-center">
            <p className="text-sm text-gray-600 mb-1">Navegación</p>
            <p className="text-lg font-semibold text-gray-800">
              {currentCardIndex + 1} / {cards.length}
            </p>
          </div>

          <button
            onClick={goToNextCard}
            disabled={currentCardIndex === cards.length - 1}
            className={`flex items-center px-6 py-3 rounded-lg font-medium transition-all ${
              currentCardIndex === cards.length - 1
                ? 'bg-gray-200 text-gray-400 cursor-not-allowed'
                : 'bg-blue-600 text-white hover:bg-blue-700 shadow-md hover:shadow-lg'
            }`}
          >
            Siguiente
            <ChevronRightIcon className="w-5 h-5 ml-2" />
          </button>
        </div>

        {/* Complete Section Button */}
        {currentCardIndex === cards.length - 1 && (
          <div className="mt-8 text-center">
            <div className="bg-green-50 border border-green-200 rounded-lg p-6">
              <h3 className="text-lg font-semibold text-green-800 mb-2">
                ¡Has completado todas las cartas!
              </h3>
              <p className="text-green-700 mb-4">
                Ahora puedes continuar con los ejercicios de este tema.
              </p>
              <button
                onClick={onBack}
                className="bg-green-600 hover:bg-green-700 text-white px-8 py-3 rounded-lg font-medium transition-colors"
              >
                Continuar con Ejercicios
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default CardsView; 