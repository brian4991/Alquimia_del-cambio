import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { config } from '../config'
import { login, register } from '../services/api'

const Login = () => {
  const navigate = useNavigate()
  const isLocalMode = config.environment === 'development'
  const [showRegister, setShowRegister] = useState(false)
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: ''
  })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleGoogleLogin = () => {
    window.location.href = `${config.apiUrl}/auth/google`
  }

  const handleLocalLogin = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)
    
    try {
      await login(formData.username, formData.password)
      navigate('/dashboard')
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al iniciar sesión')
    } finally {
      setLoading(false)
    }
  }

  const handleLocalRegister = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)
    
    try {
      await register(formData.username, formData.email, formData.password)
      navigate('/dashboard')
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al registrarse')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div 
      className="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 relative overflow-hidden"
      style={{
        backgroundImage: 'url(/café.jpg)',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat'
      }}
    >
      {/* Overlay */}
      <div className="absolute inset-0 bg-black bg-opacity-60"></div>

      <div className="max-w-md w-full space-y-8 relative z-10">
        {/* Header */}
        <div className="text-center">
          <h1 className="text-4xl font-inter font-bold text-white mb-4">
            Cambio de Paradigma
          </h1>
          <p className="text-sage-200 text-lg">
            Bienvenido a tu viaje de transformación
          </p>
        </div>

        {/* Login Container */}
        <div className="bg-white/90 backdrop-blur-sm rounded-2xl shadow-2xl p-10 border border-sage-200">
          <div className="text-center mb-8">
            <h2 className="text-2xl font-semibold text-sage-800 mb-2">
              Inicia Sesión
            </h2>
            <p className="text-sage-600 text-sm">
              Conecta con tu cuenta de Google para continuar
            </p>
          </div>

          {/* Local Dev Login Form - Only in Development */}
          {isLocalMode && (
            <form onSubmit={showRegister ? handleLocalRegister : handleLocalLogin} className="space-y-4 mb-6">
              {error && (
                <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm">
                  {error}
                </div>
              )}
              
              <div>
                <label className="block text-sm font-medium text-sage-700 mb-2">
                  Usuario
                </label>
                <input
                  type="text"
                  value={formData.username}
                  onChange={(e) => setFormData({...formData, username: e.target.value})}
                  className="w-full px-4 py-3 border border-sage-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sage-400"
                  required
                  disabled={loading}
                />
              </div>

              {showRegister && (
                <div>
                  <label className="block text-sm font-medium text-sage-700 mb-2">
                    Email
                  </label>
                  <input
                    type="email"
                    value={formData.email}
                    onChange={(e) => setFormData({...formData, email: e.target.value})}
                    className="w-full px-4 py-3 border border-sage-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sage-400"
                    required
                    disabled={loading}
                  />
                </div>
              )}

              <div>
                <label className="block text-sm font-medium text-sage-700 mb-2">
                  Contraseña
                </label>
                <input
                  type="password"
                  value={formData.password}
                  onChange={(e) => setFormData({...formData, password: e.target.value})}
                  className="w-full px-4 py-3 border border-sage-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sage-400"
                  required
                  disabled={loading}
                />
              </div>

              <button
                type="submit"
                disabled={loading}
                className="w-full py-3 px-6 bg-sage-600 text-white rounded-lg font-medium hover:bg-sage-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? 'Cargando...' : (showRegister ? 'Registrarse' : 'Iniciar Sesión')}
              </button>

              <button
                type="button"
                onClick={() => {
                  setShowRegister(!showRegister)
                  setError('')
                }}
                className="w-full text-sm text-sage-600 hover:text-sage-800 transition-colors"
                disabled={loading}
              >
                {showRegister ? '¿Ya tienes cuenta? Inicia sesión' : '¿No tienes cuenta? Regístrate'}
              </button>

              <div className="relative my-6">
                <div className="absolute inset-0 flex items-center">
                  <div className="w-full border-t border-sage-300"></div>
                </div>
                <div className="relative flex justify-center text-sm">
                  <span className="px-2 bg-white text-sage-500">O continúa con</span>
                </div>
              </div>
            </form>
          )}

          {/* Google Login Button */}
          <button
            type="button"
            onClick={handleGoogleLogin}
            className="w-full inline-flex items-center justify-center py-4 px-6 border-2 border-sage-300 rounded-xl shadow-lg bg-white text-base font-medium text-sage-700 hover:bg-sage-50 hover:border-sage-400 transition-all duration-200 transform hover:scale-105"
          >
            <svg className="w-6 h-6" viewBox="0 0 24 24">
              <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
              <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
              <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
              <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
            </svg>
            <span className="ml-3 text-lg">Continuar con Google</span>
          </button>

          {/* Dev Mode Indicator */}
          {isLocalMode && (
            <div className="mt-4 text-center">
              <span className="inline-block px-3 py-1 bg-yellow-100 text-yellow-800 text-xs font-medium rounded-full">
                🔧 Modo Desarrollo
              </span>
            </div>
          )}
        </div>

        {/* Bottom decorative text */}
        <div className="text-center">
          <p className="text-white text-lg italic font-light">
            "El cambio comienza con un paso, una respiración, un momento de consciencia."
          </p>
        </div>
      </div>
    </div>
  )
}

export default Login 
