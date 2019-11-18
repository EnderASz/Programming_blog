# Static files (HTML Templates, CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

include(
    'base.py',
)

# CSS, JavaScript, Images
STATICFILES_FINDERS = []

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets")
]
STATIC_URL = '/assets/'
STATIC_ROOT = ""

#HTML TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "assets\\html"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
