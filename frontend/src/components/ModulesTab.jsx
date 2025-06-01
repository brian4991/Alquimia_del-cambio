import React, { useState } from 'react';
import { PlusIcon, PencilIcon, TrashIcon } from '@heroicons/react/24/outline';

const ModulesTab = ({ modules, onModuleSelect, onReload }) => {
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingModule, setEditingModule] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    objective: '',
    belief_to_transform: '',
    expected_results: '',
    recommended_book: '',
    audio_file: '',
    order_number: 1
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    
    try {
      const token = localStorage.getItem('token');
      const url = editingModule ? `/api/modules/${editingModule.id}` : '/api/modules';
      const method = editingModule ? 'PUT' : 'POST';
      
      console.log(`${method} request to ${url}`, formData); // Debug log
      
      const response = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(formData)
      });

      const responseData = await response.json();
      console.log('Response:', response.status, responseData); // Debug log

      if (response.ok) {
        setShowCreateForm(false);
        setEditingModule(null);
        resetForm();
        onReload();
        alert(editingModule ? 'Module mis à jour avec succès!' : 'Module créé avec succès!');
      } else {
        const errorMessage = responseData.detail || responseData.message || `Erreur ${response.status}`;
        setError(errorMessage);
        console.error('API Error:', errorMessage);
      }
    } catch (error) {
      console.error('Network Error:', error);
      setError('Erreur de connexion. Vérifiez que le serveur backend est démarré.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleDelete = async (moduleId) => {
    if (!confirm('Êtes-vous sûr de vouloir supprimer ce module ?')) return;
    
    setIsLoading(true);
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`/api/modules/${moduleId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });

      if (response.ok) {
        onReload();
        alert('Module supprimé avec succès!');
      } else {
        const errorData = await response.json();
        alert(`Erreur lors de la suppression: ${errorData.detail || 'Erreur inconnue'}`);
      }
    } catch (error) {
      console.error('Error deleting module:', error);
      alert('Erreur de connexion lors de la suppression.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleEdit = (module) => {
    setEditingModule(module);
    setError(null);
    setFormData({
      title: module.title || '',
      description: module.description || '',
      objective: module.objective || '',
      belief_to_transform: module.belief_to_transform || '',
      expected_results: module.expected_results || '',
      recommended_book: module.recommended_book || '',
      audio_file: module.audio_file || '',
      order_number: module.order_number || 1
    });
    setShowCreateForm(true);
  };

  const resetForm = () => {
    setFormData({
      title: '',
      description: '',
      objective: '',
      belief_to_transform: '',
      expected_results: '',
      recommended_book: '',
      audio_file: '',
      order_number: Math.max(1, Array.isArray(modules) ? modules.length + 1 : 1)
    });
    setError(null);
  };

  const handleCancel = () => {
    setShowCreateForm(false);
    setEditingModule(null);
    resetForm();
  };

  // Sécurité : s'assurer que modules est un array
  const safeModules = Array.isArray(modules) ? modules : [];

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-900">Gestion des Modules</h2>
        <button
          onClick={() => setShowCreateForm(true)}
          className="bg-blue-600 text-white px-4 py-2 rounded-lg flex items-center hover:bg-blue-700"
        >
          <PlusIcon className="w-5 h-5 mr-2" />
          Nouveau Module
        </button>
      </div>

      {/* Create/Edit Form */}
      {showCreateForm && (
        <div className="mb-8 bg-gray-50 p-6 rounded-lg">
          <h3 className="text-lg font-semibold mb-4">
            {editingModule ? 'Modifier le Module' : 'Créer un Nouveau Module'}
          </h3>
          
          {/* Error Message */}
          {error && (
            <div className="mb-4 p-4 bg-red-50 border border-red-200 rounded-md">
              <p className="text-red-700 text-sm">{error}</p>
            </div>
          )}
          
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
                  className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  required
                  disabled={isLoading}
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Numéro d'ordre
                </label>
                <input
                  type="number"
                  value={formData.order_number}
                  onChange={(e) => setFormData({ ...formData, order_number: parseInt(e.target.value) || 1 })}
                  className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  required
                  min="1"
                  disabled={isLoading}
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Description
              </label>
              <textarea
                value={formData.description}
                onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                rows="3"
                disabled={isLoading}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Objectif
              </label>
              <textarea
                value={formData.objective}
                onChange={(e) => setFormData({ ...formData, objective: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                rows="3"
                disabled={isLoading}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Croyance à transformer
              </label>
              <textarea
                value={formData.belief_to_transform}
                onChange={(e) => setFormData({ ...formData, belief_to_transform: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                rows="3"
                disabled={isLoading}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Résultats attendus
              </label>
              <textarea
                value={formData.expected_results}
                onChange={(e) => setFormData({ ...formData, expected_results: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                rows="3"
                disabled={isLoading}
              />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Livre recommandé
                </label>
                <input
                  type="text"
                  value={formData.recommended_book}
                  onChange={(e) => setFormData({ ...formData, recommended_book: e.target.value })}
                  className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  disabled={isLoading}
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Fichier audio
                </label>
                <input
                  type="text"
                  value={formData.audio_file}
                  onChange={(e) => setFormData({ ...formData, audio_file: e.target.value })}
                  className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  placeholder="URL ou nom du fichier"
                  disabled={isLoading}
                />
              </div>
            </div>

            <div className="flex space-x-4">
              <button
                type="submit"
                disabled={isLoading}
                className={`px-6 py-2 rounded-lg flex items-center ${
                  isLoading 
                    ? 'bg-gray-400 cursor-not-allowed' 
                    : 'bg-blue-600 hover:bg-blue-700'
                } text-white transition-colors`}
              >
                {isLoading && (
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                )}
                {isLoading 
                  ? (editingModule ? 'Mise à jour...' : 'Création...') 
                  : (editingModule ? 'Mettre à jour' : 'Créer')
                }
              </button>
              <button
                type="button"
                onClick={handleCancel}
                disabled={isLoading}
                className="bg-gray-300 text-gray-700 px-6 py-2 rounded-lg hover:bg-gray-400 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                Annuler
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Modules List */}
      <div className="space-y-4">
        {safeModules.length === 0 ? (
          <div className="text-center py-8 text-gray-500">
            {safeModules === modules ? 'Aucun module trouvé. Créez votre premier module !' : 'Chargement des modules...'}
          </div>
        ) : (
          safeModules.map((module) => (
            <div
              key={module.id}
              className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer"
              onClick={() => onModuleSelect(module)}
            >
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <h3 className="text-lg font-semibold text-gray-900 mb-2">
                    {module.order_number}. {module.title}
                  </h3>
                  {module.description && (
                    <p className="text-gray-600 mb-2">{module.description}</p>
                  )}
                  <div className="flex items-center space-x-4 text-sm text-gray-500">
                    <span>ID: {module.id}</span>
                    {module.audio_file && <span>🎵 Audio</span>}
                    {module.recommended_book && <span>📚 Livre</span>}
                  </div>
                </div>
                <div className="flex space-x-2 ml-4">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleEdit(module);
                    }}
                    disabled={isLoading}
                    className="text-blue-600 hover:text-blue-800 p-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                    title="Modifier ce module"
                  >
                    <PencilIcon className="w-5 h-5" />
                  </button>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleDelete(module.id);
                    }}
                    disabled={isLoading}
                    className="text-red-600 hover:text-red-800 p-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                    title="Supprimer ce module"
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

export default ModulesTab; 
