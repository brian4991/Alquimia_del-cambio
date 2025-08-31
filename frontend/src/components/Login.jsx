import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { login, register } from '../services/api'
import { config } from '../config'

const Login = () => {
  const [isLogin, setIsLogin] = useState(true)
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
  })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      let result
      if (isLogin) {
        result = await login(formData.username, formData.password)
      } else {
        result = await register(formData.username, formData.email, formData.password)
      }

      localStorage.setItem('token', result.access_token)
      
      // Check if user is admin to redirect appropriately
      try {
        const payload = JSON.parse(atob(result.access_token.split('.')[1]));
        if (payload.role === 'admin') {
          navigate('/admin/users');
        } else {
          navigate('/dashboard');
        }
      } catch (error) {
        // Fallback to dashboard if token parsing fails
        navigate('/dashboard');
      }
    } catch (err) {
      setError(err.message || 'Une erreur est survenue')
    } finally {
      setLoading(false)
    }
  }

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    })
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
      {/* Overlay grisé */}
      <div className="absolute inset-0 bg-black bg-opacity-60"></div>

      <div className="max-w-md w-full space-y-8 relative z-10">
        {/* Header */}
        <div className="text-center">
          <h1 className="text-4xl font-inter font-bold text-white mb-8">
            Alquimia del Cambio
          </h1>
        </div>

        {/* Form Container */}
        <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-2xl p-8 border border-sage-200">
          {/* Toggle Buttons */}
          <div className="flex mb-8 bg-sage-100 rounded-xl p-1">
            <button
              type="button"
              onClick={() => setIsLogin(true)}
              className={`flex-1 py-3 px-4 rounded-lg text-sm font-medium transition-all duration-200 ${
                isLogin
                  ? 'bg-white text-primary-700 shadow-md'
                  : 'text-sage-600 hover:text-primary-600'
              }`}
            >
              Iniciar Sesión
            </button>
            <button
              type="button"
              onClick={() => setIsLogin(false)}
              className={`flex-1 py-3 px-4 rounded-lg text-sm font-medium transition-all duration-200 ${
                !isLogin
                  ? 'bg-white text-primary-700 shadow-md'
                  : 'text-sage-600 hover:text-primary-600'
              }`}
            >
              Registrarse
            </button>
          </div>

          {/* Error Message */}
          {error && (
            <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg">
              <p className="text-red-700 text-sm">{error}</p>
            </div>
          )}

          {/* Form */}
          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Username */}
            <div>
              <label htmlFor="username" className="block text-sm font-medium text-sage-700 mb-2">
                Nombre de usuario
              </label>
              <div className="relative">
                <input
                  id="username"
                  name="username"
                  type="text"
                  required
                  value={formData.username}
                  onChange={handleChange}
                  className="w-full pl-4 pr-4 py-3 border border-sage-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 bg-white/80 backdrop-blur-sm transition-colors"
                  placeholder="Tu nombre de usuario"
                />
              </div>
            </div>

            {/* Email (only for registration) */}
            {!isLogin && (
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-sage-700 mb-2">
                  Correo electrónico
                </label>
                <div className="relative">
                  <input
                    id="email"
                    name="email"
                    type="email"
                    required
                    value={formData.email}
                    onChange={handleChange}
                    className="w-full pl-4 pr-4 py-3 border border-sage-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 bg-white/80 backdrop-blur-sm transition-colors"
                    placeholder="tu@email.com"
                  />
                </div>
              </div>
            )}

            {/* Password */}
            <div>
              <label htmlFor="password" className="block text-sm font-medium text-sage-700 mb-2">
                Contraseña
              </label>
              <div className="relative">
                <input
                  id="password"
                  name="password"
                  type="password"
                  required
                  value={formData.password}
                  onChange={handleChange}
                  className="w-full pl-4 pr-4 py-3 border border-sage-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 bg-white/80 backdrop-blur-sm transition-colors"
                  placeholder="Tu contraseña"
                />
              </div>
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={loading}
              className="w-full py-3 px-4 text-white font-medium rounded-lg focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 shadow-lg"
              style={{
                backgroundColor: '#6b745a'
              }}
              onMouseEnter={(e) => e.target.style.backgroundColor = '#5a6349'}
              onMouseLeave={(e) => e.target.style.backgroundColor = '#6b745a'}
            >
              {loading ? (
                <div className="flex items-center justify-center">
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  {isLogin ? 'Iniciando sesión...' : 'Registrando...'}
                </div>
              ) : (
                <span className="flex items-center justify-center">
                  {isLogin ? 'Iniciar Sesión' : 'Registrarse'}
                  <svg className="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                  </svg>
                </span>
              )}
            </button>
          </form>

          {/* OAuth Login Section */}
          {isLogin && (
            <>
              <div className="mt-6 relative">
                <div className="absolute inset-0 flex items-center">
                  <div className="w-full border-t border-sage-300"></div>
                </div>
                <div className="relative flex justify-center text-sm">
                  <span className="px-3 bg-white text-sage-500">O continuar con</span>
                </div>
              </div>

              <div className="mt-6 grid grid-cols-2 gap-3">
                {/* Google Login */}
                <button
                  type="button"
                  onClick={() => window.location.href = `${config.apiUrl}/auth/google`}
                  className="w-full inline-flex justify-center py-3 px-4 border border-sage-300 rounded-lg shadow-sm bg-white text-sm font-medium text-sage-700 hover:bg-sage-50 transition-colors"
                >
                  <svg className="w-5 h-5" viewBox="0 0 24 24">
                    <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                    <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                    <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                    <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                  </svg>
                  <span className="ml-2">Google</span>
                </button>

                {/* Facebook Login */}
                <button
                  type="button"
                  onClick={() => window.location.href = `${config.apiUrl}/auth/facebook`}
                  className="w-full inline-flex justify-center py-3 px-4 border border-sage-300 rounded-lg shadow-sm bg-white text-sm font-medium text-sage-700 hover:bg-sage-50 transition-colors"
                >
                  <svg className="w-5 h-5" fill="#1877F2" viewBox="0 0 24 24">
                    <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                  </svg>
                  <span className="ml-2">Facebook</span>
                </button>
              </div>
            </>
          )}

          {/* Footer */}
          <div className="mt-8 text-center">
            <p className="text-xs text-sage-500">
              Al conectarte, aceptas comenzar tu viaje de transformación personal con amor y respeto hacia ti mismo.
            </p>
          </div>
        </div>

        {/* Bottom decorative text */}
        <div className="text-center">
          <p className="text-sage-600 italic">
            "El cambio comienza con un paso, una respiración, un momento de consciencia."
          </p>
        </div>
      </div>
    </div>
  )
}

export default Login 
