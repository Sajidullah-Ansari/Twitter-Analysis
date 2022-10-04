"""
Django settings for TweetAnalysis project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import date, datetime
from pytz import timezone
tz = timezone('MST')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-+!@@f26(622oh)^bpz=g8wajdj33fj4sq=1256oqj#o1@%qja'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'twitter.apps.TwitterConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TweetAnalysis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'TweetAnalysis.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = 'static'
# STATICFILES_DIR = (os.path.join(BASE_DIR, 'static'))
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Twitter App access keys for @user

# Consume:
TWITTER_CONSUMER_KEY = 'F3gfb2aWx2w1cvIHZc8wKkV46'
TWITTER_CONSUMER_SECRET = 'Oo8cXMbgLOpi1ILQooEZbhVHxz0AhWyt4YZ2qRacanhVgx33ZK'

# Access:
TWITTER_ACCESS_TOKEN = '723542359208665088-cKnIyfXaf9qykEuAZW08HX8yeLohTUE'
TWITTER_ACCESS_SECRET = 'HdwAWoInJxdutcLevfhfPZZQ3Q0YQWoMWgegQ9xYaYV06'

# Spotify access keys
SPOTIFY_CLIENT_ID = '0c50dfea2fde470db10062a1f59c197a'
SPOTIFY_CLIENT_SECRET_KEY = '659079c7bfef407cbf839acf3764a46f'

# TMDB access keys
TMDB_API_KEY = 'f45455dbf3bd1e1380acb63db68aeb9c'
TMDB_LANGUAGE = 'en'

# Number of movies,songs and tweets
d = datetime.now(tz)
DATE_SINCE = str(d.date())
NUMBER_OF_MOVIES = 5
NUMBER_OF_MOVIES_TWEETS = 5
NUMBER_OF_SONGS = 5
NUMBER_OF_SONGS_TWEETS = 5

# Variables for PUB-SUB
PROJECT_ID = "certain-torus-307806"
TOPIC_ID = "cc_project2"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "cloudcomputing39@gmail.com"
EMAIL_HOST_PASSWORD = "cloud@1234"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER