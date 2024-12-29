module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        primary: '#4caf50',
        secondary: '#f39c12',
        background: '#1e1e2f',
        accent: '#282840',
        textPrimary: '#ffffff',
        textSecondary: '#dddddd',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      boxShadow: {
        soft: '0px 4px 12px rgba(0, 0, 0, 0.1)',
        strong: '0px 6px 20px rgba(0, 0, 0, 0.2)',
      },
    },
  },
  plugins: [require('@tailwindcss/forms')],
};
