from pathlib import Path
from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()

SECRET_KEY = env.str('SECRET_KEY', '123Secret123')
DEBUG = env.bool('DEBUG', False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', ['127.0.0.1', 'localhost', '0.0.0.0'])
CSRF_COOKIE_DOMAIN = env.list('CSRF_COOKIE_DOMAIN', 'http://127.0.0.1:1337')
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', 'http://127.0.0.1:1337')

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'



DATABASES = {
    'default': env.dj_db_url('DATABASE_URL', 'postgres://...'),
}


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


LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
