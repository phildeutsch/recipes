"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import configparser
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+cj-_c)q^6#&a)$ezl+6jo0uxz_htsqp88l-7=_$zm(h*jd268'

# SECURITY WARNING: don't run with debug turned on in production!
if 'ON_HEROKU' in os.environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False

if ON_HEROKU:
    DEBUG = False

    # DB settings
    DB_NAME = os.environ['DB_NAME']
    DB_USERNAME = os.environ['DB_USERNAME']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']

    # AWS settings
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
else:
    DEBUG = True

    # DB settings
    DB = 'DATABASE_LOCAL'
    # DB = 'DATABASE_PROD'
    config = configparser.ConfigParser()
    config.read('app/config.ini')
    DB_NAME = config[DB]['DB_NAME']
    DB_USERNAME = config[DB]['DB_USERNAME']
    DB_PASSWORD = config[DB]['DB_PASSWORD']
    DB_HOST = config[DB]['DB_HOST']
    DB_PORT = config[DB]['DB_PORT']

    # AWS settings
    AWS_ACCESS_KEY_ID = config['AWS']['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = config['AWS']['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = config['AWS']['AWS_STORAGE_BUCKET_NAME']

# Set who can connect to DB
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'rezeptothek.herokuapp.com']


# Application definition
INSTALLED_APPS = [
    'app',
    'recipes',
    'django_registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Redirect users after login and logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# AWS settings
AWS_DEFAULT_ACL = None
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com'

# Django Storages settings for S3
STATICFILES_STORAGE = 'app.storage_backends.StaticStorage'
DEFAULT_FILE_STORAGE = 'app.storage_backends.PublicMediaStorage'

# static settings
STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media settings
MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
