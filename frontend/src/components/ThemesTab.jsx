import React, { useState, useEffect } from 'react';
import { PlusIcon, PencilIcon, TrashIcon, ExclamationTriangleIcon } from '@heroicons/react/24/outline';
import { config } from '../config';

const ThemesTab = ({ selectedModule, selectedTheme, themes, modules, onThemeSelect, onLoadThemes }) => {
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingTheme, setEditingTheme] = useState(null);
  const [formData, setFormData] = useState({
    title: '',
    content: '',
    order_number: 1
  });

  // Load themes when module is selected
  useEffect(() => {
    if (selectedModule) {
      onLoadThemes(selectedModule.id);
    }
  }, [selectedModule]);

  // Filter out recursos (only show normal themes)
  const normalThemes = themes.filter(theme => {
    console.log('[DEBUG] Theme:', theme.title, 'type:', theme.theme_type);
    return !theme.theme_type || theme.theme_type === 'theme';
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedModule) {
      alert('Veuillez sélectionner un module d\'abord');
      return;
    }

    try {
      const token = localStorage.getItem('token');
      const url = editingTheme 
        ? `${config.apiUrl}/themes/${editingTheme.id}` 
        : `${config.apiUrl}/modules/${selectedModule.id}/themes`;
      const method = editingTheme ? 'PUT' : 'POST';
      
      const response = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          ...formData,
          theme_type: 'theme'  // Explicitly mark as theme (not resource)
        })
      });

      if (response.ok) {
        setShowCreateForm(false);
        setEditingTheme(null);
        resetForm();
        onLoadThemes(selectedModule.id);
      }
    } catch (error) {
      console.error('Error saving theme:', error);
    }
  };

  const handleDelete = async (themeId) => {
    if (!confirm('Êtes-vous sûr de vouloir supprimer ce thème ?')) return;
    
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/themes/${themeId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });

      if (response.ok && selectedModule) {
        onLoadThemes(selectedModule.id);
      }
    } catch (error) {
      console.error('Error deleting theme:', error);
    }
  };

  const handleEdit = (theme) => {
    setEditingTheme(theme);
    setFormData({
      title: theme.title,
      content: theme.content || '',
      order_number: theme.order_number
    });
    setShowCreateForm(true);
  };

  const resetForm = () => {
    setFormData({
      title: '',
      content: '',
      order_number: normalThemes.length + 1
    });
  };

  const handleCancel = () => {
    setShowCreateForm(false);
    setEditingTheme(null);
    resetForm();
  };

  if (!selectedModule) {
    return (
      <div className="text-center py-12">
        <ExclamationTriangleIcon className="w-16 h-16 text-gray-400 mx-auto mb-4" />
        <h3 className="text-lg font-medium text-gray-900 mb-2">Aucun module sélectionné</h3>
        <p className="text-gray-600">
          Veuillez d'abord sélectionner un module dans l'onglet "Modules" pour gérer ses thèmes.
        </p>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Gestion des Thèmes</h2>
          <p className="text-gray-600">Module sélectionné: {selectedModule.title}</p>
        </div>
        <button
          onClick={() => setShowCreateForm(true)}
          className="bg-green-600 text-white px-4 py-2 rounded-lg flex items-center hover:bg-green-700"
        >
          <PlusIcon className="w-5 h-5 mr-2" />
          Nouveau Thème
        </button>
      </div>

      {/* Create/Edit Form */}
      {showCreateForm && (
        <div className="mb-8 bg-gray-50 p-6 rounded-lg">
          <h3 className="text-lg font-semibold mb-4">
            {editingTheme ? 'Modifier le Thème' : 'Créer un Nouveau Thème'}
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
                Contenu
              </label>
              <textarea
                value={formData.content}
                onChange={(e) => setFormData({ ...formData, content: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2"
                rows="6"
                placeholder="Contenu descriptif du thème..."
              />
            </div>

            <div className="flex space-x-4">
              <button
                type="submit"
                className="bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700"
              >
                {editingTheme ? 'Mettre à jour' : 'Créer'}
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

      {/* Themes List */}
      <div className="space-y-4">
        {normalThemes.length === 0 ? (
          <div className="text-center py-8 text-gray-500">
            Aucun thème trouvé pour ce module. Créez votre premier thème !
          </div>
        ) : (
          normalThemes.map((theme) => (
            <div
              key={theme.id}
              className={`border rounded-lg p-4 hover:shadow-md transition-all cursor-pointer ${
                selectedTheme && selectedTheme.id === theme.id
                  ? 'border-green-500 bg-green-50 shadow-md ring-2 ring-green-200'
                  : 'border-gray-200 hover:border-gray-300'
              }`}
              onClick={() => onThemeSelect(theme)}
            >
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <h3 className="text-lg font-semibold text-gray-900 mb-2">
                    {theme.order_number}. {theme.title}
                  </h3>
                  {theme.content && (
                    <p className="text-gray-600 mb-2 line-clamp-3">{theme.content}</p>
                  )}
                  <div className="flex items-center space-x-4 text-sm text-gray-500">
                    <span>ID: {theme.id}</span>
                    <span>📊 {theme.total_cards} cartes</span>
                    <span className={`px-2 py-1 rounded-full text-xs ${
                      theme.is_completed ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'
                    }`}>
                      {theme.is_completed ? 'Terminé' : 'En cours'}
                    </span>
                  </div>
                </div>
                <div className="flex space-x-2 ml-4">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleEdit(theme);
                    }}
                    className="text-green-600 hover:text-green-800 p-2"
                  >
                    <PencilIcon className="w-5 h-5" />
                  </button>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleDelete(theme.id);
                    }}
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

export default ThemesTab; 
