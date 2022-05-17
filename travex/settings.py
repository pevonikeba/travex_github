"""
Django settings for travex project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get('DEBUG')) == "1"

ALLOWED_HOSTS = ['go.attaplace.info', '3.67.98.251', '127.0.0.1', '159.223.216.170']


_VERSION = {
    "WORKING": False,  # set True while working on new version of project. When True apps (mobile, ...) not work
    "WHITELIST": ['1.0.0', ],
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    ############################
    'django_filters',
    'django_countries',
    'django_extensions',
    'mptt',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    # 'rest_framework_swagger',
    'rest_framework_simplejwt',
    'oauth2_provider',
    # 'oauth2_provider',
    # 'oauth2_provider.models.Application',
    'dj_rest_auth',
    'django_otp',
    'django_otp.plugins.otp_totp',
    # 'oauth2_provider',
    # 'social_django',
    # 'drf_social_oauth2',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.apple',
    "colorfield",
    # 'location_field.apps.DefaultConfig',
    # 'django.contrib.gis',
    # "leaflet",
    'place',
    'achievement',
]
AUTH_USER_MODEL = 'place.CustomUser'

AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.google.GooglePlusAuth',
    # 'rest_framework_social_oauth2.backends.DjangoOAuth2',
    # 'django.contrib.auth.backends.ModelBackend',
    # # Google OAuth2
    # 'social_core.backends.google.GoogleOAuth2',
    # # drf-social-oauth2
    # 'drf_social_oauth2.backends.DjangoOAuth2',
    # # Django
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)


SOCIALACCOUNT_PROVIDERS = {
    "apple": {
        "APP": {
            # Your service identifier.
            "client_id": os.environ.get("APPLE_CLIENT_ID"),
            # The KEY ID (visible in the "View Key Details" page).
            "secret": os.environ.get("APPLE_SECRET"),
            "key": os.environ.get("APPLE_KEY"),
            "certificate_key": os.environ.get("APPLE_CERTIFICATE_KEY").replace(r'\n', '\n'),
        }
    },
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SITE_ID = 2
REST_USE_JWT = True    # this is for djangorestframework-jwt

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '577310907448-790k81c4127oamun4d753gbuot20itva.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

# APPEND_SLASH = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'place.middleware.format_middleware.FormatMiddleware',
    'achievement.middleware.achievement_middleware.CheckAchievementMiddleware',
    # 'place.middleware.log.APILogMiddleware',
]

ROOT_URLCONF = 'travex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'travex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'travex_db',
        'USER': 'travex_user',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# LEAFLET_CONFIG = {
#     # "SPATIAL_EXTENT": (5.0, 44.0, 7.5, 46),
#     "DEFAULT_CENTER": (13.3888599, 52.5170365), #set your corordinate
#     "DEFAULT_ZOOM": 16,
#     "MIN_ZOOM": 3,
#     "MAX_ZOOM": 20,
#     "DEFAULT_PRECISION": 6,
#     "SCALE": "both",
#     "ATTRIBUTION_PREFIX": "powered by me",
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# LANGUAGES = (
#     ('en', _('English')),
#     ('ru', _('Russian')),
# )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {

    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 100,
    'EXCEPTION_HANDLER': 'place.utils.utils.custom_exception_handler',

    'DEFAULT_RENDERER_CLASSES': (
        # 'rest_framework.renderers.JSONRenderer',
        'place.renderer.custom_renderer.CustomRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        # 'rest_framework.parsers.FormParser',
        # 'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
        # 'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=360),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=7),
}
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'travel.guid2022@gmail.com'
EMAIL_HOST_PASSWORD = 'Helloworld98!'
EMAIL_PORT = 587
# MAILER_LIST = ['arslion@@yandex.ru']
# ADMINS = [('Arslion', 'arslion@yandex.ru')]
# DEFAULT_FROM_EMAIL = 'travel.guid2022@gmail.com'

# DOMAIN = '127.0.0.1:8000'
# DOMAIN = '159.223.216.170'
DOMAIN = 'go.attaplace.info'
SITE_NAME = 'Attaplace'

DJOSER = {
    "LOGIN_FIELD": "email",
    # "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    'ACTIVATION_URL': 'auth/user/activate/{uid}/{token}',
    "SEND_ACTIVATION_EMAIL": True,
    "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    # "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
    #     "http://127.0.0.1:8000/admin/place/customuser/",
    #     # "your redirect url",
    # ],
    "SERIALIZERS": {
        "user_create": "place.serializers.serializers.CustomUserSerializer",  # custom serializer
        "user": "place.serializers.serializers.CustomUserSerializer",
        "current_user": "place.serializers.serializers.CustomUserSerializer",
        "user_delete": "place.serializers.serializers.CustomUserSerializer",
    },
    'EMAIL': {
        'activation': 'djoser.email.ActivationEmail',
    },
}

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# SOCIAL_AUTH_JSONFIELD_ENABLED = True
#
#
# SOCIAL_AUTH_GITHUB_KEY = '4b67f6944142c331f5ea'
# SOCIAL_AUTH_GITHUB_SECRET = 'aae4618e66c98dcf25e3e51cc1f447eb0e4b3ebf'

# GDAL_LIBRARY_PATH = '/opt/homebrew/opt/gdal/lib/libgdal.dylib'
# GEOS_LIBRARY_PATH = '/opt/homebrew/opt/geos/lib/libgeos_c.dylib'
# #
# LOCATION_FIELD = {
#     'provider.openstreetmap.max_zoom': 18,
# }

MPTT_ADMIN_LEVEL_INDENT = 20

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#     'verbose': {
#     'format': '%(levelname)s [%(asctime)s] %(module)s %(message)s'
#     },
#     },
#     'handlers': {
#         # 'console': {
#         # 'level': 'DEBUG',
#         # 'class': 'logging.StreamHandler',
#         # 'formatter': 'simple'
#         # },
#         # 'file': {
#         # 'class': 'logging.handlers.RotatingFileHandler',
#         # 'formatter': 'verbose',
#         # 'filename': '/var/www/logs/ibiddjango.log',
#         # 'maxBytes': 1024000,
#         # 'backupCount': 3,
#         # },
#         'mail_admins': {
#         'level': 'ERROR',
#         'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django': {
#         'handlers': ['mail_admins'],
#         'propagate': True,
#         'level': 'DEBUG',
#         },
#     }
# }
