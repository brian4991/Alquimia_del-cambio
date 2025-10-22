import React, { useState, useEffect } from 'react';
import { PlusIcon, PencilIcon, TrashIcon, ExclamationTriangleIcon, BookOpenIcon } from '@heroicons/react/24/outline';
import { config } from '../config';

const RecursosTab = ({ selectedModule, modules, selectedRecurso, onRecursoSelect, onLoadRecursos }) => {
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingRecurso, setEditingRecurso] = useState(null);
  const [recursos, setRecursos] = useState([]);
  const [formData, setFormData] = useState({
    title: '',
    content: '',
    order_number: 1
  });

  // Load recursos when module is selected
  useEffect(() => {
    if (selectedModule) {
      fetchRecursos(selectedModule.id);
    }
  }, [selectedModule]);

  const fetchRecursos = async (moduleId) => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/modules/${moduleId}/themes`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const themes = await response.json();
      // Filter only recursos (theme_type = "resource")
      const recursosData = themes.filter(theme => theme.theme_type === 'resource');
      setRecursos(recursosData);
      if (onLoadRecursos) {
        onLoadRecursos(recursosData);
      }
    } catch (error) {
      console.error('Error fetching recursos:', error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedModule) {
      alert('Por favor, selecciona primero un módulo');
      return;
    }

    try {
      const token = localStorage.getItem('token');
      const url = editingRecurso 
        ? `${config.apiUrl}/themes/${editingRecurso.id}` 
        : `${config.apiUrl}/modules/${selectedModule.id}/themes`;
      const method = editingRecurso ? 'PUT' : 'POST';
      
      const response = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          ...formData,
          theme_type: 'resource'  // Mark as resource
        })
      });

      if (response.ok) {
        setShowCreateForm(false);
        setEditingRecurso(null);
        resetForm();
        fetchRecursos(selectedModule.id);
      }
    } catch (error) {
      console.error('Error saving recurso:', error);
    }
  };

  const handleDelete = async (recursoId) => {
    if (!confirm('¿Estás seguro de querer eliminar este recurso?')) return;
    
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/themes/${recursoId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });

      if (response.ok && selectedModule) {
        fetchRecursos(selectedModule.id);
      }
    } catch (error) {
      console.error('Error deleting recurso:', error);
    }
  };

  const handleEdit = (recurso) => {
    setEditingRecurso(recurso);
    setFormData({
      title: recurso.title,
      content: recurso.content || '',
      order_number: recurso.order_number
    });
    setShowCreateForm(true);
  };

  const resetForm = () => {
    setFormData({
      title: '',
      content: '',
      order_number: recursos.length + 1
    });
  };

  const handleCancel = () => {
    setShowCreateForm(false);
    setEditingRecurso(null);
    resetForm();
  };

  if (!selectedModule) {
    return (
      <div className="text-center py-12">
        <ExclamationTriangleIcon className="w-16 h-16 text-gray-400 mx-auto mb-4" />
        <h3 className="text-lg font-medium text-gray-900 mb-2">Ningún módulo seleccionado</h3>
        <p className="text-gray-600">
          Por favor, selecciona primero un módulo en la pestaña "Módulos" para gestionar sus recursos.
        </p>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Gestión de Recursos</h2>
          <p className="text-gray-600">Módulo seleccionado: {selectedModule.title}</p>
          <p className="text-sm text-amber-600 mt-1">
            💡 Los recursos son contenidos adicionales mostrados en columna a la derecha de los temas
          </p>
        </div>
        <button
          onClick={() => setShowCreateForm(true)}
          className="bg-amber-600 text-white px-4 py-2 rounded-lg flex items-center hover:bg-amber-700"
        >
          <PlusIcon className="w-5 h-5 mr-2" />
          Nuevo Recurso
        </button>
      </div>

      {/* Create/Edit Form */}
      {showCreateForm && (
        <div className="mb-8 bg-amber-50 p-6 rounded-lg border-2 border-amber-200">
          <h3 className="text-lg font-semibold mb-4 text-amber-900">
            {editingRecurso ? 'Modificar Recurso' : 'Crear Nuevo Recurso'}
          </h3>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Título del Recurso *
                </label>
                <input
                  type="text"
                  value={formData.title}
                  onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                  className="w-full border border-gray-300 rounded-md px-3 py-2"
                  placeholder="Ej: Libro Recomendado"
                  required
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Número de orden
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
                Descripción del Recurso *
              </label>
              <textarea
                value={formData.content}
                onChange={(e) => setFormData({ ...formData, content: e.target.value })}
                className="w-full border border-gray-300 rounded-md px-3 py-2 h-32"
                placeholder="Descripción corta del recurso..."
                required
              />
            </div>

            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
              <h4 className="font-medium text-blue-900 mb-2">💡 Nota importante</h4>
              <p className="text-sm text-blue-800">
                Después de crear el recurso, ve a la pestaña <strong>"Cartas"</strong> para añadir 
                el contenido detallado en forma de cartas (como para los temas normales).
              </p>
            </div>

            <div className="flex space-x-4">
              <button
                type="submit"
                className="bg-amber-600 text-white px-6 py-2 rounded-lg hover:bg-amber-700"
              >
                {editingRecurso ? 'Actualizar' : 'Crear'}
              </button>
              <button
                type="button"
                onClick={handleCancel}
                className="bg-gray-300 text-gray-700 px-6 py-2 rounded-lg hover:bg-gray-400"
              >
                Cancelar
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Recursos List */}
      <div className="space-y-4">
        {recursos.length === 0 ? (
          <div className="text-center py-12 bg-amber-50 rounded-lg border-2 border-dashed border-amber-300">
            <BookOpenIcon className="w-16 h-16 text-amber-400 mx-auto mb-4" />
            <p className="text-amber-800 mb-2">No se encontraron recursos para este módulo.</p>
            <p className="text-amber-600 text-sm">¡Crea tu primer recurso!</p>
          </div>
        ) : (
          recursos.map((recurso) => (
            <div
              key={recurso.id}
              onClick={() => onRecursoSelect && onRecursoSelect(recurso)}
              className={`border-2 rounded-lg p-4 hover:shadow-md transition-all cursor-pointer ${
                selectedRecurso && selectedRecurso.id === recurso.id
                  ? 'border-amber-400 bg-amber-50 bg-opacity-60 shadow-md ring-1 ring-amber-400 ring-opacity-30'
                  : 'border-amber-200 bg-amber-50 bg-opacity-30'
              }`}
            >
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <div className="flex items-center mb-2">
                    <span className="text-2xl mr-2">📚</span>
                    <h3 className="text-lg font-semibold text-gray-900">
                      {recurso.order_number}. {recurso.title}
                    </h3>
                    <span className="ml-2 px-2 py-1 bg-amber-200 text-amber-800 rounded-full text-xs font-medium">
                      Recurso
                    </span>
                  </div>
                  <p className="text-gray-700 mb-3">{recurso.content}</p>
                  <div className="flex items-center space-x-4 text-sm text-gray-500">
                    <span>ID: {recurso.id}</span>
                    <span>Module: {selectedModule.title}</span>
                  </div>
                </div>
                <div className="flex space-x-2 ml-4">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleEdit(recurso);
                    }}
                    className="text-amber-600 hover:text-amber-800 p-2"
                  >
                    <PencilIcon className="w-5 h-5" />
                  </button>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleDelete(recurso.id);
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

export default RecursosTab;

