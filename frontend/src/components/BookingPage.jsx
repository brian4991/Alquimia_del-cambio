import React, { useState, useEffect } from 'react';
import { Calendar, Clock, User, CheckCircle, XCircle, AlertCircle, ChevronLeft, ChevronRight } from 'lucide-react';
import { config } from '../config';

const BookingPage = () => {
  const [appointments, setAppointments] = useState([]);
  const [availableSlots, setAvailableSlots] = useState([]);
  const [selectedDate, setSelectedDate] = useState(null);
  const [currentMonth, setCurrentMonth] = useState(new Date());
  const [selectedSlot, setSelectedSlot] = useState(null);
  const [notes, setNotes] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [adminId, setAdminId] = useState(null);

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
    if (!adminId || !selectedDate) return;
    
    setLoading(true);
    setSelectedSlot(null);
    try {
      const startDate = new Date(selectedDate);
      startDate.setHours(0, 0, 0, 0);
      
      const endDate = new Date(selectedDate);
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

  // Calendar helpers
  const getDaysInMonth = (date) => {
    const year = date.getFullYear();
    const month = date.getMonth();
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const daysInMonth = lastDay.getDate();
    const startingDay = firstDay.getDay();
    
    return { daysInMonth, startingDay };
  };

  const isSameDay = (date1, date2) => {
    if (!date1 || !date2) return false;
    return date1.getFullYear() === date2.getFullYear() &&
           date1.getMonth() === date2.getMonth() &&
           date1.getDate() === date2.getDate();
  };

  const isToday = (date) => {
    return isSameDay(date, new Date());
  };

  const isPastDate = (date) => {
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    return date < today;
  };

  const goToPreviousMonth = () => {
    setCurrentMonth(new Date(currentMonth.getFullYear(), currentMonth.getMonth() - 1, 1));
  };

  const goToNextMonth = () => {
    setCurrentMonth(new Date(currentMonth.getFullYear(), currentMonth.getMonth() + 1, 1));
  };

  const handleDateClick = (day) => {
    const newDate = new Date(currentMonth.getFullYear(), currentMonth.getMonth(), day);
    if (!isPastDate(newDate)) {
      setSelectedDate(newDate);
      setAvailableSlots([]);
    }
  };

  const { daysInMonth, startingDay } = getDaysInMonth(currentMonth);
  const monthNames = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
                      'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
  const dayNames = ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'];

  const formatSelectedDate = () => {
    if (!selectedDate) return '';
    return selectedDate.toLocaleDateString('es-ES', {
      weekday: 'long',
      day: 'numeric',
      month: 'long',
      year: 'numeric'
    });
  };

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

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Calendar */}
          <div className="bg-white rounded-lg shadow-elegant p-6">
            <h2 className="text-xl font-semibold mb-4 flex items-center">
              <Calendar className="w-6 h-6 mr-2 text-sage" />
              Selecciona un día
            </h2>

            {/* Month Navigation */}
            <div className="flex items-center justify-between mb-4">
              <button
                onClick={goToPreviousMonth}
                className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
              >
                <ChevronLeft className="w-5 h-5 text-gray-600" />
              </button>
              <h3 className="font-semibold text-gray-800">
                {monthNames[currentMonth.getMonth()]} {currentMonth.getFullYear()}
              </h3>
              <button
                onClick={goToNextMonth}
                className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
              >
                <ChevronRight className="w-5 h-5 text-gray-600" />
              </button>
            </div>

            {/* Day Names */}
            <div className="grid grid-cols-7 gap-1 mb-2">
              {dayNames.map((day) => (
                <div key={day} className="text-center text-sm font-medium text-gray-500 py-2">
                  {day}
                </div>
              ))}
            </div>

            {/* Calendar Days */}
            <div className="grid grid-cols-7 gap-1">
              {/* Empty cells for days before the first of the month */}
              {Array.from({ length: startingDay }, (_, i) => (
                <div key={`empty-${i}`} className="aspect-square"></div>
              ))}
              
              {/* Days of the month */}
              {Array.from({ length: daysInMonth }, (_, i) => {
                const day = i + 1;
                const date = new Date(currentMonth.getFullYear(), currentMonth.getMonth(), day);
                const isSelected = isSameDay(date, selectedDate);
                const isTodayDate = isToday(date);
                const isPast = isPastDate(date);
                
                return (
                  <button
                    key={day}
                    onClick={() => handleDateClick(day)}
                    disabled={isPast}
                    className={`aspect-square flex items-center justify-center rounded-lg text-sm font-medium transition-all
                      ${isPast 
                        ? 'text-gray-300 cursor-not-allowed' 
                        : isSelected 
                          ? 'bg-sage text-white shadow-lg' 
                          : isTodayDate 
                            ? 'bg-sage-light text-sage border-2 border-sage' 
                            : 'hover:bg-gray-100 text-gray-700'
                      }`}
                  >
                    {day}
                  </button>
                );
              })}
            </div>
          </div>

          {/* Available Slots */}
          <div className="bg-white rounded-lg shadow-elegant p-6">
            <h2 className="text-xl font-semibold mb-4 flex items-center">
              <Clock className="w-6 h-6 mr-2 text-sage" />
              Horarios disponibles
            </h2>

            {!selectedDate ? (
              <div className="text-center py-8 text-gray-500">
                <Calendar className="w-12 h-12 mx-auto mb-4 opacity-50" />
                <p>Selecciona un día en el calendario</p>
              </div>
            ) : loading ? (
              <div className="text-center py-8">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-sage mx-auto"></div>
                <p className="mt-4 text-gray-600">Cargando...</p>
              </div>
            ) : availableSlots.length === 0 ? (
              <div className="text-center py-8 text-gray-500">
                <Clock className="w-12 h-12 mx-auto mb-4 opacity-50" />
                <p>No hay horarios disponibles para este día</p>
              </div>
            ) : (
              <>
                <p className="text-sm text-gray-600 mb-4 capitalize font-medium">
                  {formatSelectedDate()}
                </p>
                <div className="grid grid-cols-2 gap-2">
                  {availableSlots.map((slot, index) => {
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
              </>
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
