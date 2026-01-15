import React, { useState, useEffect } from 'react';
import { config } from '../../config';
import {
  PaperAirplaneIcon,
  UserGroupIcon,
  SparklesIcon,
  DocumentTextIcon,
  PencilIcon,
  ChatBubbleLeftRightIcon,
  ShieldCheckIcon,
  ChartBarIcon,
} from '@heroicons/react/24/outline';

/**
 * Agent Chat - Chat interface with the marketing team coordinator
 */
const AgentChat = ({ contextContent }) => {
  const [messages, setMessages] = useState([
    {
      role: 'coordinator',
      content: 'Hola, soy el Coordinador del equipo de marketing. ¿En qué puedo ayudarte hoy? Puedo organizar reuniones, generar contenido, o consultar con el equipo sobre cualquier tema.',
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [actionLoading, setActionLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const [error, setError] = useState(null);
  const [selectedAgents, setSelectedAgents] = useState([
    'strategist',
    'creative_director',
    'copywriter',
  ]);
  const [maxAgents, setMaxAgents] = useState(3);
  const [lastUserMessage, setLastUserMessage] = useState('');
  const [draftContent, setDraftContent] = useState(null);
  const [contentType, setContentType] = useState('reel');
  const [contentPlatform, setContentPlatform] = useState('instagram');
  const [scheduleDate, setScheduleDate] = useState('');
  const [scheduleTime, setScheduleTime] = useState('');
  const [showScheduleForm, setShowScheduleForm] = useState(false);
  const [showFeedbackForm, setShowFeedbackForm] = useState(false);
  const [feedbackText, setFeedbackText] = useState('');

  useEffect(() => {
    if (contextContent?.content) {
      const baseTopic = contextContent.content.title || contextContent.content.content_type || 'Contenido';
      const platformLabel = contextContent.platform ? ` en ${contextContent.platform}` : '';
      const scheduled = contextContent.scheduled_date ? ` (${contextContent.scheduled_date})` : '';
      setLastUserMessage(`Post planificado: ${baseTopic}${platformLabel}${scheduled}`);
      setMessages((prev) => [
        ...prev,
        {
          role: 'coordinator',
          content: `Trabajemos este post del calendario: ${baseTopic}${platformLabel}${scheduled}.`,
        },
      ]);
    }
  }, [contextContent]);

  const agentOptions = [
    { role: 'strategist', label: 'Estratega', icon: SparklesIcon },
    { role: 'content_lead', label: 'Content Lead', icon: DocumentTextIcon },
    { role: 'creative_director', label: 'Director Creativo', icon: ChatBubbleLeftRightIcon },
    { role: 'copywriter', label: 'Copywriter', icon: PencilIcon },
    { role: 'community_manager', label: 'Community', icon: UserGroupIcon },
    { role: 'brand_guardian', label: 'Brand Guardian', icon: ShieldCheckIcon },
    { role: 'analyst', label: 'Analista', icon: ChartBarIcon },
  ];

  const roleLabels = agentOptions.reduce((acc, agent) => {
    acc[agent.role] = agent.label;
    return acc;
  }, {});

  const toggleAgent = (role) => {
    setSelectedAgents((prev) => {
      if (prev.includes(role)) {
        return prev.filter((item) => item !== role);
      }
      return [...prev, role];
    });
  };

  const renderFormattedLine = (line, lineIndex) => {
    const parts = line.split(/(\*\*[^*]+\*\*)/g).filter(Boolean);
    return (
      <p key={lineIndex} className="text-sm whitespace-pre-wrap">
        {parts.map((part, idx) => {
          if (part.startsWith('**') && part.endsWith('**')) {
            const content = part.slice(2, -2);
            return (
              <strong key={`${lineIndex}-${idx}`} className="font-semibold text-gray-900">
                {content}
              </strong>
            );
          }
          return <span key={`${lineIndex}-${idx}`}>{part}</span>;
        })}
      </p>
    );
  };

  const renderMessageContent = (content) => {
    const lines = content.split('\n');
    return lines.map((line, index) => renderFormattedLine(line, index));
  };

  const handleSend = async () => {
    if (!input.trim() || loading) return;
    if (selectedAgents.length === 0) {
      setError('Selecciona al menos un agente');
      return;
    }

    const userMessage = input.trim();
    setInput('');
    setLastUserMessage(userMessage);
    
    // Add user message
    setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
    
    setLoading(true);
    setError(null);
    
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/chat/message`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: userMessage,
          session_id: sessionId,
          selected_agents: selectedAgents,
          max_agents: maxAgents,
        }),
      });

      if (!response.ok) {
        throw new Error('No se pudo contactar al equipo de agentes');
      }

      const data = await response.json();
      setSessionId(data.session_id);

      const agentMessages = (data.agent_messages || []).map((agent) => ({
        role: 'agent',
        agentRole: agent.role,
        content: agent.content,
      }));

      const coordinatorMessage = {
        role: 'coordinator',
        content: data.coordinator_message,
      };

      setMessages((prev) => [...prev, ...agentMessages, coordinatorMessage]);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleGenerateScript = async () => {
    if (!lastUserMessage || actionLoading) return;
    setActionLoading(true);
    setError(null);
    try {
      const token = localStorage.getItem('token');
      const topicFromCalendar = contextContent?.content?.title
        || contextContent?.content?.text_content
        || lastUserMessage;
      const response = await fetch(`${config.apiUrl}/api/marketing/content/generate`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          content_type: contentType,
          platform: contentPlatform,
          topic: topicFromCalendar,
          objective: 'engagement',
        }),
      });

      if (!response.ok) {
        throw new Error('No se pudo generar el script');
      }

      const data = await response.json();
      setDraftContent(data);
      setMessages((prev) => [
        ...prev,
        {
          role: 'coordinator',
          content: 'Script generado. Puedes validar, ajustar o programar.',
        },
      ]);
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const handleApproveScript = async () => {
    if (!draftContent?.id || actionLoading) return;
    setActionLoading(true);
    setError(null);
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(
        `${config.apiUrl}/api/marketing/content/${draftContent.id}/approve`,
        {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        }
      );
      if (!response.ok) {
        throw new Error('No se pudo aprobar el contenido');
      }
      const data = await response.json();
      setDraftContent(data);
      setShowFeedbackForm(false);
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const handleRejectScript = async () => {
    if (!draftContent?.id || actionLoading) return;
    setActionLoading(true);
    setError(null);
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(
        `${config.apiUrl}/api/marketing/content/${draftContent.id}/reject?feedback=${encodeURIComponent(feedbackText || '')}`,
        {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        }
      );
      if (!response.ok) {
        throw new Error('No se pudo rechazar el contenido');
      }
      const data = await response.json();
      setDraftContent(data);
      setShowFeedbackForm(false);
      setFeedbackText('');
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const handleSchedule = async () => {
    if (!draftContent?.id || !scheduleDate || actionLoading) return;
    setActionLoading(true);
    setError(null);
    try {
      const token = localStorage.getItem('token');
      const params = new URLSearchParams({
        scheduled_date: scheduleDate,
      });
      if (scheduleTime) params.append('scheduled_time', scheduleTime);
      if (contentPlatform) params.append('platform', contentPlatform);

      const response = await fetch(
        `${config.apiUrl}/api/marketing/calendar/schedule/${draftContent.id}?${params.toString()}`,
        {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        }
      );
      if (!response.ok) {
        throw new Error('No se pudo programar en el calendario');
      }
      setShowScheduleForm(false);
      setMessages((prev) => [
        ...prev,
        {
          role: 'coordinator',
          content: `Contenido programado para ${scheduleDate}${scheduleTime ? ` ${scheduleTime}` : ''}.`,
        },
      ]);
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="flex flex-col h-[600px] bg-white rounded-lg shadow">
      {/* Header */}
      <div className="flex items-center gap-3 p-4 border-b">
        <div className="w-10 h-10 bg-sage rounded-full flex items-center justify-center">
          <UserGroupIcon className="w-6 h-6 text-white" />
        </div>
        <div>
          <h3 className="font-semibold text-gray-900">Coordinador del Equipo</h3>
          <p className="text-sm text-gray-500">Tu punto de contacto con el equipo de marketing</p>
        </div>
      </div>

      {/* Agent Selection */}
      <div className="px-4 py-3 border-b bg-gray-50">
        <div className="flex items-center justify-between mb-2">
          <h4 className="text-sm font-medium text-gray-700">Agentes activos</h4>
          <div className="flex items-center gap-2">
            <label className="text-xs text-gray-500">Max agentes</label>
            <select
              value={maxAgents}
              onChange={(e) => setMaxAgents(Number(e.target.value))}
              className="px-2 py-1 text-xs border border-gray-300 rounded"
            >
              <option value={1}>1</option>
              <option value={2}>2</option>
              <option value={3}>3</option>
              <option value={4}>4</option>
              <option value={5}>5</option>
            </select>
          </div>
        </div>
        <div className="flex flex-wrap gap-2">
          {agentOptions.map((agent) => {
            const Icon = agent.icon;
            const isActive = selectedAgents.includes(agent.role);
            return (
              <button
                key={agent.role}
                onClick={() => toggleAgent(agent.role)}
                className={`flex items-center gap-2 px-3 py-2 rounded-lg border text-sm transition-colors ${
                  isActive
                    ? 'border-sage bg-sage-light/10 text-sage'
                    : 'border-gray-200 text-gray-600 hover:border-gray-300'
                }`}
                type="button"
              >
                <Icon className="w-4 h-4" />
                {agent.label}
              </button>
            );
          })}
        </div>
        <p className="mt-2 text-xs text-gray-500">
          El coordinador prioriza a los agentes seleccionados para evitar debates largos.
        </p>
      </div>

      {contextContent?.content && (
        <div className="px-4 py-3 border-b bg-white">
          <div className="text-xs text-gray-500">Post seleccionado</div>
          <div className="text-sm font-medium text-gray-900">
            {contextContent.content.title || contextContent.content.content_type || 'Contenido'}
          </div>
          <div className="text-xs text-gray-500">
            {contextContent.platform || 'plataforma'} {contextContent.scheduled_date ? `· ${contextContent.scheduled_date}` : ''}
          </div>
        </div>
      )}

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-[80%] rounded-lg px-4 py-3 ${
                message.role === 'user'
                  ? 'bg-sage text-white'
                  : 'bg-gray-100 text-gray-900'
              }`}
            >
              {message.role === 'coordinator' && (
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xs font-medium text-sage">Coordinador</span>
                </div>
              )}
              {message.role === 'agent' && (
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xs font-medium text-sage">
                    {roleLabels[message.agentRole] || message.agentRole}
                  </span>
                </div>
              )}
              {renderMessageContent(message.content)}
            </div>
          </div>
        ))}
        
        {loading && (
          <div className="flex justify-start">
            <div className="bg-gray-100 rounded-lg px-4 py-3">
              <div className="flex items-center gap-2">
                <div className="animate-bounce w-2 h-2 bg-gray-400 rounded-full"></div>
                <div className="animate-bounce w-2 h-2 bg-gray-400 rounded-full" style={{ animationDelay: '0.1s' }}></div>
                <div className="animate-bounce w-2 h-2 bg-gray-400 rounded-full" style={{ animationDelay: '0.2s' }}></div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Workflow */}
      <div className="border-t bg-white px-4 py-3 space-y-3">
        <div className="flex items-center justify-between">
          <h4 className="text-sm font-medium text-gray-700">Workflow</h4>
          <span className="text-xs text-gray-500">
            {draftContent?.status ? `Estado: ${draftContent.status}` : 'Sin script'}
          </span>
        </div>

        <div className="flex flex-wrap gap-2 items-center">
          <select
            value={contentType}
            onChange={(e) => setContentType(e.target.value)}
            className="px-3 py-2 text-sm border border-gray-300 rounded-lg"
          >
            <option value="reel">Reel</option>
            <option value="video_script">Video Script</option>
            <option value="post">Post</option>
          </select>
          <select
            value={contentPlatform}
            onChange={(e) => setContentPlatform(e.target.value)}
            className="px-3 py-2 text-sm border border-gray-300 rounded-lg"
          >
            <option value="instagram">Instagram</option>
            <option value="tiktok">TikTok</option>
            <option value="youtube">YouTube</option>
            <option value="linkedin">LinkedIn</option>
            <option value="facebook">Facebook</option>
          </select>
          <button
            onClick={handleGenerateScript}
            disabled={!lastUserMessage || actionLoading}
            className="px-3 py-2 text-sm bg-sage text-white rounded-lg disabled:opacity-50"
          >
            Generar script
          </button>
          <button
            onClick={() => setShowScheduleForm((prev) => !prev)}
            disabled={!draftContent}
            className="px-3 py-2 text-sm border border-gray-300 rounded-lg disabled:opacity-50"
          >
            Programar
          </button>
          <button
            onClick={handleApproveScript}
            disabled={!draftContent || actionLoading}
            className="px-3 py-2 text-sm border border-green-300 text-green-700 rounded-lg disabled:opacity-50"
          >
            Validar
          </button>
          <button
            onClick={() => setShowFeedbackForm((prev) => !prev)}
            disabled={!draftContent}
            className="px-3 py-2 text-sm border border-red-300 text-red-700 rounded-lg disabled:opacity-50"
          >
            Rechazar
          </button>
        </div>

        {draftContent && (
          <div className="bg-gray-50 rounded-lg p-3 space-y-2">
            <div className="text-xs text-gray-500">Script generado</div>
            <div className="text-sm text-gray-900 whitespace-pre-wrap">
              {draftContent.text_content}
            </div>
            {draftContent.visual_brief && (
              <div className="text-sm text-gray-700 whitespace-pre-wrap">
                <span className="text-xs text-gray-500">Brief visual</span>
                <div>{draftContent.visual_brief}</div>
              </div>
            )}
          </div>
        )}

        {showFeedbackForm && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-3 space-y-2">
            <textarea
              value={feedbackText}
              onChange={(e) => setFeedbackText(e.target.value)}
              rows={2}
              className="w-full px-3 py-2 border border-red-200 rounded-lg text-sm"
              placeholder="Feedback para mejorar el script..."
            />
            <button
              onClick={handleRejectScript}
              disabled={actionLoading}
              className="px-3 py-2 text-sm bg-red-600 text-white rounded-lg disabled:opacity-50"
            >
              Confirmar rechazo
            </button>
          </div>
        )}

        {showScheduleForm && (
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-3 space-y-2">
            <div className="flex items-center gap-2">
              <input
                type="date"
                value={scheduleDate}
                onChange={(e) => setScheduleDate(e.target.value)}
                className="px-3 py-2 border border-blue-200 rounded-lg text-sm"
              />
              <input
                type="time"
                value={scheduleTime}
                onChange={(e) => setScheduleTime(e.target.value)}
                className="px-3 py-2 border border-blue-200 rounded-lg text-sm"
              />
            </div>
            <button
              onClick={handleSchedule}
              disabled={!scheduleDate || actionLoading}
              className="px-3 py-2 text-sm bg-blue-600 text-white rounded-lg disabled:opacity-50"
            >
              Añadir al calendario
            </button>
          </div>
        )}
      </div>

      {error && (
        <div className="px-4 pb-2 text-sm text-red-600">
          {error}
        </div>
      )}

      {/* Input */}
      <div className="p-4 border-t">
        <div className="flex items-end gap-2">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            rows={1}
            className="flex-1 px-4 py-2 border border-gray-300 rounded-lg resize-none focus:ring-2 focus:ring-sage focus:border-sage"
            placeholder="Escribe tu mensaje..."
          />
          <button
            onClick={handleSend}
            disabled={!input.trim() || loading}
            className="p-2 bg-sage text-white rounded-lg hover:bg-sage-dark disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <PaperAirplaneIcon className="w-5 h-5" />
          </button>
        </div>
        <p className="mt-2 text-xs text-gray-500">
          Presiona Enter para enviar. El coordinador puede organizar reuniones con todo el equipo.
        </p>
      </div>
    </div>
  );
};

export default AgentChat;
