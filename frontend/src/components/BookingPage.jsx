import React from 'react';
import { Calendar, ExternalLink } from 'lucide-react';

const GOOGLE_CALENDAR_LINK = 'https://calendar.google.com/calendar/u/0/appointments/schedules/AcZssZ3wquE64w9KchPbPLdH_IxKfOOxm9NT8N2wJb73NuSvXQx8OuaIo5GXF1NXnEfAkNj0CBita1yB';

const BookingPage = () => {
  const handleOpenCalendar = () => {
    window.open(GOOGLE_CALENDAR_LINK, '_blank', 'noopener,noreferrer');
  };

  return (
    <div className="min-h-screen bg-gradient-elegant p-6">
      <div className="max-w-2xl mx-auto">
        <div className="bg-white rounded-2xl shadow-elegant p-8 text-center">
          <div className="w-20 h-20 bg-sage-light rounded-full flex items-center justify-center mx-auto mb-6">
            <Calendar className="w-10 h-10 text-sage" />
          </div>
          
          <h1 className="text-3xl font-bold text-gray-900 mb-4">
            Reservar una cita
          </h1>
          
          <p className="text-gray-600 mb-8 max-w-md mx-auto">
            Agenda una sesión individual conmigo. Selecciona el horario que mejor te convenga en mi calendario.
          </p>
          
          <button
            onClick={handleOpenCalendar}
            className="inline-flex items-center gap-3 bg-sage text-white px-8 py-4 rounded-xl text-lg font-semibold hover:bg-sage-dark transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
          >
            <Calendar className="w-6 h-6" />
            Ver horarios disponibles
            <ExternalLink className="w-5 h-5" />
          </button>
          
          <p className="text-sm text-gray-500 mt-6">
            Serás redirigido a Google Calendar para completar tu reserva
          </p>
        </div>
      </div>
    </div>
  );
};

export default BookingPage;
