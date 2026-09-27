import React, { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, ArrowDown, Check, X } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from '@/components/ui/accordion';
import './NicoleLandingMobile.css';

const BOOKING_URL = 'https://calendly.com/contacto-nicoleramirezpsicoach/24horas';
const CONTACT_EMAIL = 'contacto@nicoleramirezpsicoach.com';

const experiences = [
  ['Tu mente no se apaga:', 'pensás demasiado en lo que pasó o en qué hacer ahora.'],
  ['Extrañás algo de tu vida anterior:', 'una persona, un país, una relación, un proyecto o incluso quién eras antes.'],
  ['Hay una decisión que no conseguís tomar:', 'quedarte, volver, terminar, continuar o empezar de nuevo.'],
  ['Una parte de vos quiere avanzar y otra sigue vinculada a lo que perdió.', ''],
  ['Te exigís estar bien porque “ya pasó tiempo”,', 'pero hay emociones que siguen apareciendo.'],
  ['Sentís que vos también cambiaste', 'y ya no tenés tan claro qué querés para esta etapa.'],
];

const goals = [
  'Comprender y regular mejor tus emociones.',
  'Procesar la pérdida o el cambio que estás atravesando.',
  'Reconectar con tus necesidades, límites e identidad.',
  'Comprender patrones que se repiten en tus relaciones.',
  'Reducir la autoexigencia y la culpa.',
  'Tomar decisiones con mayor claridad.',
  'Construir una nueva etapa que tenga sentido para vos.',
];

const included = [
  'Sesiones individuales 1:1',
  'Ejercicios y herramientas entre sesiones',
  'Guías, audios y recursos complementarios',
  'Herramientas de regulación emocional',
  'Evaluaciones personalizadas cuando sean necesarias',
  'Acompañamiento durante el proceso',
];

const audience = [
  'Estás atravesando un duelo, una migración o un cambio importante.',
  'Sentís que lo ocurrido sigue afectando cómo te sentís, te relacionás o tomás decisiones.',
  'Llevás tiempo intentando resolver lo mismo y necesitás trabajarlo con mayor profundidad.',
  'Querés participar activamente en tu proceso.',
  'Buscás un acompañamiento individual, estructurado y con continuidad.',
  'Podés comprometerte con un proceso de 17 semanas.',
];

const notSuitable = [
  'Buscás únicamente una conversación puntual.',
  'Buscás una recomendación rápida.',
  'Necesitás atención inmediata ante una crisis.',
];

const differences = [
  ['17 semanas con continuidad', 'Para profundizar y dar seguimiento a lo que vamos trabajando.'],
  ['Personalizado', 'Partimos de tu historia, tu momento actual y tus necesidades.'],
  ['Más allá de la sesión', 'Contás con herramientas y recursos para continuar trabajando entre nuestros encuentros.'],
  ['Una mirada integral', 'Trabajamos emociones, vínculos, identidad, creencias y decisiones cuando forman parte de tu proceso.'],
];

const questions = [
  {
    question: '¿Tengo que ser migrante para trabajar con vos?',
    paragraphs: ['No. Mi trabajo está enfocado principalmente en duelo, migración y transiciones vitales. Esto incluye procesos relacionados con rupturas, pérdidas, duelo migratorio y cierres o cambios importantes en la vida.'],
  },
  {
    question: '¿La llamada de claridad es una sesión de terapia?',
    paragraphs: ['Es un primer espacio para conocer tu situación y valorar si Cambio de Paradigma se ajusta a lo que necesitás.'],
  },
  {
    question: '¿Tengo que saber exactamente qué quiero trabajar?',
    paragraphs: ['No. Podemos empezar por comprender qué está ocurriendo y definir juntas los objetivos del proceso.'],
  },
  {
    question: '¿Las sesiones son online?',
    paragraphs: ['Sí. El acompañamiento psicológico se realiza online y en español.'],
  },
  {
    question: '¿Cuánto dura Cambio de Paradigma?',
    paragraphs: ['17 semanas.'],
  },
];

function CheckList({ items, negative = false }) {
  const Icon = negative ? X : Check;
  return <ul className="nl-check-list" role="list">{items.map(item => <li key={item}>
    <Icon size={20} aria-hidden="true" /><span>{item}</span>
  </li>)}</ul>;
}

