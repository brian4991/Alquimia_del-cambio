export const config = {
  apiUrl: import.meta.env.PROD 
    ? 'https://api.nicoleramirezpsicoach.com' 
    : 'http://localhost:8000',
  environment: import.meta.env.MODE || 'development'
} 