# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import os
from django.conf import settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}
