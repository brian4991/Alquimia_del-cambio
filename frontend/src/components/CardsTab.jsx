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
    exercise_questions: [],
    exercise_sections: []
  });
  
  // Exercise-specific states
  const [newQuestion, setNewQuestion] = useState('');
  const [questionType, setQuestionType] = useState('text'); // 'text' or 'table'
  const [tableConfig, setTableConfig] = useState({
    columns: [{ title: 'Colonne 1', type: 'text' }],
    rows: 3
  });
  
  // Exercise sections states
  const [currentSectionIndex, setCurrentSectionIndex] = useState(0);
  const [newSectionTitle, setNewSectionTitle] = useState('');
  const [newSectionInstructions, setNewSectionInstructions] = useState('');

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
        ? `${config.apiUrl}/api/cards/${editingCard.id}` 
        : `${config.apiUrl}/themes/${selectedTheme.id}/cards`;
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
      } else {
        const responseData = await response.json();
        console.error('API Error:', responseData);
        alert('Erreur lors de la sauvegarde: ' + (responseData.detail || 'Erreur inconnue'));
      }
    } catch (error) {
      console.error('Error saving card:', error);
      alert('Erreur réseau: ' + error.message);
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
      exercise_questions: card.exercise_questions || [],
      exercise_sections: card.exercise_sections || []
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
      exercise_questions: [],
      exercise_sections: []
    });
    setNewQuestion('');
    setCurrentSectionIndex(0);
    setNewSectionTitle('');
    setNewSectionInstructions('');
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
      const questionObj = {
        type: questionType,
        question: newQuestion.trim(),
        ...(questionType === 'table' ? { table_config: { ...tableConfig } } : {})
      };
      
      setFormData({
        ...formData,
        exercise_questions: [...formData.exercise_questions, questionObj]
      });
      
      // Reset form
      setNewQuestion('');
      setQuestionType('text');
      setTableConfig({
        columns: [{ title: 'Colonne 1', type: 'text' }],
        rows: 3
      });
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
    if (typeof updatedQuestions[index] === 'string') {
      // Legacy string format - convert to object
      updatedQuestions[index] = { type: 'text', question: newText };
    } else {
      // New object format
      updatedQuestions[index] = { ...updatedQuestions[index], question: newText };
    }
    setFormData({
      ...formData,
      exercise_questions: updatedQuestions
    });
  };

  // Table configuration functions
  const addTableColumn = () => {
    setTableConfig({
      ...tableConfig,
      columns: [...tableConfig.columns, { title: `Colonne ${tableConfig.columns.length + 1}`, type: 'text' }]
    });
  };

  const updateTableColumn = (index, field, value) => {
    const updatedColumns = [...tableConfig.columns];
    updatedColumns[index] = { ...updatedColumns[index], [field]: value };
    setTableConfig({
      ...tableConfig,
      columns: updatedColumns
    });
  };

  const removeTableColumn = (index) => {
    if (tableConfig.columns.length > 1) {
      const updatedColumns = tableConfig.columns.filter((_, i) => i !== index);
      setTableConfig({
        ...tableConfig,
        columns: updatedColumns
      });
    }
  };

  // Exercise sections management functions
  const addSection = () => {
    if (newSectionTitle.trim()) {
      const newSection = {
        title: newSectionTitle.trim(),
        instructions: newSectionInstructions.trim(),
        questions: []
      };
      
      setFormData({
        ...formData,
        exercise_sections: [...formData.exercise_sections, newSection]
      });
      
      setNewSectionTitle('');
      setNewSectionInstructions('');
      setCurrentSectionIndex(formData.exercise_sections.length);
    }
  };

  const removeSection = (index) => {
    const updatedSections = formData.exercise_sections.filter((_, i) => i !== index);
    setFormData({
      ...formData,
      exercise_sections: updatedSections
    });
    
    if (currentSectionIndex >= updatedSections.length && updatedSections.length > 0) {
      setCurrentSectionIndex(updatedSections.length - 1);
    } else if (updatedSections.length === 0) {
      setCurrentSectionIndex(0);
    }
  };

  const addQuestionToSection = (sectionIndex) => {
    if (newQuestion.trim() && sectionIndex < formData.exercise_sections.length) {
      const questionObj = {
        type: questionType,
        question: newQuestion.trim(),
        ...(questionType === 'table' ? { table_config: { ...tableConfig } } : {})
      };
      
      const updatedSections = [...formData.exercise_sections];
      updatedSections[sectionIndex] = {
        ...updatedSections[sectionIndex],
        questions: [...updatedSections[sectionIndex].questions, questionObj]
      };
      
      setFormData({
        ...formData,
        exercise_sections: updatedSections
      });
      
      // Reset form
      setNewQuestion('');
      setQuestionType('text');
      setTableConfig({
        columns: [{ title: 'Colonne 1', type: 'text' }],
        rows: 3
      });
    }
  };

  const removeQuestionFromSection = (sectionIndex, questionIndex) => {
    const updatedSections = [...formData.exercise_sections];
    updatedSections[sectionIndex] = {
      ...updatedSections[sectionIndex],
      questions: updatedSections[sectionIndex].questions.filter((_, i) => i !== questionIndex)
    };
    
    setFormData({
      ...formData,
      exercise_sections: updatedSections
    });
  };

  if (!selectedTheme) {
    return (
      <div className="text-center py-12">
        <ExclamationTriangleIcon className="w-16 h-16 text-gray-400 mx-auto mb-4" />
        <h3 className="text-lg font-medium text-gray-900 mb-2">Aucun thème/recurso sélectionné</h3>
        <p className="text-gray-600">
          Veuillez d'abord sélectionner un thème (onglet "Thèmes") ou un recurso (onglet "Recursos") pour gérer ses cartes.
        </p>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Gestion des Cartes</h2>
          <p className="text-gray-600">
            {selectedTheme.theme_type === 'resource' ? 'Recurso' : 'Thème'} sélectionné: {selectedTheme.title}
          </p>
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
              <div className="space-y-6 border-t pt-4">
                <h3 className="text-lg font-medium text-gray-900 flex items-center">
                  <span className="mr-2">📝</span>
                  Configuration de l'exercice par sections
                </h3>
                
                {/* New Exercise Sections System */}
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <h4 className="text-md font-medium text-gray-900">
                      🎯 Sections d'exercices ({formData.exercise_sections.length})
                    </h4>
                  </div>

                  {/* Add new section form */}
                  <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 space-y-3">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                          Titre de la section
                        </label>
                        <input
                          type="text"
                          value={newSectionTitle}
                          onChange={(e) => setNewSectionTitle(e.target.value)}
                          className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm"
                          placeholder="Ex: Réflexion personnelle"
                        />
                      </div>
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                          Instructions
                        </label>
                        <textarea
                          value={newSectionInstructions}
                          onChange={(e) => setNewSectionInstructions(e.target.value)}
                          className="w-full border border-gray-300 rounded-md px-3 py-2 min-h-[60px] text-sm"
                          placeholder="Instructions pour cette section..."
                        />
                      </div>
                    </div>
                    <button
                      type="button"
                      onClick={addSection}
                      className="bg-blue-600 text-white px-4 py-2 rounded-md text-sm hover:bg-blue-700"
                      disabled={!newSectionTitle.trim()}
                    >
                      + Ajouter Section
                    </button>
                  </div>

                  {/* Exercise Sections List */}
                  {formData.exercise_sections.length > 0 && (
                    <div className="space-y-4">
                      {formData.exercise_sections.map((section, sectionIndex) => (
                        <div key={sectionIndex} className="bg-white border border-gray-200 rounded-lg p-4">
                          <div className="flex items-center justify-between mb-3">
                            <h5 className="font-medium text-gray-900 flex items-center">
                              <span className="mr-2">📋</span>
                              {section.title}
                              <span className="ml-2 text-sm text-gray-500">
                                ({section.questions.length} questions)
                              </span>
                            </h5>
                            <button
                              type="button"
                              onClick={() => removeSection(sectionIndex)}
                              className="text-red-600 hover:text-red-800 text-sm"
                            >
                              <TrashIcon className="w-4 h-4" />
                            </button>
                          </div>
                          
                          {section.instructions && (
                            <p className="text-sm text-gray-600 mb-3 italic">
                              "{section.instructions}"
                            </p>
                          )}

                          {/* Add question to this section */}
                          {currentSectionIndex === sectionIndex && (
                            <div className="mb-3 p-3 bg-green-50 border border-green-200 rounded">
                              <div className="space-y-2">
                                <div className="flex items-center space-x-2">
                                  <select
                                    value={questionType}
                                    onChange={(e) => setQuestionType(e.target.value)}
                                    className="border border-gray-300 rounded px-2 py-1 text-sm"
                                  >
                                    <option value="text">📝 Texte</option>
                                    <option value="table">📊 Tableau</option>
                                  </select>
                                  <input
                                    type="text"
                                    value={newQuestion}
                                    onChange={(e) => setNewQuestion(e.target.value)}
                                    className="flex-1 border border-gray-300 rounded px-2 py-1 text-sm"
                                    placeholder="Question..."
                                    onKeyPress={(e) => e.key === 'Enter' && (e.preventDefault(), addQuestionToSection(sectionIndex))}
                                  />
                                  <button
                                    type="button"
                                    onClick={() => addQuestionToSection(sectionIndex)}
                                    className="bg-green-600 text-white px-3 py-1 rounded text-sm hover:bg-green-700"
                                  >
                                    + Question
                                  </button>
                                </div>

                                {/* Table configuration */}
                                {questionType === 'table' && (
                                  <div className="bg-white p-3 rounded border text-sm">
                                    <div className="flex items-center justify-between mb-2">
                                      <span className="font-medium">Configuration tableau:</span>
                                      <div className="flex items-center space-x-2">
                                        <span>Lignes:</span>
                                        <input
                                          type="number"
                                          value={tableConfig.rows}
                                          onChange={(e) => setTableConfig({ ...tableConfig, rows: parseInt(e.target.value) || 3 })}
                                          className="w-16 border border-gray-300 rounded px-2 py-1"
                                          min="1"
                                        />
                                      </div>
                                    </div>
                                    <div className="space-y-1">
                                      {tableConfig.columns.map((col, colIndex) => (
                                        <div key={colIndex} className="flex items-center space-x-2">
                                          <input
                                            type="text"
                                            value={col.title}
                                            onChange={(e) => updateTableColumn(colIndex, 'title', e.target.value)}
                                            className="flex-1 border border-gray-300 rounded px-2 py-1"
                                            placeholder="Colonne..."
                                          />
                                          <select
                                            value={col.type}
                                            onChange={(e) => updateTableColumn(colIndex, 'type', e.target.value)}
                                            className="border border-gray-300 rounded px-2 py-1"
                                          >
                                            <option value="text">Texte</option>
                                            <option value="number">Nombre</option>
                                          </select>
                                          {tableConfig.columns.length > 1 && (
                                            <button
                                              type="button"
                                              onClick={() => removeTableColumn(colIndex)}
                                              className="text-red-500 hover:text-red-700"
                                            >
                                              <TrashIcon className="w-4 h-4" />
                                            </button>
                                          )}
                                        </div>
                                      ))}
                                      <button
                                        type="button"
                                        onClick={addTableColumn}
                                        className="text-blue-600 hover:text-blue-800 text-sm"
                                      >
                                        + Colonne
                                      </button>
                                    </div>
                                  </div>
                                )}
                              </div>
                            </div>
                          )}

                          {/* Questions for this section */}
                          <div className="space-y-2">
                            {section.questions.map((question, qIndex) => (
                              <div key={qIndex} className="flex items-center justify-between bg-gray-50 p-2 rounded">
                                <div className="flex-1">
                                  <span className="text-sm">
                                    {question.type === 'table' ? '📊' : '📝'} {question.question}
                                  </span>
                                </div>
                                <button
                                  type="button"
                                  onClick={() => removeQuestionFromSection(sectionIndex, qIndex)}
                                  className="text-red-500 hover:text-red-700 ml-2"
                                >
                                  <TrashIcon className="w-4 h-4" />
                                </button>
                              </div>
                            ))}
                          </div>

                          {/* Button to activate question adding for this section */}
                          {currentSectionIndex !== sectionIndex && (
                            <button
                              type="button"
                              onClick={() => setCurrentSectionIndex(sectionIndex)}
                              className="mt-2 text-blue-600 hover:text-blue-800 text-sm"
                            >
                              + Ajouter questions à cette section
                            </button>
                          )}
                        </div>
                      ))}
                    </div>
                  )}

                  {formData.exercise_sections.length === 0 && (
                    <div className="text-center py-6 text-gray-500 bg-gray-50 rounded-lg border-2 border-dashed border-gray-300">
                      <p className="mb-2">Aucune section d'exercice créée</p>
                      <p className="text-sm">Ajoutez un titre et des instructions ci-dessus, puis cliquez sur "Ajouter Section"</p>
                    </div>
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

                {/* Exercise Preview Section */}
                {formData.card_type === 'exercise' && (
                  <div className="mt-8 border-t pt-8">
                    <div className="space-y-6">
                      {/* Exercise Sections Preview */}
                      {formData.exercise_sections && formData.exercise_sections.length > 0 ? (
                        <div className="space-y-8">
                          <h4 className="font-inter text-xl font-semibold text-orange-800 flex items-center">
                            <span className="mr-2">🎯</span>
                            Vista previa del ejercicio por secciones
                          </h4>
                          
                          {formData.exercise_sections.map((section, sectionIndex) => (
                            <div key={sectionIndex} className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl border-2 border-blue-200 p-6">
                              {/* Section Header */}
                              <div className="mb-6">
                                <h5 className="font-inter text-xl font-bold text-blue-800 mb-2 flex items-center">
                                  <span className="mr-2">📋</span>
                                  {section.title}
                                </h5>
                                {section.instructions && (
                                  <div className="bg-white/70 rounded-lg p-4 border border-blue-200">
                                    <p className="font-inter text-blue-900 leading-relaxed italic">
                                      "{section.instructions}"
                                    </p>
                                  </div>
                                )}
                              </div>

                              {/* Section Questions */}
                              {section.questions && section.questions.length > 0 && (
                                <div className="space-y-4">
                                  {section.questions.map((question, questionIndex) => (
                                    <div key={questionIndex} className="bg-white rounded-lg border border-blue-200 p-4">
                                      <div className="flex items-start justify-between mb-3">
                                        <h6 className="font-inter text-md font-semibold text-gray-800">
                                          Pregunta {questionIndex + 1}
                                        </h6>
                                        <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded-full text-xs font-medium">
                                          {question.type === 'table' ? '📊 Tabla' : '📝 Texto'}
                                        </span>
                                      </div>
                                      
                                      <p className="font-inter text-gray-700 mb-4">
                                        {question.question}
                                      </p>

                                      {/* Table Preview */}
                                      {question.type === 'table' && question.table_config && (
                                        <div className="bg-gray-50 rounded-lg p-4">
                                          <h6 className="font-medium text-gray-800 mb-3">Vista previa de tabla:</h6>
                                          <div className="overflow-x-auto">
                                            <table className="w-full border-collapse border border-gray-300">
                                              <thead>
                                                <tr className="bg-gray-100">
                                                  {question.table_config.columns.map((col, colIndex) => (
                                                    <th key={colIndex} className="border border-gray-300 px-3 py-2 text-left font-medium">
                                                      {col.title}
                                                    </th>
                                                  ))}
                                                </tr>
                                              </thead>
                                              <tbody>
                                                {Array.from({ length: question.table_config.rows }, (_, rowIndex) => (
                                                  <tr key={rowIndex}>
                                                    {question.table_config.columns.map((col, colIndex) => (
                                                      <td key={colIndex} className="border border-gray-300 px-3 py-2">
                                                        <div className="h-8 bg-gray-100 rounded opacity-50"></div>
                                                      </td>
                                                    ))}
                                                  </tr>
                                                ))}
                                              </tbody>
                                            </table>
                                          </div>
                                        </div>
                                      )}

                                      {/* Text Input Preview */}
                                      {question.type === 'text' && (
                                        <div className="bg-gray-50 rounded-lg p-4">
                                          <div className="h-24 bg-gray-100 rounded opacity-50 flex items-center justify-center">
                                            <span className="text-gray-500 text-sm">Área de respuesta de texto</span>
                                          </div>
                                        </div>
                                      )}
                                    </div>
                                  ))}
                                </div>
                              )}

                              {/* Empty section indicator */}
                              {(!section.questions || section.questions.length === 0) && (
                                <div className="text-center py-4 text-blue-600 bg-blue-50 rounded-lg border border-blue-200">
                                  <p className="text-sm italic">Esta sección no tiene preguntas aún</p>
                                </div>
                              )}
                            </div>
                          ))}
                        </div>
                      ) : (
                        <div className="text-center py-8 text-gray-500 bg-gray-50 rounded-lg border-2 border-dashed border-gray-300">
                          <p className="mb-2">Sin secciones de ejercicio</p>
                          <p className="text-sm">Crea secciones arriba para ver la vista previa aquí</p>
                        </div>
                      )}
                    </div>
                  </div>
                )}
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
                      {card.card_type === 'exercise' && (
                        <span className="ml-2 px-2 py-1 bg-orange-100 text-orange-800 rounded-full text-xs">
                          ID: {card.id} | Q: {card.exercise_questions ? card.exercise_questions.length : 0}
                        </span>
                      )}
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
