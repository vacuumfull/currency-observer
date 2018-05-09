import os
from exchanger.settings import * # NOQA

BASE_DIR = os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), os.pardir)

DEBUG = False

ENVIRONMENT = 'production'

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')