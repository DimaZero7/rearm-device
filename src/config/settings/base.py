import os
from pathlib import Path
import toml

BASE_DIR = Path(__file__).resolve().parent.parent.parent

if os.path.exists(BASE_DIR / 'config_local.toml'):
    _config_path = 'config_local.toml'
elif os.path.exists(BASE_DIR / 'config.toml'):
    _config_path = 'config.toml'
else:
    _config_path = 'default_config.toml'

with open(BASE_DIR / _config_path, 'r') as f:
    config = toml.load(f)

SECRET_KEY = config['base']['secret_key']

DEBUG = config['base']['debug']

ALLOWED_HOSTS = config['base']['allowed_hosts']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config["database"]["name"],
        "USER": config["database"]["user"],
        "PASSWORD": config["database"]["password"],
        "HOST": config["database"]["host"],
        "PORT": config["database"]["port"],
        "ATOMIC_REQUESTS": True,
    }
}

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
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'apps.basket.utils.get_basket_item',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGE_CODE = 'ru'
