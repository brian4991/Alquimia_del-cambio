import React, { useState, useEffect } from 'react';
import { PlusIcon, PencilIcon, TrashIcon, ExclamationTriangleIcon } from '@heroicons/react/24/outline';
import { Target, BookOpen, Settings, FolderOpen, Sparkles, FileText, Eye } from 'lucide-react';
import RichTextEditor from './RichTextEditor';
import { config } from '../config';

const ExercisesTab = ({ selectedTheme, themes, exercises, onLoadExercises }) => {
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingExercise, setEditingExercise] = useState(null);
  const [showPreview, setShowPreview] = useState(false);
  const [formData, setFormData] = useState({
    title: '',
    parent_title: '',
    instructions: '',
    order_number: exercises.length + 1,
    exercise_sections: []
  });
  
  // Exercise-specific states (same as CardsTab)
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

  // Load exercises when theme is selected
  useEffect(() => {
    if (selectedTheme) {
      onLoadExercises(selectedTheme.id);
    }
  }, [selectedTheme]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedTheme) {
      alert('Veuillez sélectionner un thème d\'abord');
      return;
    }

    // Validation: Must have at least one sub-exercise
    const hasSections = formData.exercise_sections && formData.exercise_sections.length > 0;
    
    if (!hasSections) {
      alert('Veuillez ajouter au moins un sous-exercice');
      return;
    }

    try {
      const token = localStorage.getItem('token');
      const url = editingExercise 
        ? `${config.apiUrl}/exercises/${editingExercise.id}` 
        : `${config.apiUrl}/themes/${selectedTheme.id}/exercises`;
      const method = editingExercise ? 'PUT' : 'POST';
      
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
        setEditingExercise(null);
        resetForm();
        onLoadExercises(selectedTheme.id);
      }
    } catch (error) {
      console.error('Error saving exercise:', error);
    }
  };

  const handleDelete = async (exerciseId) => {
    if (window.confirm('Êtes-vous sûr de vouloir supprimer cet exercice ?')) {
      try {
        const token = localStorage.getItem('token');
        const response = await fetch(`${config.apiUrl}/exercises/${exerciseId}`, {
          method: 'DELETE',
          headers: { 'Authorization': `Bearer ${token}` }
        });

        if (response.ok) {
          onLoadExercises(selectedTheme.id);
        }
      } catch (error) {
        console.error('Error deleting exercise:', error);
      }
    }
  };

  const handleEdit = (exercise) => {
    setEditingExercise(exercise);
    setFormData({
      title: exercise.title,
      parent_title: exercise.parent_title || '',
      instructions: exercise.instructions,
      order_number: exercise.order_number,
      exercise_sections: exercise.exercise_sections || []
    });
    setShowCreateForm(true);
  };

  const resetForm = () => {
    setFormData({
      title: '',
      parent_title: '',
      instructions: '',
      order_number: exercises.length + 1,
      exercise_sections: []
    });
    setNewQuestion('');
    setCurrentSectionIndex(0);
    setNewSectionTitle('');
    setNewSectionInstructions('');
  };

  const handleCancel = () => {
    setShowCreateForm(false);
    setEditingExercise(null);
    resetForm();
  };


  // Section management functions
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

  // Table configuration functions
  const addColumn = () => {
    setTableConfig({
      ...tableConfig,
      columns: [...tableConfig.columns, { title: `Colonne ${tableConfig.columns.length + 1}`, type: 'text' }]
    });
  };

  const removeColumn = (index) => {
    if (tableConfig.columns.length > 1) {
      setTableConfig({
        ...tableConfig,
        columns: tableConfig.columns.filter((_, i) => i !== index)
      });
    }
  };

  const updateColumnTitle = (index, title) => {
    const updatedColumns = [...tableConfig.columns];
    updatedColumns[index] = { ...updatedColumns[index], title };
    setTableConfig({
      ...tableConfig,
      columns: updatedColumns
    });
  };

  if (!selectedTheme) {
    return (
      <div className="text-center py-12">
        <ExclamationTriangleIcon className="w-16 h-16 text-gray-400 mx-auto mb-4" />
        <h3 className="text-lg font-medium text-gray-900 mb-2">Aucun thème sélectionné</h3>
        <p className="text-gray-600">
          Veuillez d'abord sélectionner un thème dans l'onglet "Thèmes" pour gérer ses exercices.
        </p>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Gestion des Exercices</h2>
          <p className="text-gray-600">Thème sélectionné: {selectedTheme.title}</p>
        </div>
        <button
          onClick={() => setShowCreateForm(true)}
          className="bg-orange-600 text-white px-4 py-2 rounded-lg flex items-center hover:bg-orange-700"
        >
          <PlusIcon className="w-5 h-5 mr-2" />
          Nouvel Exercice
        </button>
      </div>

      {/* Create/Edit Form */}
      {showCreateForm && (
        <div className="mb-8 bg-gray-50 p-6 rounded-lg">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-lg font-semibold">
              {editingExercise ? 'Modifier l\'Exercice' : 'Créer un Nouvel Exercice'}
            </h3>
            <div className="flex space-x-2">
              <button
                type="button"
                onClick={() => setShowPreview(!showPreview)}
                className="bg-blue-500 text-white px-3 py-1 rounded text-sm hover:bg-blue-600 flex items-center"
              >
                <Eye className="w-4 h-4 mr-1" />
                {showPreview ? 'Masquer l\'aperçu' : 'Aperçu'}
              </button>
            </div>
          </div>
          
          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Basic Fields */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Titre de l'exercice (ex: "Ejercicio 1.1: Titre")
                </label>
                <input
                  type="text"
                  value={formData.title}
                  onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                  className="w-full p-3 border border-gray-300 rounded-md"
                  placeholder="Ejercicio 1.1: ..."
                  required
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Numéro d'ordre
                </label>
                <input
                  type="number"
                  value={formData.order_number}
                  onChange={(e) => setFormData({ ...formData, order_number: parseInt(e.target.value) })}
                  className="w-full p-3 border border-gray-300 rounded-md"
                  min="1"
                />
              </div>
            </div>

            {/* Parent Title Field */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Titre du groupe (parent_title) - Affiché en haut
              </label>
              <input
                type="text"
                value={formData.parent_title}
                onChange={(e) => setFormData({ ...formData, parent_title: e.target.value })}
                className="w-full p-3 border border-gray-300 rounded-md"
                placeholder="Ex: Ejercicio #1: Historia"
              />
              <p className="text-sm text-gray-500 mt-1">
                Ce titre regroupe plusieurs exercices (ex: tous les exercices 1.1, 1.2, 1.3 afficheront ce titre en haut)
              </p>
            </div>

            {/* Instructions */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Instructions générales
              </label>
              <textarea
                value={formData.instructions}
                onChange={(e) => setFormData({ ...formData, instructions: e.target.value })}
                rows="3"
                className="w-full p-3 border border-gray-300 rounded-md"
                placeholder="Instructions générales pour l'exercice..."
              />
            </div>

            {/* Sub-Exercises */}
            <div className="border-t pt-6">
              <h4 className="text-lg font-semibold mb-4 text-gray-800 flex items-center">
                🎯 Sous-exercices ({formData.exercise_sections.length})
              </h4>

              {/* Add Sub-Exercise Form */}
              <div className="bg-green-50 rounded-lg p-4 mb-4">
                <h5 className="font-medium mb-3">Ajouter un nouveau sous-exercice:</h5>
                <div className="space-y-3">
                  <input
                    type="text"
                    value={newSectionTitle}
                    onChange={(e) => setNewSectionTitle(e.target.value)}
                    placeholder="Titre du sous-exercice..."
                    className="w-full p-3 border border-gray-300 rounded-md"
                  />
                  <textarea
                    value={newSectionInstructions}
                    onChange={(e) => setNewSectionInstructions(e.target.value)}
                    placeholder="Instructions pour ce sous-exercice..."
                    rows="2"
                    className="w-full p-3 border border-gray-300 rounded-md"
                  />
                  <button
                    type="button"
                    onClick={addSection}
                    className="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700"
                  >
                    Ajouter le sous-exercice
                  </button>
                </div>
              </div>

              {/* Sub-Exercises List */}
              {formData.exercise_sections.length > 0 && (
                <div className="space-y-4">
                  {formData.exercise_sections.map((section, sectionIndex) => (
                    <div key={sectionIndex} className="bg-white rounded-lg border-2 border-green-200 p-4">
                      <div className="flex justify-between items-start mb-3">
                        <div className="flex-1">
                          <h5 className="font-semibold text-gray-800 mb-1">
                            📋 {section.title}
                          </h5>
                          {section.instructions && (
                            <p className="text-gray-600 italic text-sm">"{section.instructions}"</p>
                          )}
                        </div>
                        <button
                          type="button"
                          onClick={() => removeSection(sectionIndex)}
                          className="text-red-600 hover:text-red-800 ml-2"
                        >
                          <TrashIcon className="w-4 h-4" />
                        </button>
                      </div>

                      {/* Add Question to Sub-Exercise */}
                      <div className="bg-blue-50 rounded p-3 mb-3">
                        <div className="flex gap-2 mb-2">
                          <select
                            value={questionType}
                            onChange={(e) => setQuestionType(e.target.value)}
                            className="p-2 border border-gray-300 rounded text-sm"
                          >
                            <option value="text">Question texte</option>
                            <option value="table">Question tableau</option>
                          </select>
                        </div>
                        <div className="flex gap-2">
                          <input
                            type="text"
                            value={newQuestion}
                            onChange={(e) => setNewQuestion(e.target.value)}
                            placeholder="Question pour ce sous-exercice..."
                            className="flex-1 p-2 border border-gray-300 rounded text-sm"
                          />
                          <button
                            type="button"
                            onClick={() => addQuestionToSection(sectionIndex)}
                            className="bg-blue-600 text-white px-3 py-2 rounded text-sm hover:bg-blue-700"
                          >
                            Ajouter
                          </button>
                        </div>
                        
                        {/* Table Configuration */}
                        {questionType === 'table' && (
                          <div className="bg-white rounded-md p-3 border mt-2">
                            <h6 className="font-medium mb-2 text-sm">Configuration du tableau:</h6>
                            <div className="space-y-2">
                              {tableConfig.columns.map((col, index) => (
                                <div key={index} className="flex gap-2 items-center">
                                  <input
                                    type="text"
                                    value={col.title}
                                    onChange={(e) => updateColumnTitle(index, e.target.value)}
                                    className="flex-1 p-2 border rounded text-sm"
                                  />
                                  {tableConfig.columns.length > 1 && (
                                    <button
                                      type="button"
                                      onClick={() => removeColumn(index)}
                                      className="text-red-600 hover:text-red-800"
                                    >
                                      ✕
                                    </button>
                                  )}
                                </div>
                              ))}
                              <button
                                type="button"
                                onClick={addColumn}
                                className="text-blue-600 hover:text-blue-800 text-xs"
                              >
                                + Ajouter une colonne
                              </button>
                            </div>
                            <div className="mt-2">
                              <label className="text-xs">Nombre de lignes:</label>
                              <input
                                type="number"
                                value={tableConfig.rows}
                                onChange={(e) => setTableConfig({ ...tableConfig, rows: parseInt(e.target.value) || 3 })}
                                min="1"
                                max="20"
                                className="ml-2 p-1 border rounded w-16 text-sm"
                              />
                            </div>
                          </div>
                        )}
                      </div>

                      {/* Sub-Exercise Questions */}
                      {section.questions && section.questions.length > 0 && (
                        <div className="space-y-2">
                          {section.questions.map((question, questionIndex) => (
                            <div key={questionIndex} className="bg-gray-50 rounded p-3 border-l-4 border-blue-400">
                              <div className="flex justify-between items-start">
                                <div className="flex-1">
                                  <span className="text-gray-800">{question.question}</span>
                                  {question.type === 'table' && (
                                    <div className="text-xs text-gray-500 mt-1">
                                      Tableau: {question.table_config?.columns?.length || 0} colonnes, {question.table_config?.rows || 3} lignes
                                    </div>
                                  )}
                                </div>
                                <button
                                  type="button"
                                  onClick={() => removeQuestionFromSection(sectionIndex, questionIndex)}
                                  className="text-red-600 hover:text-red-800 ml-2"
                                >
                                  <TrashIcon className="w-3 h-3" />
                                </button>
                              </div>
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}

              {formData.exercise_sections.length === 0 && (
                <div className="text-center py-8 text-gray-500 bg-gray-50 rounded-lg">
                  Aucun sous-exercice ajouté. Créez votre premier sous-exercice ci-dessus.
                </div>
              )}
            </div>

            {/* Form Actions */}
            <div className="flex justify-end space-x-4 pt-6 border-t">
              <button
                type="button"
                onClick={handleCancel}
                className="px-4 py-2 text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300"
              >
                Annuler
              </button>
              <button
                type="submit"
                className="px-4 py-2 bg-orange-600 text-white rounded-md hover:bg-orange-700"
              >
                {editingExercise ? 'Mettre à jour' : 'Créer'} l'Exercice
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Preview Section */}
      {showPreview && (showCreateForm || editingExercise) && (
        <div className="mb-8">
          <div className="bg-gradient-to-r from-blue-50 to-indigo-50 border-2 border-blue-200 rounded-lg p-6">
            <div className="flex items-center mb-4">
              <Eye className="w-6 h-6 text-blue-600 mr-2" />
              <h3 className="text-xl font-semibold text-blue-800">Aperçu de l'exercice</h3>
            </div>
            
            <div className="bg-white rounded-lg border border-blue-200 p-6">
              <div className="flex items-center mb-6">
                <span className="text-2xl mr-3">🎯</span>
                <h4 className="text-2xl font-bold text-gray-900">
                  {formData.order_number}. {formData.title || 'Titre de l\'exercice'}
                </h4>
              </div>
              
              {formData.instructions && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                  <h5 className="font-semibold text-gray-800 mb-2 flex items-center">
                    <span className="mr-2">📝</span>
                    Instructions générales
                  </h5>
                  <p className="text-gray-700 leading-relaxed">{formData.instructions}</p>
                </div>
              )}

              {/* Sub-Exercises Preview */}
              {formData.exercise_sections && formData.exercise_sections.length > 0 ? (
                <div className="space-y-6">
                  <h5 className="text-lg font-semibold text-gray-800 mb-4 flex items-center">
                    <span className="mr-2">🎯</span>
                    Sous-exercices ({formData.exercise_sections.length})
                  </h5>
                  {formData.exercise_sections.map((section, sectionIndex) => (
                    <div key={sectionIndex} className="bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl border-2 border-green-200 p-5">
                      <div className="mb-4">
                        <h6 className="text-xl font-bold text-green-800 mb-3 flex items-center">
                          <span className="mr-2">📋</span>
                          {section.title}
                        </h6>
                        {section.instructions && (
                          <div className="bg-white/80 rounded-lg p-4 border border-green-200">
                            <h7 className="font-medium text-green-900 mb-2 block">Instructions:</h7>
                            <p className="text-green-800 italic leading-relaxed">"{section.instructions}"</p>
                          </div>
                        )}
                      </div>

                      {section.questions && section.questions.length > 0 ? (
                        <div className="space-y-3">
                          <h7 className="font-semibold text-gray-800 text-sm">Questions ({section.questions.length}):</h7>
                          {section.questions.map((question, questionIndex) => (
                            <div key={questionIndex} className="bg-white rounded-lg border border-green-200 p-4">
                              <div className="flex items-start">
                                <span className="bg-green-100 text-green-800 text-xs font-medium px-2 py-1 rounded-full mr-3 mt-1">
                                  Q{questionIndex + 1}
                                </span>
                                <div className="flex-1">
                                  <div className="font-medium text-gray-800 mb-2">
                                    {question.question}
                                  </div>
                                  {question.type === 'table' && question.table_config && (
                                    <div className="bg-blue-50 rounded-md p-3 border border-blue-200">
                                      <div className="flex items-center text-sm text-blue-800">
                                        <span className="mr-2">📊</span>
                                        <span className="font-medium">Tableau à remplir:</span>
                                      </div>
                                      <div className="text-xs text-blue-600 mt-1">
                                        {question.table_config.columns?.length || 0} colonnes × {question.table_config.rows || 3} lignes
                                      </div>
                                      {question.table_config.columns && question.table_config.columns.length > 0 && (
                                        <div className="mt-2">
                                          <div className="text-xs text-blue-700 font-medium mb-1">Colonnes:</div>
                                          <div className="flex flex-wrap gap-1">
                                            {question.table_config.columns.map((col, colIndex) => (
                                              <span key={colIndex} className="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded">
                                                {col.title}
                                              </span>
                                            ))}
                                          </div>
                                        </div>
                                      )}
                                    </div>
                                  )}
                                </div>
                              </div>
                            </div>
                          ))}
                        </div>
                      ) : (
                        <div className="text-center py-4 text-gray-500 bg-gray-50 rounded-lg border border-gray-200">
                          <span className="text-sm">Aucune question ajoutée à ce sous-exercice</span>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              ) : (
                <div className="text-center py-8 text-gray-500 bg-gray-50 rounded-lg border border-gray-200">
                  <span className="text-sm">Aucun sous-exercice ajouté</span>
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Exercises List */}
      <div className="space-y-4">
        {exercises.length === 0 ? (
          <div className="text-center py-8 text-gray-500">
            Aucun exercice trouvé pour ce thème. Créez votre premier exercice !
          </div>
        ) : (
          exercises.map((exercise) => (
            <div
              key={exercise.id}
              className="border-2 border-orange-200 bg-orange-50 rounded-lg p-4 hover:shadow-md transition-shadow"
            >
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <div className="flex items-center mb-3">
                    <span className="text-lg mr-2">🎯</span>
                    <div>
                      <h3 className="text-lg font-semibold text-gray-900">
                        {exercise.order_number}. {exercise.title}
                      </h3>
                      {exercise.parent_title && (
                        <p className="text-sm text-purple-600 mt-1">
                          📂 Groupe: {exercise.parent_title}
                        </p>
                      )}
                    </div>
                  </div>
                  
                  {/* Sub-Exercises */}
                  {exercise.exercise_sections && exercise.exercise_sections.length > 0 && (
                    <div className="space-y-3">
                      <h4 className="font-medium text-gray-900">Sous-exercices :</h4>
                      {exercise.exercise_sections.map((section, sectionIndex) => (
                        <div key={sectionIndex} className="bg-green-50 rounded-md p-3 border border-green-200">
                          <h5 className="font-medium text-green-900 mb-2">
                            📋 {section.title}
                          </h5>
                          {section.instructions && (
                            <p className="text-green-800 italic text-sm mb-2">"{section.instructions}"</p>
                          )}
                          {section.questions && section.questions.length > 0 && (
                            <div className="space-y-1">
                              {section.questions.map((question, qIndex) => (
                                <div key={qIndex} className="text-sm text-gray-700 pl-3 border-l-2 border-green-300">
                                  {question.question}
                                  {question.type === 'table' && <span className="text-xs text-gray-500 ml-1">(Tableau)</span>}
                                </div>
                              ))}
                            </div>
                          )}
                        </div>
                      ))}
                    </div>
                  )}

                  {exercise.instructions && (
                    <div className="bg-gray-50 rounded-md p-3 mt-3">
                      <h4 className="font-medium text-gray-900 mb-2">Instructions générales :</h4>
                      <p className="text-gray-700">{exercise.instructions}</p>
                    </div>
                  )}
                </div>

                <div className="flex space-x-2 ml-4">
                  <button
                    onClick={() => handleEdit(exercise)}
                    className="text-blue-600 hover:text-blue-800"
                  >
                    <PencilIcon className="w-5 h-5" />
                  </button>
                  <button
                    onClick={() => handleDelete(exercise.id)}
                    className="text-red-600 hover:text-red-800"
                  >
                    <TrashIcon className="w-5 h-5" />
                  </button>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default ExercisesTab;