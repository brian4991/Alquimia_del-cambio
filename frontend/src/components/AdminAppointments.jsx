import React, { useState, useEffect } from 'react';
import { Calendar, Clock, User, Mail, CheckCircle, XCircle, AlertCircle, Settings, Link as LinkIcon } from 'lucide-react';
import { config } from '../config';

const AdminAppointments = () => {
  const [appointments, setAppointments] = useState([]);
  const [calendarSettings, setCalendarSettings] = useState(null);
  const [pendingCount, setPendingCount] = useState(0);
  const [filterStatus, setFilterStatus] = useState('all');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [showSettings, setShowSettings] = useState(false);
  const [slotDuration, setSlotDuration] = useState(60);
  const [availabilityBuffer, setAvailabilityBuffer] = useState(60);

  useEffect(() => {
    loadAppointments();
    loadPendingCount();
    loadCalendarSettings();
  }, []);

  useEffect(() => {
    loadAppointments();
  }, [filterStatus]);

  const loadCalendarSettings = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/admin/calendar/settings`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      
      if (response.ok) {
        const data = await response.json();
        setCalendarSettings(data);
        setSlotDuration(data.slot_duration);
        setAvailabilityBuffer(data.availability_buffer);
      }
    } catch (err) {
      console.error('Error loading calendar settings:', err);
    }
  };

  const loadAppointments = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem('token');
      const url = filterStatus === 'all' 
        ? `${config.apiUrl}/admin/appointments`
        : `${config.apiUrl}/admin/appointments?status=${filterStatus}`;
        
      const response = await fetch(url, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      
      if (response.ok) {
        const data = await response.json();
        setAppointments(data);
      }
    } catch (err) {
      console.error('Error loading appointments:', err);
      setError('Error al cargar las citas');
    } finally {
      setLoading(false);
    }
  };

  const loadPendingCount = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/admin/appointments/count`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      
      if (response.ok) {
        const data = await response.json();
        setPendingCount(data.pending_count);
      }
    } catch (err) {
      console.error('Error loading pending count:', err);
    }
  };

  const handleUpdateStatus = async (appointmentId, newStatus) => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/admin/appointments/${appointmentId}/status`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ status: newStatus })
      });

      if (response.ok) {
        setSuccess(`Cita ${newStatus === 'confirmed' ? 'confirmada' : 'cancelada'} con éxito`);
        loadAppointments();
        loadPendingCount();
      } else {
        setError('Error al actualizar');
      }
    } catch (err) {
      console.error('Error updating status:', err);
      setError('Error al actualizar el estado');
    }
  };

  const handleConnectCalendar = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/admin/calendar/connect`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      
      if (response.ok) {
        const data = await response.json();
        // Open Google OAuth in new window
        window.open(data.authorization_url, '_blank');
        setSuccess('Por favor, autoriza el acceso a tu Google Calendar en la nueva ventana');
      }
    } catch (err) {
      console.error('Error connecting calendar:', err);
      setError('Error al conectar el calendario');
    }
  };

  const handleDisconnectCalendar = async () => {
    if (!confirm('¿Estás seguro de que quieres desconectar Google Calendar?')) {
      return;
    }

    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/admin/calendar/disconnect`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      
      if (response.ok) {
        setSuccess('Google Calendar desconectado con éxito');
        loadCalendarSettings();
      }
    } catch (err) {
      console.error('Error disconnecting calendar:', err);
      setError('Error al desconectar');
    }
  };

  const handleUpdateSettings = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/admin/calendar/settings`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          slot_duration: slotDuration,
          availability_buffer: availabilityBuffer
        })
      });

      if (response.ok) {
        setSuccess('Configuración actualizada con éxito');
        setShowSettings(false);
        loadCalendarSettings();
      }
    } catch (err) {
      console.error('Error updating settings:', err);
      setError('Error al actualizar la configuración');
    }
  };

  const formatDateTime = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleString('es-ES', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getStatusBadge = (status) => {
    const badges = {
      pending: { color: 'bg-yellow-100 text-yellow-800', icon: AlertCircle, text: 'Pendiente' },
      confirmed: { color: 'bg-green-100 text-green-800', icon: CheckCircle, text: 'Confirmada' },
      cancelled: { color: 'bg-red-100 text-red-800', icon: XCircle, text: 'Cancelada' }
    };
    
    const badge = badges[status] || badges.pending;
    const Icon = badge.icon;
    
    return (
      <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium ${badge.color}`}>
        <Icon className="w-4 h-4 mr-1" />
        {badge.text}
      </span>
    );
  };

  return (
    <div className="min-h-screen bg-gradient-elegant p-6">
      <div className="max-w-7xl mx-auto">
        <div className="mb-8 flex justify-between items-start">
          <div>
            <h1 className="text-3xl font-bold text-gray-900 mb-2">Gestión de Citas</h1>
            <p className="text-gray-600">Gestiona tus citas con los usuarios</p>
          </div>
          <button
            onClick={() => setShowSettings(!showSettings)}
            className="flex items-center gap-2 px-4 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50"
          >
            <Settings className="w-5 h-5" />
            Configuración
          </button>
        </div>

        {error && (
          <div className="mb-6 bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
            {error}
          </div>
        )}

        {success && (
          <div className="mb-6 bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded-lg">
            {success}
          </div>
        )}

        {showSettings && (
          <div className="mb-6 bg-white rounded-lg shadow-elegant p-6">
            <h2 className="text-xl font-semibold mb-4">Configuración del Calendario</h2>
            
            <div className="space-y-4">
              {/* Calendar Connection */}
              <div className="p-4 border border-gray-200 rounded-lg">
                <div className="flex items-center justify-between">
                  <div>
                    <h3 className="font-medium mb-1">Google Calendar</h3>
                    <p className="text-sm text-gray-600">
                      {calendarSettings?.has_calendar_connected
                        ? 'Conectado y sincronizado'
                        : 'Conecta tu Google Calendar para mostrar tu disponibilidad'}
                    </p>
                  </div>
                  {calendarSettings?.has_calendar_connected ? (
                    <button
                      onClick={handleDisconnectCalendar}
                      className="px-4 py-2 text-red-600 border border-red-300 rounded-lg hover:bg-red-50"
                    >
                      Desconectar
                    </button>
                  ) : (
                    <button
                      onClick={handleConnectCalendar}
                      className="flex items-center gap-2 px-4 py-2 bg-sage text-white rounded-lg hover:bg-sage-dark"
                    >
                      <LinkIcon className="w-4 h-4" />
                      Conectar
                    </button>
                  )}
                </div>
              </div>

              {/* Slot Duration */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Duración de los horarios (minutos)
                </label>
                <select
                  value={slotDuration}
                  onChange={(e) => setSlotDuration(parseInt(e.target.value))}
                  className="w-full p-3 border border-gray-300 rounded-lg"
                >
                  <option value={30}>30 minutos</option>
                  <option value={45}>45 minutos</option>
                  <option value={60}>60 minutos</option>
                  <option value={90}>90 minutos</option>
                  <option value={120}>120 minutos</option>
                </select>
              </div>

              {/* Buffer Time */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Tiempo mínimo antes de reservar (minutos)
                </label>
                <select
                  value={availabilityBuffer}
                  onChange={(e) => setAvailabilityBuffer(parseInt(e.target.value))}
                  className="w-full p-3 border border-gray-300 rounded-lg"
                >
                  <option value={30}>30 minutos</option>
                  <option value={60}>1 hora</option>
                  <option value={120}>2 horas</option>
                  <option value={240}>4 horas</option>
                  <option value={1440}>24 horas</option>
                </select>
              </div>

              <button
                onClick={handleUpdateSettings}
                className="w-full py-3 bg-sage text-white rounded-lg hover:bg-sage-dark"
              >
                Guardar configuración
              </button>
            </div>
          </div>
        )}

        {/* Filter Tabs */}
        <div className="bg-white rounded-lg shadow-elegant mb-6">
          <div className="flex border-b border-gray-200">
            {[
              { id: 'all', label: 'Todas', count: appointments.length },
              { id: 'pending', label: 'Pendientes', count: pendingCount },
              { id: 'confirmed', label: 'Confirmadas' },
              { id: 'cancelled', label: 'Canceladas' }
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setFilterStatus(tab.id)}
                className={`flex items-center px-6 py-4 text-sm font-medium border-b-2 transition-colors ${
                  filterStatus === tab.id
                    ? 'border-sage text-sage'
                    : 'border-transparent text-gray-500 hover:text-sage hover:border-sage-light'
                }`}
              >
                {tab.label}
                {tab.count !== undefined && tab.count > 0 && (
                  <span className={`ml-2 px-2 py-0.5 rounded-full text-xs ${
                    tab.id === 'pending' ? 'bg-yellow-100 text-yellow-800' : 'bg-gray-100 text-gray-600'
                  }`}>
                    {tab.count}
                  </span>
                )}
              </button>
            ))}
          </div>
        </div>

        {/* Appointments List */}
        <div className="bg-white rounded-lg shadow-elegant p-6">
          {loading ? (
            <div className="text-center py-8">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-sage mx-auto"></div>
              <p className="mt-4 text-gray-600">Cargando...</p>
            </div>
          ) : appointments.length === 0 ? (
            <div className="text-center py-8 text-gray-500">
              <Calendar className="w-12 h-12 mx-auto mb-4 opacity-50" />
              <p>No hay citas</p>
            </div>
          ) : (
            <div className="space-y-4">
              {appointments.map((appointment) => (
                <div
                  key={appointment.id}
                  className="p-6 border border-gray-200 rounded-lg hover:shadow-md transition-shadow"
                >
                  <div className="flex justify-between items-start mb-4">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <User className="w-5 h-5 text-sage" />
                        <h3 className="font-semibold text-lg">{appointment.user_name}</h3>
                        {getStatusBadge(appointment.status)}
                      </div>
                      
                      <div className="space-y-2 ml-8">
                        <div className="flex items-center gap-2 text-gray-600">
                          <Mail className="w-4 h-4" />
                          <span className="text-sm">{appointment.user_email}</span>
                        </div>
                        
                        <div className="flex items-center gap-2 text-gray-600">
                          <Clock className="w-4 h-4" />
                          <span className="text-sm">{formatDateTime(appointment.start_time)}</span>
                        </div>
                        
                        {appointment.notes && (
                          <div className="mt-3 p-3 bg-gray-50 rounded-lg">
                            <p className="text-sm text-gray-700">
                              <strong>Notas:</strong> {appointment.notes}
                            </p>
                          </div>
                        )}
                      </div>
                    </div>
                  </div>

                  {appointment.status === 'pending' && (
                    <div className="flex gap-2 ml-8">
                      <button
                        onClick={() => handleUpdateStatus(appointment.id, 'confirmed')}
                        className="flex items-center gap-2 px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700"
                      >
                        <CheckCircle className="w-4 h-4" />
                        Confirmar
                      </button>
                      <button
                        onClick={() => handleUpdateStatus(appointment.id, 'cancelled')}
                        className="flex items-center gap-2 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700"
                      >
                        <XCircle className="w-4 h-4" />
                        Cancelar
                      </button>
                    </div>
                  )}
                  
                  {appointment.status === 'confirmed' && (
                    <button
                      onClick={() => handleUpdateStatus(appointment.id, 'cancelled')}
                      className="ml-8 text-sm text-red-600 hover:text-red-800 font-medium"
                    >
                      Cancelar esta cita
                    </button>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default AdminAppointments;

