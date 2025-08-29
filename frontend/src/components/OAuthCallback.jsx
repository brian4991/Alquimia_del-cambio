import React, { useEffect, useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';

const OAuthCallback = () => {
  const [searchParams] = useSearchParams();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const handleOAuthCallback = async () => {
      try {
        const token = searchParams.get('token');
        const errorParam = searchParams.get('error');

        if (errorParam) {
          setError(`Erreur d'authentification: ${errorParam}`);
          setLoading(false);
          return;
        }

        if (token) {
          // Store the token
          localStorage.setItem('token', token);
          
          // Check if user is admin to redirect appropriately
          try {
            const payload = JSON.parse(atob(token.split('.')[1]));
            if (payload.role === 'admin') {
              navigate('/admin/users');
            } else {
              navigate('/dashboard');
            }
          } catch (error) {
            // Fallback to dashboard if token parsing fails
            navigate('/dashboard');
          }
        } else {
          setError('Token non reçu. Veuillez réessayer.');
          setLoading(false);
        }
      } catch (err) {
        console.error('OAuth callback error:', err);
        setError('Une erreur est survenue lors de l\'authentification.');
        setLoading(false);
      }
    };

    handleOAuthCallback();
  }, [searchParams, navigate]);

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-serene flex items-center justify-center">
        <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-2xl p-8 border border-sage-200 text-center max-w-md">
          <div className="flex justify-center mb-6">
            <div className="w-16 h-16 bg-gradient-to-br from-primary-400 to-primary-600 rounded-full flex items-center justify-center shadow-lg">
              <span className="text-2xl">🌱</span>
            </div>
          </div>
          
          <h2 className="text-2xl font-inter font-bold text-sage-800 mb-4">
            Connexion en cours...
          </h2>
          
          <div className="flex items-center justify-center mb-4">
            <svg className="animate-spin h-8 w-8 text-primary-600" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
          </div>
          
          <p className="text-sage-600">
            Finalisation de votre authentification...
          </p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-serene flex items-center justify-center">
        <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-2xl p-8 border border-sage-200 text-center max-w-md">
          <div className="flex justify-center mb-6">
            <div className="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center shadow-lg">
              <span className="text-2xl">❌</span>
            </div>
          </div>
          
          <h2 className="text-2xl font-inter font-bold text-red-800 mb-4">
            Erreur d'authentification
          </h2>
          
          <p className="text-red-600 mb-6">
            {error}
          </p>
          
          <button
            onClick={() => navigate('/login')}
            className="w-full py-3 px-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-medium rounded-lg hover:from-primary-600 hover:to-primary-700 transition-all duration-200 shadow-lg"
          >
            Retour à la connexion
          </button>
        </div>
      </div>
    );
  }

  return null;
};

export default OAuthCallback;