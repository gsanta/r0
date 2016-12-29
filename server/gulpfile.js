var gulp = require('gulp');
var ts = require('gulp-typescript');
var merge = require('merge2');
var del = require('del');

var tsProject = ts.createProject({
    declaration: true
});

gulp.task('clean', function () {
  return del([
    'build'
  ]);
});

gulp.task('scripts', function() {
    var tsResult = gulp.src("src/**/*.ts")
        .pipe(tsProject());

    return merge([ // Merge the two output streams, so this task is finished when the IO of both operations is done.
        tsResult.dts.pipe(gulp.dest('build/definitions')),
        tsResult.js.pipe(gulp.dest('build/js'))
    ]);
});

gulp.task('watch', ['scripts'], function() {
    gulp.watch('src/**/*.ts', ['scripts']);
});
