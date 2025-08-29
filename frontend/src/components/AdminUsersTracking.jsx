import React, { useState, useEffect } from 'react';
import { 
  UsersIcon, 
  ChartBarIcon, 
  DocumentTextIcon,
  CheckCircleIcon,
  ClockIcon,
  EyeIcon,
  UserIcon,
  BookOpenIcon
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

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('es-ES', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-serene flex items-center justify-center">
        <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-2xl p-8 border border-sage-200 text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-4 border-sage border-t-transparent mx-auto mb-4"></div>
          <p className="text-sage font-inter text-lg">Cargando datos de usuarios...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-7xl mx-auto px-6 py-12">
        <div className="bg-red-50 border border-red-200 rounded-2xl p-8 text-center">
          <h2 className="text-2xl font-bold text-red-800 mb-4">Error</h2>
          <p className="text-red-600 mb-6">{error}</p>
          <button 
            onClick={loadUsersData}
            className="bg-red-600 text-white px-6 py-3 rounded-lg hover:bg-red-700 transition-colors"
          >
            Reintentar
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-6 py-12">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center space-x-4 mb-4">
          <div className="p-3 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl">
            <UsersIcon className="w-8 h-8 text-white" />
          </div>
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Seguimiento de Usuarios</h1>
            <p className="text-gray-600">Monitorea el progreso y las respuestas de tus usuarios</p>
          </div>
        </div>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600 mb-1">Total Usuarios</p>
              <p className="text-3xl font-bold text-gray-900">{stats.totalUsers}</p>
            </div>
            <div className="p-3 bg-blue-100 rounded-lg">
              <UsersIcon className="w-6 h-6 text-blue-600" />
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600 mb-1">Usuarios Activos</p>
              <p className="text-3xl font-bold text-green-600">{stats.activeUsers}</p>
            </div>
            <div className="p-3 bg-green-100 rounded-lg">
              <CheckCircleIconSolid className="w-6 h-6 text-green-600" />
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600 mb-1">Módulos Completados</p>
              <p className="text-3xl font-bold text-purple-600">{stats.completedModules}</p>
            </div>
            <div className="p-3 bg-purple-100 rounded-lg">
              <BookOpenIcon className="w-6 h-6 text-purple-600" />
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600 mb-1">Total Respuestas</p>
              <p className="text-3xl font-bold text-orange-600">{stats.totalResponses}</p>
            </div>
            <div className="p-3 bg-orange-100 rounded-lg">
              <DocumentTextIcon className="w-6 h-6 text-orange-600" />
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Users List */}
        <div className="bg-white rounded-xl shadow-lg border border-gray-200">
          <div className="p-6 border-b border-gray-200">
            <h2 className="text-xl font-bold text-gray-900 flex items-center">
              <UsersIcon className="w-5 h-5 mr-2" />
              Lista de Usuarios
            </h2>
          </div>
          
          <div className="p-6">
            {users.length === 0 ? (
              <div className="text-center py-8 text-gray-500">
                <UsersIcon className="w-12 h-12 mx-auto mb-4 opacity-50" />
                <p>No hay usuarios registrados</p>
              </div>
            ) : (
              <div className="space-y-3 max-h-96 overflow-y-auto">
                {users.map((user) => (
                  <div
                    key={user.id}
                    onClick={() => handleUserSelect(user)}
                    className={`p-4 rounded-lg border transition-all cursor-pointer hover:shadow-md ${
                      selectedUser?.id === user.id
                        ? 'border-blue-300 bg-blue-50 shadow-md'
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center space-x-3">
                        <div className="flex-shrink-0">
                          <span className="text-2xl">{getProviderIcon(user.provider)}</span>
                        </div>
                        <div>
                          <h3 className="font-semibold text-gray-900">{user.username}</h3>
                          <p className="text-sm text-gray-600">{user.email}</p>
                          <p className="text-xs text-blue-600">{user.response_count} respuestas</p>
                        </div>
                      </div>
                      <div className="text-right">
                        <div className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium ${
                          user.role === 'admin' 
                            ? 'bg-purple-100 text-purple-700' 
                            : 'bg-gray-100 text-gray-700'
                        }`}>
                          {user.role}
                        </div>
                        {user.is_active ? (
                          <p className="text-xs text-green-600 mt-1">Activo</p>
                        ) : (
                          <p className="text-xs text-red-600 mt-1">Inactivo</p>
                        )}
                      </div>
                    </div>
                    <div className="mt-2 text-xs text-gray-500">
                      Registrado: {formatDate(user.created_at)}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* User Details */}
        <div className="bg-white rounded-xl shadow-lg border border-gray-200">
          <div className="p-6 border-b border-gray-200">
            <h2 className="text-xl font-bold text-gray-900 flex items-center">
              <EyeIcon className="w-5 h-5 mr-2" />
              Detalles del Usuario
            </h2>
          </div>
          
          <div className="p-6">
            {!selectedUser ? (
              <div className="text-center py-12 text-gray-500">
                <UserIcon className="w-12 h-12 mx-auto mb-4 opacity-50" />
                <p>Selecciona un usuario para ver sus detalles</p>
              </div>
            ) : (
              <div className="space-y-6">
                {/* User Info */}
                <div className="bg-gray-50 rounded-lg p-4">
                  <h3 className="font-semibold text-gray-900 mb-3">Información del Usuario</h3>
                  <div className="space-y-2 text-sm">
                    <div className="flex justify-between">
                      <span className="text-gray-600">Nombre:</span>
                      <span className="font-medium">{selectedUser.username}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-gray-600">Email:</span>
                      <span className="font-medium">{selectedUser.email}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-gray-600">Proveedor:</span>
                      <span className="font-medium capitalize">{selectedUser.provider}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-gray-600">Estado:</span>
                      <span className={`font-medium ${selectedUser.is_active ? 'text-green-600' : 'text-red-600'}`}>
                        {selectedUser.is_active ? 'Activo' : 'Inactivo'}
                      </span>
                    </div>
                  </div>
                </div>

                {/* User Responses */}
                <div>
                  <h3 className="font-semibold text-gray-900 mb-3">Respuestas a Ejercicios</h3>
                  {userResponses.length === 0 ? (
                    <div className="text-center py-8 text-gray-500 bg-gray-50 rounded-lg">
                      <DocumentTextIcon className="w-8 h-8 mx-auto mb-2 opacity-50" />
                      <p>No hay respuestas registradas</p>
                    </div>
                  ) : (
                    <div className="space-y-3 max-h-64 overflow-y-auto">
                      {userResponses.map((response, index) => (
                        <div key={index} className="bg-gray-50 rounded-lg p-4">
                          <div className="flex justify-between items-start mb-2">
                            <h4 className="font-medium text-gray-900 text-sm">
                              Ejercicio #{response.exercise_id}
                            </h4>
                            <span className="text-xs text-gray-500">
                              {formatDate(response.submitted_at)}
                            </span>
                          </div>
                          <p className="text-sm text-gray-700 leading-relaxed">
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
  );
};

export default AdminUsersTracking;