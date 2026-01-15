import React, { useState, useEffect } from 'react';
import { config } from '../../config';
import { CheckIcon, XMarkIcon, EyeIcon, PencilIcon } from '@heroicons/react/24/outline';

/**
 * Content Queue - Review and approve generated content
 */
const ContentQueue = ({ queue: initialQueue, onUpdate }) => {
  const [queue, setQueue] = useState(initialQueue || []);
  const [selectedContent, setSelectedContent] = useState(null);
  const [loading, setLoading] = useState(!initialQueue);
  const [filter, setFilter] = useState('all');

  useEffect(() => {
    if (!initialQueue) {
      loadQueue();
    }
  }, []);

  useEffect(() => {
    if (initialQueue) {
      setQueue(initialQueue);
    }
  }, [initialQueue]);

  const loadQueue = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/content/queue`, {
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        const data = await response.json();
        setQueue(data.content || []);
      }
    } catch (error) {
      console.error('Error loading queue:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleApprove = async (contentId) => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/content/${contentId}/approve`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        loadQueue();
        if (onUpdate) onUpdate();
      }
    } catch (error) {
      console.error('Error approving content:', error);
    }
  };

  const handleReject = async (contentId, feedback) => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/content/${contentId}/reject?feedback=${encodeURIComponent(feedback || '')}`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        loadQueue();
        if (onUpdate) onUpdate();
      }
    } catch (error) {
      console.error('Error rejecting content:', error);
    }
  };

  const filteredQueue = queue.filter(item => {
    if (filter === 'all') return true;
    return item.platform === filter;
  });

  const platforms = [...new Set(queue.map(item => item.platform))];

  const getContentTypeBadge = (type) => {
    const styles = {
      'post': 'bg-blue-100 text-blue-800',
      'reel': 'bg-purple-100 text-purple-800',
      'story': 'bg-pink-100 text-pink-800',
      'carousel': 'bg-indigo-100 text-indigo-800',
      'video_script': 'bg-red-100 text-red-800',
    };
    return (
      <span className={`px-2 py-1 text-xs font-medium rounded ${styles[type] || 'bg-gray-100'}`}>
        {type}
      </span>
    );
  };

  const getPlatformIcon = (platform) => {
    const icons = {
      'instagram': '📸',
      'tiktok': '🎵',
      'youtube': '▶️',
      'linkedin': '💼',
      'facebook': '👥',
    };
    return icons[platform] || '📱';
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
        <h2 className="text-lg font-semibold text-gray-900">
          Contenido por Revisar ({filteredQueue.length})
        </h2>
        
        {/* Platform Filter */}
        <div className="flex items-center gap-2">
          <span className="text-sm text-gray-500">Filtrar:</span>
          <select
            value={filter}
            onChange={(e) => setFilter(e.target.value)}
            className="px-3 py-1 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-sage"
          >
            <option value="all">Todas las plataformas</option>
            {platforms.map(platform => (
              <option key={platform} value={platform}>{platform}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Content Grid */}
      {filteredQueue.length === 0 ? (
        <div className="bg-white rounded-lg shadow p-8 text-center text-gray-500">
          No hay contenido pendiente de revisión
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredQueue.map((content) => (
            <div key={content.id} className="bg-white rounded-lg shadow overflow-hidden">
              {/* Header */}
              <div className="p-4 border-b bg-gray-50">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <span className="text-xl">{getPlatformIcon(content.platform)}</span>
                    {getContentTypeBadge(content.content_type)}
                  </div>
                  <span className="text-xs text-gray-500">
                    {new Date(content.created_at).toLocaleDateString()}
                  </span>
                </div>
              </div>

              {/* Content Preview */}
              <div className="p-4">
                <p className="text-sm text-gray-700 line-clamp-4">
                  {content.text_content}
                </p>
                
                {content.hashtags && content.hashtags.length > 0 && (
                  <div className="mt-3 flex flex-wrap gap-1">
                    {content.hashtags.slice(0, 5).map((tag, index) => (
                      <span key={index} className="text-xs text-sage">#{tag}</span>
                    ))}
                  </div>
                )}
              </div>

              {/* Actions */}
              <div className="p-4 border-t bg-gray-50 flex items-center justify-between">
                <button
                  onClick={() => setSelectedContent(content)}
                  className="flex items-center text-sm text-gray-600 hover:text-gray-900"
                >
                  <EyeIcon className="w-4 h-4 mr-1" />
                  Ver
                </button>
                
                <div className="flex items-center gap-2">
                  <button
                    onClick={() => handleReject(content.id)}
                    className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                    title="Rechazar"
                  >
                    <XMarkIcon className="w-5 h-5" />
                  </button>
                  <button
                    onClick={() => handleApprove(content.id)}
                    className="p-2 text-green-600 hover:bg-green-50 rounded-lg transition-colors"
                    title="Aprobar"
                  >
                    <CheckIcon className="w-5 h-5" />
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Content Detail Modal */}
      {selectedContent && (
        <ContentDetailModal
          content={selectedContent}
          onClose={() => setSelectedContent(null)}
          onApprove={() => {
            handleApprove(selectedContent.id);
            setSelectedContent(null);
          }}
          onReject={(feedback) => {
            handleReject(selectedContent.id, feedback);
            setSelectedContent(null);
          }}
        />
      )}
    </div>
  );
};

/**
 * Content Detail Modal
 */
const ContentDetailModal = ({ content, onClose, onApprove, onReject }) => {
  const [feedback, setFeedback] = useState('');
  const [showRejectForm, setShowRejectForm] = useState(false);

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-xl shadow-xl max-w-3xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b">
          <div className="flex items-center gap-3">
            <span className="text-2xl">{content.platform === 'instagram' ? '📸' : '📱'}</span>
            <div>
              <h2 className="text-xl font-semibold text-gray-900">
                {content.title || `${content.content_type} para ${content.platform}`}
              </h2>
              <p className="text-sm text-gray-500">{content.content_type} - {content.platform}</p>
            </div>
          </div>
          <button onClick={onClose} className="text-gray-400 hover:text-gray-600">
            <XMarkIcon className="w-6 h-6" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 space-y-6">
          {/* Text Content */}
          <div>
            <h3 className="text-sm font-medium text-gray-500 mb-2">Contenido</h3>
            <div className="bg-gray-50 rounded-lg p-4">
              <p className="whitespace-pre-wrap text-gray-900">{content.text_content}</p>
            </div>
          </div>

          {/* Visual Brief */}
          {content.visual_brief && (
            <div>
              <h3 className="text-sm font-medium text-gray-500 mb-2">Brief Visual (Canva)</h3>
              <div className="bg-blue-50 rounded-lg p-4">
                <p className="whitespace-pre-wrap text-gray-700 text-sm">{content.visual_brief}</p>
              </div>
            </div>
          )}

          {/* Hashtags */}
          {content.hashtags && content.hashtags.length > 0 && (
            <div>
              <h3 className="text-sm font-medium text-gray-500 mb-2">Hashtags</h3>
              <div className="flex flex-wrap gap-2">
                {content.hashtags.map((tag, index) => (
                  <span key={index} className="px-3 py-1 bg-sage-light/20 text-sage rounded-full text-sm">
                    #{tag}
                  </span>
                ))}
              </div>
            </div>
          )}

          {/* Reject Form */}
          {showRejectForm && (
            <div className="border-t pt-4">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Feedback para el equipo
              </label>
              <textarea
                value={feedback}
                onChange={(e) => setFeedback(e.target.value)}
                rows={3}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-sage"
                placeholder="Explica qué cambios necesita..."
              />
            </div>
          )}
        </div>

        {/* Actions */}
        <div className="p-6 border-t bg-gray-50 flex justify-end gap-4">
          {showRejectForm ? (
            <>
              <button
                onClick={() => setShowRejectForm(false)}
                className="px-4 py-2 text-gray-700 hover:text-gray-900"
              >
                Cancelar
              </button>
              <button
                onClick={() => onReject(feedback)}
                className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700"
              >
                Confirmar Rechazo
              </button>
            </>
          ) : (
            <>
              <button
                onClick={() => setShowRejectForm(true)}
                className="px-4 py-2 border border-red-300 text-red-600 rounded-lg hover:bg-red-50"
              >
                Rechazar
              </button>
              <button
                onClick={onApprove}
                className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700"
              >
                Aprobar
              </button>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default ContentQueue;
