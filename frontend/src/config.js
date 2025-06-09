export const config = {
  apiUrl: import.meta.env.PROD 
    ? 'https://alquimiadel-cambio-production.up.railway.app' 
    : 'http://localhost:8000',
  environment: import.meta.env.MODE || 'development'
} 