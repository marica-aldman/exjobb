from .base import *
from decouple import config
import os

DEBUG = False
ALLOWED_HOSTS = ['84.216.113.116']
#SECRET_KEY = config('SECRET_KEY_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}

STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY_VAR')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY_VAR')
STRIPE_ENDPOINT_SECRET = config('STRIPE_ENDPOINT_SECRET_KEY')


# Activate Django-Heroku.
django_heroku.settings(locals())
