import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { login, register } from '../services/api'

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
      navigate('/dashboard')
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
    <div className="min-h-screen bg-gradient-serene flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
      {/* Floating background elements */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-20 left-10 opacity-10">
          <div className="text-8xl">🌿</div>
        </div>
        <div className="absolute top-40 right-20 opacity-8">
          <div className="text-6xl">🍃</div>
        </div>
        <div className="absolute bottom-32 left-20 opacity-12">
          <div className="text-7xl">🌱</div>
        </div>
        <div className="absolute bottom-20 right-16 opacity-8">
          <div className="text-5xl">🌸</div>
        </div>
        <div className="absolute top-60 left-1/3 opacity-6">
          <div className="text-4xl">🦋</div>
        </div>
      </div>

      <div className="max-w-md w-full space-y-8 relative z-10">
        {/* Header */}
        <div className="text-center">
          <div className="flex justify-center mb-6">
            <div className="w-16 h-16 bg-gradient-to-br from-primary-400 to-primary-600 rounded-full flex items-center justify-center shadow-lg">
              <span className="text-2xl">🌱</span>
            </div>
          </div>
          <h1 className="text-4xl font-inter font-bold text-sage-800 mb-2">
            Alquimia del Cambio
          </h1>
          <p className="text-sage-600 text-lg">
            Transformez votre relation avec vous-même
          </p>
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
              Se connecter
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
              S'inscrire
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
                Nom d'utilisateur
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
                  placeholder="Votre nom d'utilisateur"
                />
              </div>
            </div>

            {/* Email (only for registration) */}
            {!isLogin && (
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-sage-700 mb-2">
                  Email
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
                    placeholder="votre@email.com"
                  />
                </div>
              </div>
            )}

            {/* Password */}
            <div>
              <label htmlFor="password" className="block text-sm font-medium text-sage-700 mb-2">
                Mot de passe
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
                  placeholder="Votre mot de passe"
                />
              </div>
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={loading}
              className="w-full py-3 px-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-medium rounded-lg hover:from-primary-600 hover:to-primary-700 focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 shadow-lg"
            >
              {loading ? (
                <div className="flex items-center justify-center">
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  {isLogin ? 'Connexion...' : 'Inscription...'}
                </div>
              ) : (
                <span className="flex items-center justify-center">
                  {isLogin ? 'Se connecter' : "S'inscrire"}
                  <svg className="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                  </svg>
                </span>
              )}
            </button>
          </form>

          {/* Footer */}
          <div className="mt-8 text-center">
            <p className="text-xs text-sage-500">
              En vous connectant, vous acceptez de commencer votre voyage de transformation personnelle avec bienveillance et respect de vous-même.
            </p>
          </div>
        </div>

        {/* Bottom decorative text */}
        <div className="text-center">
          <p className="text-sage-600 italic">
            "Le changement commence par un pas, une respiration, un moment de conscience."
          </p>
        </div>
      </div>
    </div>
  )
}

export default Login 
