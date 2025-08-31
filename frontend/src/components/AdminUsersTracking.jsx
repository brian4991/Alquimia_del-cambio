import React, { useState, useEffect } from 'react';
import { 
  UsersIcon, 
  ChartBarIcon, 
  DocumentTextIcon,
  CheckCircleIcon,
  ClockIcon,
  EyeIcon,
  UserIcon,
  BookOpenIcon,
  AcademicCapIcon,
  MapPinIcon,
  ArrowRightIcon,
  CalendarIcon,
  SparklesIcon
} from '@heroicons/react/24/outline';
import { getAdminUsersStats, getUserResponses } from '../services/api';
import { CheckCircleIcon as CheckCircleIconSolid } from '@heroicons/react/24/solid';

const AdminUsersTracking = () => {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [userResponses, setUserResponses] = useState([]);  
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [stats, setStats] = useState({
    totalUsers: 0,
    activeUsers: 0,
    completedModules: 0,
    totalResponses: 0
  });

  useEffect(() => {
    loadUsersData();
  }, []);

  const loadUsersData = async () => {
    try {
      setLoading(true);
      
      // Get users and stats in one call
      const data = await getAdminUsersStats();
      setUsers(data.users);
      setStats({
        totalUsers: data.stats.total_users,
        activeUsers: data.stats.active_users,
        completedModules: 0, // Will be calculated when we have progress data
        totalResponses: data.stats.total_responses
      });
      
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const loadUserResponses = async (userId) => {
    try {
      const responses = await getUserResponses(userId);
      setUserResponses(responses);
    } catch (err) {
      console.error('Error loading user responses:', err);
    }
  };

  const handleUserSelect = (user) => {
    setSelectedUser(user);
    loadUserResponses(user.id);
  };

  const getProviderIcon = (provider) => {
    switch (provider) {
      case 'google':
        return '🔵';
      case 'facebook':
        return '🔵';
      case 'local':
      default:
        return '👤';
    }
  };

  const getProviderColor = (provider) => {
    switch (provider) {
      case 'google':
        return 'bg-red-100 text-red-700';
      case 'facebook':
        return 'bg-blue-100 text-blue-700';
      case 'local':
      default:
        return 'bg-gray-100 text-gray-700';
    }
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('es-ES', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getProgressColor = (percentage) => {
    if (percentage >= 80) return 'bg-green-500';
    if (percentage >= 60) return 'bg-blue-500';
    if (percentage >= 40) return 'bg-yellow-500';
    if (percentage >= 20) return 'bg-orange-500';
    return 'bg-red-500';
  };

  const getProgressTextColor = (percentage) => {
    if (percentage >= 80) return 'text-green-600';
    if (percentage >= 60) return 'text-blue-600';
    if (percentage >= 40) return 'text-yellow-600';
    if (percentage >= 20) return 'text-orange-600';
    return 'text-red-600';
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 flex items-center justify-center">
        <div className="bg-white/90 backdrop-blur-sm rounded-3xl shadow-2xl p-12 border border-slate-200 text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-4 border-blue-500 border-t-transparent mx-auto mb-6"></div>
          <p className="text-slate-600 text-xl font-medium">Cargando datos de usuarios...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-7xl mx-auto px-6 py-12">
        <div className="bg-red-50 border border-red-200 rounded-3xl p-12 text-center shadow-lg">
          <div className="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <ChartBarIcon className="w-8 h-8 text-red-600" />
          </div>
          <h2 className="text-3xl font-bold text-red-800 mb-4">Error</h2>
          <p className="text-red-600 mb-8 text-lg">{error}</p>
          <button 
            onClick={loadUsersData}
            className="bg-red-600 text-white px-8 py-4 rounded-xl hover:bg-red-700 transition-all duration-200 font-medium shadow-lg hover:shadow-xl"
          >
            Reintentar
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50">
      <div className="max-w-7xl mx-auto px-6 py-12">
        {/* Header */}
        <div className="mb-12">
          <div className="flex items-center space-x-6 mb-6">
            <div className="p-4 bg-gradient-to-br from-blue-500 to-purple-600 rounded-2xl shadow-lg">
              <UsersIcon className="w-10 h-10 text-white" />
            </div>
            <div>
              <h1 className="text-4xl font-bold text-slate-900 mb-2">Seguimiento de Usuarios</h1>
              <p className="text-slate-600 text-lg">Monitorea el progreso y las respuestas de tus usuarios</p>
            </div>
          </div>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
          <div className="bg-white rounded-2xl shadow-lg p-8 border border-slate-200 hover:shadow-xl transition-all duration-300">
            <div className="flex items-center justify-between mb-4">
              <div className="p-3 bg-blue-100 rounded-xl">
                <UsersIcon className="w-8 h-8 text-blue-600" />
              </div>
              <SparklesIcon className="w-6 h-6 text-blue-400" />
            </div>
            <p className="text-slate-600 text-sm font-medium mb-2">Total Usuarios</p>
            <p className="text-4xl font-bold text-slate-900">{stats.totalUsers}</p>
          </div>

          <div className="bg-white rounded-2xl shadow-lg p-8 border border-slate-200 hover:shadow-xl transition-all duration-300">
            <div className="flex items-center justify-between mb-4">
              <div className="p-3 bg-green-100 rounded-xl">
                <CheckCircleIconSolid className="w-8 h-8 text-green-600" />
              </div>
              <SparklesIcon className="w-6 h-6 text-green-400" />
            </div>
            <p className="text-slate-600 text-sm font-medium mb-2">Usuarios Activos</p>
            <p className="text-4xl font-bold text-green-600">{stats.activeUsers}</p>
          </div>

          <div className="bg-white rounded-2xl shadow-lg p-8 border border-slate-200 hover:shadow-xl transition-all duration-300">
            <div className="flex items-center justify-between mb-4">
              <div className="p-3 bg-purple-100 rounded-xl">
                <BookOpenIcon className="w-8 h-8 text-purple-600" />
              </div>
              <SparklesIcon className="w-6 h-6 text-purple-400" />
            </div>
            <p className="text-slate-600 text-sm font-medium mb-2">Módulos Completados</p>
            <p className="text-4xl font-bold text-purple-600">{stats.completedModules}</p>
          </div>

          <div className="bg-white rounded-2xl shadow-lg p-8 border border-slate-200 hover:shadow-xl transition-all duration-300">
            <div className="flex items-center justify-between mb-4">
              <div className="p-3 bg-orange-100 rounded-xl">
                <DocumentTextIcon className="w-8 h-8 text-orange-600" />
              </div>
              <SparklesIcon className="w-6 h-6 text-orange-400" />
            </div>
            <p className="text-slate-600 text-sm font-medium mb-2">Total Respuestas</p>
            <p className="text-4xl font-bold text-orange-600">{stats.totalResponses}</p>
          </div>
        </div>

        <div className="grid grid-cols-1 xl:grid-cols-3 gap-8">
          {/* Users List */}
          <div className="xl:col-span-2 bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
            <div className="p-8 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-blue-50">
              <h2 className="text-2xl font-bold text-slate-900 flex items-center">
                <UsersIcon className="w-6 h-6 mr-3 text-blue-600" />
                Lista de Usuarios
              </h2>
              <p className="text-slate-600 mt-2">Selecciona un usuario para ver su progreso detallado</p>
            </div>
            
            <div className="p-8">
              {users.length === 0 ? (
                <div className="text-center py-16 text-slate-500">
                  <UsersIcon className="w-16 h-16 mx-auto mb-6 opacity-50" />
                  <p className="text-xl font-medium">No hay usuarios registrados</p>
                </div>
              ) : (
                <div className="space-y-6 max-h-[600px] overflow-y-auto">
                  {users.map((user) => (
                    <div
                      key={user.id}
                      onClick={() => handleUserSelect(user)}
                      className={`p-6 rounded-2xl border-2 transition-all duration-300 cursor-pointer hover:shadow-lg ${
                        selectedUser?.id === user.id
                          ? 'border-blue-300 bg-blue-50 shadow-lg scale-[1.02]'
                          : 'border-slate-200 hover:border-slate-300 hover:scale-[1.01]'
                      }`}
                    >
                      <div className="flex items-start justify-between mb-4">
                        <div className="flex items-center space-x-4">
                          <div className="flex-shrink-0">
                            <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center text-white font-bold text-lg">
                              {user.username.charAt(0).toUpperCase()}
                            </div>
                          </div>
                          <div>
                            <h3 className="font-bold text-slate-900 text-lg">{user.username}</h3>
                            <p className="text-slate-600">{user.email}</p>
                            <div className="flex items-center space-x-2 mt-2">
                              <span className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-medium ${getProviderColor(user.provider)}`}>
                                {getProviderIcon(user.provider)} {user.provider}
                              </span>
                              <span className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-medium ${
                                user.role === 'admin' 
                                  ? 'bg-purple-100 text-purple-700' 
                                  : 'bg-slate-100 text-slate-700'
                              }`}>
                                {user.role}
                              </span>
                            </div>
                          </div>
                        </div>
                        <div className="text-right">
                          {user.is_active ? (
                            <div className="flex items-center text-green-600 text-sm font-medium">
                              <CheckCircleIconSolid className="w-4 h-4 mr-1" />
                              Activo
                            </div>
                          ) : (
                            <div className="flex items-center text-red-600 text-sm font-medium">
                              <ClockIcon className="w-4 h-4 mr-1" />
                              Inactivo
                            </div>
                          )}
                        </div>
                      </div>

                      {/* Progress Section */}
                      {user.progress && (
                        <div className="bg-slate-50 rounded-xl p-4 mb-4">
                          <div className="flex items-center justify-between mb-3">
                            <h4 className="font-semibold text-slate-900 flex items-center">
                              <MapPinIcon className="w-4 h-4 mr-2 text-blue-600" />
                              Progreso Actual
                            </h4>
                            <span className={`text-sm font-bold ${getProgressTextColor(user.progress?.progress_percentage || 0)}`}>
                              {user.progress?.progress_percentage || 0}%
                            </span>
                          </div>
                          
                          {/* Progress Bar */}
                          <div className="w-full bg-slate-200 rounded-full h-3 mb-4">
                            <div 
                              className={`h-3 rounded-full transition-all duration-500 ${getProgressColor(user.progress?.progress_percentage || 0)}`}
                              style={{ width: `${user.progress?.progress_percentage || 0}%` }}
                            ></div>
                          </div>

                          {/* Current Position */}
                          {user.progress && user.progress.current_module ? (
                            <div className="flex items-center space-x-2 text-sm text-slate-600">
                              <span className="font-medium">Módulo {user.progress.current_module.order}:</span>
                              <span>{user.progress.current_module.title}</span>
                              <ArrowRightIcon className="w-4 h-4" />
                              <span className="font-medium">Tema {user.progress.current_theme.order}:</span>
                              <span>{user.progress.current_theme.title}</span>
                            </div>
                          ) : (
                            <div className="text-sm text-slate-500 italic">
                              Aún no ha comenzado el programa
                            </div>
                          )}

                          {/* Stats */}
                          <div className="grid grid-cols-3 gap-4 mt-4 pt-4 border-t border-slate-200">
                            <div className="text-center">
                              <div className="text-lg font-bold text-blue-600">{user.progress?.completed_exercises || 0}</div>
                              <div className="text-xs text-slate-500">Ejercicios</div>
                            </div>
                            <div className="text-center">
                              <div className="text-lg font-bold text-purple-600">{user.progress?.completed_themes || 0}</div>
                              <div className="text-xs text-slate-500">Temas</div>
                            </div>
                            <div className="text-center">
                              <div className="text-lg font-bold text-green-600">{user.progress?.completed_modules || 0}</div>
                              <div className="text-xs text-slate-500">Módulos</div>
                            </div>
                          </div>
                        </div>
                      )}

                      <div className="flex items-center justify-between text-sm text-slate-500">
                        <div className="flex items-center">
                          <CalendarIcon className="w-4 h-4 mr-1" />
                          Registrado: {formatDate(user.created_at)}
                        </div>
                        <div className="flex items-center">
                          <DocumentTextIcon className="w-4 h-4 mr-1" />
                          {user.response_count} respuestas
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* User Details */}
          <div className="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
            <div className="p-8 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-blue-50">
              <h2 className="text-2xl font-bold text-slate-900 flex items-center">
                <EyeIcon className="w-6 h-6 mr-3 text-blue-600" />
                Detalles del Usuario
              </h2>
              <p className="text-slate-600 mt-2">Información detallada y respuestas</p>
            </div>
            
            <div className="p-8">
              {!selectedUser ? (
                <div className="text-center py-16 text-slate-500">
                  <UserIcon className="w-16 h-16 mx-auto mb-6 opacity-50" />
                  <p className="text-xl font-medium">Selecciona un usuario</p>
                  <p className="text-sm mt-2">para ver sus detalles y respuestas</p>
                </div>
              ) : (
                <div className="space-y-8">
                  {/* User Info */}
                  <div className="bg-gradient-to-br from-blue-50 to-purple-50 rounded-2xl p-6">
                    <h3 className="font-bold text-slate-900 mb-4 flex items-center">
                      <UserIcon className="w-5 h-5 mr-2 text-blue-600" />
                      Información del Usuario
                    </h3>
                    <div className="space-y-3 text-sm">
                      <div className="flex justify-between items-center py-2 border-b border-blue-100">
                        <span className="text-slate-600 font-medium">Nombre:</span>
                        <span className="font-bold text-slate-900">{selectedUser.username}</span>
                      </div>
                      <div className="flex justify-between items-center py-2 border-b border-blue-100">
                        <span className="text-slate-600 font-medium">Email:</span>
                        <span className="font-bold text-slate-900">{selectedUser.email}</span>
                      </div>
                      <div className="flex justify-between items-center py-2 border-b border-blue-100">
                        <span className="text-slate-600 font-medium">Proveedor:</span>
                        <span className={`font-bold px-3 py-1 rounded-full text-xs ${getProviderColor(selectedUser.provider)}`}>
                          {selectedUser.provider}
                        </span>
                      </div>
                      <div className="flex justify-between items-center py-2">
                        <span className="text-slate-600 font-medium">Estado:</span>
                        <span className={`font-bold ${selectedUser.is_active ? 'text-green-600' : 'text-red-600'}`}>
                          {selectedUser.is_active ? 'Activo' : 'Inactivo'}
                        </span>
                      </div>
                    </div>
                  </div>

                  {/* User Responses */}
                  <div>
                    <h3 className="font-bold text-slate-900 mb-4 flex items-center">
                      <DocumentTextIcon className="w-5 h-5 mr-2 text-blue-600" />
                      Respuestas a Ejercicios
                    </h3>
                    {userResponses.length === 0 ? (
                      <div className="text-center py-12 text-slate-500 bg-slate-50 rounded-2xl">
                        <DocumentTextIcon className="w-12 h-12 mx-auto mb-4 opacity-50" />
                        <p className="font-medium">No hay respuestas registradas</p>
                        <p className="text-sm mt-1">El usuario aún no ha completado ejercicios</p>
                      </div>
                    ) : (
                      <div className="space-y-4 max-h-96 overflow-y-auto">
                        {userResponses.map((response, index) => (
                          <div key={index} className="bg-slate-50 rounded-xl p-4 border border-slate-200">
                            <div className="flex justify-between items-start mb-3">
                              <div>
                                <h4 className="font-semibold text-slate-900 text-sm">
                                  {response.module_title} → {response.theme_title}
                                </h4>
                                <p className="text-xs text-slate-500 mt-1">
                                  Ejercicio: {response.exercise_title}
                                </p>
                              </div>
                              <span className="text-xs text-slate-500 bg-white px-2 py-1 rounded-full">
                                {formatDate(response.submitted_at)}
                              </span>
                            </div>
                            <p className="text-sm text-slate-700 leading-relaxed bg-white p-3 rounded-lg border">
                              {response.response_text}
                            </p>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminUsersTracking;