# compressor settings
include(
 'base.py',
 'static.py',
)

INSTALLED_APPS += ['compressor']

STATICFILES_FINDERS += [
    'compressor.finders.CompressorFinder',
]

COMPRESS_ROOT = 'assets/'

COMPRESS_PRECOMPILERS = [
    ('text/x-scss', 'django_libsass.SassCompiler'),
]
