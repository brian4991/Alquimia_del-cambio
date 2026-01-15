import React, { lazy, Suspense } from 'react';

const MarketingTabLazy = lazy(() =>
  import('./marketing/index.js')
    .then((module) => ({ default: module.MarketingTab }))
    .catch((error) => {
      console.warn('Marketing module not available:', error);
      return {
        default: () => (
          <div className="p-8 text-center text-gray-500">
            Module Marketing non disponible. Vérifiez la configuration.
          </div>
        )
      };
    })
);

const MarketingPage = () => (
  <div className="min-h-screen bg-gradient-elegant p-6">
    <div className="max-w-7xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Marketing</h1>
        <p className="text-gray-600">Gestion et coordination du marketing</p>
      </div>
      <div className="bg-white rounded-lg shadow-elegant p-6">
        <Suspense
          fallback={
            <div className="p-8 text-center text-gray-500">
              Chargement du module Marketing...
            </div>
          }
        >
          <MarketingTabLazy />
        </Suspense>
      </div>
    </div>
  </div>
);

export default MarketingPage;
