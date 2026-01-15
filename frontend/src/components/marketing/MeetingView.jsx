import React, { useState, useEffect } from 'react';
import { config } from '../../config';
import MeetingLauncher from './MeetingLauncher';

/**
 * Meeting View - Display and manage team meetings
 */
const MeetingView = ({ onMeetingComplete }) => {
  const [meetings, setMeetings] = useState([]);
  const [selectedMeeting, setSelectedMeeting] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showLauncher, setShowLauncher] = useState(false);

  useEffect(() => {
    loadMeetings();
  }, []);

  const loadMeetings = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/meetings/?limit=20`, {
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        const data = await response.json();
        setMeetings(data.meetings || []);
      }
    } catch (error) {
      console.error('Error loading meetings:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleDecision = async (meetingId, decision, feedback) => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/meetings/${meetingId}/decision`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ decision, feedback }),
      });

      if (response.ok) {
        loadMeetings();
        setSelectedMeeting(null);
        if (onMeetingComplete) onMeetingComplete();
      }
    } catch (error) {
      console.error('Error submitting decision:', error);
    }
  };

  const getStatusBadge = (status) => {
    const styles = {
      'in_progress': 'bg-yellow-100 text-yellow-800',
      'awaiting_decision': 'bg-amber-100 text-amber-800',
      'completed': 'bg-green-100 text-green-800',
      'cancelled': 'bg-gray-100 text-gray-800',
    };
    const labels = {
      'in_progress': 'En progreso',
      'awaiting_decision': 'Esperando decisión',
      'completed': 'Completada',
      'cancelled': 'Cancelada',
    };
    return (
      <span className={`px-2 py-1 text-xs font-medium rounded ${styles[status] || 'bg-gray-100'}`}>
        {labels[status] || status}
      </span>
    );
  };

  const getMeetingTypeBadge = (type) => {
    const styles = {
      'brainstorm': 'bg-purple-100 text-purple-800',
      'review': 'bg-blue-100 text-blue-800',
      'planning': 'bg-green-100 text-green-800',
    };
    return (
      <span className={`px-2 py-1 text-xs font-medium rounded ${styles[type] || 'bg-gray-100'}`}>
        {type}
      </span>
    );
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-sage"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-semibold text-gray-900">Reuniones del Equipo</h2>
        <button
          onClick={() => setShowLauncher(true)}
          className="px-4 py-2 bg-sage text-white rounded-lg hover:bg-sage-dark transition-colors"
        >
          Nueva Reunión
        </button>
      </div>

      {/* Meetings List */}
      <div className="bg-white rounded-lg shadow overflow-hidden">
        {meetings.length === 0 ? (
          <div className="p-8 text-center text-gray-500">
            No hay reuniones registradas. Lanza tu primera reunión para comenzar.
          </div>
        ) : (
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Tipo</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Brief</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Estado</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Fecha</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Acciones</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {meetings.map((meeting) => (
                <tr key={meeting.id} className="hover:bg-gray-50">
                  <td className="px-6 py-4 whitespace-nowrap">
                    {getMeetingTypeBadge(meeting.meeting_type)}
                  </td>
                  <td className="px-6 py-4">
                    <p className="text-sm text-gray-900 truncate max-w-xs">
                      {meeting.brief_initial}
                    </p>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    {getStatusBadge(meeting.status)}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {new Date(meeting.created_at).toLocaleDateString()}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <button
                      onClick={() => setSelectedMeeting(meeting)}
                      className="text-sage hover:text-sage-dark text-sm font-medium"
                    >
                      Ver detalles
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      {/* Meeting Detail Modal */}
      {selectedMeeting && (
        <MeetingDetailModal
          meeting={selectedMeeting}
          onClose={() => setSelectedMeeting(null)}
          onDecision={handleDecision}
        />
      )}

      {/* Meeting Launcher */}
      {showLauncher && (
        <MeetingLauncher
          onClose={() => setShowLauncher(false)}
          onMeetingCreated={() => {
            setShowLauncher(false);
            loadMeetings();
          }}
        />
      )}
    </div>
  );
};

/**
 * Meeting Detail Modal
 */
const MeetingDetailModal = ({ meeting, onClose, onDecision }) => {
  const [decision, setDecision] = useState('');
  const [feedback, setFeedback] = useState('');
  const [submitting, setSubmitting] = useState(false);

  const handleSubmit = async () => {
    if (!decision.trim()) return;
    setSubmitting(true);
    await onDecision(meeting.id, decision, feedback);
    setSubmitting(false);
  };

  const needsDecision = meeting.status === 'awaiting_decision';

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-xl shadow-xl max-w-3xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b">
          <h2 className="text-xl font-semibold text-gray-900">
            Reunión: {meeting.meeting_type}
          </h2>
          <button onClick={onClose} className="text-gray-400 hover:text-gray-600">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Content */}
        <div className="p-6 space-y-6">
          {/* Brief */}
          <div>
            <h3 className="text-sm font-medium text-gray-500 mb-2">Brief Original</h3>
            <p className="text-gray-900">{meeting.brief_initial}</p>
          </div>

          {/* Debate Summary */}
          {meeting.debate_summary && (
            <div>
              <h3 className="text-sm font-medium text-gray-500 mb-2">Resumen del Debate</h3>
              <div className="bg-gray-50 rounded-lg p-4 prose prose-sm max-w-none">
                <p className="whitespace-pre-wrap">{meeting.debate_summary}</p>
              </div>
            </div>
          )}

          {/* Options */}
          {meeting.options_proposed && meeting.options_proposed.length > 0 && (
            <div>
              <h3 className="text-sm font-medium text-gray-500 mb-2">Opciones Propuestas</h3>
              <div className="space-y-3">
                {meeting.options_proposed.map((option, index) => (
                  <div 
                    key={index}
                    className={`border rounded-lg p-4 cursor-pointer transition-colors ${
                      decision === option.option_id 
                        ? 'border-sage bg-sage-light/10' 
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                    onClick={() => needsDecision && setDecision(option.option_id)}
                  >
                    <div className="flex items-center gap-2 mb-2">
                      <span className="font-semibold text-sage">Opción {option.option_id}</span>
                      <span className="text-gray-900">{option.title}</span>
                    </div>
                    <p className="text-sm text-gray-600">{option.description}</p>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Decision Form */}
          {needsDecision && (
            <div className="border-t pt-6">
              <h3 className="text-sm font-medium text-gray-500 mb-3">Tu Decisión</h3>
              
              <div className="space-y-4">
                <div>
                  <label className="block text-sm text-gray-700 mb-1">
                    Decisión (opción o texto libre)
                  </label>
                  <input
                    type="text"
                    value={decision}
                    onChange={(e) => setDecision(e.target.value)}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-sage focus:border-sage"
                    placeholder="A, B, C o tu propia decisión..."
                  />
                </div>

                <div>
                  <label className="block text-sm text-gray-700 mb-1">
                    Feedback (opcional)
                  </label>
                  <textarea
                    value={feedback}
                    onChange={(e) => setFeedback(e.target.value)}
                    rows={3}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-sage focus:border-sage"
                    placeholder="Comentarios para el equipo..."
                  />
                </div>

                <button
                  onClick={handleSubmit}
                  disabled={!decision.trim() || submitting}
                  className="w-full py-2 bg-sage text-white rounded-lg hover:bg-sage-dark transition-colors disabled:opacity-50"
                >
                  {submitting ? 'Enviando...' : 'Enviar Decisión'}
                </button>
              </div>
            </div>
          )}

          {/* Previous Decision */}
          {meeting.nicole_decision && (
            <div className="border-t pt-6">
              <h3 className="text-sm font-medium text-gray-500 mb-2">Decisión Tomada</h3>
              <p className="text-gray-900">{meeting.nicole_decision}</p>
              {meeting.nicole_feedback && (
                <p className="text-sm text-gray-600 mt-2">Feedback: {meeting.nicole_feedback}</p>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default MeetingView;
