const webpackConf = require('./webpack.config.js');
delete webpackConf.entry

module.exports = function(config) {
    config.set({
        basePath: './resources/tests/',
        frameworks: ['jasmine'],
        files: [
            { pattern: 'components/*.spec.js', watched: false }
        ],
        exclude: [],

        webpack: webpackConf,
        webpackMiddleware: {
            noInfo: true,
            stats: 'errors-only'
        },
        preprocessors: {
            'app.js': ['webpack'],
            'components/*.spec.js': ['webpack']
        },

        reporters: ['progress'],
        port: 9876,
        colors: true,
        logLevel: config.LOG_INFO,
        autoWatch: true,
        browsers: ['ChromeHeadless'],
        singleRun: false,
        concurrency: Infinity
    })
}