function BookingLink({ className = '' }) {
  // Same-tab navigation also works inside social apps without relying on popups.
  return <Button asChild className={`nl-button ${className}`}>
    <a href={BOOKING_URL}>
      <span>Reserva una llamada de claridad</span><ArrowRight size={19} aria-hidden="true" />
    </a>
  </Button>;
}

export default function NicoleRamirezLanding() {
  const heroAction = useRef(null);
  const closingAction = useRef(null);
  const [showMobileBooking, setShowMobileBooking] = useState(false);

  useEffect(() => {
    if (!window.location.hash) window.scrollTo(0, 0);
    if (!('IntersectionObserver' in window)) return;
    const update = () => {
      const hero = heroAction.current?.getBoundingClientRect();
      const closing = closingAction.current?.getBoundingClientRect();
      setShowMobileBooking(Boolean(hero && closing && hero.bottom <= 0 && !(closing.top < window.innerHeight && closing.bottom > 0)));
    };
    const observer = new IntersectionObserver(update);
    observer.observe(heroAction.current);
    observer.observe(closingAction.current);
    return () => observer.disconnect();
  }, []);

  return <div className="nicole-landing">
    <a href="#landing-content" className="skip-link">Saltar al contenido</a>
    <header className="nl-header nl-container">
      <a href="/" className="nl-brand" aria-label="Nicole Ramírez · Inicio">
        <svg className="nl-monogram" viewBox="530 680 2180 1880" aria-hidden="true" focusable="false">
          <image href="/assets/landing/nicole-monogram-brand.jpg" width="3240" height="3241" />
        </svg>
        <span className="nl-brand-role">Psicóloga</span>
      </a>
      <nav className="nl-navigation" aria-label="Conocé el acompañamiento">
        <a href="#programa">El proceso</a><a href="#sobre-mi">Sobre mí</a><a href="#preguntas">Preguntas</a>
      </nav>
    </header>

    <main id="landing-content" tabIndex={-1}>
      <section className="nl-hero nl-container" aria-labelledby="landing-title">
        <div className="nl-hero-copy">
          <p className="nl-specialty">Psicóloga especializada en duelo, migración y transiciones vitales</p>
          <h1 id="landing-title">Hay cambios que también implican <span>despedirte de una vida que conocías.</span></h1>
          <p>Una ruptura. Migrar a otro país. Perder a alguien. Dejar atrás una relación, un lugar, un proyecto o una versión de tu vida que imaginabas diferente.</p>
          <p>A veces el cambio ya ocurrió, pero emocionalmente todavía estás intentando encontrar tu lugar después de él.</p>
          <div ref={heroAction} className="nl-action"><BookingLink /></div>
          <a className="nl-explore" href="#programa">Conocé el proceso<ArrowDown size={17} aria-hidden="true" /></a>
        </div>
        <figure className="nl-hero-photo">
          <img src="/assets/landing/nicole-consultation-dsc2578-960.webp" srcSet="/assets/landing/nicole-consultation-dsc2578-480.webp 480w, /assets/landing/nicole-consultation-dsc2578-960.webp 960w" sizes="(min-width: 1200px) 480px, (min-width: 900px) 42vw, (min-width: 600px) 440px, calc(100vw - 40px)" alt="Nicole Ramírez en su espacio de trabajo online" width="960" height="625" decoding="async" />
          <figcaption>Nicole Ramírez · Atención online en español</figcaption>
        </figure>
      </section>

      <section className="nl-section nl-paper-section" aria-labelledby="experiences-title">
        <div className="nl-container">
          <h2 id="experiences-title">¿Esto te está pasando?</h2>
          <p className="nl-lead">Aunque desde fuera parezca que seguís con tu vida...</p>
          <ul className="nl-experiences" role="list">
            {experiences.map(([title, description]) => <li key={title}>
              <Card className="nl-card nl-experience-card">
                <CardContent className="nl-experience-content">
                  <CardTitle>{title}</CardTitle>
                  {description && <p>{description}</p>}
                </CardContent>
              </Card>
            </li>)}
          </ul>
          <div className="nl-migration">
            <div>
              <h3>Y si migraste...</h3>
              <p>Podés estar construyendo una vida nueva y, al mismo tiempo, extrañar profundamente la anterior.</p>
              <p>Tu gente, tu lugar, tus costumbres, tu idioma o incluso la persona que eras antes de irte.</p>
            </div>
            <div>
              <p>Y quizás te preguntás:</p>
              <ul className="nl-migration-questions">
                <li>¿Quiero quedarme o volver?</li><li>¿Dónde pertenezco ahora?</li><li>¿Por qué conseguí lo que quería y aun así me siento así?</li>
              </ul>
            </div>
          </div>
          <div className="nl-takeaway-action">
            <p className="nl-takeaway">El duelo también es un proceso de adaptarte a lo nuevo mientras procesás aquello que dejaste atrás.</p>
            <BookingLink />
          </div>
        </div>
      </section>

      <section id="sobre-mi" className="nl-section nl-paper-section" aria-labelledby="about-title">
        <div className="nl-container nl-about">
          <div className="nl-about-intro"><h2 id="about-title">Soy Nicole Ramírez</h2>
            <p>Desde 2022 acompaño a personas que atraviesan procesos de duelo, migración y transiciones importantes.</p>
          </div>
          <figure className="nl-about-photo"><img src="/assets/landing/nicole-portrait-dsc8219-960.webp" srcSet="/assets/landing/nicole-portrait-dsc8219-480.webp 480w, /assets/landing/nicole-portrait-dsc8219-960.webp 960w" sizes="(min-width: 1200px) 411px, (min-width: 900px) 35vw, (min-width: 600px) 440px, calc(100vw - 40px)" alt="Nicole Ramírez, psicóloga" width="960" height="1440" loading="lazy" decoding="async" /></figure>
          <div className="nl-about-copy">
            <p>Mi propia experiencia migratoria me permite comprender de cerca algunas de las contradicciones que aparecen cuando una vida cambia: extrañar mientras construís algo nuevo, cuestionarte decisiones que antes parecían claras o descubrir que vos también cambiaste durante el proceso.</p>
            <p>Como psicóloga clínica, trabajo desde un enfoque integrativo, utilizando herramientas de Terapia Cognitivo-Conductual (TCC), Terapia de Aceptación y Compromiso (ACT) y EMDR, según las necesidades y objetivos de cada proceso.</p>
            <p>Mi trabajo es ayudarte a comprender lo que estás viviendo y acompañarte profesionalmente en lo que necesitás trabajar para esta nueva etapa.</p>
          </div>
        </div>
      </section>

      <section id="enfoque" className="nl-section nl-container nl-framed-section nl-understanding" aria-labelledby="goals-title">
        <div className="nl-reading-split">
          <div><h2 id="goals-title">Lo que vas a lograr</h2>
            <p className="nl-lead">El objetivo es que puedas atravesar esta etapa con más recursos y claridad.</p>
          </div>
          <div>
            <p>Durante el proceso trabajaremos para que puedas:</p>
            <CheckList items={goals} />
            <div className="nl-action"><BookingLink /></div>
          </div>
        </div>
      </section>

      <section id="programa" className="nl-section" aria-labelledby="program-title">
        <div className="nl-container">
          <h2 id="program-title">Cambio de Paradigma</h2>
          <div className="nl-program-layout">
            <div>
              <p className="nl-lead">Un proceso de 17 semanas para trabajar lo que estás viviendo y construir lo que viene después.</p>
              <p>Cambio de Paradigma es un proceso de acompañamiento psicológico individual, estructurado y adaptado a tu historia, necesidades y objetivos.</p>
            </div>
            <aside className="nl-includes-aside" aria-labelledby="includes-title">
              <Card className="nl-card nl-includes">
                <CardHeader className="nl-card-header"><CardTitle id="includes-title">¿Qué incluye?</CardTitle></CardHeader>
                <CardContent className="nl-card-content">
                  <CheckList items={included} />
                </CardContent>
              </Card>
            </aside>
          </div>
          <div className="nl-takeaway-action">
            <p>Lo que trabajamos en sesión continúa fuera de ella, para que puedas llevarlo progresivamente a situaciones reales de tu vida.</p>
            <BookingLink />
          </div>
        </div>
      </section>

      <section id="para-vos" className="nl-section nl-container nl-framed-section nl-clarity" aria-labelledby="audience-title">
        <div>
          <h2 id="audience-title">¿Es para vos?</h2>
          <p>Cambio de Paradigma está pensado como un proceso psicológico continuado.</p>
          <div className="nl-fit-grid">
            <section aria-labelledby="fit-yes-title">
              <h3 id="fit-yes-title">Puede ser para vos si...</h3>
              <CheckList items={audience} />
            </section>
            <section aria-labelledby="fit-no-title">
              <h3 id="fit-no-title">Puede no ser para vos si...</h3>
              <CheckList items={notSuitable} negative />
            </section>
          </div>
        </div>
      </section>

      <section id="diferencia" className="nl-section" aria-labelledby="difference-title">
        <div className="nl-container">
          <h2 id="difference-title">¿Qué hace diferente a Cambio de Paradigma?</h2>
          <ul className="nl-areas" role="list">{differences.map(([title, description]) => <li key={title}>
            <Card className="nl-card nl-area-card">
              <CardHeader className="nl-card-header"><CardTitle>{title}</CardTitle></CardHeader>
              <CardContent className="nl-card-content"><p>{description}</p></CardContent>
            </Card>
          </li>)}</ul>
        </div>
      </section>

      <section id="preguntas" className="nl-section" aria-labelledby="faq-title">
        <div className="nl-container nl-faq-layout">
          <h2 id="faq-title">Preguntas frecuentes</h2>
          <Accordion type="multiple" className="nl-faq">{questions.map(({ question, paragraphs }) => <AccordionItem value={question} key={question} className="nl-faq-item">
            <AccordionTrigger className="nl-faq-trigger">{question}</AccordionTrigger>
            <AccordionContent className="nl-faq-answer">{paragraphs.map(paragraph => <p key={paragraph}>{paragraph}</p>)}</AccordionContent>
          </AccordionItem>)}</Accordion>
        </div>
      </section>

      <section id="llamada" className="nl-section nl-closing" aria-labelledby="closing-title">
        <div className="nl-container">
          <h2 id="closing-title">Si algo cambió en tu vida y todavía estás intentando encontrar tu lugar después de eso, podemos empezar por hablar de lo que estás viviendo.</h2>
          <p>La llamada de claridad es un primer espacio para conocer tu situación y valorar si Cambio de Paradigma puede ser adecuado para vos.</p>
          <div ref={closingAction}><BookingLink className="nl-button-light" /></div>
        </div>
      </section>
    </main>

    <footer className="nl-footer nl-container">
      <div className="nl-footer-identity">
        <svg className="nl-wordmark" viewBox="207 1420 2826 400" aria-hidden="true" focusable="false">
          <image href="/assets/landing/nicole-wordmark-brand.jpg" width="3240" height="3241" />
        </svg>
        <div><p className="nl-footer-name">Nicole Ramírez | Psicóloga</p><p>Psicología online especializada en duelo, duelo migratorio y procesos de migración.</p><p>Atención psicológica online en español.</p></div>
      </div>
      <div className="nl-footer-links">
        <a href={`mailto:${CONTACT_EMAIL}`}>{CONTACT_EMAIL}</a>
        <a href="https://www.instagram.com/nicoleramirezpsicologa/" target="_blank" rel="noopener noreferrer">Instagram · @nicoleramirezpsicologa</a>
        <a href="https://www.tiktok.com/@nicoleramirezpsicologa" target="_blank" rel="noopener noreferrer">TikTok · @nicoleramirezpsicologa</a>
        <Link to="/informacion">Información del servicio</Link>
        <Link to="/privacidad">Política de privacidad</Link>
        <Link to="/login">Acceder a mi programa</Link>
      </div>
      <p className="nl-copyright">© {new Date().getFullYear()} Nicole Ramírez</p>
    </footer>
    {showMobileBooking && <div className="nl-mobile-booking" aria-label="Reservar una llamada"><BookingLink /></div>}
  </div>;
}
