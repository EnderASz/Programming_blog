# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = []

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets")
]
STATIC_URL = '/assets/'
STATIC_ROOT = ""
