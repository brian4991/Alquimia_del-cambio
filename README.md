# 🌱 Alquimia del Cambio - Programa de Transformación Personal

Una aplicación web moderna para programas de psicología y desarrollo personal con módulos, temas y ejercicios interactivos.

## ✨ Características Principales

- **Estructura Modular**: Organización en módulos → temas → ejercicios
- **Audio de Introducción**: Cada módulo incluye audio introductorio
- **Progreso Bloqueado**: Los temas se desbloquean secuencialmente
- **Interfaz Moderna**: Diseño sereno con colores naturales y efectos de transparencia
- **Responsive**: Funciona perfectamente en dispositivos móviles y escritorio

## 🏗️ Arquitectura

### Backend (FastAPI + SQLAlchemy)
```
backend/
├── main.py              # Aplicación principal con API
├── requirements.txt     # Dependencias Python
└── app.db              # Base de datos SQLite (auto-generada)
```

### Frontend (React + Vite + TailwindCSS)
```
frontend/
├── src/
│   ├── components/
│   │   ├── Login.jsx       # Autenticación
│   │   ├── Layout.jsx      # Layout principal con navegación
│   │   ├── Dashboard.jsx   # Vista principal de módulos
│   │   ├── ModuleView.jsx  # Vista detallada de un módulo
│   │   ├── ThemeView.jsx   # Vista de tema con ejercicios
│   │   └── StepView.jsx    # Vista legacy (compatibilidad)
│   ├── services/
│   │   └── api.js          # Funciones API
│   └── App.jsx            # Enrutamiento principal
├── public/
│   └── audio/             # 🎵 AQUÍ VAN LOS ARCHIVOS DE AUDIO
└── package.json
```

## 🎵 Configuración de Audio

### Ubicación de Archivos
Los archivos de audio deben colocarse en: `frontend/public/audio/`

### Nomenclatura
- **Módulo 1**: `modulo-1-intro.mp3`
- **Módulo 2**: `modulo-2-intro.mp3`
- **Módulo N**: `modulo-N-intro.mp3`

### Formatos Soportados
- **Recomendado**: `.mp3` (mejor compatibilidad)
- **Alternativos**: `.wav`, `.ogg`, `.m4a`

### Ejemplo de Estructura
```
frontend/public/audio/
├── modulo-1-intro.mp3    # Audio para "El Mapa de tus Emociones"
├── modulo-2-intro.mp3    # Audio para "Celebra tu Ser"
├── modulo-3-intro.mp3    # Audio para "El Arte de Amar"
├── modulo-4-intro.mp3    # Audio para "De la expectativa a la realidad"
└── modulo-5-intro.mp3    # Audio para "Libertad en Acción"
```

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.8+
- Node.js 16+
- npm o yarn

### 1. Configurar Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 2. Configurar Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3. Acceder a la Aplicación
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **Documentación API**: http://localhost:8000/docs

## 📚 Estructura del Programa

### Módulo 1: El Mapa de tus Emociones
**Objetivo**: Gestionar el mundo emocional y expresar sentimientos con consciencia
- **Tema 1**: Explorando mi historia emocional (3 ejercicios)
- **Tema 2**: Autoconocimiento emocional profundo (3 ejercicios)  
- **Tema 3**: Gestionando y expresando emociones (3 ejercicios)

### Flujo de Usuario
1. **Login/Registro** → Autenticación segura
2. **Dashboard** → Vista general de módulos disponibles
3. **Módulo** → Audio de introducción + lista de temas
4. **Tema** → Contenido educativo + ejercicios prácticos
5. **Ejercicios** → Respuestas libres guardadas automáticamente
6. **Progreso** → Desbloqueo secuencial de contenido

## 🎨 Diseño y UI

### Paleta de Colores
- **Primary**: Verdes naturales (`#22c55e` - `#14532d`)
- **Secondary**: Amarillos cálidos (`#eab308` - `#713f12`)
- **Sage**: Tonos tierra (`#5c735c` - `#293329`)
- **Lavender**: Morados suaves (`#9d72ff` - `#581c87`)
- **Cream**: Cremas acogedores (`#f59e0b` - `#78350f`)

### Elementos Visuales
- **Gradientes suaves**: `bg-gradient-serene`, `bg-gradient-calm`, `bg-gradient-nature`
- **Transparencias**: `bg-white/80`, `backdrop-blur-sm`
- **Iconos naturales**: 🌱, 🍃, 🌸, 🦋, ✨
- **Tipografía**: Crimson Text (serif) + Inter (sans-serif)

## 📡 API Endpoints

### Autenticación
- `POST /register` - Registro de usuario
- `POST /login` - Inicio de sesión
- `GET /profile` - Perfil del usuario

### Módulos y Contenido
- `GET /modules` - Lista de módulos
- `GET /modules/{id}/themes` - Temas de un módulo
- `GET /themes/{id}/exercises` - Ejercicios de un tema

### Progreso y Respuestas
- `POST /submit-response` - Guardar respuesta a ejercicio
- `POST /complete-theme/{id}` - Marcar tema como completado

### Legacy (Compatibilidad)
- `GET /steps` - Lista módulos (formato antiguo)
- `GET /steps/{id}/exercises` - Ejercicios (formato antiguo)

## 🔧 Configuración de Base de Datos

La base de datos se crea automáticamente al iniciar el backend con el contenido completo del **Módulo 1**:

### Modelos Principales
- **User**: Usuarios y autenticación
- **Module**: Módulos del programa
- **Theme**: Temas dentro de cada módulo  
- **Exercise**: Ejercicios dentro de cada tema
- **UserProgress**: Progreso del usuario
- **UserResponse**: Respuestas a ejercicios

## 🎯 Próximos Pasos

Para expandir la aplicación, puedes:

1. **Agregar más módulos** editando la función `init_database()` en `backend/main.py`
2. **Personalizar audio** colocando archivos MP3 en `frontend/public/audio/`
3. **Modificar diseño** editando las clases Tailwind en los componentes
4. **Añadir funciones** como estadísticas, certificados, etc.

## 📞 Soporte

Para obtener ayuda o reportar problemas:
- Revisa los logs del backend y frontend
- Verifica que los archivos de audio estén en la ubicación correcta
- Confirma que los puertos 8000 y 5173 estén disponibles

---

### 🌟 ¡Tu transformación personal comienza aquí!

*"La transformación personal comienza con la observación amorosa de uno mismo."* 