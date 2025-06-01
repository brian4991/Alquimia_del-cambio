import React from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { 
  HomeIcon, 
  UserIcon, 
  CogIcon, 
  ArrowRightOnRectangleIcon,
  SparklesIcon,
  HeartIcon 
} from '@heroicons/react/24/outline';

const Layout = ({ children }) => {
  const location = useLocation();
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  const navItems = [
    { 
      path: '/dashboard', 
      icon: HomeIcon, 
      label: 'Panel de Control',
      description: 'Vista general de tu recorrido'
    },
    { 
      path: '/admin', 
      icon: CogIcon, 
      label: 'Administración',
      description: 'Gestión del contenido'
    }
  ];

  return (
    <div className="min-h-screen gradient-elegant">
      {/* Header moderne pleine largeur */}
      <nav className="bg-gradient-to-r from-stone-100 to-stone-50 border-b border-stone-200 shadow-xl sticky top-0 z-50 backdrop-blur-md">
        <div className="w-full px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-24">
            {/* Logo et titre */}
            <div className="flex items-center space-x-6">
              <div className="flex items-center space-x-4">
                <div className="relative">
                  <img 
                    src="/Logo nr.png" 
                    alt="Alquimia del Cambio" 
                    className="w-16 h-16 object-contain drop-shadow-lg hover:scale-105 transition-transform duration-300"
                    onError={(e) => {
                      // Fallback vers l'icône si le logo n'est pas trouvé
                      e.target.style.display = 'none';
                      e.target.nextElementSibling.style.display = 'flex';
                    }}
                  />
                  <div className="w-16 h-16 bg-gradient-to-br from-sage-400 to-sage-600 rounded-2xl hidden items-center justify-center shadow-lg">
                    <SparklesIcon className="w-8 h-8 text-white" />
                  </div>
                </div>
                <div className="hidden sm:block">
                              <h1 className="font-inter text-3xl font-bold text-gray-800 tracking-tight">
              Alquimia del Cambio
            </h1>
                  <p className="font-inter text-sm text-gray-600 mt-1">
                    Tu camino de transformación personal
                  </p>
                </div>
              </div>
              
              {/* Titre mobile */}
              <div className="sm:hidden">
                              <h1 className="font-inter text-xl font-bold text-gray-800 tracking-tight">
                Alquimia del Cambio
              </h1>
              </div>
            </div>

            {/* Navigation centrale moderne */}
            <div className="hidden lg:flex items-center space-x-1">
              {navItems.map((item) => {
                const IconComponent = item.icon;
                const isActive = location.pathname === item.path;
                
                return (
                  <Link
                    key={item.path}
                    to={item.path}
                    className={`group relative flex items-center space-x-3 px-6 py-4 rounded-2xl font-inter font-medium transition-all duration-300 hover:shadow-lg ${
                      isActive
                        ? 'bg-gradient-to-r from-sage-500 to-sage-600 text-white shadow-lg transform scale-105'
                        : 'text-gray-700 hover:bg-gradient-to-r hover:from-sage-50 hover:to-taupe-50 hover:text-sage-700 hover:scale-102'
                    }`}
                    title={item.description}
                  >
                    <IconComponent className={`w-5 h-5 transition-transform duration-300 ${
                      isActive ? 'text-white' : 'text-gray-600 group-hover:text-sage-600 group-hover:scale-110'
                    }`} />
                    <span className="relative">
                      {item.label}
                      {isActive && (
                        <div className="absolute -bottom-1 left-0 right-0 h-0.5 bg-white rounded-full"></div>
                      )}
                    </span>
                  </Link>
                );
              })}
            </div>

            {/* Actions utilisateur modernes */}
            <div className="flex items-center space-x-3">
              <div className="hidden md:block text-right">
                <p className="font-inter text-xs text-gray-500 uppercase tracking-wide">
                  Conectado como
                </p>
                <p className="font-inter font-semibold text-gray-800 text-sm">
                  Usuario
                </p>
              </div>
              
              <div className="flex items-center space-x-2">
                <button
                  className="group relative p-3 text-gray-600 hover:text-sage-600 rounded-2xl hover:bg-sage-50 transition-all duration-300 hover:scale-105 hover:shadow-md"
                  title="Perfil de usuario"
                >
                  <UserIcon className="w-6 h-6 transition-transform duration-300 group-hover:scale-110" />
                  <div className="absolute inset-0 rounded-2xl bg-gradient-to-r from-sage-500 to-taupe-500 opacity-0 group-hover:opacity-10 transition-opacity duration-300"></div>
                </button>
                
                <button
                  onClick={handleLogout}
                  className="group flex items-center space-x-2 px-4 py-3 text-red-600 hover:text-red-700 bg-red-50 hover:bg-red-100 rounded-2xl transition-all duration-300 font-inter font-medium hover:shadow-md hover:scale-105 border border-red-200 hover:border-red-300"
                  title="Cerrar sesión"
                >
                  <ArrowRightOnRectangleIcon className="w-5 h-5 transition-transform duration-300 group-hover:scale-110" />
                  <span className="hidden sm:inline">Cerrar sesión</span>
                </button>
              </div>
            </div>
          </div>

          {/* Navigation mobile moderne */}
          <div className="lg:hidden px-4 pb-6">
            <div className="flex space-x-2 bg-white/50 backdrop-blur-sm rounded-2xl p-2 shadow-inner">
              {navItems.map((item) => {
                const IconComponent = item.icon;
                const isActive = location.pathname === item.path;
                
                return (
                  <Link
                    key={item.path}
                    to={item.path}
                    className={`flex items-center justify-center space-x-2 px-4 py-3 rounded-xl font-inter text-sm font-medium transition-all duration-300 flex-1 ${
                      isActive
                        ? 'bg-gradient-to-r from-sage-500 to-sage-600 text-white shadow-lg'
                        : 'text-gray-700 hover:bg-gradient-to-r hover:from-sage-50 hover:to-taupe-50 hover:text-sage-700'
                    }`}
                  >
                    <IconComponent className={`w-5 h-5 ${isActive ? 'text-white' : 'text-gray-600'}`} />
                    <span className="hidden sm:inline">{item.label}</span>
                  </Link>
                );
              })}
            </div>
          </div>
        </div>
      </nav>

      {/* Contenu principal */}
      <main className="flex-1">
        {children}
      </main>

      {/* Footer moderne */}
      <footer className="glass-effect border-t border-gray-200 mt-20">
        <div className="max-w-7xl mx-auto px-6 py-12">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
            {/* À propos */}
            <div>
              <div className="flex items-center space-x-3 mb-4">
                <div className="p-2 gradient-taupe rounded-lg">
                  <HeartIcon className="w-6 h-6 text-white" />
                </div>
                <h3 className="font-inter text-lg font-semibold text-black">
                  Nuestra misión
                </h3>
              </div>
              <p className="font-inter text-taupe-dark leading-relaxed">
                Acompañar tu camino de transformación personal con amabilidad y autenticidad.
              </p>
            </div>

            {/* Liens rapides */}
            <div>
              <h3 className="font-inter text-lg font-semibold text-black mb-4">
                Acceso rápido
              </h3>
              <div className="space-y-2">
                {navItems.map((item) => (
                  <Link
                    key={item.path}
                    to={item.path}
                    className="block font-inter text-taupe hover:text-sage transition-elegant"
                  >
                    {item.label}
                  </Link>
                ))}
              </div>
            </div>

            {/* Support */}
            <div>
              <h3 className="font-inter text-lg font-semibold text-black mb-4">
                Soporte
              </h3>
              <p className="font-inter text-taupe-dark leading-relaxed">
                Para cualquier pregunta o asistencia, estamos aquí para acompañarte en tu proceso.
              </p>
            </div>
          </div>

          {/* Ligne de séparation */}
          <div className="border-t border-gray-200 pt-8">
            <div className="flex flex-col md:flex-row justify-between items-center">
              <div className="flex items-center space-x-3 mb-4 md:mb-0">
                <div className="p-2 gradient-sage rounded-lg">
                  <SparklesIcon className="w-5 h-5 text-white" />
                </div>
                <span className="font-inter text-lg font-semibold text-black">
                  Alquimia del Cambio
                </span>
              </div>
              <p className="font-inter text-sm text-taupe">
                © 2024 Alquimia del Cambio. Desarrollado con pasión para tu florecimiento.
              </p>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Layout; 
