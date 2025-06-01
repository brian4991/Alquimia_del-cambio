/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0fdf4',
          100: '#dcfce7',
          200: '#bbf7d0',
          300: '#86efac',
          400: '#4ade80',
          500: '#22c55e',
          600: '#16a34a',
          700: '#15803d',
          800: '#166534',
          900: '#14532d',
        },
        secondary: {
          50: '#fefce8',
          100: '#fef9c3',
          200: '#fef08a',
          300: '#fde047',
          400: '#facc15',
          500: '#eab308',
          600: '#ca8a04',
          700: '#a16207',
          800: '#854d0e',
          900: '#713f12',
        },
        sage: {
          50: '#f6f7f6',
          100: '#e3e8e3',
          200: '#c7d2c7',
          300: '#a3b3a3',
          400: '#7a8f7a',
          500: '#5c735c',
          600: '#475a47',
          700: '#3a493a',
          800: '#303d30',
          900: '#293329',
        },
        lavender: {
          50: '#f8f7ff',
          100: '#f1edff',
          200: '#e5ddff',
          300: '#d2bfff',
          400: '#b899ff',
          500: '#9d72ff',
          600: '#8b4dff',
          700: '#7c3aed',
          800: '#6b21a8',
          900: '#581c87',
        },
        cream: {
          50: '#fffef7',
          100: '#fffbeb',
          200: '#fef3c7',
          300: '#fde68a',
          400: '#fcd34d',
          500: '#f59e0b',
          600: '#d97706',
          700: '#b45309',
          800: '#92400e',
          900: '#78350f',
        }
      },
      fontFamily: {
        'serif': ['Crimson Text', 'serif'],
        'sans': ['Inter', 'system-ui', 'sans-serif'],
      },
      backgroundImage: {
        'gradient-serene': 'linear-gradient(135deg, #f0fdf4 0%, #fefce8 100%)',
        'gradient-calm': 'linear-gradient(135deg, #f8f7ff 0%, #f6f7f6 100%)',
        'gradient-nature': 'linear-gradient(135deg, #dcfce7 0%, #e3e8e3 100%)',
      }
    },
  },
  plugins: [],
} 