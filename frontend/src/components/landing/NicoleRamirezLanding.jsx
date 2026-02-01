import React, { useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { 
  ArrowRight, 
  CheckCircle2, 
  XCircle,
  Moon,
  Brain,
  Compass,
  Battery,
  Users,
  User,
  Briefcase,
  Heart,
  Calendar,
  BookOpen,
  Headphones,
  ClipboardCheck,
  Sparkles,
  MessageCircle,
  Quote
} from 'lucide-react';

const BOOKING_URL = 'https://calendly.com/contacto-nicoleramirezpsicoach/24horas';
const CONTACT_EMAIL = 'contacto@nicoleramirezpsicoach.com';

// Badge component
const Badge = ({ children, className = "" }) => (
  <span className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-medium tracking-wide ${className}`}>
    {children}
  </span>
);

const NicoleRamirezLanding = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const symptoms = [
    { text: "Te cuesta dormir o tu mente no se apaga en la noche", icon: Moon },
    { text: "Sientes ansiedad, presión en el pecho o irritabilidad sin \"razón\"", icon: Brain },
    { text: "Te sientes perdida: no sabes qué decisión tomar (pareja, trabajo, rumbo)", icon: Compass },
    { text: "Te exiges demasiado y luego procrastinas o te culpas", icon: Battery },
    { text: "Te invade la soledad aunque tengas gente cerca", icon: Users },
    { text: "Sientes que perdiste identidad: \"ya no sé quién soy aquí\"", icon: User },
    { text: "Los temas administrativos en tu nuevo país, dinero o estabilidad te desregulan más de lo que quisieras", icon: Briefcase },
  ];

  const benefits = [
    "Regularte cuando el cuerpo se desborda (ansiedad/rumiación/insomnio)",
    "Recuperar claridad para tomar decisiones sin quedarte congelada",
    "Reconstruir autoestima y valor interno sin depender del entorno",
    "Mejorar relaciones y comunicación (límites, apego, vínculos sanos)",
    "Romper creencias de exigencia y culpa que te drenan",
    "Volver a accionar con consistencia, sin violencia interna"
  ];

  const programFeatures = [
    {
      title: "Sesiones 1:1 cada 2 semanas",
      desc: "60–90 min de terapia + coaching para avanzar con dirección",
      icon: Calendar,
      color: "bg-sage-50 text-sage-700"
    },
    {
      title: "Plataforma semanal",
      desc: "Ejercicios guiados para regularte, entenderte y sostener cambios reales",
      icon: BookOpen,
      color: "bg-taupe-50 text-taupe-700"
    },
    {
      title: "Guías y recursos",
      desc: "Audios, lecturas y prácticas para acompañarte entre sesiones",
      icon: Headphones,
      color: "bg-stone-100 text-stone-700"
    },
    {
      title: "Entrenamientos de regulación",
      desc: "Herramientas prácticas para bajar el ruido interno y recuperar calma",
      icon: Sparkles,
      color: "bg-orange-50 text-orange-700"
    },
    {
      title: "Evaluaciones personalizadas",
      desc: "Conoce tus patrones, necesidades emocionales y estilo de vínculo",
      icon: ClipboardCheck,
      color: "bg-sage-50 text-sage-700"
    }
  ];

  const forYou = [
    "Eres migrante o hija de padres migrantes y en momentos de cambio vuelves a sentirte desregulada o perdida",
    "Quieres un proceso profundo, pero también práctico y estructurado",
    "Te importa sanar tu historia sin romantizar el dolor",
    "Estás lista para comprometerte con un proceso (no solo consumir contenido)"
  ];

  const notForYou = [
    "Buscas una solución rápida o promesas inmediatas",
    "No quieres hacer ejercicios entre sesiones",
    "Quieres que alguien decida por ti (aquí construimos tu autonomía)"
  ];

  const differentiators = [
    { title: "No es solo hablar", desc: "Es un camino con estructura" },
    { title: "No es teoría suelta", desc: "Es un método completo" },
    { title: "No estás sola", desc: "Hay acompañamiento real, con límites sanos y dirección" },
    { title: "Tu historia importa", desc: "Integramos lo emocional, lo relacional y lo práctico" }
  ];

  return (
    <div className="min-h-screen bg-[#F9F8F6] text-stone-900 selection:bg-sage-200 selection:text-sage-900 font-sans">
      
      <main>
        {/* HERO SECTION */}
        <section className="relative pt-16 pb-20 lg:pt-24 lg:pb-32 px-4 overflow-hidden">
          <div className="max-w-7xl mx-auto">
            <div className="grid lg:grid-cols-[1.1fr_0.9fr] gap-12 lg:gap-24 items-center">
              
              <div className="relative z-10 space-y-8">
                <Badge className="bg-sage-100 text-sage-800 border border-sage-200">
                  Psicóloga & Coach · Migración y Cambios de Vida
                </Badge>
                
                <h1 className="text-4xl sm:text-5xl lg:text-6xl font-playfair leading-[1.1] text-stone-900 tracking-tight">
                  De sobrevivir a <span className="italic text-sage-700">habitarte</span>
                </h1>
                
                <p className="text-lg sm:text-xl text-stone-600 font-light leading-relaxed max-w-xl font-sans">
                  Si eres migrante y por fuera "todo está bien", pero por dentro vuelven la ansiedad, la confusión o el vacío cuando atraviesas una ruptura, una infidelidad, una etapa de crianza lejos de tu red, inestabilidad laboral o problemas administrativos…
                </p>

                <p className="text-lg text-sage-700 font-medium italic">
                  Esto tiene sentido.
                </p>

                <div className="bg-white/70 backdrop-blur border border-sage-200 rounded-2xl p-6 max-w-lg">
                  <p className="text-stone-700 leading-relaxed">
                    <span className="font-semibold text-stone-900">No es que estés retrocediendo.</span><br/>
                    Es que tu sistema emocional se re-activa cuando la vida vuelve a exigirte sostén interno.
                  </p>
                </div>

                <div className="flex flex-col gap-3 pt-4">
                  <Button
                    asChild
                    size="lg"
                    className="bg-sage-600 text-white hover:bg-sage-700 hover:text-white rounded-full px-8 text-base h-14 transition-all duration-300 shadow-lg shadow-sage-900/10 w-fit"
                  >
                    <a href={BOOKING_URL} target="_blank" rel="noreferrer">
                      Agendar cita gratuita de descubrimiento
                      <ArrowRight className="ml-2 h-5 w-5" />
                    </a>
                  </Button>
                  <p className="text-sm text-stone-500 pl-1">
                    40 min para entender tu situación y ver si este proceso es para ti
                  </p>
                </div>
              </div>

              {/* Image */}
              <div className="relative mt-8 lg:mt-0">
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[120%] h-[120%] bg-gradient-radial from-sage-200/30 to-transparent blur-3xl -z-10"></div>
                <div className="relative aspect-[4/5] rounded-[2rem] overflow-hidden shadow-2xl shadow-stone-900/5">
                  <img
                    src="/mood/dsc1497.jpg"
                    alt="Nicole Ramírez"
                    className="w-full h-full object-cover transform hover:scale-105 transition-transform duration-700 ease-out"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-sage-900/20 to-transparent"></div>
                </div>
              </div>

            </div>
          </div>
        </section>

        {/* SECTION: ¿Esto te está pasando? */}
        <section className="py-24 bg-white border-t border-stone-100">
          <div className="max-w-5xl mx-auto px-4">
            <div className="max-w-3xl mx-auto text-center mb-16 space-y-4">
              <h2 className="text-3xl sm:text-4xl font-playfair text-stone-900">
                ¿Esto te está <span className="italic text-sage-700">pasando</span>?
              </h2>
              <p className="text-stone-600 text-lg">
                Aunque lleves solo meses o años en el país:
              </p>
            </div>

            <div className="grid sm:grid-cols-2 gap-4 max-w-4xl mx-auto">
              {symptoms.map((item, idx) => (
                <div key={idx} className="group flex items-start gap-4 p-5 rounded-2xl bg-[#F9F8F6] border border-stone-200 hover:border-sage-300 transition-colors duration-300">
                  <div className="w-10 h-10 bg-white rounded-xl flex items-center justify-center text-sage-600 shadow-sm border border-stone-200 flex-shrink-0">
                    <item.icon size={20} strokeWidth={1.5} />
                  </div>
                  <p className="text-stone-700 leading-relaxed text-sm pt-1.5">
                    {item.text}
                  </p>
                </div>
              ))}
            </div>

            {/* Important message */}
            <div className="mt-12 max-w-2xl mx-auto">
              <div className="bg-sage-50 border border-sage-200 rounded-2xl p-8 text-center">
                <p className="text-sage-800 text-lg font-medium">
                  Lo importante: lo que sientes no es exageración
                </p>
                <p className="text-sage-700 mt-2">
                  Es tu sistema nervioso pidiendo ayuda.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* SECTION: Mi enfoque */}
        <section id="enfoque" className="py-24 bg-[#dcd5cf] text-stone-900 overflow-hidden relative">
          <div className="absolute inset-0 opacity-[0.03]" style={{ backgroundImage: 'radial-gradient(#000000 1px, transparent 1px)', backgroundSize: '32px 32px' }}></div>
          
          <div className="max-w-6xl mx-auto px-4 relative z-10">
            <div className="grid lg:grid-cols-2 gap-16 items-center">
              <div className="relative order-2 lg:order-1">
                <div className="aspect-square rounded-full overflow-hidden border-8 border-white shadow-2xl shadow-stone-400/20 w-72 h-72 sm:w-96 sm:h-96 mx-auto">
                  <img src="/photo_nicole.jpg" alt="Nicole Ramírez" className="w-full h-full object-cover" />
                </div>
                <div className="absolute -bottom-4 left-1/2 -translate-x-1/2 bg-white px-6 py-3 rounded-full shadow-md border border-stone-200 whitespace-nowrap">
                  <span className="font-playfair italic text-sage-700 text-lg">Nicole Ramírez</span>
                </div>
              </div>

              <div className="order-1 lg:order-2 space-y-6">
                <Badge className="bg-stone-800 text-stone-100 border border-stone-600">Mi Enfoque</Badge>
                <h2 className="text-3xl sm:text-4xl font-playfair leading-tight">
                  Soy Nicole Ramírez,<br/>
                  <span className="text-stone-700 italic">psicóloga y coach.</span>
                </h2>
                <p className="text-stone-700 text-lg leading-relaxed">
                Acompaño a migrantes a transformar momentos de crisis en claridad, estabilidad emocional y acción sostenida.
                </p>
                <p className="text-stone-600 leading-relaxed">
                  Trabajo con un método propio: <span className="font-semibold text-stone-800">Cambio de Paradigma</span>, un proceso estructurado que integra psicología basada en evidencia y prácticas de integración como meditaciones guiadas y ejercicios de introspección.
                </p>
                
                <div className="bg-white/60 backdrop-blur border border-stone-300 rounded-2xl p-6 space-y-4">
                  <p className="text-stone-800 font-medium">
                    Aquí no vienes a "ser fuerte".
                  </p>
                  <p className="text-stone-700">
                    Vienes a aprender a sostenerte por dentro y a reconstruir tu dirección.
                  </p>
                  <p className="text-sage-700 font-medium italic text-lg">
                    Te enseño a transformar tu dolor en tu mejor aliado para el cambio.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* SECTION: Qué vas a lograr */}
        <section className="py-24 bg-[#F9F8F6]">
          <div className="max-w-4xl mx-auto px-4">
            <div className="text-center mb-16 space-y-4">
              <h2 className="text-3xl sm:text-4xl font-playfair text-stone-900">
                Qué vas a <span className="italic text-sage-700">lograr</span>
              </h2>
              <p className="text-stone-600 text-lg">
                En un proceso de acompañamiento trabajamos para que puedas:
              </p>
            </div>

            <div className="grid gap-4">
              {benefits.map((benefit, idx) => (
                <div key={idx} className="flex items-center gap-4 bg-white p-5 rounded-2xl border border-stone-200 hover:border-sage-300 hover:shadow-md transition-all duration-300">
                  <div className="w-8 h-8 bg-sage-100 rounded-full flex items-center justify-center text-sage-700 flex-shrink-0">
                    <CheckCircle2 size={18} strokeWidth={2} />
                  </div>
                  <p className="text-stone-700">{benefit}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* SECTION: Cómo funciona */}
        <section id="programa" className="py-24 bg-white">
          <div className="max-w-5xl mx-auto px-4">
            <div className="text-center mb-16 space-y-4">
              <Badge className="bg-sage-100 text-sage-800 border border-sage-200">
                Programa de 15 semanas
              </Badge>
              <h2 className="text-3xl sm:text-4xl font-playfair text-stone-900">
                Cómo <span className="italic text-sage-700">funciona</span>
              </h2>
              <p className="text-stone-600 text-lg max-w-2xl mx-auto">
                1:1 + plataforma: un sistema completo para sostener tu transformación
              </p>
            </div>

            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
              {programFeatures.map((feature, i) => (
                <div key={i} className="bg-[#F9F8F6] p-6 rounded-[2rem] border border-stone-200 hover:border-sage-300 hover:shadow-lg transition-all duration-300">
                  <div className={`p-4 rounded-2xl ${feature.color} w-fit mb-4`}>
                    <feature.icon size={24} strokeWidth={1.5} />
                  </div>
                  <h3 className="text-lg font-semibold text-stone-900 mb-2">{feature.title}</h3>
                  <p className="text-stone-600 text-sm leading-relaxed">{feature.desc}</p>
                </div>
              ))}
            </div>

            {/* Closing phrase */}
            <div className="mt-12 text-center">
              <p className="text-stone-600 italic text-lg max-w-2xl mx-auto">
                "Para que no solo entiendas lo que te pasa: para que puedas sostener cambios en tu día a día."
              </p>
            </div>

            {/* CTA */}
            <div className="mt-12 bg-sage-50 rounded-[2.5rem] p-8 sm:p-12 border border-sage-200 text-center max-w-2xl mx-auto">
              <Button
                asChild
                size="lg"
                className="bg-sage-600 text-white hover:bg-sage-700 rounded-full px-10 h-14 text-base shadow-lg shadow-sage-900/10"
              >
                <a href={BOOKING_URL} target="_blank" rel="noreferrer">
                  Agendar cita de descubrimiento
                  <ArrowRight className="ml-2 h-5 w-5" />
                </a>
              </Button>
              <p className="text-sm text-stone-600 mt-4">
                En la llamada vemos tu caso, tus objetivos y si este proceso encaja contigo.
              </p>
            </div>
          </div>
        </section>

        {/* SECTION: Para quién es (y para quién no) */}
        <section className="py-24 bg-[#F9F8F6]">
          <div className="max-w-5xl mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl sm:text-4xl font-playfair text-stone-900">
                Para quién es <span className="italic text-sage-700">(y para quién no)</span>
              </h2>
            </div>

            <div className="grid md:grid-cols-2 gap-8">
              {/* For you */}
              <div className="bg-white rounded-[2rem] p-8 border border-sage-200 shadow-sm">
                <h3 className="text-xl font-playfair text-stone-900 mb-6 flex items-center gap-3">
                  <span className="w-10 h-10 bg-sage-100 rounded-full flex items-center justify-center text-sage-700">
                    <CheckCircle2 size={20} />
                  </span>
                  Este espacio es para ti si:
                </h3>
                <ul className="space-y-4">
                  {forYou.map((item, idx) => (
                    <li key={idx} className="flex items-start gap-3">
                      <CheckCircle2 className="text-sage-600 mt-1 flex-shrink-0" size={18} />
                      <span className="text-stone-700 text-sm leading-relaxed">{item}</span>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Not for you */}
              <div className="bg-stone-100 rounded-[2rem] p-8 border border-stone-200">
                <h3 className="text-xl font-playfair text-stone-900 mb-6 flex items-center gap-3">
                  <span className="w-10 h-10 bg-stone-200 rounded-full flex items-center justify-center text-stone-600">
                    <XCircle size={20} />
                  </span>
                  No es para ti si:
                </h3>
                <ul className="space-y-4">
                  {notForYou.map((item, idx) => (
                    <li key={idx} className="flex items-start gap-3">
                      <XCircle className="text-stone-500 mt-1 flex-shrink-0" size={18} />
                      <span className="text-stone-600 text-sm leading-relaxed">{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </section>

        {/* SECTION: Lo que hace diferente este proceso */}
        <section className="py-24 bg-white">
          <div className="max-w-4xl mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl sm:text-4xl font-playfair text-stone-900">
                Lo que hace <span className="italic text-sage-700">diferente</span> este proceso
              </h2>
            </div>

            <div className="grid sm:grid-cols-2 gap-6">
              {differentiators.map((item, idx) => (
                <div key={idx} className="bg-[#F9F8F6] p-6 rounded-2xl border border-stone-200 hover:border-sage-300 transition-colors">
                  <h3 className="font-semibold text-stone-900 mb-2">{item.title}</h3>
                  <p className="text-stone-600 text-sm">{item.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* CTA FINAL */}
        <section className="py-24 bg-gradient-to-b from-[#F9F8F6] to-sage-100">
          <div className="max-w-3xl mx-auto px-4 text-center">
            <div className="space-y-8">
              <h2 className="text-3xl sm:text-4xl font-playfair text-stone-900 leading-relaxed">
                Si sientes que tu vida ya no te pertenece<br/>cuando llegan los cambios…
              </h2>
              <p className="text-xl text-sage-700 italic font-medium">
                Hay una forma de volver a ti.
              </p>
              
              <div className="pt-4 space-y-4">
                <Button
                  asChild
                  size="lg"
                  className="bg-sage-600 text-white hover:bg-sage-700 rounded-full px-10 h-16 text-lg shadow-xl shadow-sage-900/15"
                >
                  <a href={BOOKING_URL} target="_blank" rel="noreferrer">
                    Agendar cita gratuita de descubrimiento
                    <ArrowRight className="ml-2 h-5 w-5" />
                  </a>
                </Button>
                <p className="text-sm text-stone-500">
                  Cupos limitados para 1:1. La llamada es para conocerte y que evaluemos juntos si este proceso es para ti.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* FOOTER */}
        <footer className="bg-sage-600 text-white py-16 text-sm">
          <div className="max-w-6xl mx-auto px-4">
            <div className="grid md:grid-cols-2 gap-12 mb-12 border-b border-sage-500 pb-12">
              <div className="space-y-4">
                <img src="/Logo nr.png" alt="Logo" className="h-8 w-8 opacity-70 invert brightness-0" />
                <p className="max-w-xs leading-relaxed text-sage-100">
                  Psicóloga & coach especializada en migración y cambios de vida. Acompañamiento para  migrantes que buscan claridad, estabilidad emocional y acción sostenida.
                </p>
              </div>
              <div className="md:text-right space-y-2">
                <p className="text-sage-200 uppercase tracking-widest text-xs font-semibold">Contacto</p>
                <a href={`mailto:${CONTACT_EMAIL}`} className="block text-sage-100 hover:text-white transition-colors">{CONTACT_EMAIL}</a>
                <a href="#" className="block text-sage-100 hover:text-white transition-colors">Términos y Condiciones</a>
                <a href="#" className="block text-sage-100 hover:text-white transition-colors">Política de Privacidad</a>
              </div>
            </div>
            
            <div className="flex flex-col md:flex-row justify-between items-center gap-6 text-sage-200">
              <p className="text-xs max-w-2xl">
                <span className="font-bold block mb-1">Nota Ética Importante:</span>
                Este programa es un acompañamiento de desarrollo personal y bienestar. No sustituye tratamiento psiquiátrico ni es adecuado para crisis agudas, ideación suicida o patologías severas que requieran intervención clínica intensiva.
              </p>
              <p className="text-xs">
                © {new Date().getFullYear()} Nicole Ramírez.
              </p>
            </div>
          </div>
        </footer>

      </main>
    </div>
  );
};

export default NicoleRamirezLanding;
