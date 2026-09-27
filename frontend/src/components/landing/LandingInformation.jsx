import React from 'react';
import { Link } from 'react-router-dom';
import './NicoleLandingMobile.css';

const CONTACT_EMAIL = 'contacto@nicoleramirezpsicoach.com';

// Public information stays independent of the unpublished programme changes.
export default function LandingInformation({ privacy = false }) {
  return <main className="nicole-landing nl-information nl-section">
    <article className="nl-container">
      <Link to="/" className="nl-information-back">Volver al inicio</Link>
      <h1>{privacy ? 'Privacidad y uso de tus datos' : 'Información del servicio'}</h1>
      {privacy ? <>
        <h2>Qué información utiliza la plataforma</h2>
        <p>La plataforma utiliza los datos de tu cuenta, tus respuestas a los ejercicios y tu progreso. La sesión de acceso se conserva en este navegador mientras está iniciada.</p>
        <h2>Quién puede consultar lo que escribes</h2>
        <p>Las personas con acceso de administración al programa pueden consultar tus respuestas para acompañarte. En un dispositivo compartido, cierra la sesión cuando termines.</p>
        <h2>Servicios externos</h2>
        <p>El acceso con Google, los vídeos de YouTube y los enlaces de reserva de Calendly utilizan servicios externos. Estos proveedores aplican sus propias condiciones y políticas al utilizar sus servicios. Los vídeos incorporados pueden establecer conexiones con YouTube al abrir una página que los contiene.</p>
        <h2>Consultas sobre tus datos</h2>
        <p>Para consultar, corregir o solicitar la eliminación de tus datos, escribe a <a href={`mailto:${CONTACT_EMAIL}`}>{CONTACT_EMAIL}</a>. Esta página describe el funcionamiento de la plataforma; no establece un plazo de conservación ni promete una respuesta automática.</p>
      </> : <>
        <h2>Tu programa</h2>
        <p>Cambio de Paradigma reúne contenidos, recursos y ejercicios de reflexión. Puedes consultar tu recorrido y guardar tus respuestas.</p>
        <h2>Ritmo y acceso</h2>
        <p>La fecha de inicio, las sesiones y el acceso a los módulos se acuerdan individualmente con Nicole. La lectura y la práctica se realizan a tu ritmo según ese acuerdo.</p>
        <h2>Reservas y condiciones individuales</h2>
        <p>El acceso a una agenda externa no confirma por sí mismo una reserva ni un pago. Confirma con Nicole las fechas, el precio y las condiciones de tu acompañamiento antes de contratar o cambiar una sesión.</p>
        <h2>Consultas</h2>
        <p>Para dudas sobre el programa o tu cuenta, escribe a <a href={`mailto:${CONTACT_EMAIL}`}>{CONTACT_EMAIL}</a>. Esta página es información práctica sobre la plataforma y no sustituye el acuerdo individual del servicio.</p>
      </>}
      <nav aria-label="Información y acceso">
        <Link to={privacy ? '/informacion' : '/privacidad'}>{privacy ? 'Información del servicio' : 'Privacidad y uso de tus datos'}</Link>
        <Link to="/login">Acceder a mi programa</Link>
      </nav>
    </article>
  </main>;
}
