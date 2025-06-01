import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import StepView from './components/StepView';
import ModuleView from './components/ModuleView';
import ThemeView from './components/ThemeView';
import AdminPanel from './components/AdminPanel';
import Layout from './components/Layout';
import './index.css';

const ProtectedRoute = ({ children }) => {
  const token = localStorage.getItem('token');
  return token ? children : <Navigate to="/login" />;
};

const App = () => {
  return (
    <Router>
      <div className="min-h-screen">
        <Routes>
          <Route path="/login" element={<Login />} />
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
              <ProtectedRoute>
                <Layout>
                  <AdminPanel />
                </Layout>
              </ProtectedRoute>
            } 
          />
          <Route path="/" element={<Navigate to="/dashboard" />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App; 