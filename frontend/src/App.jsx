import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import StepView from './components/StepView';
import ModuleView from './components/ModuleView';
import ThemeView from './components/ThemeView';
import AdminPanel from './components/AdminPanel';
import AdminUsersTracking from './components/AdminUsersTracking';
import UserDetailView from './components/UserDetailView';
// BookingPage removed
import Layout from './components/Layout';
// import ProgramLanding from './components/ProgramLanding';
// import RetiroAmateLanding from './components/RetiroAmateLanding';
import RetiroAmateStyle from './components/RetiroAmateStyle';
// import CambioDeParadigmaLanding from './components/landing/CambioDeParadigmaLanding';
import NicoleRamirezLanding from './components/landing/NicoleRamirezLanding';
import OAuthCallback from './components/OAuthCallback';
import MeditationsPage from './components/MeditationsPage';
import './index.css';

// Utility function to decode JWT and get user info
const decodeToken = (token) => {
  // #region agent log
  fetch('http://127.0.0.1:7242/ingest/6dcdf81b-125d-4c23-b88d-0ce3c90d0db7',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'frontend/src/App.jsx:20',message:'H6: Token decode attempt',data:{token_exists:!!token,token_parts:token?token.split('.').length:0},timestamp:Date.now(),sessionId:'debug-session',hypothesisId:'H6'})}).catch(()=>{});
  // #endregion
  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    // #region agent log
    fetch('http://127.0.0.1:7242/ingest/6dcdf81b-125d-4c23-b88d-0ce3c90d0db7',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'frontend/src/App.jsx:22',message:'H6: Token decoded successfully',data:{payload_has_role:!!payload.role,role:payload.role},timestamp:Date.now(),sessionId:'debug-session',hypothesisId:'H6'})}).catch(()=>{});
    // #endregion
    return payload;
  } catch (error) {
    // #region agent log
    fetch('http://127.0.0.1:7242/ingest/6dcdf81b-125d-4c23-b88d-0ce3c90d0db7',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'frontend/src/App.jsx:24',message:'H6: Token decode ERROR',data:{error:error.message,token_sample:token?token.substring(0,20):'null'},timestamp:Date.now(),sessionId:'debug-session',hypothesisId:'H6'})}).catch(()=>{});
    // #endregion
    console.error('Error decoding token:', error);
    return null;
  }
};

const ProtectedRoute = ({ children, requireAdmin = false }) => {
  const token = localStorage.getItem('token');
  // #region agent log
  fetch('http://127.0.0.1:7242/ingest/6dcdf81b-125d-4c23-b88d-0ce3c90d0db7',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'frontend/src/App.jsx:30',message:'H6: ProtectedRoute check',data:{has_token:!!token,requireAdmin:requireAdmin},timestamp:Date.now(),sessionId:'debug-session',hypothesisId:'H6'})}).catch(()=>{});
  // #endregion
  
  if (!token) {
    return <Navigate to="/login" />;
  }

  if (requireAdmin) {
    const userData = decodeToken(token);
    // #region agent log
    fetch('http://127.0.0.1:7242/ingest/6dcdf81b-125d-4c23-b88d-0ce3c90d0db7',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'frontend/src/App.jsx:37',message:'H6: Admin check result',data:{userData_exists:!!userData,role:userData?.role,is_admin:userData?.role==='admin'},timestamp:Date.now(),sessionId:'debug-session',hypothesisId:'H6'})}).catch(()=>{});
    // #endregion
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
          {/* Public routes - only login and OAuth callback */}
          <Route path="/login" element={<Login />} />
          <Route path="/auth/callback" element={<OAuthCallback />} />
          
          {/* Public landing pages */}
          <Route path="/" element={<NicoleRamirezLanding />} />
          <Route path="/nicole" element={<NicoleRamirezLanding />} />
          {/* <Route path="/cambio-de-paradigma" element={<CambioDeParadigmaLanding />} /> */}
          <Route path="/retiro-renacer" element={<RetiroAmateStyle />} />
          {/* <Route path="/retiro-renacer-old" element={<RetiroAmateLanding />} /> */}
          
          {/* Protected routes - require authentication */}
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
            path="/meditaciones" 
            element={
              <ProtectedRoute>
                <Layout>
                  <MeditationsPage />
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
          <Route 
            path="/admin/users/:userId" 
            element={
              <ProtectedRoute requireAdmin={true}>
                <Layout>
                  <UserDetailView />
                </Layout>
              </ProtectedRoute>
            } 
          />
          
          {/* Redirect all other routes to login */}
          <Route path="*" element={<Navigate to="/login" replace />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App; 