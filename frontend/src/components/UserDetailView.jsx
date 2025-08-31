import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { 
  ArrowLeftIcon,
  UserIcon,
  CheckCircleIcon,
  XCircleIcon,
  DocumentTextIcon,
  BookOpenIcon,
  ClockIcon,
  SparklesIcon,
  AcademicCapIcon,
  ShieldCheckIcon,
  ExclamationTriangleIcon
} from '@heroicons/react/24/outline';
import { CheckCircleIcon as CheckCircleIconSolid } from '@heroicons/react/24/solid';
import { getUserResponses, getAllModulesAdmin, validateUserModule, revokeUserModule, validateUser, revokeUserValidation } from '../services/api';
import { config } from '../config';

const UserDetailView = () => {
  const { userId } = useParams();
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [userResponses, setUserResponses] = useState([]);
  const [modules, setModules] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [validatingModule, setValidatingModule] = useState(null);

  useEffect(() => {
    loadUserData();
  }, [userId]);

  const loadUserData = async () => {
    try {
      setLoading(true);
      
      // Get user responses
      const responses = await getUserResponses(userId);
      setUserResponses(responses);
      
      // Get all modules for validation (admin endpoint)
      const modulesData = await getAllModulesAdmin();
      setModules(modulesData);
      
      // Get user info from admin stats
      const token = localStorage.getItem('token');
      const usersResponse = await fetch(`${config.apiUrl}/auth/admin/users/stats`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const usersData = await usersResponse.json();
      const foundUser = usersData.users.find(u => u.id === parseInt(userId));
      
      if (foundUser) {
        // Parse validated_modules if it's a string
        if (foundUser.validated_modules && typeof foundUser.validated_modules === 'string') {
          try {
            foundUser.validated_modules = JSON.parse(foundUser.validated_modules);
          } catch (e) {
            console.error('Error parsing validated_modules:', e);
            foundUser.validated_modules = [];
          }
        }
        setUser(foundUser);
      } else {
        setError('Usuario no encontrado');
      }
      
    } catch (err) {
      setError('Error al cargar los datos del usuario');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleValidateModule = async (moduleId, isValidating = true) => {
    try {
      setValidatingModule(moduleId);
      
      let result;
      if (isValidating) {
        result = await validateUserModule(userId, moduleId);
      } else {
        result = await revokeUserModule(userId, moduleId);
      }
      
      // Update user's validated modules
      setUser(prev => ({
        ...prev,
        validated_modules: result.validated_modules
      }));
      
      // Show success message
      const action = isValidating ? 'validado' : 'revocado';
      alert(`Módulo ${action} exitosamente`);
      
    } catch (err) {
      alert('Error al validar el módulo');
      console.error(err);
    } finally {
      setValidatingModule(null);
    }
  };

  const handleValidateUser = async () => {
    try {
      await validateUser(userId);
      await loadUserData(); // Reload user data
      
      // Notify other components that user validation changed
      localStorage.setItem('userValidationChanged', Date.now().toString());
      window.dispatchEvent(new Event('userValidationChanged'));
      
      alert('Usuario validado exitosamente');
    } catch (error) {
      console.error('Error validating user:', error);
      alert('Error al validar el usuario');
    }
  };

  const handleRevokeUserValidation = async () => {
    try {
      await revokeUserValidation(userId);
      await loadUserData(); // Reload user data
      
      // Notify other components that user validation changed
      localStorage.setItem('userValidationChanged', Date.now().toString());
      window.dispatchEvent(new Event('userValidationChanged'));
      
      alert('Validación del usuario revocada exitosamente');
    } catch (error) {
      console.error('Error revoking user validation:', error);
      alert('Error al revocar la validación del usuario');
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

  const getModuleResponses = (moduleId) => {
    return userResponses.filter(response => {
      // We need to match responses to modules somehow
      // For now, we'll group by module_title
      return response.module_title;
    });
  };

  const groupResponsesByModule = () => {
    const grouped = {};
    userResponses.forEach(response => {
      const moduleTitle = response.module_title;
      if (!grouped[moduleTitle]) {
        grouped[moduleTitle] = {
          title: moduleTitle,
          themes: {}
        };
      }
      
      const themeTitle = response.theme_title;
      if (!grouped[moduleTitle].themes[themeTitle]) {
        grouped[moduleTitle].themes[themeTitle] = [];
      }
      
      grouped[moduleTitle].themes[themeTitle].push(response);
    });
    
    return grouped;
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 flex items-center justify-center">
        <div className="bg-white/90 backdrop-blur-sm rounded-3xl shadow-2xl p-12 border border-slate-200 text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-4 border-blue-500 border-t-transparent mx-auto mb-6"></div>
          <p className="text-slate-600 text-xl font-medium">Cargando datos del usuario...</p>
        </div>
      </div>
    );
  }

  if (error || !user) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 flex items-center justify-center">
        <div className="bg-red-50 border border-red-200 rounded-3xl p-12 text-center shadow-lg max-w-md">
          <ExclamationTriangleIcon className="w-16 h-16 text-red-600 mx-auto mb-6" />
          <h2 className="text-2xl font-bold text-red-800 mb-4">Error</h2>
          <p className="text-red-600 mb-8">{error}</p>
          <button 
            onClick={() => navigate('/admin/users')}
            className="bg-red-600 text-white px-6 py-3 rounded-xl hover:bg-red-700 transition-all duration-200 font-medium"
          >
            Volver a usuarios
          </button>
        </div>
      </div>
    );
  }

  const responsesByModule = groupResponsesByModule();
  
  // Parse validated_modules correctly
  let userValidatedModules = [];
  try {
    if (user.validated_modules) {
      if (typeof user.validated_modules === 'string') {
        userValidatedModules = JSON.parse(user.validated_modules);
      } else if (Array.isArray(user.validated_modules)) {
        userValidatedModules = user.validated_modules;
      }
    }
  } catch (e) {
    console.error('Error parsing validated_modules:', e);
    userValidatedModules = [];
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-stone-100 to-amber-50">
      <div className="max-w-7xl mx-auto px-6 py-12">
        {/* Header */}
        <div className="mb-12">
          <div className="flex items-center space-x-4 mb-6">
            <button
              onClick={() => navigate('/admin/users')}
              className="p-3 bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-200 border border-slate-200 hover:border-slate-200"
            >
              <ArrowLeftIcon className="w-6 h-6 text-slate-600" />
            </button>
            <div className="p-4 bg-gradient-to-br from-blue-500 to-purple-600 rounded-2xl shadow-lg">
              <UserIcon className="w-10 h-10 text-white" />
            </div>
            <div>
              <h1 className="text-4xl font-bold text-slate-900 mb-2">Perfil de {user.username}</h1>
              <p className="text-slate-600 text-lg">Detalles completos y validación de progreso</p>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 xl:grid-cols-3 gap-8">
          {/* User Info */}
          <div className="xl:col-span-1 space-y-8">
            {/* Basic Info */}
            <div className="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
              <div className="p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-blue-50">
                <h2 className="text-2xl font-bold text-slate-900 flex items-center">
                  <UserIcon className="w-6 h-6 mr-3 text-blue-600" />
                  Información del Usuario
                </h2>
              </div>
              
              <div className="p-6">
                <div className="flex items-center space-x-4 mb-6">
                  <div className="w-16 h-16 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center text-white font-bold text-2xl">
                    {user.username.charAt(0).toUpperCase()}
                  </div>
                  <div>
                    <h3 className="font-bold text-slate-900 text-xl">{user.username}</h3>
                    <p className="text-slate-600">{user.email}</p>
                  </div>
                </div>
                
                <div className="space-y-4">
                  <div className="flex justify-between items-center p-3 bg-white rounded-lg">
                    <span className="text-slate-600 font-medium">Estado:</span>
                    <span className={`font-bold flex items-center ${user.is_active ? 'text-green-600' : 'text-red-600'}`}>
                      {user.is_active ? (
                        <>
                          <CheckCircleIconSolid className="w-4 h-4 mr-1" />
                          Activo
                        </>
                      ) : (
                        <>
                          <XCircleIcon className="w-4 h-4 mr-1" />
                          Inactivo
                        </>
                      )}
                    </span>
                  </div>
                  
                  <div className="flex justify-between items-center p-3 bg-white rounded-lg">
                    <span className="text-slate-600 font-medium">Rol:</span>
                    <span className={`font-bold px-3 py-1 rounded-full text-sm ${
                      user.role === 'admin' 
                        ? 'bg-purple-100 text-purple-700' 
                        : 'bg-slate-100 text-slate-700'
                    }`}>
                      {user.role}
                    </span>
                  </div>
                  
                  <div className="flex justify-between items-center p-3 bg-white rounded-lg">
                    <span className="text-slate-600 font-medium">Respuestas:</span>
                    <span className="font-bold text-slate-900">{user.response_count}</span>
                  </div>
                  
                  <div className="flex justify-between items-center p-3 bg-white rounded-lg">
                    <span className="text-slate-600 font-medium">Registrado:</span>
                    <span className="font-bold text-slate-900 text-sm">{formatDate(user.created_at)}</span>
                  </div>
                </div>
              </div>
            </div>

            {/* User Global Validation */}
            <div className="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
              <div className="p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-orange-50">
                <h2 className="text-2xl font-bold text-slate-900 flex items-center">
                  <ShieldCheckIcon className="w-6 h-6 mr-3 text-orange-600" />
                  Validación Global
                </h2>
                <p className="text-slate-600 mt-2">Controla el acceso general del usuario</p>
              </div>
              
              <div className="p-6">
                <div className="space-y-4">
                  <div className="border border-slate-200 rounded-xl p-4">
                    <div className="flex items-center justify-between mb-3">
                      <div>
                        <h4 className="font-semibold text-slate-900">Estado de Validación</h4>
                        <p className="text-sm text-slate-600">
                          {user.is_validated 
                            ? 'Usuario validado - Progresión normal habilitada'
                            : 'Usuario no validado - Solo acceso al primer tema del Módulo 1'
                          }
                        </p>
                      </div>
                      
                      <div className="flex items-center space-x-2">
                        {user.is_validated ? (
                          <>
                            <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-700">
                              <CheckCircleIconSolid className="w-3 h-3 mr-1" />
                              Validado
                            </span>
                            <button
                              onClick={handleRevokeUserValidation}
                              className="px-3 py-2 bg-red-600 text-white text-sm rounded-lg hover:bg-red-700 transition-colors"
                            >
                              Revocar Validación
                            </button>
                          </>
                        ) : (
                          <>
                            <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-orange-100 text-orange-700">
                              <ExclamationTriangleIcon className="w-3 h-3 mr-1" />
                              No Validado
                            </span>
                            <button
                              onClick={handleValidateUser}
                              className="px-3 py-2 bg-green-600 text-white text-sm rounded-lg hover:bg-green-700 transition-colors"
                            >
                              Validar Usuario
                            </button>
                          </>
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Module Validation */}
            <div className="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
              <div className="p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-green-50">
                <h2 className="text-2xl font-bold text-slate-900 flex items-center">
                  <ShieldCheckIcon className="w-6 h-6 mr-3 text-green-600" />
                  Validación de Módulos
                </h2>
                <p className="text-slate-600 mt-2">Controla el acceso a módulos</p>
              </div>
              
              <div className="p-6">
                <div className="space-y-4">
                  {modules.map((module) => {
                    const isValidated = userValidatedModules.includes(module.id);
                    const isModule1 = module.order_number === 1;
                    
                    return (
                      <div key={module.id} className="border border-slate-200 rounded-xl p-4">
                        <div className="flex items-center justify-between mb-3">
                          <div>
                            <h4 className="font-semibold text-slate-900">{module.title}</h4>
                            <p className="text-sm text-slate-600">Módulo {module.order_number}</p>
                          </div>
                          
                          {isModule1 ? (
                            <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-700">
                              <BookOpenIcon className="w-3 h-3 mr-1" />
                              Acceso por defecto
                            </span>
                          ) : (
                            <span className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-medium ${
                              isValidated 
                                ? 'bg-green-100 text-green-700' 
                                : 'bg-red-100 text-red-700'
                            }`}>
                              {isValidated ? (
                                <>
                                  <CheckCircleIconSolid className="w-3 h-3 mr-1" />
                                  Validado
                                </>
                              ) : (
                                <>
                                  <XCircleIcon className="w-3 h-3 mr-1" />
                                  Sin validar
                                </>
                              )}
                            </span>
                          )}
                        </div>
                        
                        {!isModule1 && (
                          <div className="flex space-x-2">
                            <button
                              onClick={() => handleValidateModule(module.id, true)}
                              disabled={validatingModule === module.id || isValidated}
                              className="flex-1 px-3 py-2 bg-green-600 text-white text-sm rounded-lg hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                            >
                              {validatingModule === module.id ? 'Validando...' : 'Validar'}
                            </button>
                            <button
                              onClick={() => handleValidateModule(module.id, false)}
                              disabled={validatingModule === module.id || !isValidated}
                              className="flex-1 px-3 py-2 bg-red-600 text-white text-sm rounded-lg hover:bg-red-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                            >
                              {validatingModule === module.id ? 'Revocando...' : 'Revocar'}
                            </button>
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>
            </div>
          </div>

          {/* User Responses */}
          <div className="xl:col-span-2">
            <div className="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
              <div className="p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-purple-50">
                <h2 className="text-2xl font-bold text-slate-900 flex items-center">
                  <DocumentTextIcon className="w-6 h-6 mr-3 text-purple-600" />
                  Respuestas por Módulo
                </h2>
                <p className="text-slate-600 mt-2">Revisa las respuestas organizadas por módulo y tema</p>
              </div>
              
              <div className="p-6">
                {Object.keys(responsesByModule).length === 0 ? (
                  <div className="text-center py-16 text-slate-500">
                    <DocumentTextIcon className="w-16 h-16 mx-auto mb-6 opacity-50" />
                    <p className="text-xl font-medium">No hay respuestas registradas</p>
                    <p className="text-sm mt-2">El usuario aún no ha completado ejercicios</p>
                  </div>
                ) : (
                  <div className="space-y-8">
                    {Object.entries(responsesByModule).map(([moduleTitle, moduleData]) => (
                      <div key={moduleTitle} className="border border-slate-200 rounded-xl overflow-hidden">
                        <div className="p-4 bg-gradient-to-r from-blue-50 to-purple-50 border-b border-slate-200">
                          <h3 className="text-lg font-bold text-slate-900 flex items-center">
                            <AcademicCapIcon className="w-5 h-5 mr-2 text-blue-600" />
                            {moduleTitle}
                          </h3>
                        </div>
                        
                        <div className="p-4">
                          <div className="space-y-6">
                            {Object.entries(moduleData.themes).map(([themeTitle, responses]) => (
                              <div key={themeTitle} className="bg-white rounded-lg p-4">
                                <h4 className="font-semibold text-slate-900 mb-3 flex items-center">
                                  <SparklesIcon className="w-4 h-4 mr-2 text-purple-600" />
                                  {themeTitle}
                                </h4>
                                
                                <div className="space-y-3">
                                  {responses.map((response, index) => (
                                    <div key={index} className="bg-white rounded-lg p-4 border border-slate-200">
                                      <div className="flex justify-between items-start mb-3">
                                        <div>
                                          <h5 className="font-medium text-slate-900 text-sm">
                                            {response.exercise_title}
                                          </h5>
                                          {response.response_type === 'sub_question' && response.sub_question_text && (
                                            <p className="text-xs text-blue-600 mt-1 font-medium">
                                              📝 {response.sub_question_text}
                                            </p>
                                          )}
                                        </div>
                                        <div className="flex flex-col items-end space-y-1">
                                          <span className={`text-xs px-2 py-1 rounded-full flex items-center ${
                                            response.response_type === 'sub_question' 
                                              ? 'bg-blue-100 text-blue-700' 
                                              : 'bg-slate-100 text-slate-500'
                                          }`}>
                                            {response.response_type === 'sub_question' ? '🔸 Sous-question' : '📝 Principal'}
                                          </span>
                                          <span className="text-xs text-slate-500 bg-slate-100 px-2 py-1 rounded-full flex items-center">
                                            <ClockIcon className="w-3 h-3 mr-1" />
                                            {formatDate(response.submitted_at)}
                                          </span>
                                        </div>
                                      </div>
                                      <div className="bg-white rounded-lg p-3">
                                        <p className="text-sm text-slate-700 leading-relaxed">
                                          {response.response_text}
                                        </p>
                                      </div>
                                    </div>
                                  ))}
                                </div>
                              </div>
                            ))}
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UserDetailView;
