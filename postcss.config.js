// module.exports = {
//     plugins: [
//       require('tailwindcss'),
//       require('autoprefixer'),
//     ],
//   }
  /* webpack.config.js */
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const isProd = process.env.NODE_ENV === 'production';

module.exports = {
  // ... other options
  module: {
    rules: [
      // ... other rules
      {
        test: /\.css$/i,
        use: [
          isProd ? MiniCssExtractPlugin.loader : 'style-loader',
          'css-loader',
          'postcss-loader',
        ],
      },
    ],
  },
  plugins: [
    // ... other plugins
    isProd && new MiniCssExtractPlugin({
      filename: 'css/app.css',
    }),
  ].filter(Boolean),
};
