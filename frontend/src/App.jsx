import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import StepView from './components/StepView';
import ModuleView from './components/ModuleView';
import ThemeView from './components/ThemeView';
import AdminPanel from './components/AdminPanel';
import AdminUsersTracking from './components/AdminUsersTracking';
import Layout from './components/Layout';
import PsychologyLanding from './components/PsychologyLanding';
import OAuthCallback from './components/OAuthCallback';
import './index.css';

// Utility function to decode JWT and get user info
const decodeToken = (token) => {
  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload;
  } catch (error) {
    console.error('Error decoding token:', error);
    return null;
  }
};

const ProtectedRoute = ({ children, requireAdmin = false }) => {
  const token = localStorage.getItem('token');
  
  if (!token) {
    return <Navigate to="/login" />;
  }

  if (requireAdmin) {
    const userData = decodeToken(token);
    if (!userData || userData.role !== 'admin') {
      return (
        <div className="min-h-screen bg-gradient-serene flex items-center justify-center">
          <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-2xl p-8 border border-sage-200 text-center max-w-md">
            <div className="flex justify-center mb-6">
              <div className="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center shadow-lg">
                <span className="text-2xl">🚫</span>
              </div>
            </div>
            <h2 className="text-2xl font-inter font-bold text-red-800 mb-4">
              Accès restreint
            </h2>
            <p className="text-red-600 mb-6">
              Vous n'avez pas les permissions nécessaires pour accéder à cette page.
            </p>
            <button
              onClick={() => {
                const token = localStorage.getItem('token');
                if (token) {
                  try {
                    const payload = JSON.parse(atob(token.split('.')[1]));
                    if (payload.role === 'admin') {
                      window.location.href = '/admin/users';
                    } else {
                      window.location.href = '/dashboard';
                    }
                  } catch (error) {
                    window.location.href = '/dashboard';
                  }
                } else {
                  window.location.href = '/dashboard';
                }
              }}
              className="w-full py-3 px-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-medium rounded-lg hover:from-primary-600 hover:to-primary-700 transition-all duration-200 shadow-lg"
            >
              Retour au tableau de bord
            </button>
          </div>
        </div>
      );
    }
  }

  return children;
};

const App = () => {
  return (
    <Router>
      <div className="min-h-screen">
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/auth/callback" element={<OAuthCallback />} />
          <Route 
            path="/dashboard" 
            element={
              <ProtectedRoute>
                <Layout>
                  <Dashboard />
                </Layout>
              </ProtectedRoute>
            } 
          />
          <Route 
            path="/module/:moduleId" 
            element={
              <ProtectedRoute>
                <Layout>
                  <ModuleView />
                </Layout>
              </ProtectedRoute>
            } 
          />
          <Route 
            path="/theme/:themeId" 
            element={
              <ProtectedRoute>
                <Layout>
                  <ThemeView />
                </Layout>
              </ProtectedRoute>
            } 
          />
          <Route 
            path="/step/:stepId" 
            element={
              <ProtectedRoute>
                <Layout>
                  <StepView />
                </Layout>
              </ProtectedRoute>
            } 
          />
          <Route 
            path="/profile" 
            element={
              <ProtectedRoute>
                <Layout>
                  <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                    <div className="bg-white/70 backdrop-blur-sm rounded-2xl shadow-xl p-8 border border-sage-200">
                      <h1 className="text-3xl font-inter font-bold text-sage-800 mb-6">Mon Profil</h1>
                      <div className="space-y-4">
                        <div className="p-4 bg-gradient-nature rounded-lg">
                          <p className="text-sage-700">Fonctionnalité en développement...</p>
                          <p className="text-sm text-sage-600 mt-2">Bientôt vous pourrez voir vos statistiques de progression et personnaliser votre expérience.</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </Layout>
              </ProtectedRoute>
            } 
          />
          <Route 
            path="/admin" 
            element={
              <ProtectedRoute requireAdmin={true}>
                <Layout>
                  <AdminPanel />
                </Layout>
              </ProtectedRoute>
            } 
          />
          <Route 
            path="/admin/users" 
            element={
              <ProtectedRoute requireAdmin={true}>
                <Layout>
                  <AdminUsersTracking />
                </Layout>
              </ProtectedRoute>
            } 
          />
          <Route path="/" element={<PsychologyLanding />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App; 