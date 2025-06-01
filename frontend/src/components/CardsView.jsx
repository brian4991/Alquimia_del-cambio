import React, { useState, useEffect } from 'react';
import { ChevronLeftIcon, PencilIcon, EyeIcon, CheckIcon, XMarkIcon } from '@heroicons/react/24/outline';
import api from '../services/api';

const CardsView = ({ themeId, themeName, onBack }) => {
  const [cards, setCards] = useState([]);
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
    } catch (err) {
      setError('Error loading cards');
      console.error('Error fetching cards:', err);
    } finally {
      setLoading(false);
    }
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
                <p className="text-gray-600">{cards.length} contenidos disponibles</p>
              </div>
            </div>
            <div className="text-sm text-gray-500">
              Sistema de Cards Editable
            </div>
          </div>
        </div>
      </div>

      {/* Cards Container */}
      <div className="max-w-4xl mx-auto px-4 py-8">
        <div className="space-y-6">
          {cards.map((card, index) => (
            <div 
              key={card.id} 
              className={`card-container ${getCardBorderColor(card.card_type)} border-2 rounded-lg overflow-hidden transition-all duration-300 hover:shadow-lg`}
            >
              {/* Card Header */}
              <div className="bg-white border-b px-6 py-4 flex items-center justify-between">
                <div className="flex items-center space-x-3">
                  <span className="text-2xl">{getCardIcon(card.card_type)}</span>
                  <div>
                    {editingCard === card.id ? (
                      <input
                        type="text"
                        value={editTitle}
                        onChange={(e) => setEditTitle(e.target.value)}
                        className="text-lg font-semibold text-gray-900 bg-gray-100 px-2 py-1 rounded border-2 border-blue-300 focus:outline-none focus:border-blue-500"
                        autoFocus
                      />
                    ) : (
                      <h3 className="text-lg font-semibold text-gray-900">{card.title}</h3>
                    )}
                    <p className="text-sm text-gray-500 capitalize">
                      {card.card_type.replace('_', ' ')} • Card {index + 1}
                    </p>
                  </div>
                </div>
                
                <div className="flex items-center space-x-2">
                  {editingCard === card.id ? (
                    <>
                      <button
                        onClick={() => saveCard(card.id)}
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
                      onClick={() => startEditing(card)}
                      className="p-2 text-blue-600 hover:bg-blue-100 rounded-lg transition-colors"
                      title="Editar contenido"
                    >
                      <PencilIcon className="w-4 h-4" />
                    </button>
                  )}
                </div>
              </div>

              {/* Card Content */}
              <div className="p-6">
                {editingCard === card.id ? (
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
                      __html: card.content.replace(/\n/g, '<br>').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\*(.*?)\*/g, '<em>$1</em>') 
                    }}
                  />
                )}
              </div>
            </div>
          ))}
        </div>

        {/* Bottom Navigation */}
        <div className="mt-12 flex justify-center">
          <button
            onClick={onBack}
            className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-medium transition-colors"
          >
            Continuar con Ejercicios
          </button>
        </div>
      </div>
    </div>
  );
};

export default CardsView; 