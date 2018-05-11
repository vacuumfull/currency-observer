const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const isProd = process.env.NODE_ENV === 'production' || process.argv.indexOf('production') > -1;

const config = {
	entry: { 
		main: './resources/frontend/index.js' 
	},
	output: {
		path: path.resolve(__dirname, 'static/dist'),
		filename: isProd ? '[name].bundle.min.js' : '[name].bundle.js'
	},
	module: {
		rules: [
		{
			test: /\.vue$/,
			loader: 'vue-loader',
			options: {
				loaders: {
					js: 'babel-loader'
				},
			}
		},
		{
			test: /\.css$/,
			use: ExtractTextPlugin.extract({
				fallback: "style-loader",
				use: { 
					loader: 'css-loader', 
					options: { minimize: isProd ? true : false } 
				},
			})
		  },
		{
			test: /\.js$/,
			exclude: /node_modules/,
			use: {
				loader: 'babel-loader',
				options: { presets: ['es2015'] }
			}
		},
		{
			test: /\.scss$/,
			use: ExtractTextPlugin.extract({
				fallback: 'style-loader',
				use: { 
					loader: 'css-loader', 
					options: { minimize: isProd ? true : false } 
				},
			})
		},
		{
			test: /\.sass$/,
			use: [
			  'vue-style-loader',
			  'css-loader',
			  {
				loader: 'sass-loader',
				options: {
				  indentedSyntax: true
				}
			  }
			]
		},
		{
            test: /\.(woff|woff2|eot|ttf)$/,
            loader: 'file-loader',
            options: {
                name: '../fonts/[name].[ext]'
            }
        }]
	},
	plugins: [ 
		new ExtractTextPlugin({
			filename: isProd ? 'style.min.css' : 'style.css'
		}),
		new VueLoaderPlugin()
	]
};

if (isProd) {
    config.plugins.push(
        new CleanWebpackPlugin(['static/dist'])
    )
}

module.exports = config;