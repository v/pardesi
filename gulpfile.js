var gulp = require('gulp');
var gutil = require('gulp-util');
var browserify = require('gulp-browserify');
var concat = require('gulp-concat');

var compile_path = 'assets/compiled';
var bower_path = 'assets/bower';

var paths = {
    vendor_scripts: [
        bower_path + '/modernizr/modernizr.js',
        bower_path + '/jquery/dist/jquery.js',
        bower_path + '/sizzle/dist/sizzle.js',
        bower_path + '/foundation/js/foundation.js',
    ],
    vendor_css: [
        bower_path + '/foundation/css/normalize.css',
        bower_path + '/foundation/css/foundation.min.css',
    ],
};

gulp.task('app_scripts', function() {
    gulp.src('assets/scripts/src/main.js')
        .pipe(browserify({
            insertGlobals: true,
            debug: true,
        }))
        .pipe(concat('app.js'))
        .pipe(gulp.dest(compile_path))
});

gulp.task('vendor_scripts', function() {
    gulp.src(paths.vendor_scripts)
        .pipe(browserify({
            insertGlobals: true,
            debug: true,
        }))
        .pipe(concat('vendor.js'))
        .pipe(gulp.dest(compile_path))
});


gulp.task('vendor_css', function() {
    gulp.src(paths.vendor_css)
        .pipe(concat('vendor.css'))
        .pipe(gulp.dest(compile_path))
});

gulp.task('watch', function() {
    gulp.watch('scripts/**/*.js', ['default']);
});

gulp.task('default', ['app_scripts', 'vendor_scripts', 'vendor_css']);
