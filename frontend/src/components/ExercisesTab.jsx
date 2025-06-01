import React, { useState, useEffect } from 'react';
import { PlusIcon, PencilIcon, TrashIcon, ExclamationTriangleIcon } from '@heroicons/react/24/outline';

const ExercisesTab = ({ selectedTheme, themes, exercises, onLoadExercises }) => {
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingExercise, setEditingExercise] = useState(null);
  const [formData, setFormData] = useState({
    title: '',
    question: '',
    instructions: '',
    order_number: exercises.length + 1
  });

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

    try {
      const token = localStorage.getItem('token');
      const url = editingExercise 
        ? `/api/exercises/${editingExercise.id}` 
        : `/api/themes/${selectedTheme.id}/exercises`;
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
    if (!confirm('Êtes-vous sûr de vouloir supprimer cet exercice ?')) return;
    
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`/api/exercises/${exerciseId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });

      if (response.ok && selectedTheme) {
        onLoadExercises(selectedTheme.id);
      }
    } catch (error) {
      console.error('Error deleting exercise:', error);
    }
  };

  const handleEdit = (exercise) => {
    setEditingExercise(exercise);
    setFormData({
      title: exercise.title,
      question: exercise.question,
      instructions: exercise.instructions || '',
      order_number: exercise.order_number
    });
    setShowCreateForm(true);
  };

  const resetForm = () => {
    setFormData({
      title: '',
      question: '',
      instructions: '',
      order_number: exercises.length + 1
    });
  };

  const handleCancel = () => {
    setShowCreateForm(false);
    setEditingExercise(null);
    resetForm();
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
          <h3 className="text-lg font-semibold mb-4">
            {editingExercise ? 'Modifier l\'Exercice' : 'Créer un Nouvel Exercice'}
          </h3>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
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
                  placeholder="Ex: Exercice de réflexion personnelle"
                />
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
                Question principale *
              </label>
              <textarea
                value={formData.question}
                onChange={(e) => setFormData({ ...formData, question: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2"
                rows="4"
                placeholder="Formulez la question ou consigne principale de l'exercice..."
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Instructions complémentaires
              </label>
              <textarea
                value={formData.instructions}
                onChange={(e) => setFormData({ ...formData, instructions: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2"
                rows="4"
                placeholder="Instructions détaillées pour guider l'utilisateur (optionnel)..."
              />
            </div>

            <div className="flex space-x-4">
              <button
                type="submit"
                className="bg-orange-600 text-white px-6 py-2 rounded-lg hover:bg-orange-700"
              >
                {editingExercise ? 'Mettre à jour' : 'Créer'}
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
                    <h3 className="text-lg font-semibold text-gray-900">
                      {exercise.order_number}. {exercise.title}
                    </h3>
                  </div>
                  
                  <div className="bg-white rounded-md p-3 mb-3">
                    <h4 className="font-medium text-gray-900 mb-2">Question :</h4>
                    <p className="text-gray-700">{exercise.question}</p>
                  </div>

                  {exercise.instructions && (
                    <div className="bg-white rounded-md p-3 mb-3">
                      <h4 className="font-medium text-gray-900 mb-2">Instructions :</h4>
                      <p className="text-gray-700">{exercise.instructions}</p>
                    </div>
                  )}

                  <div className="flex items-center space-x-4 text-sm text-gray-500">
                    <span>ID: {exercise.id}</span>
                    {exercise.user_response && (
                      <span className="px-2 py-1 bg-green-100 text-green-800 rounded-full text-xs">
                        Répondu
                      </span>
                    )}
                  </div>
                </div>
                
                <div className="flex space-x-2 ml-4">
                  <button
                    onClick={() => handleEdit(exercise)}
                    className="text-orange-600 hover:text-orange-800 p-2"
                  >
                    <PencilIcon className="w-5 h-5" />
                  </button>
                  <button
                    onClick={() => handleDelete(exercise.id)}
                    className="text-red-600 hover:text-red-800 p-2"
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