import React, { useState } from 'react';
import { XMarkIcon, UserGroupIcon, DocumentMagnifyingGlassIcon, CalendarDaysIcon } from '@heroicons/react/24/outline';
import { config } from '../../config';

/**
 * Meeting Launcher - Modal to create new team meetings
 */
const MeetingLauncher = ({ onClose, onMeetingCreated }) => {
  const [meetingType, setMeetingType] = useState('brainstorm');
  const [brief, setBrief] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const meetingTypes = [
    {
      id: 'brainstorm',
      label: 'Brainstorming',
      description: 'Generar ideas y propuestas creativas',
      icon: UserGroupIcon,
      color: 'bg-purple-100 text-purple-800 border-purple-200',
    },
    {
      id: 'review',
      label: 'Review',
      description: 'Revisar y mejorar contenido existente',
      icon: DocumentMagnifyingGlassIcon,
      color: 'bg-blue-100 text-blue-800 border-blue-200',
    },
    {
      id: 'planning',
      label: 'Planning',
      description: 'Planificar calendario editorial',
      icon: CalendarDaysIcon,
      color: 'bg-green-100 text-green-800 border-green-200',
    },
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!brief.trim()) {
      setError('Por favor, describe el objetivo de la reunión');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/meetings/`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          meeting_type: meetingType,
          brief: brief,
        }),
      });

      if (!response.ok) {
        throw new Error('Error al crear la reunión');
      }

      const data = await response.json();
      onMeetingCreated(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-xl shadow-xl max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b">
          <h2 className="text-xl font-semibold text-gray-900">
            Lanzar Reunión del Equipo
          </h2>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 transition-colors"
          >
            <XMarkIcon className="w-6 h-6" />
          </button>
        </div>

        {/* Content */}
        <form onSubmit={handleSubmit} className="p-6 space-y-6">
          {/* Meeting Type Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-3">
              Tipo de Reunión
            </label>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {meetingTypes.map((type) => {
                const Icon = type.icon;
                const isSelected = meetingType === type.id;
                return (
                  <button
                    key={type.id}
                    type="button"
                    onClick={() => setMeetingType(type.id)}
                    className={`p-4 rounded-lg border-2 text-left transition-all ${
                      isSelected
                        ? `${type.color} border-current`
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <Icon className={`w-8 h-8 mb-2 ${isSelected ? '' : 'text-gray-400'}`} />
                    <h3 className={`font-medium ${isSelected ? '' : 'text-gray-900'}`}>
                      {type.label}
                    </h3>
                    <p className={`text-sm mt-1 ${isSelected ? 'opacity-80' : 'text-gray-500'}`}>
                      {type.description}
                    </p>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Brief Input */}
          <div>
            <label htmlFor="brief" className="block text-sm font-medium text-gray-700 mb-2">
              Brief para el equipo
            </label>
            <textarea
              id="brief"
              value={brief}
              onChange={(e) => setBrief(e.target.value)}
              rows={4}
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-sage focus:border-sage transition-colors"
              placeholder="Describe el objetivo de la reunión. Por ejemplo: 'Necesitamos ideas para promocionar el próximo retiro de marzo...'"
            />
            <p className="mt-2 text-sm text-gray-500">
              El equipo de 7 agentes debatirá y te presentará opciones para que decidas.
            </p>
          </div>

          {/* Error Message */}
          {error && (
            <div className="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
              {error}
            </div>
          )}

          {/* Actions */}
          <div className="flex justify-end gap-4 pt-4 border-t">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 text-gray-700 hover:text-gray-900 transition-colors"
            >
              Cancelar
            </button>
            <button
              type="submit"
              disabled={loading}
              className="px-6 py-2 bg-sage text-white rounded-lg hover:bg-sage-dark transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center"
            >
              {loading ? (
                <>
                  <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                  </svg>
                  Iniciando reunión...
                </>
              ) : (
                'Lanzar Reunión'
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default MeetingLauncher;
