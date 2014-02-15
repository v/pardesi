var gulp = require('gulp');
var gutil = require('gulp-util');
var browserify = require('gulp-browserify');
var concat = require('gulp-concat');

gulp.task('default', function() {
    gulp.src('scripts/src/main.js')
        .pipe(browserify({
            insertGlobals: true,
            debug: true,
        }))
        .pipe(concat('bundle.js'))
        .pipe(gulp.dest('scripts/compiled'))
});


gulp.task('watch', function() {
    gulp.watch('scripts/**/*.js', ['default']);
});
