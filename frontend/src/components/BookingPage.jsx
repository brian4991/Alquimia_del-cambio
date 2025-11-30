import React, { useState, useEffect } from 'react';
import { Calendar, Clock, User, CheckCircle, XCircle, AlertCircle, ChevronDown, ChevronUp } from 'lucide-react';
import { config } from '../config';

const BookingPage = () => {
  const [appointments, setAppointments] = useState([]);
  const [availableSlots, setAvailableSlots] = useState([]);
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [selectedSlot, setSelectedSlot] = useState(null);
  const [notes, setNotes] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [adminId, setAdminId] = useState(null);
  const [expandedDays, setExpandedDays] = useState({});

  useEffect(() => {
    loadAdminId();
    loadMyAppointments();
  }, []);

  useEffect(() => {
    if (adminId && selectedDate) {
      loadAvailableSlots();
    }
  }, [selectedDate, adminId]);

  const loadAdminId = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/appointments/admin-info`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      
      if (response.ok) {
        const data = await response.json();
        if (data.admin_id && data.has_calendar) {
          setAdminId(data.admin_id);
        } else if (!data.has_calendar) {
          setError('El calendario aún no está configurado. Por favor, inténtalo más tarde.');
        }
      }
    } catch (err) {
      console.error('Error loading admin:', err);
    }
  };

  const loadMyAppointments = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/appointments/my`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      
      if (response.ok) {
        const data = await response.json();
        setAppointments(data);
      }
    } catch (err) {
      console.error('Error loading appointments:', err);
    }
  };

  const loadAvailableSlots = async () => {
    if (!adminId) return;
    
    setLoading(true);
    try {
      const startDate = new Date(selectedDate);
      startDate.setHours(0, 0, 0, 0);
      
      const endDate = new Date(selectedDate);
      endDate.setDate(endDate.getDate() + 7); // Load 7 days
      endDate.setHours(23, 59, 59, 999);
      
      const token = localStorage.getItem('token');
      const response = await fetch(
        `${config.apiUrl}/appointments/availability?admin_id=${adminId}&start_date=${startDate.toISOString()}&end_date=${endDate.toISOString()}`,
        {
          headers: { 'Authorization': `Bearer ${token}` }
        }
      );
      
      if (response.ok) {
        const data = await response.json();
        setAvailableSlots(data.slots || []);
      }
    } catch (err) {
      console.error('Error loading slots:', err);
      setError('Error al cargar los horarios disponibles');
    } finally {
      setLoading(false);
    }
  };

  const handleBookAppointment = async () => {
    if (!selectedSlot) {
      setError('Por favor, selecciona un horario');
      return;
    }

    setLoading(true);
    setError('');
    setSuccess('');

    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/appointments/book`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          admin_id: adminId,
          start_time: selectedSlot.start,
          end_time: selectedSlot.end,
          notes: notes
        })
      });

      if (response.ok) {
        setSuccess('Cita reservada con éxito. Recibirás una confirmación por email.');
        setSelectedSlot(null);
        setNotes('');
        loadMyAppointments();
        loadAvailableSlots();
      } else {
        const data = await response.json();
        setError(data.detail || 'Error al reservar la cita');
      }
    } catch (err) {
      console.error('Error booking appointment:', err);
      setError('Error al reservar la cita');
    } finally {
      setLoading(false);
    }
  };

  const handleCancelAppointment = async (appointmentId) => {
    if (!confirm('¿Estás seguro de que quieres cancelar esta cita?')) {
      return;
    }

    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/appointments/${appointmentId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });

      if (response.ok) {
        setSuccess('Cita cancelada con éxito');
        loadMyAppointments();
        loadAvailableSlots();
      }
    } catch (err) {
      console.error('Error cancelling appointment:', err);
      setError('Error al cancelar la cita');
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

  const formatDateHeader = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('es-ES', {
      weekday: 'long',
      day: 'numeric',
      month: 'long'
    });
  };

  const toggleDay = (dateKey) => {
    setExpandedDays(prev => ({
      ...prev,
      [dateKey]: !prev[dateKey]
    }));
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

  const groupSlotsByDate = () => {
    const grouped = {};
    
    availableSlots.forEach(slot => {
      const date = new Date(slot.start);
      const dateKey = date.toISOString().split('T')[0];
      
      if (!grouped[dateKey]) {
        grouped[dateKey] = {
          displayDate: formatDateHeader(slot.start),
          slots: []
        };
      }
      grouped[dateKey].slots.push(slot);
    });
    
    return grouped;
  };

  const slotsByDate = groupSlotsByDate();

  return (
    <div className="min-h-screen bg-gradient-elegant p-6">
      <div className="max-w-7xl mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Mis Citas</h1>
          <p className="text-gray-600">Reserva un horario para una sesión individual</p>
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

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Available Slots */}
          <div className="bg-white rounded-lg shadow-elegant p-6">
            <h2 className="text-xl font-semibold mb-4 flex items-center">
              <Calendar className="w-6 h-6 mr-2 text-sage" />
              Horarios disponibles
            </h2>

            {loading ? (
              <div className="text-center py-8">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-sage mx-auto"></div>
                <p className="mt-4 text-gray-600">Cargando...</p>
              </div>
            ) : Object.keys(slotsByDate).length === 0 ? (
              <div className="text-center py-8 text-gray-500">
                <Clock className="w-12 h-12 mx-auto mb-4 opacity-50" />
                <p>No hay horarios disponibles por el momento</p>
              </div>
            ) : (
              <div className="space-y-3">
                {Object.entries(slotsByDate).map(([dateKey, { displayDate, slots }]) => {
                  const isExpanded = expandedDays[dateKey];
                  
                  return (
                    <div key={dateKey} className="border border-gray-200 rounded-lg overflow-hidden">
                      <button
                        onClick={() => toggleDay(dateKey)}
                        className="w-full flex items-center justify-between p-4 bg-gray-50 hover:bg-gray-100 transition-colors text-left"
                      >
                        <div className="flex items-center">
                          <Calendar className="w-5 h-5 mr-3 text-sage" />
                          <span className="font-medium text-gray-700 capitalize">{displayDate}</span>
                          <span className="ml-2 text-sm text-gray-500">({slots.length} horarios)</span>
                        </div>
                        {isExpanded ? (
                          <ChevronUp className="w-5 h-5 text-gray-500" />
                        ) : (
                          <ChevronDown className="w-5 h-5 text-gray-500" />
                        )}
                      </button>
                      
                      {isExpanded && (
                        <div className="p-4 bg-white">
                          <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
                            {slots.map((slot, index) => {
                              const startTime = new Date(slot.start).toLocaleTimeString('es-ES', {
                                hour: '2-digit',
                                minute: '2-digit'
                              });
                              const isSelected = selectedSlot?.start === slot.start;
                              
                              return (
                                <button
                                  key={index}
                                  onClick={() => setSelectedSlot(slot)}
                                  className={`p-3 rounded-lg border-2 transition-all ${
                                    isSelected
                                      ? 'border-sage bg-sage text-white'
                                      : 'border-gray-200 hover:border-sage hover:bg-sage-light'
                                  }`}
                                >
                                  <Clock className="w-4 h-4 mb-1 mx-auto" />
                                  <div className="text-sm font-medium">{startTime}</div>
                                  <div className="text-xs opacity-75">{slot.duration_minutes}min</div>
                                </button>
                              );
                            })}
                          </div>
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            )}

            {selectedSlot && (
              <div className="mt-6 p-4 bg-sage-light rounded-lg border-2 border-sage">
                <h3 className="font-medium mb-3">Reservar este horario</h3>
                <p className="text-sm text-gray-700 mb-3">
                  {formatDateTime(selectedSlot.start)}
                </p>
                
                <textarea
                  value={notes}
                  onChange={(e) => setNotes(e.target.value)}
                  placeholder="Notas o motivo de la consulta (opcional)"
                  className="w-full p-3 border border-gray-300 rounded-lg mb-3"
                  rows="3"
                />
                
                <div className="flex gap-2">
                  <button
                    onClick={handleBookAppointment}
                    disabled={loading}
                    className="flex-1 bg-sage text-white px-4 py-2 rounded-lg hover:bg-sage-dark transition-colors disabled:opacity-50"
                  >
                    Confirmar reserva
                  </button>
                  <button
                    onClick={() => setSelectedSlot(null)}
                    className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
                  >
                    Cancelar
                  </button>
                </div>
              </div>
            )}
          </div>

          {/* My Appointments */}
          <div className="bg-white rounded-lg shadow-elegant p-6">
            <h2 className="text-xl font-semibold mb-4 flex items-center">
              <User className="w-6 h-6 mr-2 text-sage" />
              Mis citas
            </h2>

            {appointments.length === 0 ? (
              <div className="text-center py-8 text-gray-500">
                <Calendar className="w-12 h-12 mx-auto mb-4 opacity-50" />
                <p>Aún no tienes citas programadas</p>
              </div>
            ) : (
              <div className="space-y-4">
                {appointments.map((appointment) => (
                  <div
                    key={appointment.id}
                    className="p-4 border border-gray-200 rounded-lg hover:shadow-md transition-shadow"
                  >
                    <div className="flex justify-between items-start mb-2">
                      <div className="flex-1">
                        <p className="font-medium text-gray-900">
                          Cita con {appointment.admin_name}
                        </p>
                        <p className="text-sm text-gray-600 mt-1">
                          {formatDateTime(appointment.start_time)}
                        </p>
                        {appointment.notes && (
                          <p className="text-sm text-gray-500 mt-2 italic">
                            "{appointment.notes}"
                          </p>
                        )}
                      </div>
                      {getStatusBadge(appointment.status)}
                    </div>
                    
                    {appointment.status !== 'cancelled' && (
                      <button
                        onClick={() => handleCancelAppointment(appointment.id)}
                        className="mt-3 text-sm text-red-600 hover:text-red-800 font-medium"
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
    </div>
  );
};

export default BookingPage;

