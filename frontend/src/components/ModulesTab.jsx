import React, { useState } from 'react';
import { PlusIcon, PencilIcon, TrashIcon } from '@heroicons/react/24/outline';
import { config } from '../config';

const ModulesTab = ({ modules, selectedModule, onModuleSelect, onReload }) => {
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingModule, setEditingModule] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [audioFile, setAudioFile] = useState(null);
  const [uploadingAudio, setUploadingAudio] = useState(false);
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

  const handleAudioUpload = async (file) => {
    if (!file) return null;
    
    setUploadingAudio(true);
    try {
      const token = localStorage.getItem('token');
      const uploadFormData = new FormData();
      uploadFormData.append('file', file);
      
      const response = await fetch(`${config.apiUrl}/api/upload/audio`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`
        },
        body: uploadFormData
      });
      
      const data = await response.json();
      if (response.ok) {
        return data.filename;
      } else {
        throw new Error(data.detail || 'Upload failed');
      }
    } catch (error) {
      console.error('Audio upload error:', error);
      setError(`Error al subir audio: ${error.message}`);
      return null;
    } finally {
      setUploadingAudio(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    
    try {
      // Upload audio file if present
      let audioFileName = formData.audio_file;
      if (audioFile) {
        const uploadedFileName = await handleAudioUpload(audioFile);
        if (uploadedFileName) {
          audioFileName = uploadedFileName;
        } else {
          setIsLoading(false);
          return; // Stop if upload failed
        }
      }
      
      const token = localStorage.getItem('token');
      const url = editingModule ? `${config.apiUrl}/modules/${editingModule.id}` : `${config.apiUrl}/modules`;
      const method = editingModule ? 'PUT' : 'POST';
      
      const dataToSubmit = {
        ...formData,
        audio_file: audioFileName
      };
      
      console.log(`${method} request to ${url}`, dataToSubmit); // Debug log
      
      const response = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(dataToSubmit)
      });

      const responseData = await response.json();
      console.log('Response:', response.status, responseData); // Debug log

      if (response.ok) {
        setShowCreateForm(false);
        setEditingModule(null);
        resetForm();
        onReload();
        alert(editingModule ? '¡Módulo actualizado con éxito!' : '¡Módulo creado con éxito!');
      } else {
        const errorMessage = responseData.detail || responseData.message || `Error ${response.status}`;
        setError(errorMessage);
        console.error('API Error:', errorMessage);
      }
    } catch (error) {
      console.error('Network Error:', error);
      setError('Error de conexión. Verifica que el servidor backend esté iniciado.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleDelete = async (moduleId) => {
    if (!confirm('¿Estás seguro de querer eliminar este módulo?')) return;
    
    setIsLoading(true);
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/modules/${moduleId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });

      if (response.ok) {
        onReload();
        alert('¡Módulo eliminado con éxito!');
      } else {
        const errorData = await response.json();
        alert(`Error al eliminar: ${errorData.detail || 'Error desconocido'}`);
      }
    } catch (error) {
      console.error('Error deleting module:', error);
      alert('Error de conexión al eliminar.');
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
    setAudioFile(null);
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
        <h2 className="text-2xl font-bold text-gray-900">Gestión de Módulos</h2>
        <button
          onClick={() => setShowCreateForm(true)}
          className="bg-sage text-white px-4 py-2 rounded-lg flex items-center hover:bg-sage-dark transition-colors"
        >
          <PlusIcon className="w-5 h-5 mr-2" />
          Nuevo Módulo
        </button>
      </div>

      {/* Create/Edit Form */}
      {showCreateForm && (
        <div className="mb-8 bg-beige p-6 rounded-lg border border-gray-200">
          <h3 className="text-lg font-semibold mb-4 text-sage-dark">
            {editingModule ? 'Modificar Módulo' : 'Crear Nuevo Módulo'}
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
                  Título *
                </label>
                <input
                  type="text"
                  value={formData.title}
                  onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                  className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-sage focus:border-sage"
                  required
                  disabled={isLoading}
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Número de orden
                </label>
                <input
                  type="number"
                  value={formData.order_number}
                  onChange={(e) => setFormData({ ...formData, order_number: parseInt(e.target.value) || 1 })}
                  className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-sage focus:border-sage"
                  required
                  min="1"
                  disabled={isLoading}
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Descripción
              </label>
              <textarea
                value={formData.description}
                onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-sage focus:border-sage"
                rows="3"
                disabled={isLoading}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Objetivo
              </label>
              <textarea
                value={formData.objective}
                onChange={(e) => setFormData({ ...formData, objective: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-sage focus:border-sage"
                rows="3"
                disabled={isLoading}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Creencia a transformar
              </label>
              <textarea
                value={formData.belief_to_transform}
                onChange={(e) => setFormData({ ...formData, belief_to_transform: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-sage focus:border-sage"
                rows="3"
                disabled={isLoading}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Resultados esperados
              </label>
              <textarea
                value={formData.expected_results}
                onChange={(e) => setFormData({ ...formData, expected_results: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-sage focus:border-sage"
                rows="3"
                disabled={isLoading}
              />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Libro recomendado
                </label>
                <input
                  type="text"
                  value={formData.recommended_book}
                  onChange={(e) => setFormData({ ...formData, recommended_book: e.target.value })}
                  className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-sage focus:border-sage"
                  disabled={isLoading}
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Archivo de audio (MP3)
                </label>
                <div className="space-y-2">
                  <input
                    type="file"
                    accept=".mp3,audio/mpeg"
                    onChange={(e) => setAudioFile(e.target.files[0])}
                    className="w-full border border-gray-300 rounded-md px-3 py-2 focus:ring-2 focus:ring-sage focus:border-sage"
                    disabled={isLoading || uploadingAudio}
                  />
                  {audioFile && (
                    <p className="text-sm text-gray-600">
                      Archivo seleccionado: {audioFile.name}
                    </p>
                  )}
                  {formData.audio_file && !audioFile && (
                    <p className="text-sm text-green-600">
                      Archivo actual: {formData.audio_file}
                    </p>
                  )}
                  {uploadingAudio && (
                    <p className="text-sm text-sage">
                      Subiendo...
                    </p>
                  )}
                </div>
              </div>
            </div>

            <div className="flex space-x-4">
              <button
                type="submit"
                disabled={isLoading}
                className={`px-6 py-2 rounded-lg flex items-center ${
                  isLoading 
                    ? 'bg-gray-400 cursor-not-allowed' 
                    : 'bg-sage hover:bg-sage-dark'
                } text-white transition-colors`}
              >
                {isLoading && (
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                )}
                {isLoading 
                  ? (editingModule ? 'Actualizando...' : 'Creando...') 
                  : (editingModule ? 'Actualizar' : 'Crear')
                }
              </button>
              <button
                type="button"
                onClick={handleCancel}
                disabled={isLoading}
                className="bg-gray-300 text-gray-700 px-6 py-2 rounded-lg hover:bg-gray-400 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                Cancelar
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Modules List */}
      <div className="space-y-4">
        {safeModules.length === 0 ? (
          <div className="text-center py-8 text-gray-500">
            {safeModules === modules ? 'No se encontraron módulos. ¡Crea tu primer módulo!' : 'Cargando módulos...'}
          </div>
        ) : (
          safeModules.map((module) => (
            <div
              key={module.id}
              className={`border-2 rounded-lg p-4 hover:shadow-sage transition-all cursor-pointer ${
                selectedModule && selectedModule.id === module.id
                  ? 'border-sage bg-sage bg-opacity-5 shadow-sage ring-2 ring-sage-light'
                  : 'border-gray-200 hover:border-sage-light'
              }`}
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
                    className="text-sage hover:text-sage-dark p-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                    title="Modificar este módulo"
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
                    title="Eliminar este módulo"
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
