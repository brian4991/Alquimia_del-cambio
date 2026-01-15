import React, { useState, useEffect } from 'react';
import { config } from '../../config';
import { ChevronLeftIcon, ChevronRightIcon } from '@heroicons/react/24/outline';

/**
 * Calendar View - Editorial calendar with drag-and-drop
 */
const CalendarView = ({ onSelectContent }) => {
  const [currentDate, setCurrentDate] = useState(new Date());
  const [calendarItems, setCalendarItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [viewMode, setViewMode] = useState('week'); // 'week' or 'month'

  useEffect(() => {
    loadCalendar();
  }, [currentDate, viewMode]);

  const loadCalendar = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem('token');
      
      let url;
      if (viewMode === 'week') {
        const weekOffset = getWeekOffset();
        url = `${config.apiUrl}/api/marketing/calendar/week?week_offset=${weekOffset}`;
      } else {
        url = `${config.apiUrl}/api/marketing/calendar/month?year=${currentDate.getFullYear()}&month=${currentDate.getMonth() + 1}`;
      }

      const response = await fetch(url, {
        headers: { 'Authorization': `Bearer ${token}` },
      });
      
      if (response.ok) {
        const data = await response.json();
        setCalendarItems(data.items || []);
      }
    } catch (error) {
      console.error('Error loading calendar:', error);
    } finally {
      setLoading(false);
    }
  };

  const getWeekOffset = () => {
    const today = new Date();
    const diffTime = currentDate.getTime() - today.getTime();
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    return Math.floor(diffDays / 7);
  };

  const navigatePrev = () => {
    const newDate = new Date(currentDate);
    if (viewMode === 'week') {
      newDate.setDate(newDate.getDate() - 7);
    } else {
      newDate.setMonth(newDate.getMonth() - 1);
    }
    setCurrentDate(newDate);
  };

  const navigateNext = () => {
    const newDate = new Date(currentDate);
    if (viewMode === 'week') {
      newDate.setDate(newDate.getDate() + 7);
    } else {
      newDate.setMonth(newDate.getMonth() + 1);
    }
    setCurrentDate(newDate);
  };

  const goToToday = () => {
    setCurrentDate(new Date());
  };

  const getWeekDays = () => {
    const start = new Date(currentDate);
    start.setDate(start.getDate() - start.getDay() + 1); // Monday
    
    const days = [];
    for (let i = 0; i < 7; i++) {
      const day = new Date(start);
      day.setDate(start.getDate() + i);
      days.push(day);
    }
    return days;
  };

  const getItemsForDate = (date) => {
    const dateStr = date.toISOString().split('T')[0];
    return calendarItems.filter(item => item.scheduled_date === dateStr);
  };

  const getPlatformColor = (platform) => {
    const colors = {
      'instagram': 'bg-pink-100 border-pink-300 text-pink-800',
      'tiktok': 'bg-gray-900 border-gray-700 text-white',
      'youtube': 'bg-red-100 border-red-300 text-red-800',
      'linkedin': 'bg-blue-100 border-blue-300 text-blue-800',
      'facebook': 'bg-indigo-100 border-indigo-300 text-indigo-800',
    };
    return colors[platform] || 'bg-gray-100 border-gray-300 text-gray-800';
  };

  const formatDateHeader = () => {
    if (viewMode === 'week') {
      const days = getWeekDays();
      const start = days[0];
      const end = days[6];
      return `${start.toLocaleDateString('es-ES', { day: 'numeric', month: 'short' })} - ${end.toLocaleDateString('es-ES', { day: 'numeric', month: 'short', year: 'numeric' })}`;
    }
    return currentDate.toLocaleDateString('es-ES', { month: 'long', year: 'numeric' });
  };

  const weekDays = getWeekDays();
  const dayNames = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-4">
          <h2 className="text-lg font-semibold text-gray-900">Calendario Editorial</h2>
          
          {/* View Toggle */}
          <div className="flex rounded-lg border border-gray-300 overflow-hidden">
            <button
              onClick={() => setViewMode('week')}
              className={`px-3 py-1 text-sm ${viewMode === 'week' ? 'bg-sage text-white' : 'bg-white text-gray-700 hover:bg-gray-50'}`}
            >
              Semana
            </button>
            <button
              onClick={() => setViewMode('month')}
              className={`px-3 py-1 text-sm ${viewMode === 'month' ? 'bg-sage text-white' : 'bg-white text-gray-700 hover:bg-gray-50'}`}
            >
              Mes
            </button>
          </div>
        </div>

        {/* Navigation */}
        <div className="flex items-center gap-4">
          <button
            onClick={goToToday}
            className="px-3 py-1 text-sm border border-gray-300 rounded-lg hover:bg-gray-50"
          >
            Hoy
          </button>
          
          <div className="flex items-center gap-2">
            <button
              onClick={navigatePrev}
              className="p-1 rounded-lg hover:bg-gray-100"
            >
              <ChevronLeftIcon className="w-5 h-5" />
            </button>
            
            <span className="text-sm font-medium text-gray-900 min-w-[200px] text-center">
              {formatDateHeader()}
            </span>
            
            <button
              onClick={navigateNext}
              className="p-1 rounded-lg hover:bg-gray-100"
            >
              <ChevronRightIcon className="w-5 h-5" />
            </button>
          </div>
        </div>
      </div>

      {/* Calendar Grid */}
      {loading ? (
        <div className="flex items-center justify-center py-12">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-sage"></div>
        </div>
      ) : (
        <div className="bg-white rounded-lg shadow overflow-hidden">
          {/* Day Headers */}
          <div className="grid grid-cols-7 border-b bg-gray-50">
            {dayNames.map((name, index) => (
              <div key={name} className="px-4 py-3 text-center">
                <span className="text-sm font-medium text-gray-500">{name}</span>
                {viewMode === 'week' && (
                  <div className={`text-lg font-semibold mt-1 ${
                    weekDays[index].toDateString() === new Date().toDateString()
                      ? 'text-sage'
                      : 'text-gray-900'
                  }`}>
                    {weekDays[index].getDate()}
                  </div>
                )}
              </div>
            ))}
          </div>

          {/* Week View */}
          {viewMode === 'week' && (
            <div className="grid grid-cols-7 min-h-[400px]">
              {weekDays.map((day, index) => {
                const items = getItemsForDate(day);
                const isToday = day.toDateString() === new Date().toDateString();
                
                return (
                  <div
                    key={index}
                    className={`border-r last:border-r-0 p-2 ${isToday ? 'bg-sage-light/10' : ''}`}
                  >
                    <div className="space-y-2">
                      {items.map((item) => (
                        <button
                          key={item.id}
                          type="button"
                          onClick={() => onSelectContent?.(item)}
                          className={`w-full text-left p-2 rounded border text-xs ${getPlatformColor(item.platform)} ${
                            onSelectContent ? 'hover:opacity-90' : ''
                          }`}
                        >
                          <div className="font-medium truncate">
                            {item.content?.title || item.content?.content_type || 'Contenido'}
                          </div>
                          {item.scheduled_time && (
                            <div className="opacity-75 mt-1">{item.scheduled_time}</div>
                          )}
                        </button>
                      ))}
                      
                      {items.length === 0 && (
                        <div className="text-center py-4 text-gray-400 text-xs">
                          Sin contenido
                        </div>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          )}

          {/* Month View */}
          {viewMode === 'month' && (
            <MonthGrid 
              currentDate={currentDate} 
              items={calendarItems}
              getPlatformColor={getPlatformColor}
              onSelectContent={onSelectContent}
            />
          )}
        </div>
      )}

      {/* Legend */}
      <div className="flex items-center gap-4 text-sm">
        <span className="text-gray-500">Plataformas:</span>
        {['instagram', 'tiktok', 'youtube', 'linkedin', 'facebook'].map((platform) => (
          <span key={platform} className={`px-2 py-1 rounded ${getPlatformColor(platform)}`}>
            {platform}
          </span>
        ))}
      </div>
    </div>
  );
};

/**
 * Month Grid Component
 */
const MonthGrid = ({ currentDate, items, getPlatformColor, onSelectContent }) => {
  const getDaysInMonth = () => {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    
    const days = [];
    
    // Add empty cells for days before the first of the month
    const startDay = firstDay.getDay() || 7; // Convert Sunday (0) to 7
    for (let i = 1; i < startDay; i++) {
      days.push(null);
    }
    
    // Add all days of the month
    for (let i = 1; i <= lastDay.getDate(); i++) {
      days.push(new Date(year, month, i));
    }
    
    return days;
  };

  const getItemsForDate = (date) => {
    if (!date) return [];
    const dateStr = date.toISOString().split('T')[0];
    return items.filter(item => item.scheduled_date === dateStr);
  };

  const days = getDaysInMonth();
  const weeks = [];
  for (let i = 0; i < days.length; i += 7) {
    weeks.push(days.slice(i, i + 7));
  }

  return (
    <div className="divide-y">
      {weeks.map((week, weekIndex) => (
        <div key={weekIndex} className="grid grid-cols-7">
          {week.map((day, dayIndex) => {
            const dayItems = getItemsForDate(day);
            const isToday = day && day.toDateString() === new Date().toDateString();
            
            return (
              <div
                key={dayIndex}
                className={`min-h-[100px] border-r last:border-r-0 p-2 ${
                  !day ? 'bg-gray-50' : isToday ? 'bg-sage-light/10' : ''
                }`}
              >
                {day && (
                  <>
                    <div className={`text-sm font-medium mb-2 ${isToday ? 'text-sage' : 'text-gray-900'}`}>
                      {day.getDate()}
                    </div>
                    <div className="space-y-1">
                      {dayItems.slice(0, 3).map((item) => (
                        <button
                          key={item.id}
                          type="button"
                          onClick={() => onSelectContent?.(item)}
                          className={`w-full text-left px-1 py-0.5 rounded text-xs truncate ${getPlatformColor(item.platform)} ${
                            onSelectContent ? 'hover:opacity-90' : ''
                          }`}
                        >
                          {item.platform}
                        </button>
                      ))}
                      {dayItems.length > 3 && (
                        <div className="text-xs text-gray-500">
                          +{dayItems.length - 3} más
                        </div>
                      )}
                    </div>
                  </>
                )}
              </div>
            );
          })}
        </div>
      ))}
    </div>
  );
};

export default CalendarView;
