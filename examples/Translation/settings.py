"""
Django settings for DjAI project

Generated by 'django-admin startproject' using Django

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings
"""


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '???'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1', '0.0.0.0', 'localhost',
    'apps.aitomatic.com',
    '.elasticbeanstalk.com',
    '.ngrok.io'
]


# Application definition
INSTALLED_APPS = [
    # Django Admin Themes: add to INSTALLED_APPS before django.contrib.admin
    'jazzmin',

    # Django Default/Main Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django Extensions: Extra Management Commands
    'django_extensions',

    # Django REST Framework UI Templates
    'rest_framework',

    # CORS Headers
    'corsheaders',

    # this app's Django modules
    # ...
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # CorsMiddleware should be placed as high as possible,
    # especially before any middleware that can generate responses
    # such as Django’s CommonMiddleware or Whitenoise’s WhiteNoiseMiddleware.
    # If it is not before, it will not be able to add the CORS headers
    # to these responses.
    # Also if you are using CORS_REPLACE_HTTPS_REFERER it should be placed
    # before Django’s CsrfViewMiddleware.
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    dict(
        BACKEND='django.template.backends.django.DjangoTemplates',
        DIRS=[],
        APP_DIRS=True,
        OPTIONS=dict(
                    context_processors=[
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ]
                )
    )
]


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    dict(NAME='django.contrib.auth.password_validation.'
              'UserAttributeSimilarityValidator'),
    dict(NAME='django.contrib.auth.password_validation.'
              'MinimumLengthValidator'),
    dict(NAME='django.contrib.auth.password_validation.'
              'CommonPasswordValidator'),
    dict(NAME='django.contrib.auth.password_validation.'
              'NumericPasswordValidator')
]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files
STATIC_ROOT = '.staticfiles'
STATIC_URL = '/static/'   # must end with a slash


# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.fields.AutoField'


# Jazzmin Admin
JAZZMIN_SETTINGS = dict(
    # UI Customizer
    # Jazzmin has a built in UI configurator,
    # mimicked + enhanced from adminlte demo,
    # that allows you to customise parts of the interface interactively.
    # There will be an icon in the top right of the screen
    # that allows you to customise the interface.
    show_ui_builder=True,

    # title of the window
    site_title='H1st AI App',

    # Title on the brand, and the login screen (19 chars max)
    site_header='H1st AI App',

    # Welcome text on the login screen
    welcome_sign='Welcome to H1st AI App',

    # Copyright on the footer
    copyright='H1st AI App'
)


# REST Framework
REST_FRAMEWORK = dict(
    DEFAULT_AUTHENTICATION_CLASSES=[
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ],

    DEFAULT_PERMISSION_CLASSES=[
        'rest_framework.permissions.IsAuthenticated',
    ],

    DEFAULT_FILTER_BACKENDS=[
        'rest_framework.filters.OrderingFilter',
        'rest_framework_filters.backends.ComplexFilterBackend',
        'rest_framework_filters.backends.RestFrameworkFilterBackend'
    ],

    DEFAULT_PAGINATION_CLASS='rest_framework.pagination.LimitOffsetPagination',
    PAGE_SIZE=10,

    DEFAULT_RENDERER_CLASSES=[
        # 'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.CoreJSONRenderer',
        'rest_framework.renderers.JSONRenderer'
    ]
)


# CORS Headers
CORS_ALLOW_ALL_ORIGINS = CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = []
