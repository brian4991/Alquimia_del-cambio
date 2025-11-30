import React, { useState, useEffect } from 'react';
import { Calendar, Clock, User, CheckCircle, XCircle, AlertCircle } from 'lucide-react';
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
          setError('Le calendrier n\'est pas encore configuré. Veuillez réessayer plus tard.');
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
      setError('Erreur lors du chargement des disponibilités');
    } finally {
      setLoading(false);
    }
  };

  const handleBookAppointment = async () => {
    if (!selectedSlot) {
      setError('Veuillez sélectionner un créneau');
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
        setSuccess('Rendez-vous réservé avec succès! Vous recevrez une confirmation par email.');
        setSelectedSlot(null);
        setNotes('');
        loadMyAppointments();
        loadAvailableSlots();
      } else {
        const data = await response.json();
        setError(data.detail || 'Erreur lors de la réservation');
      }
    } catch (err) {
      console.error('Error booking appointment:', err);
      setError('Erreur lors de la réservation du rendez-vous');
    } finally {
      setLoading(false);
    }
  };

  const handleCancelAppointment = async (appointmentId) => {
    if (!confirm('Êtes-vous sûr de vouloir annuler ce rendez-vous?')) {
      return;
    }

    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/appointments/${appointmentId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });

      if (response.ok) {
        setSuccess('Rendez-vous annulé avec succès');
        loadMyAppointments();
        loadAvailableSlots();
      }
    } catch (err) {
      console.error('Error cancelling appointment:', err);
      setError('Erreur lors de l\'annulation');
    }
  };

  const formatDateTime = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleString('fr-FR', {
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
      pending: { color: 'bg-yellow-100 text-yellow-800', icon: AlertCircle, text: 'En attente' },
      confirmed: { color: 'bg-green-100 text-green-800', icon: CheckCircle, text: 'Confirmé' },
      cancelled: { color: 'bg-red-100 text-red-800', icon: XCircle, text: 'Annulé' }
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
      const dateKey = date.toLocaleDateString('fr-FR');
      
      if (!grouped[dateKey]) {
        grouped[dateKey] = [];
      }
      grouped[dateKey].push(slot);
    });
    
    return grouped;
  };

  const slotsByDate = groupSlotsByDate();

  return (
    <div className="min-h-screen bg-gradient-elegant p-6">
      <div className="max-w-7xl mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Mes Rendez-vous</h1>
          <p className="text-gray-600">Réservez un créneau pour un entretien individuel</p>
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
              Créneaux disponibles
            </h2>

            {loading ? (
              <div className="text-center py-8">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-sage mx-auto"></div>
                <p className="mt-4 text-gray-600">Chargement...</p>
              </div>
            ) : Object.keys(slotsByDate).length === 0 ? (
              <div className="text-center py-8 text-gray-500">
                <Clock className="w-12 h-12 mx-auto mb-4 opacity-50" />
                <p>Aucun créneau disponible pour le moment</p>
              </div>
            ) : (
              <div className="space-y-6">
                {Object.entries(slotsByDate).map(([date, slots]) => (
                  <div key={date}>
                    <h3 className="font-medium text-gray-700 mb-3">{date}</h3>
                    <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
                      {slots.map((slot, index) => {
                        const startTime = new Date(slot.start).toLocaleTimeString('fr-FR', {
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
                ))}
              </div>
            )}

            {selectedSlot && (
              <div className="mt-6 p-4 bg-sage-light rounded-lg border-2 border-sage">
                <h3 className="font-medium mb-3">Réserver ce créneau</h3>
                <p className="text-sm text-gray-700 mb-3">
                  {formatDateTime(selectedSlot.start)}
                </p>
                
                <textarea
                  value={notes}
                  onChange={(e) => setNotes(e.target.value)}
                  placeholder="Notes ou raison de la consultation (optionnel)"
                  className="w-full p-3 border border-gray-300 rounded-lg mb-3"
                  rows="3"
                />
                
                <div className="flex gap-2">
                  <button
                    onClick={handleBookAppointment}
                    disabled={loading}
                    className="flex-1 bg-sage text-white px-4 py-2 rounded-lg hover:bg-sage-dark transition-colors disabled:opacity-50"
                  >
                    Confirmer la réservation
                  </button>
                  <button
                    onClick={() => setSelectedSlot(null)}
                    className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
                  >
                    Annuler
                  </button>
                </div>
              </div>
            )}
          </div>

          {/* My Appointments */}
          <div className="bg-white rounded-lg shadow-elegant p-6">
            <h2 className="text-xl font-semibold mb-4 flex items-center">
              <User className="w-6 h-6 mr-2 text-sage" />
              Mes rendez-vous
            </h2>

            {appointments.length === 0 ? (
              <div className="text-center py-8 text-gray-500">
                <Calendar className="w-12 h-12 mx-auto mb-4 opacity-50" />
                <p>Vous n'avez pas encore de rendez-vous</p>
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
                          Rendez-vous avec {appointment.admin_name}
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
                        Annuler ce rendez-vous
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

