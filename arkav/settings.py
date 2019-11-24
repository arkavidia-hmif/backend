'''
Django settings for arkav project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
'''
from corsheaders.defaults import default_headers
from datetime import timedelta
from distutils.util import strtobool
import dj_database_url
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '(uc8i&7l81878%b6-x5%$n=0fvfb=rxfkw_+l!od^u#q#=+5_3')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG') != 'False'

ALLOWED_HOSTS = [
    'dashboard.arkavidia.id',
    'api.arkavidia.id',
    'arkavidia.id',
    'localhost',
] if not DEBUG else ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'nested_admin',
    'storages',
    'corsheaders',

    'arkav.arkavauth',
    'arkav.uploader',
    'arkav.announcement',
    'arkav.competition',
    'arkav.preevent',
    # 'arkav.quiz',
    'arkav.mainevent',
]
AUTH_USER_MODEL = 'arkavauth.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'arkav.urls'

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

WSGI_APPLICATION = 'arkav.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')),
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = os.getenv('TIME_ZONE', 'Asia/Jakarta')
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, 'static/'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'aoutbdiawdnamoidaoob')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '86vr6ab7dya7gn8oappe3e03aonta8m9u10papmhuzg')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', 'arkavidia')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'sgp1')
AWS_S3_ENDPOINT_URL = 'https://{}.{}.digitaloceanspaces.com'.format(AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME)
AWS_S3_CUSTOM_DOMAIN = '{}.{}.digitaloceanspaces.com'.format(AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read-write'
AWS_LOCATION = 'uploaded-files'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Rest Framework Settings
REST_FRAMEWORK = {
    'CHARSET': 'utf-8',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_RENDERER_CLASSES': [
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'rest_framework.parsers.FormParser',
    ],
    'EXCEPTION_HANDLER': 'arkav.utils.exceptions.exception_handler_with_code',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'email',
    'USER_ID_CLAIM': 'email',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Email settings
EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', None)
EMAIL_PORT = os.getenv('EMAIL_PORT', '587')
EMAIL_USE_TLS = strtobool(os.getenv('EMAIL_USE_TLS', 'True'))

DEFAULT_FROM_EMAIL = 'Arkavidia 6.0 <noreply@arkavidia.id>'
COMPETITION_REGISTRATION_OPEN = strtobool(os.getenv('COMPETITION_REGISTRATION_OPEN', 'False'))
CODING_CLASS_REGISTRATION_OPEN = strtobool(os.getenv('CODING_CLASS_REGISTRATION_OPEN', 'False'))

# Security-related settings - only enable if HTTPS is enabled
CSRF_COOKIE_SECURE = strtobool(os.getenv('CSRF_COOKIE_SECURE', 'False'))
SESSION_COOKIE_SECURE = strtobool(os.getenv('SESSION_COOKIE_SECURE', 'False'))

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
}
REDOC_SETTINGS = {
    'PATH_IN_MIDDLE': True,
}

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = DEBUG
CORS_ORIGIN_WHITELIST = [
    'https://arkavidia.id',
    'https://www.arkavidia.id',
    'https://preview.arkavidia.id',
]
CORS_ALLOW_HEADERS = list(default_headers) + [
    'set-cookie',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'fileError': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': './arkav-error.log' if DEBUG else '/arkavlog/error.log',
            'formatter': 'simple',
        },
        'fileInfo': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': './arkav-info.log' if DEBUG else '/arkavlog/info.log',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'arkav': {
            'handlers': ['fileInfo', 'fileError'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['fileInfo', 'fileError'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
