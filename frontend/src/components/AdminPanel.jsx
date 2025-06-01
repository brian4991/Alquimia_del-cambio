import React, { useState, useEffect } from 'react';
import { PlusIcon, PencilIcon, TrashIcon, BookOpenIcon, DocumentTextIcon, AcademicCapIcon } from '@heroicons/react/24/outline';
import ModulesTab from './ModulesTab';
import ThemesTab from './ThemesTab';
import CardsTab from './CardsTab';
import ExercisesTab from './ExercisesTab';

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
      const response = await fetch('/api/modules', {
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
      const response = await fetch(`/api/modules/${moduleId}/themes`, {
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
      const response = await fetch(`/api/themes/${themeId}/cards`, {
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
      const response = await fetch(`/api/themes/${themeId}/exercises`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();
      setExercises(data);
    } catch (error) {
      console.error('Error loading exercises:', error);
    }
  };

  const tabs = [
    { id: 'modules', label: 'Modules', icon: BookOpenIcon },
    { id: 'themes', label: 'Thèmes', icon: DocumentTextIcon },
    { id: 'cards', label: 'Cartes', icon: DocumentTextIcon },
    { id: 'exercises', label: 'Exercices', icon: AcademicCapIcon }
  ];

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Panneau d'Administration</h1>
          <p className="text-gray-600">Gérez vos modules, thèmes, cartes et exercices</p>
        </div>

        {/* Navigation Tabs */}
        <div className="bg-white rounded-lg shadow-sm mb-6">
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
                        ? 'border-blue-500 text-blue-600'
                        : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
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
        <div className="bg-white rounded-lg shadow-sm p-6">
          {activeTab === 'modules' && (
            <ModulesTab 
              modules={modules} 
              onModuleSelect={setSelectedModule}
              onReload={loadModules}
            />
          )}
          
          {activeTab === 'themes' && (
            <ThemesTab 
              selectedModule={selectedModule}
              themes={themes}
              modules={modules}
              onThemeSelect={setSelectedTheme}
              onLoadThemes={loadThemes}
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