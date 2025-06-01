import React, { useState, useEffect } from 'react';
import { PlusIcon, PencilIcon, TrashIcon, ExclamationTriangleIcon } from '@heroicons/react/24/outline';

const CardsTab = ({ selectedTheme, themes, cards, onLoadCards }) => {
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingCard, setEditingCard] = useState(null);
  const [formData, setFormData] = useState({
    title: '',
    content: '',
    card_type: 'content',
    order_number: cards.length + 1
  });

  const cardTypes = [
    { value: 'intro', label: 'Introduction', color: 'bg-blue-50 border-blue-200', icon: '🎯' },
    { value: 'theory', label: 'Théorie', color: 'bg-purple-50 border-purple-200', icon: '📚' },
    { value: 'practical', label: 'Pratique', color: 'bg-green-50 border-green-200', icon: '🛠️' },
    { value: 'resources', label: 'Ressources', color: 'bg-orange-50 border-orange-200', icon: '📖' },
    { value: 'conclusion', label: 'Conclusion', color: 'bg-pink-50 border-pink-200', icon: '✨' },
    { value: 'content', label: 'Contenu général', color: 'bg-gray-50 border-gray-200', icon: '📄' }
  ];

  // Load cards when theme is selected
  useEffect(() => {
    if (selectedTheme) {
      onLoadCards(selectedTheme.id);
    }
  }, [selectedTheme]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedTheme) {
      alert('Veuillez sélectionner un thème d\'abord');
      return;
    }

    try {
      const token = localStorage.getItem('token');
      const url = editingCard 
        ? `/api/cards/${editingCard.id}` 
        : `/api/themes/${selectedTheme.id}/cards`;
      const method = editingCard ? 'PUT' : 'POST';
      
      const response = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        setShowCreateForm(false);
        setEditingCard(null);
        resetForm();
        onLoadCards(selectedTheme.id);
      }
    } catch (error) {
      console.error('Error saving card:', error);
    }
  };

  const handleDelete = async (cardId) => {
    if (!confirm('Êtes-vous sûr de vouloir supprimer cette carte ?')) return;
    
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`/api/cards/${cardId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });

      if (response.ok && selectedTheme) {
        onLoadCards(selectedTheme.id);
      }
    } catch (error) {
      console.error('Error deleting card:', error);
    }
  };

  const handleEdit = (card) => {
    setEditingCard(card);
    setFormData({
      title: card.title,
      content: card.content,
      card_type: card.card_type,
      order_number: card.order_number
    });
    setShowCreateForm(true);
  };

  const resetForm = () => {
    setFormData({
      title: '',
      content: '',
      card_type: 'content',
      order_number: cards.length + 1
    });
  };

  const handleCancel = () => {
    setShowCreateForm(false);
    setEditingCard(null);
    resetForm();
  };

  const getCardTypeInfo = (type) => {
    return cardTypes.find(ct => ct.value === type) || cardTypes[cardTypes.length - 1];
  };

  if (!selectedTheme) {
    return (
      <div className="text-center py-12">
        <ExclamationTriangleIcon className="w-16 h-16 text-gray-400 mx-auto mb-4" />
        <h3 className="text-lg font-medium text-gray-900 mb-2">Aucun thème sélectionné</h3>
        <p className="text-gray-600">
          Veuillez d'abord sélectionner un thème dans l'onglet "Thèmes" pour gérer ses cartes.
        </p>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Gestion des Cartes</h2>
          <p className="text-gray-600">Thème sélectionné: {selectedTheme.title}</p>
        </div>
        <button
          onClick={() => setShowCreateForm(true)}
          className="bg-purple-600 text-white px-4 py-2 rounded-lg flex items-center hover:bg-purple-700"
        >
          <PlusIcon className="w-5 h-5 mr-2" />
          Nouvelle Carte
        </button>
      </div>

      {/* Create/Edit Form */}
      {showCreateForm && (
        <div className="mb-8 bg-gray-50 p-6 rounded-lg">
          <h3 className="text-lg font-semibold mb-4">
            {editingCard ? 'Modifier la Carte' : 'Créer une Nouvelle Carte'}
          </h3>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Titre *
                </label>
                <input
                  type="text"
                  value={formData.title}
                  onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                  className="w-full border border-gray-300 rounded-md px-3 py-2"
                  required
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Type de carte
                </label>
                <select
                  value={formData.card_type}
                  onChange={(e) => setFormData({ ...formData, card_type: e.target.value })}
                  className="w-full border border-gray-300 rounded-md px-3 py-2"
                >
                  {cardTypes.map((type) => (
                    <option key={type.value} value={type.value}>
                      {type.icon} {type.label}
                    </option>
                  ))}
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Numéro d'ordre
                </label>
                <input
                  type="number"
                  value={formData.order_number}
                  onChange={(e) => setFormData({ ...formData, order_number: parseInt(e.target.value) })}
                  className="w-full border border-gray-300 rounded-md px-3 py-2"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Contenu *
              </label>
              <textarea
                value={formData.content}
                onChange={(e) => setFormData({ ...formData, content: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2"
                rows="8"
                placeholder="Contenu de la carte (markdown supporté)..."
                required
              />
            </div>

            <div className="flex space-x-4">
              <button
                type="submit"
                className="bg-purple-600 text-white px-6 py-2 rounded-lg hover:bg-purple-700"
              >
                {editingCard ? 'Mettre à jour' : 'Créer'}
              </button>
              <button
                type="button"
                onClick={handleCancel}
                className="bg-gray-300 text-gray-700 px-6 py-2 rounded-lg hover:bg-gray-400"
              >
                Annuler
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Cards List */}
      <div className="space-y-4">
        {cards.length === 0 ? (
          <div className="text-center py-8 text-gray-500">
            Aucune carte trouvée pour ce thème. Créez votre première carte !
          </div>
        ) : (
          cards.map((card) => {
            const cardTypeInfo = getCardTypeInfo(card.card_type);
            return (
              <div
                key={card.id}
                className={`border-2 rounded-lg p-4 hover:shadow-md transition-shadow ${cardTypeInfo.color}`}
              >
                <div className="flex justify-between items-start">
                  <div className="flex-1">
                    <div className="flex items-center mb-2">
                      <span className="text-lg mr-2">{cardTypeInfo.icon}</span>
                      <h3 className="text-lg font-semibold text-gray-900">
                        {card.order_number}. {card.title}
                      </h3>
                      <span className="ml-2 px-2 py-1 bg-white rounded-full text-xs text-gray-600">
                        {cardTypeInfo.label}
                      </span>
                    </div>
                    <p className="text-gray-700 mb-3 line-clamp-3">{card.content}</p>
                    <div className="flex items-center space-x-4 text-sm text-gray-500">
                      <span>ID: {card.id}</span>
                      <span>Créé: {new Date(card.created_at).toLocaleDateString()}</span>
                      {card.updated_at !== card.created_at && (
                        <span>Modifié: {new Date(card.updated_at).toLocaleDateString()}</span>
                      )}
                    </div>
                  </div>
                  <div className="flex space-x-2 ml-4">
                    <button
                      onClick={() => handleEdit(card)}
                      className="text-purple-600 hover:text-purple-800 p-2"
                    >
                      <PencilIcon className="w-5 h-5" />
                    </button>
                    <button
                      onClick={() => handleDelete(card.id)}
                      className="text-red-600 hover:text-red-800 p-2"
                    >
                      <TrashIcon className="w-5 h-5" />
                    </button>
                  </div>
                </div>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
};

export default CardsTab; 