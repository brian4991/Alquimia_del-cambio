import axios from 'axios'
import { config } from '../config'

const API_BASE_URL = config.apiUrl

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Handle 401 errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

// Auth API
export const login = async (username, password) => {
  const response = await api.post('/login', { username, password })
  const { access_token } = response.data
  localStorage.setItem('token', access_token)
  return response.data
}

export const register = async (username, email, password) => {
  const response = await api.post('/register', { username, email, password })
  const { access_token } = response.data
  localStorage.setItem('token', access_token)
  return response.data
}

export const getProfile = async () => {
  const response = await api.get('/profile')
  return response.data
}

// New Module-based API
export const getModules = async () => {
  const response = await api.get('/modules')
  return response.data
}

export const getModuleThemes = async (moduleId) => {
  const response = await api.get(`/modules/${moduleId}/themes`)
  return response.data
}

export const getThemeExercises = async (themeId) => {
  const response = await api.get(`/themes/${themeId}/exercises`)
  return response.data
}

export const completeTheme = async (themeId) => {
  const response = await api.post(`/complete-theme/${themeId}`)
  return response.data
}

// Legacy Steps API (for backward compatibility)
export const getSteps = async () => {
  const response = await api.get('/steps')
  return response.data
}

export const getStepExercises = async (stepId) => {
  const response = await api.get(`/steps/${stepId}/exercises`)
  return response.data
}

export const submitResponse = async (exerciseId, responseText, ratingValue) => {
  const response = await api.post('/submit-response', {
    exercise_id: exerciseId,
    response_text: responseText,
    rating_value: ratingValue
  })
  return response.data
}

export const completeStep = async (stepId) => {
  const response = await api.post(`/complete-step/${stepId}`)
  return response.data
}

export default api 