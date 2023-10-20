from pathlib import Path
import os
from configurations import Configuration, values
from dotenv import load_dotenv
import dj_database_url

load_dotenv()


class Dev(Configuration):

    BASE_DIR = Path(__file__).resolve().parent.parent

    SECRET_KEY = values.SecretValue()

    DEBUG = values.BooleanValue(default=True)

    ALLOWED_HOSTS = values.ListValue(default=['localhost', '127.0.0.1'])
    INTERNAL_IPS = values.ListValue(default=['localhost', '127.0.0.1'])

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # external modules
        'rest_framework',
        'debug_toolbar',
        'rest_framework_swagger',
        'drf_yasg',

        # app modules
        'converter.apps.ConverterConfig',
        # 'converter',

        # health check
        'health_check',
        'health_check.db',
        'health_check.cache',
        'health_check.storage',
        'health_check.contrib.migrations',
        'health_check.contrib.psutil'
    ]

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'currencyconverter.urls'

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

    WSGI_APPLICATION = 'currencyconverter.wsgi.application'

    DATABASE_URL = values.Value('sqlite:///{}'.format(BASE_DIR / 'db.sqlite3'))

    DATABASES = {
        'default': dj_database_url.parse(str(DATABASE_URL))
    }

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
        }
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

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_TZ = True

    STATIC_URL = 'static/'

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
