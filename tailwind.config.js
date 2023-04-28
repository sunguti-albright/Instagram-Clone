// /** @type {import('tailwindcss').Config} */
// module.exports = {
//   content: [
//     './templates/**/*.html',
//   ],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// }

module.exports = {
  purge: [
    './**/*.html',
    './**/*.js',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
