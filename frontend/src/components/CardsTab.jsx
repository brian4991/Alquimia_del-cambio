import React, { useState, useEffect } from 'react';
import { PlusIcon, PencilIcon, TrashIcon, ExclamationTriangleIcon } from '@heroicons/react/24/outline';
import { Target, BookOpen, Settings, FolderOpen, Sparkles, FileText, Eye } from 'lucide-react';
import RichTextEditor from './RichTextEditor';
import { config } from '../config';

const CardsTab = ({ selectedTheme, themes, cards, onLoadCards }) => {
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingCard, setEditingCard] = useState(null);
  const [showPreview, setShowPreview] = useState(false);
  const [formData, setFormData] = useState({
    title: '',
    content: '',
    card_type: 'content',
    order_number: cards.length + 1,
    exercise_instructions: '',
    exercise_questions: []
  });
  
  // Exercise-specific states
  const [newQuestion, setNewQuestion] = useState('');

  const cardTypes = [
    { value: 'intro', label: 'Introduction', color: 'bg-green-50 border-green-200', icon: '🎯' },
    { value: 'theory', label: 'Théorie', color: 'bg-purple-50 border-purple-200', icon: '📚' },
    { value: 'practical', label: 'Pratique', color: 'bg-green-50 border-green-200', icon: '🛠️' },
    { value: 'resources', label: 'Ressources', color: 'bg-orange-50 border-orange-200', icon: '📖' },
    { value: 'conclusion', label: 'Conclusion', color: 'bg-pink-50 border-pink-200', icon: '✨' },
    { value: 'exercise', label: 'Exercice', color: 'bg-orange-50 border-orange-200', icon: '📝' },
    { value: 'content', label: 'Contenu général', color: 'bg-gray-50 border-gray-200', icon: '📄' }
  ];

  // Functions for preview (same as CardsView)
  const getCardIcon = (cardType) => {
    switch (cardType) {
      case 'intro': return Target;
      case 'theory': return BookOpen;
      case 'practical': return Settings;
      case 'resources': return FolderOpen;
      case 'conclusion': return Sparkles;
      case 'exercise': return FileText; // We'll import a better icon later
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

    // Validation for exercise cards
    if (formData.card_type === 'exercise') {
      if (!formData.exercise_questions || formData.exercise_questions.length === 0) {
        alert('Veuillez ajouter au moins une question pour cet exercice');
        return;
      }
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
      const response = await fetch(`${config.apiUrl}/cards/${cardId}`, {
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
      order_number: card.order_number,
      exercise_instructions: card.exercise_instructions || '',
      exercise_questions: card.exercise_questions || []
    });
    setShowCreateForm(true);
  };

  const resetForm = () => {
    setFormData({
      title: '',
      content: '',
      card_type: 'content',
      order_number: cards.length + 1,
      exercise_instructions: '',
      exercise_questions: []
    });
    setNewQuestion('');
  };

  const handleCancel = () => {
    setShowCreateForm(false);
    setEditingCard(null);
    resetForm();
  };

  const getCardTypeInfo = (type) => {
    return cardTypes.find(ct => ct.value === type) || cardTypes[cardTypes.length - 1];
  };

  // Exercise question management functions
  const addQuestion = () => {
    if (newQuestion.trim()) {
      setFormData({
        ...formData,
        exercise_questions: [...formData.exercise_questions, newQuestion.trim()]
      });
      setNewQuestion('');
    }
  };

  const removeQuestion = (index) => {
    const updatedQuestions = formData.exercise_questions.filter((_, i) => i !== index);
    setFormData({
      ...formData,
      exercise_questions: updatedQuestions
    });
  };

  const updateQuestion = (index, newText) => {
    const updatedQuestions = [...formData.exercise_questions];
    updatedQuestions[index] = newText;
    setFormData({
      ...formData,
      exercise_questions: updatedQuestions
    });
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
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Contenu *
              </label>
              <RichTextEditor
                value={formData.content}
                onChange={(content) => setFormData({ ...formData, content })}
                placeholder="Écrivez le contenu de la carte..."
                height={300}
                showButtons={false}
              />
            </div>

            {/* Exercise-specific fields */}
            {formData.card_type === 'exercise' && (
              <div className="space-y-4 border-t pt-4">
                <h3 className="text-lg font-medium text-gray-900 flex items-center">
                  <span className="mr-2">📝</span>
                  Configuration de l'exercice
                </h3>
                
                {/* Exercise Instructions */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Instructions de l'exercice
                  </label>
                  <textarea
                    value={formData.exercise_instructions}
                    onChange={(e) => setFormData({ ...formData, exercise_instructions: e.target.value })}
                    className="w-full border border-gray-300 rounded-md px-3 py-2 min-h-[100px]"
                    placeholder="Donnez des instructions claires pour cet exercice..."
                  />
                </div>

                {/* Exercise Questions */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Questions de l'exercice
                  </label>
                  
                  {/* Add new question */}
                  <div className="flex space-x-2 mb-3">
                    <input
                      type="text"
                      value={newQuestion}
                      onChange={(e) => setNewQuestion(e.target.value)}
                      className="flex-1 border border-gray-300 rounded-md px-3 py-2"
                      placeholder="Tapez une nouvelle question..."
                      onKeyPress={(e) => e.key === 'Enter' && (e.preventDefault(), addQuestion())}
                    />
                    <button
                      type="button"
                      onClick={addQuestion}
                      className="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700"
                    >
                      Ajouter
                    </button>
                  </div>

                  {/* Questions list */}
                  {formData.exercise_questions.length > 0 && (
                    <div className="space-y-2 max-h-40 overflow-y-auto border rounded-md p-3 bg-gray-50">
                      {formData.exercise_questions.map((question, index) => (
                        <div key={index} className="flex items-center space-x-2 bg-white p-2 rounded border">
                          <span className="text-sm font-medium text-gray-500 w-8">
                            {index + 1}.
                          </span>
                          <input
                            type="text"
                            value={question}
                            onChange={(e) => updateQuestion(index, e.target.value)}
                            className="flex-1 border-0 bg-transparent focus:ring-0 text-sm"
                          />
                          <button
                            type="button"
                            onClick={() => removeQuestion(index)}
                            className="text-red-600 hover:text-red-800 p-1"
                          >
                            <TrashIcon className="w-4 h-4" />
                          </button>
                        </div>
                      ))}
                    </div>
                  )}
                  
                  {formData.exercise_questions.length === 0 && (
                    <p className="text-sm text-gray-500 italic">
                      Aucune question ajoutée. Ajoutez au moins une question pour cet exercice.
                    </p>
                  )}
                </div>
              </div>
            )}

            <div className="flex justify-between items-center">
              <button
                type="button"
                onClick={() => setShowPreview(!showPreview)}
                className="flex items-center space-x-2 text-sage hover:bg-sage hover:text-white px-4 py-2 rounded-lg transition-colors border border-sage"
              >
                <Eye className="w-4 h-4" />
                <span>{showPreview ? 'Ocultar Vista Previa' : 'Vista Previa'}</span>
              </button>
              
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
            </div>
          </form>
        </div>
      )}

      {/* Preview Section */}
      {showPreview && (showCreateForm || editingCard) && (
        <div className="mb-8">
          <h3 className="text-lg font-semibold mb-4 text-gray-800">Vista Previa - Como aparecerá en Contenidos</h3>
          <div className="max-w-4xl mx-auto">
            <div 
              className="modern-card border-2 relative overflow-hidden"
              style={{
                backgroundColor: formData.card_type === 'intro' ? getCardColors(formData.card_type).bg : undefined,
                borderColor: formData.card_type === 'intro' ? getCardColors(formData.card_type).border : undefined
              }}
            >
              {/* En-tête de carte */}
              <div className="flex items-center justify-between mb-8">
                <div className="flex items-center space-x-4">
                  <div 
                    className="p-3 rounded-xl"
                    style={{ 
                      backgroundColor: formData.card_type === 'intro' ? getCardColors(formData.card_type).accent : undefined 
                    }}
                  >
                    {(() => {
                      const IconComponent = getCardIcon(formData.card_type);
                      return (
                        <IconComponent 
                          className="w-8 h-8" 
                          style={{ 
                            color: formData.card_type === 'intro' ? getCardColors(formData.card_type).text : undefined 
                          }}
                        />
                      );
                    })()}
                  </div>
                  <div>
                    <h3 
                      className="font-inter text-2xl font-semibold mb-1"
                      style={{ 
                        color: formData.card_type === 'intro' ? getCardColors(formData.card_type).text : undefined 
                      }}
                    >
                      {formData.title || 'Título de la carta'}
                    </h3>
                    <p 
                      className="font-inter text-sm opacity-75 capitalize"
                      style={{ 
                        color: formData.card_type === 'intro' ? getCardColors(formData.card_type).text : undefined 
                      }}
                    >
                      {formData.card_type.replace('_', ' ')} • Vista previa
                    </p>
                  </div>
                </div>
              </div>

              {/* Contenu de la carte */}
              <div className="space-y-6">
                <div 
                  className="rich-content max-w-none font-inter text-lg"
                  dangerouslySetInnerHTML={{ __html: formData.content || '<p>El contenido aparecerá aquí...</p>' }}
                />
              </div>
            </div>
          </div>
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
