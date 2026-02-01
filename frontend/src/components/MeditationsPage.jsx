import React from 'react';
import { Link } from 'react-router-dom';
import { 
  ArrowLeftIcon, 
  PlayCircleIcon,
  SparklesIcon
} from '@heroicons/react/24/outline';

const MeditationsPage = () => {
  const meditations = [
    {
      id: 1,
      title: 'El mapa de tus emociones',
      description: 'Conecta con tus emociones y aprende a navegarlas con consciencia plena.',
      youtubeUrl: 'https://www.youtube.com/watch?v=bJ8rn-oTjlg',
      youtubeId: 'bJ8rn-oTjlg',
      hasVideo: true
    },
    {
      id: 2,
      title: 'Celebra tu ser',
      description: 'Una meditación para reconocer tu valor único y celebrar quien eres.',
      youtubeUrl: 'https://www.youtube.com/watch?v=Z5oV4PpfifM',
      youtubeId: 'Z5oV4PpfifM',
      hasVideo: true
    },
    {
      id: 3,
      title: 'El arte de amar',
      description: 'Cultiva el amor propio y la conexión profunda contigo misma.',
      youtubeUrl: 'https://www.youtube.com/watch?v=01JqwwTt1-w',
      youtubeId: '01JqwwTt1-w',
      hasVideo: true
    },
    {
      id: 4,
      title: 'De la expectativa a la realidad',
      description: 'Libérate de las expectativas limitantes y abraza tu presente.',
      youtubeUrl: 'https://www.youtube.com/watch?v=oqndj0aAePE',
      youtubeId: 'oqndj0aAePE',
      hasVideo: true
    },
    {
      id: 5,
      title: 'Libertad en Acción',
      description: 'Activa tu poder interior y da el siguiente paso hacia tu libertad.',
      youtubeUrl: 'https://www.youtube.com/watch?v=ZQhIth_2Ka8',
      youtubeId: 'ZQhIth_2Ka8',
      hasVideo: true
    }
  ];

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-6 sm:py-12">
      {/* Header */}
      <div className="mb-8 sm:mb-12">
        <Link 
          to="/dashboard" 
          className="inline-flex items-center text-taupe hover:text-sage transition-colors mb-6"
        >
          <ArrowLeftIcon className="w-4 h-4 mr-2" />
          <span className="font-inter text-sm">Volver a Mi Programa</span>
        </Link>
        
        <div className="modern-card text-center p-6 sm:p-10 relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-sage-100/50 to-beige/50"></div>
          <div className="relative z-10">
            <div className="flex justify-center mb-4">
              <div className="p-4 gradient-sage rounded-full">
                <SparklesIcon className="w-10 h-10 sm:w-12 sm:h-12 text-white" />
              </div>
            </div>
            <h1 className="font-inter text-2xl sm:text-3xl md:text-4xl font-semibold text-black mb-3">
              Meditaciones Guiadas
            </h1>
            <p className="font-inter text-base sm:text-lg text-taupe-dark max-w-2xl mx-auto">
              Un espacio de paz y conexión interior. Cada meditación está diseñada para acompañarte en tu proceso de transformación.
            </p>
          </div>
        </div>
      </div>

      {/* Meditations Grid */}
      <div className="space-y-6">
        {meditations.map((meditation) => (
          <div 
            key={meditation.id} 
            className="modern-card p-4 sm:p-6 hover:shadow-lg transition-shadow"
          >
            <div className="flex flex-col lg:flex-row gap-6">
              {/* Video Section */}
              <div className="w-full lg:w-2/3">
                {meditation.hasVideo ? (
                  <div className="relative w-full aspect-video rounded-xl overflow-hidden bg-gray-100">
                    <iframe
                      src={`https://www.youtube.com/embed/${meditation.youtubeId}`}
                      title={meditation.title}
                      frameBorder="0"
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowFullScreen
                      className="absolute inset-0 w-full h-full"
                    ></iframe>
                  </div>
                ) : (
                  <div className="relative w-full aspect-video rounded-xl overflow-hidden bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center">
                    <div className="text-center p-6">
                      <div className="flex justify-center mb-4">
                        <div className="p-4 bg-gray-300 rounded-full">
                          <PlayCircleIcon className="w-12 h-12 text-gray-500" />
                        </div>
                      </div>
                      <p className="font-inter text-gray-500 text-sm sm:text-base">
                        Próximamente disponible
                      </p>
                    </div>
                  </div>
                )}
              </div>
              
              {/* Info Section */}
              <div className="w-full lg:w-1/3 flex flex-col justify-center">
                <div className="flex items-center space-x-2 mb-2">
                  <span className="px-3 py-1 bg-sage/10 text-sage rounded-full text-xs font-inter font-medium">
                    Meditación {meditation.id}
                  </span>
                  {!meditation.hasVideo && (
                    <span className="px-3 py-1 bg-gray-100 text-gray-500 rounded-full text-xs font-inter font-medium">
                      Próximamente
                    </span>
                  )}
                </div>
                <h3 className="font-inter text-lg sm:text-xl font-semibold text-black mb-3">
                  {meditation.title}
                </h3>
                <p className="font-inter text-sm sm:text-base text-taupe-dark leading-relaxed">
                  {meditation.description}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Bottom motivation */}
      <div className="mt-8 sm:mt-12 modern-card text-center p-6 sm:p-8">
        <p className="font-inter text-base sm:text-lg text-taupe-dark italic max-w-2xl mx-auto">
          "La meditación no es escapar de la realidad, sino descubrir la paz que ya existe dentro de ti."
        </p>
      </div>
    </div>
  );
};

export default MeditationsPage;
