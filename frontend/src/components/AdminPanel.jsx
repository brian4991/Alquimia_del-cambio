import React, { useState, useEffect } from 'react';
import { PlusIcon, PencilIcon, TrashIcon, BookOpenIcon, DocumentTextIcon, AcademicCapIcon, LightBulbIcon } from '@heroicons/react/24/outline';
import ModulesTab from './ModulesTab';
import ThemesTab from './ThemesTab';
import RecursosTab from './RecursosTab';
import CardsTab from './CardsTab';
import ExercisesTab from './ExercisesTab';
import Dashboard from './Dashboard';
import { config } from '../config';

const AdminPanel = () => {
  const [activeTab, setActiveTab] = useState('modules');
  const [modules, setModules] = useState([]);
  const [themes, setThemes] = useState([]);
  const [cards, setCards] = useState([]);
  const [exercises, setExercises] = useState([]);
  const [selectedModule, setSelectedModule] = useState(null);
  const [selectedTheme, setSelectedTheme] = useState(null);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [editingItem, setEditingItem] = useState(null);

  // Load modules on component mount
  useEffect(() => {
    loadModules();
  }, []);

  const loadModules = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`${config.apiUrl}/modules`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();
      setModules(data);
    } catch (error) {
      console.error('Error loading modules:', error);
    }
  };

  const loadThemes = async (moduleId) => {
    try {
      const token = localStorage.getItem('token');
              const response = await fetch(`${config.apiUrl}/modules/${moduleId}/themes`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();
      setThemes(data);
    } catch (error) {
      console.error('Error loading themes:', error);
    }
  };

  const loadCards = async (themeId) => {
    try {
      const token = localStorage.getItem('token');
              const response = await fetch(`${config.apiUrl}/themes/${themeId}/cards`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();
      setCards(data);
    } catch (error) {
      console.error('Error loading cards:', error);
    }
  };

  const loadExercises = async (themeId) => {
    try {
      const token = localStorage.getItem('token');
              const response = await fetch(`${config.apiUrl}/themes/${themeId}/exercises`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();
      setExercises(data);
    } catch (error) {
      console.error('Error loading exercises:', error);
    }
  };

  const tabs = [
    { id: 'preview', label: 'Mi Programa', icon: BookOpenIcon },
    { id: 'modules', label: 'Módulos', icon: BookOpenIcon },
    { id: 'themes', label: 'Temas', icon: DocumentTextIcon },
    { id: 'recursos', label: 'Recursos', icon: LightBulbIcon },
    { id: 'cards', label: 'Cartas', icon: DocumentTextIcon },
    { id: 'exercises', label: 'Ejercicios', icon: AcademicCapIcon }
  ];

  return (
    <div className="min-h-screen bg-gradient-elegant p-6">
      <div className="max-w-7xl mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Panel de Administración</h1>
          <p className="text-gray-600">Gestiona tus módulos, temas, recursos, cartas y ejercicios</p>
        </div>

        {/* Navigation Tabs */}
        <div className="bg-white rounded-lg shadow-elegant mb-6">
          <div className="border-b border-gray-200">
            <nav className="-mb-px flex space-x-8">
              {tabs.map((tab) => {
                const Icon = tab.icon;
                return (
                  <button
                    key={tab.id}
                    onClick={() => setActiveTab(tab.id)}
                    className={`flex items-center px-4 py-4 text-sm font-medium border-b-2 transition-colors ${
                      activeTab === tab.id
                        ? 'border-sage text-sage'
                        : 'border-transparent text-gray-500 hover:text-sage hover:border-sage-light'
                    }`}
                  >
                    <Icon className="w-5 h-5 mr-2" />
                    {tab.label}
                  </button>
                );
              })}
            </nav>
          </div>
        </div>

        {/* Content Area */}
        <div className="bg-white rounded-lg shadow-elegant p-6">
          {activeTab === 'preview' && (
            <Dashboard />
          )}
          {activeTab === 'modules' && (
            <ModulesTab 
              modules={modules} 
              selectedModule={selectedModule}
              onModuleSelect={setSelectedModule}
              onReload={loadModules}
            />
          )}
          
          {activeTab === 'themes' && (
            <ThemesTab 
              selectedModule={selectedModule}
              selectedTheme={selectedTheme}
              themes={themes}
              modules={modules}
              onThemeSelect={setSelectedTheme}
              onLoadThemes={loadThemes}
            />
          )}

          {activeTab === 'recursos' && (
            <RecursosTab 
              selectedModule={selectedModule}
              modules={modules}
              selectedRecurso={selectedTheme}
              onRecursoSelect={setSelectedTheme}
              onLoadRecursos={(recursos) => {
                // You can use this to update state if needed
                console.log('Recursos loaded:', recursos);
              }}
            />
          )}

          {activeTab === 'cards' && (
            <CardsTab 
              selectedTheme={selectedTheme}
              themes={themes}
              cards={cards}
              onLoadCards={loadCards}
            />
          )}

          {activeTab === 'exercises' && (
            <ExercisesTab 
              selectedTheme={selectedTheme}
              themes={themes}
              exercises={exercises}
              onLoadExercises={loadExercises}
            />
          )}

        </div>
      </div>
    </div>
  );
};

export default AdminPanel; 
