import React, { useState, useEffect } from 'react';
import { 
  ChartBarIcon, 
  CalendarIcon, 
  ChatBubbleLeftRightIcon,
  DocumentTextIcon,
  SparklesIcon,
  UserGroupIcon,
  ClipboardDocumentListIcon
} from '@heroicons/react/24/outline';
import { config } from '../../config';
import MeetingLauncher from './MeetingLauncher';
import MeetingView from './MeetingView';
import StrategyDashboard from './StrategyDashboard';
import ContentQueue from './ContentQueue';
import CalendarView from './CalendarView';
import AgentChat from './AgentChat';

/**
 * Marketing Tab - Main container for marketing team features
 */
const MarketingTab = () => {
  const [activeSubTab, setActiveSubTab] = useState('dashboard');
  const [pendingMeetings, setPendingMeetings] = useState([]);
  const [contentQueue, setContentQueue] = useState([]);
  const [activeStrategies, setActiveStrategies] = useState({});
  const [loading, setLoading] = useState(true);
  const [chatContext, setChatContext] = useState(null);

  // Load initial data
  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem('token');
      const headers = { 'Authorization': `Bearer ${token}` };

      // Load pending meetings
      const meetingsRes = await fetch(`${config.apiUrl}/api/marketing/meetings/pending`, { headers });
      if (meetingsRes.ok) {
        const data = await meetingsRes.json();
        setPendingMeetings(data.meetings || []);
      }

      // Load content queue
      const contentRes = await fetch(`${config.apiUrl}/api/marketing/content/queue`, { headers });
      if (contentRes.ok) {
        const data = await contentRes.json();
        setContentQueue(data.content || []);
      }

      // Load active strategies
      const strategyRes = await fetch(`${config.apiUrl}/api/marketing/strategy/active`, { headers });
      if (strategyRes.ok) {
        const data = await strategyRes.json();
        setActiveStrategies(data || {});
      }
    } catch (error) {
      console.error('Error loading dashboard data:', error);
    } finally {
      setLoading(false);
    }
  };

  const subTabs = [
    { id: 'dashboard', label: 'Dashboard', icon: ChartBarIcon },
    { id: 'meetings', label: 'Reuniones', icon: UserGroupIcon },
    { id: 'content', label: 'Contenido', icon: DocumentTextIcon },
    { id: 'calendar', label: 'Calendario', icon: CalendarIcon },
    { id: 'strategy', label: 'Estrategia', icon: SparklesIcon },
    { id: 'chat', label: 'Chat', icon: ChatBubbleLeftRightIcon },
  ];

  return (
    <div className="space-y-6">
      {/* Sub-navigation */}
      <div className="border-b border-gray-200">
        <nav className="-mb-px flex space-x-6">
          {subTabs.map((tab) => {
            const Icon = tab.icon;
            return (
              <button
                key={tab.id}
                onClick={() => setActiveSubTab(tab.id)}
                className={`flex items-center px-1 py-3 text-sm font-medium border-b-2 transition-colors ${
                  activeSubTab === tab.id
                    ? 'border-sage text-sage'
                    : 'border-transparent text-gray-500 hover:text-sage hover:border-sage-light'
                }`}
              >
                <Icon className="w-5 h-5 mr-2" />
                {tab.label}
              </button>
            );
          })}
        </nav>
      </div>

      {/* Content */}
      {activeSubTab === 'dashboard' && (
        <DashboardView 
          pendingMeetings={pendingMeetings}
          contentQueue={contentQueue}
          activeStrategies={activeStrategies}
          loading={loading}
          onRefresh={loadDashboardData}
        />
      )}

      {activeSubTab === 'meetings' && (
        <MeetingView onMeetingComplete={loadDashboardData} />
      )}

      {activeSubTab === 'content' && (
        <ContentQueue 
          queue={contentQueue} 
          onUpdate={loadDashboardData} 
        />
      )}

      {activeSubTab === 'calendar' && (
        <CalendarView
          onSelectContent={(item) => {
            setChatContext(item);
            setActiveSubTab('chat');
          }}
        />
      )}

      {activeSubTab === 'strategy' && (
        <StrategyDashboard 
          strategies={activeStrategies}
          onUpdate={loadDashboardData}
        />
      )}

      {activeSubTab === 'chat' && (
        <AgentChat contextContent={chatContext} />
      )}
    </div>
  );
};

/**
 * Dashboard View - Overview of marketing status
 */
const DashboardView = ({ 
  pendingMeetings, 
  contentQueue, 
  activeStrategies, 
  loading,
  onRefresh 
}) => {
  const [showMeetingLauncher, setShowMeetingLauncher] = useState(false);

  if (loading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-sage"></div>
        <span className="ml-3 text-gray-600">Cargando...</span>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Quick Actions */}
      <div className="flex gap-4">
        <button
          onClick={() => setShowMeetingLauncher(true)}
          className="flex items-center px-4 py-2 bg-sage text-white rounded-lg hover:bg-sage-dark transition-colors"
        >
          <UserGroupIcon className="w-5 h-5 mr-2" />
          Lanzar Reunión
        </button>
        <button
          onClick={onRefresh}
          className="flex items-center px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
        >
          <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          Actualizar
        </button>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Pending Decisions */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-semibold text-gray-900">Decisiones Pendientes</h3>
            <span className="bg-amber-100 text-amber-800 text-sm font-medium px-2.5 py-0.5 rounded">
              {pendingMeetings.length}
            </span>
          </div>
          {pendingMeetings.length > 0 ? (
            <ul className="space-y-3">
              {pendingMeetings.slice(0, 3).map((meeting) => (
                <li key={meeting.id} className="flex items-center justify-between text-sm">
                  <span className="text-gray-600">{meeting.brief_initial?.substring(0, 40)}...</span>
                  <span className="text-xs text-gray-400">{meeting.meeting_type}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-gray-500 text-sm">No hay decisiones pendientes</p>
          )}
        </div>

        {/* Content Queue */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-semibold text-gray-900">Contenido por Revisar</h3>
            <span className="bg-blue-100 text-blue-800 text-sm font-medium px-2.5 py-0.5 rounded">
              {contentQueue.length}
            </span>
          </div>
          {contentQueue.length > 0 ? (
            <ul className="space-y-3">
              {contentQueue.slice(0, 3).map((content) => (
                <li key={content.id} className="flex items-center justify-between text-sm">
                  <span className="text-gray-600">{content.title || content.content_type}</span>
                  <span className="text-xs text-gray-400">{content.platform}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-gray-500 text-sm">No hay contenido pendiente</p>
          )}
        </div>

        {/* Active Strategies */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-semibold text-gray-900">Estrategias Activas</h3>
            <span className="bg-green-100 text-green-800 text-sm font-medium px-2.5 py-0.5 rounded">
              {Object.keys(activeStrategies).length}
            </span>
          </div>
          {Object.keys(activeStrategies).length > 0 ? (
            <ul className="space-y-3">
              {Object.entries(activeStrategies).map(([type, strategy]) => (
                <li key={type} className="text-sm">
                  <span className="font-medium text-gray-900 capitalize">{type}:</span>
                  <span className="text-gray-600 ml-2">{strategy.title}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-gray-500 text-sm">No hay estrategias activas</p>
          )}
        </div>
      </div>

      {/* Meeting Launcher Modal */}
      {showMeetingLauncher && (
        <MeetingLauncher 
          onClose={() => setShowMeetingLauncher(false)}
          onMeetingCreated={() => {
            setShowMeetingLauncher(false);
            onRefresh();
          }}
        />
      )}
    </div>
  );
};

export default MarketingTab;
