from split_settings.tools import include

from core.conf.environ import env

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'apps.healthz',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

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

ENVIRONMENT = env("ENVIRONMENT", default="develop")
SECRET_KEY = env("SECRET_KEY", default="insecure-secret-key")
DEBUG = env.bool("DEBUG", default=(ENVIRONMENT == "develop"))
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])


include(
    "conf/boilerplate.py",
    "conf/environ.py",
    "conf/db.py",
    "conf/static.py",
    "conf/api.py",
    "conf/cache.py",
    "conf/logger.py",
    "conf/swagger.py",
    "conf/auth.py",
    "conf/integrations/*.py",
)
