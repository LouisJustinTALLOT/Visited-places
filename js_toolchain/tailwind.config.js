module.exports = {
  purge: {
    enabled: true,
    content: ['../**/templates/**/*.html'],
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {
      fontWeight: ['hover', 'focus'],
      display: ['hover', 'focus'],
      visibility: ['hover', 'focus'],
    },
  },
  plugins: [],
}
