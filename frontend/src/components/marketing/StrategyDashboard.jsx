import React, { useState, useEffect } from 'react';
import { config } from '../../config';
import { SparklesIcon, CalendarIcon } from '@heroicons/react/24/outline';

/**
 * Strategy Dashboard - View and manage marketing strategies
 */
const StrategyDashboard = ({ strategies: initialStrategies, onUpdate }) => {
  const [strategies, setStrategies] = useState(initialStrategies || {});
  const [allStrategies, setAllStrategies] = useState([]);
  const [loading, setLoading] = useState(!initialStrategies);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [actionLoading, setActionLoading] = useState(false);
  const [actionError, setActionError] = useState(null);

  useEffect(() => {
    if (!initialStrategies) {
      loadStrategies();
    }
    loadAllStrategies();
  }, []);

  useEffect(() => {
    if (initialStrategies) {
      setStrategies(initialStrategies);
    }
  }, [initialStrategies]);

  const loadStrategies = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/strategy/active`, {
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        const data = await response.json();
        setStrategies(data || {});
      }
    } catch (error) {
      console.error('Error loading strategies:', error);
    } finally {
      setLoading(false);
    }
  };

  const loadAllStrategies = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/strategy/?limit=20`, {
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        const data = await response.json();
        setAllStrategies(data || []);
      }
    } catch (error) {
      console.error('Error loading all strategies:', error);
    }
  };

  const handleActivate = async (strategyId) => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/strategy/${strategyId}/activate`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        loadStrategies();
        loadAllStrategies();
        if (onUpdate) onUpdate();
      }
    } catch (error) {
      console.error('Error activating strategy:', error);
    }
  };

  const getPrimaryStrategyId = () => {
    const primary = strategies.medium || strategies.short || strategies.long;
    return primary?.id || null;
  };

  const handleGenerateCalendar = async () => {
    const strategyId = getPrimaryStrategyId();
    if (!strategyId || actionLoading) return;
    setActionLoading(true);
    setActionError(null);
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/strategy/${strategyId}/recommendations`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (!response.ok) {
        throw new Error('No se pudo generar el calendario');
      }
      if (onUpdate) onUpdate();
    } catch (error) {
      setActionError(error.message);
    } finally {
      setActionLoading(false);
    }
  };

  const getStrategyTypeLabel = (type) => {
    const labels = {
      'short': 'Corto plazo (1-2 semanas)',
      'medium': 'Medio plazo (1-3 meses)',
      'long': 'Largo plazo (6-12 meses)',
    };
    return labels[type] || type;
  };

  const getStrategyTypeColor = (type) => {
    const colors = {
      'short': 'bg-amber-100 text-amber-800 border-amber-200',
      'medium': 'bg-blue-100 text-blue-800 border-blue-200',
      'long': 'bg-purple-100 text-purple-800 border-purple-200',
    };
    return colors[type] || 'bg-gray-100 text-gray-800 border-gray-200';
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-sage"></div>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Active Strategies */}
      <section>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-lg font-semibold text-gray-900">Estrategias Activas</h2>
          <div className="flex items-center gap-2">
            <button
              onClick={() => setShowCreateForm(true)}
              className="flex items-center px-4 py-2 bg-sage text-white rounded-lg hover:bg-sage-dark transition-colors"
            >
              <SparklesIcon className="w-5 h-5 mr-2" />
              Generar Estrategia
            </button>
            <button
              onClick={handleGenerateCalendar}
              disabled={!getPrimaryStrategyId() || actionLoading}
              className="flex items-center px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors disabled:opacity-50"
            >
              <CalendarIcon className="w-5 h-5 mr-2" />
              Generar calendario
            </button>
          </div>
        </div>

        {actionError && (
          <div className="mb-4 text-sm text-red-600">
            {actionError}
          </div>
        )}

        {Object.keys(strategies).length === 0 ? (
          <div className="bg-white rounded-lg shadow p-8 text-center text-gray-500">
            No hay estrategias activas. Genera una nueva estrategia para comenzar.
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {['short', 'medium', 'long'].map((type) => {
              const strategy = strategies[type];
              return (
                <div
                  key={type}
                  className={`bg-white rounded-lg shadow overflow-hidden ${
                    strategy ? '' : 'opacity-50'
                  }`}
                >
                  <div className={`px-4 py-3 border-b ${getStrategyTypeColor(type)}`}>
                    <h3 className="font-medium">{getStrategyTypeLabel(type)}</h3>
                  </div>
                  
                  {strategy ? (
                    <div className="p-4 space-y-4">
                      <div>
                        <h4 className="font-semibold text-gray-900">{strategy.title}</h4>
                        <p className="text-sm text-gray-500">
                          {strategy.period_start} - {strategy.period_end}
                        </p>
                      </div>

                      {strategy.objectives && strategy.objectives.length > 0 && (
                        <div>
                          <h5 className="text-sm font-medium text-gray-700 mb-1">Objetivos</h5>
                          <ul className="text-sm text-gray-600 list-disc list-inside">
                            {strategy.objectives.slice(0, 3).map((obj, i) => (
                              <li key={i} className="truncate">{obj}</li>
                            ))}
                          </ul>
                        </div>
                      )}

                      {strategy.content_pillars && strategy.content_pillars.length > 0 && (
                        <div>
                          <h5 className="text-sm font-medium text-gray-700 mb-1">Pilares de Contenido</h5>
                          <div className="flex flex-wrap gap-1">
                            {strategy.content_pillars.map((pillar, i) => (
                              <span key={i} className="px-2 py-0.5 bg-gray-100 text-gray-700 rounded text-xs">
                                {pillar}
                              </span>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>
                  ) : (
                    <div className="p-4 text-center text-gray-400">
                      Sin estrategia activa
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </section>

      {/* All Strategies */}
      <section>
        <h2 className="text-lg font-semibold text-gray-900 mb-4">Historial de Estrategias</h2>
        
        {allStrategies.length === 0 ? (
          <div className="bg-white rounded-lg shadow p-8 text-center text-gray-500">
            No hay estrategias registradas
          </div>
        ) : (
          <div className="bg-white rounded-lg shadow overflow-hidden">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Tipo</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Título</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Período</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Estado</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Acciones</th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {allStrategies.map((strategy) => (
                  <tr key={strategy.id} className="hover:bg-gray-50">
                    <td className="px-6 py-4 whitespace-nowrap">
                      <span className={`px-2 py-1 text-xs font-medium rounded ${getStrategyTypeColor(strategy.strategy_type)}`}>
                        {strategy.strategy_type}
                      </span>
                    </td>
                    <td className="px-6 py-4">
                      <p className="text-sm text-gray-900">{strategy.title}</p>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {strategy.period_start} - {strategy.period_end}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <span className={`px-2 py-1 text-xs font-medium rounded ${
                        strategy.status === 'active' 
                          ? 'bg-green-100 text-green-800' 
                          : 'bg-gray-100 text-gray-800'
                      }`}>
                        {strategy.status}
                      </span>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      {strategy.status !== 'active' && (
                        <button
                          onClick={() => handleActivate(strategy.id)}
                          className="text-sage hover:text-sage-dark text-sm font-medium"
                        >
                          Activar
                        </button>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      {/* Create Strategy Modal */}
      {showCreateForm && (
        <CreateStrategyModal
          onClose={() => setShowCreateForm(false)}
          onCreated={() => {
            setShowCreateForm(false);
            loadStrategies();
            loadAllStrategies();
            if (onUpdate) onUpdate();
          }}
        />
      )}
    </div>
  );
};

/**
 * Create Strategy Modal
 */
const CreateStrategyModal = ({ onClose, onCreated }) => {
  const [strategyType, setStrategyType] = useState('medium');
  const [objectives, setObjectives] = useState('');
  const [periodStart, setPeriodStart] = useState('');
  const [periodEnd, setPeriodEnd] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!objectives.trim() || !periodStart || !periodEnd) {
      setError('Por favor, completa todos los campos');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/api/marketing/strategy/generate`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          strategy_type: strategyType,
          objectives: objectives,
          period_start: periodStart,
          period_end: periodEnd,
        }),
      });

      if (!response.ok) {
        throw new Error('Error al generar la estrategia');
      }

      onCreated();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-xl shadow-xl max-w-lg w-full mx-4">
        <div className="flex items-center justify-between p-6 border-b">
          <h2 className="text-xl font-semibold text-gray-900">Generar Nueva Estrategia</h2>
          <button onClick={onClose} className="text-gray-400 hover:text-gray-600">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Tipo de Estrategia
            </label>
            <select
              value={strategyType}
              onChange={(e) => setStrategyType(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-sage"
            >
              <option value="short">Corto plazo (1-2 semanas)</option>
              <option value="medium">Medio plazo (1-3 meses)</option>
              <option value="long">Largo plazo (6-12 meses)</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Objetivos de Negocio
            </label>
            <textarea
              value={objectives}
              onChange={(e) => setObjectives(e.target.value)}
              rows={3}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-sage"
              placeholder="Ej: Aumentar ventas del programa en un 20%, llenar el próximo retiro..."
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Fecha Inicio
              </label>
              <input
                type="date"
                value={periodStart}
                onChange={(e) => setPeriodStart(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-sage"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Fecha Fin
              </label>
              <input
                type="date"
                value={periodEnd}
                onChange={(e) => setPeriodEnd(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-sage"
              />
            </div>
          </div>

          {error && (
            <div className="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
              {error}
            </div>
          )}

          <div className="flex justify-end gap-4 pt-4">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 text-gray-700 hover:text-gray-900"
            >
              Cancelar
            </button>
            <button
              type="submit"
              disabled={loading}
              className="px-6 py-2 bg-sage text-white rounded-lg hover:bg-sage-dark disabled:opacity-50"
            >
              {loading ? 'Generando...' : 'Generar con IA'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default StrategyDashboard;
