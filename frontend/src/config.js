export const config = {
  apiUrl: import.meta.env.PROD 
    ? 'https://your-backend-api.com' 
    : 'http://localhost:8000',
  environment: import.meta.env.MODE || 'development'
} 