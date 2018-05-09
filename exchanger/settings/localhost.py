import os
from exchanger.settings import * # NOQA

BASE_DIR = os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), os.pardir)

DEBUG = True

ENVIRONMENT = 'localhost'

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]