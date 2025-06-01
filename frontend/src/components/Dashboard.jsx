import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getModules, getProfile } from '../services/api';

const Dashboard = () => {
  const [modules, setModules] = useState([]);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [modulesData, userData] = await Promise.all([
          getModules(),
          getProfile()
        ]);
        setModules(modulesData);
        setUser(userData);
      } catch (err) {
        setError('Erreur lors du chargement des données');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const getModuleInfo = (moduleOrder) => {
    const moduleMap = {
      1: { emoji: "🗺️", color: "from-primary-400 to-primary-600" },
      2: { emoji: "🎉", color: "from-secondary-400 to-secondary-600" },
      3: { emoji: "💖", color: "from-lavender-400 to-lavender-600" },
      4: { emoji: "🎭", color: "from-sage-400 to-sage-600" },
      5: { emoji: "🕊️", color: "from-cream-400 to-cream-600" },
    };
    return moduleMap[moduleOrder] || { emoji: "📚", color: "from-gray-400 to-gray-600" };
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="flex items-center space-x-3">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-500"></div>
          <span className="text-sage-600">Chargement de votre parcours...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="bg-red-50 border border-red-200 rounded-lg p-4">
          <p className="text-red-700">{error}</p>
        </div>
      </div>
    );
  }

  const completedModules = modules.filter(module => module.is_completed).length;
  const totalModules = modules.length;
  const progressPercentage = totalModules > 0 ? (completedModules / totalModules) * 100 : 0;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Welcome Header */}
      <div className="mb-12">
        <div className="bg-white/70 backdrop-blur-sm rounded-3xl shadow-xl p-8 border border-sage-200 relative overflow-hidden">
          {/* Background decoration */}
          <div className="absolute top-0 right-0 opacity-5">
            <div className="text-9xl">🌸</div>
          </div>
          
          <div className="relative z-10">
            <h1 className="text-4xl font-serif font-bold text-sage-800 mb-3">
              ¡Hola {user?.username}! 🌱
            </h1>
            <p className="text-lg text-sage-600 mb-6">
              Bienvenido a tu espacio de transformación personal. Cada paso cuenta en tu viaje hacia el florecimiento.
            </p>
            
            {/* Progress Section */}
            <div className="bg-gradient-nature rounded-2xl p-6 mb-6">
              <h3 className="text-lg font-semibold text-sage-800 mb-4 flex items-center">
                <span className="mr-2">📊</span>
                Tu Progreso
              </h3>
              <div className="flex items-center space-x-4">
                <div className="flex-1">
                  <div className="bg-white/60 rounded-full h-3 overflow-hidden">
                    <div 
                      className="h-full bg-gradient-to-r from-primary-400 to-primary-600 transition-all duration-500 ease-out"
                      style={{ width: `${progressPercentage}%` }}
                    ></div>
                  </div>
                </div>
                <div className="text-right">
                  <span className="text-2xl font-bold text-sage-800">{completedModules}</span>
                  <span className="text-sage-600">/{totalModules}</span>
                  <p className="text-sm text-sage-600">módulos completados</p>
                </div>
              </div>
            </div>

            {/* Quick Stats */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-white/50 rounded-xl p-4 text-center">
                <div className="text-2xl mb-2">🎯</div>
                <div className="text-lg font-semibold text-sage-800">{progressPercentage.toFixed(0)}%</div>
                <div className="text-sm text-sage-600">Progresión</div>
              </div>
              <div className="bg-white/50 rounded-xl p-4 text-center">
                <div className="text-2xl mb-2">⏱️</div>
                <div className="text-lg font-semibold text-sage-800">{Math.max(totalModules - completedModules, 0)}</div>
                <div className="text-sm text-sage-600">Módulos restantes</div>
              </div>
              <div className="bg-white/50 rounded-xl p-4 text-center">
                <div className="text-2xl mb-2">🌟</div>
                <div className="text-lg font-semibold text-sage-800">{totalModules}</div>
                <div className="text-sm text-sage-600">Módulos disponibles</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Modules Grid */}
      <div className="mb-8">
        <h2 className="text-2xl font-serif font-bold text-sage-800 mb-6 flex items-center">
          <span className="mr-3">🗺️</span>
          Tu Recorrido de Transformación
        </h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {modules.map((module) => {
            const moduleInfo = getModuleInfo(module.order_number);
            const isLocked = module.order_number > 1 && !modules.find(m => m.order_number === module.order_number - 1)?.is_completed;
            
            return (
              <div
                key={module.id}
                className={`relative group ${
                  isLocked ? 'opacity-60' : 'hover:scale-105'
                } transition-all duration-300`}
              >
                <div className={`bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl border border-sage-200 p-6 h-full ${
                  module.is_completed ? 'ring-2 ring-primary-300' : ''
                } relative overflow-hidden`}>
                  
                  {/* Background Gradient */}
                  <div className={`absolute top-0 right-0 w-20 h-20 bg-gradient-to-br ${moduleInfo.color} opacity-10 rounded-bl-full`}></div>
                  
                  {/* Status Indicator */}
                  <div className="absolute top-4 right-4">
                    {module.is_completed ? (
                      <div className="w-8 h-8 bg-primary-500 rounded-full flex items-center justify-center">
                        <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                        </svg>
                      </div>
                    ) : isLocked ? (
                      <div className="w-8 h-8 bg-sage-300 rounded-full flex items-center justify-center">
                        <svg className="w-4 h-4 text-sage-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 2h12a2 2 0 002-2V7a2 2 0 00-2-2H6a2 2 0 00-2 2v10a2 2 0 002 2zM9 5a3 3 0 016 0v2H9V5z" />
                        </svg>
                      </div>
                    ) : (
                      <div className="w-8 h-8 bg-secondary-400 rounded-full flex items-center justify-center">
                        <span className="text-white font-bold text-sm">{module.order_number}</span>
                      </div>
                    )}
                  </div>

                  {/* Module Emoji */}
                  <div className="text-4xl mb-4">{moduleInfo.emoji}</div>

                  {/* Content */}
                  <div className="space-y-3">
                    <div>
                      <span className="inline-block bg-sage-100 text-sage-700 text-xs px-2 py-1 rounded-full mb-2">
                        Módulo {module.order_number}
                      </span>
                      <h3 className="text-lg font-semibold text-sage-800 leading-tight">
                        {module.title}
                      </h3>
                    </div>
                    
                    <p className="text-sm text-sage-600 line-clamp-3">
                      {module.description}
                    </p>

                    {/* Objective */}
                    {module.objective && (
                      <p className="text-xs text-sage-500 italic">
                        🎯 {module.objective}
                      </p>
                    )}
                  </div>

                  {/* Action Button */}
                  <div className="mt-6">
                    {isLocked ? (
                      <div className="w-full py-3 px-4 bg-sage-200 text-sage-500 rounded-lg text-center text-sm">
                        <span className="flex items-center justify-center">
                          <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 2h12a2 2 0 002-2V7a2 2 0 00-2-2H6a2 2 0 00-2 2v10a2 2 0 002 2zM9 5a3 3 0 016 0v2H9V5z" />
                          </svg>
                          Bloqueado
                        </span>
                      </div>
                    ) : (
                      <Link
                        to={`/module/${module.id}`}
                        className={`block w-full py-3 px-4 rounded-lg text-center text-sm font-medium transition-colors ${
                          module.is_completed
                            ? 'bg-primary-100 text-primary-700 hover:bg-primary-200'
                            : 'bg-gradient-to-r from-primary-500 to-primary-600 text-white hover:from-primary-600 hover:to-primary-700'
                        }`}
                      >
                        {module.is_completed ? 'Repasar módulo' : 'Comenzar módulo'}
                      </Link>
                    )}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Motivation Section */}
      <div className="bg-gradient-calm rounded-3xl shadow-xl p-8 border border-sage-200 relative overflow-hidden">
        <div className="absolute bottom-0 left-0 opacity-5">
          <div className="text-8xl">🌺</div>
        </div>
        <div className="relative z-10 text-center">
          <h3 className="text-2xl font-serif font-bold text-sage-800 mb-4">
            Tu transformación comienza hoy
          </h3>
          <p className="text-sage-600 max-w-2xl mx-auto">
            Cada módulo es una oportunidad de reconectarte con tu esencia auténtica. 
            Tómate tu tiempo, respira profundamente, y déjate guiar por tu intuición.
          </p>
          <div className="mt-6 flex justify-center space-x-4 text-3xl">
            <span>🌱</span>
            <span>🦋</span>
            <span>🌸</span>
            <span>✨</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard; 