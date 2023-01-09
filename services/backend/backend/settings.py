from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config("SECRET", default="insecure-django-secrets")

DEBUG = config("DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = ['*'] if DEBUG else config(
    "ALLOWED_HOST",
    cast=lambda hosts_str: [host_ip.strip() for host_ip in hosts_str.split(",")]
)

TIME_ZONE = config("TIME_ZONE", default="Asia/Tehran")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Installed apps :
    'drf_yasg',
    'rest_framework',
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

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'backend.wsgi.application'

CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*'] if DEBUG else config(
    "ALLOWED_HOST",
    cast=lambda hosts_str: ['http://' + host_ip.strip() for host_ip in hosts_str.split(",")]
)

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = ALLOWED_HOSTS.copy()

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'PASSWORD': config("DB_PASSWORD"),
            'HOST': config("DB_HOST"),
            'USER': config("DB_USER"),
            'NAME': config("DB_NAME"),
            'PORT': config("DB_PORT"),
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
MEDIA_URL = "media/"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [BASE_DIR / "staticfiles"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
