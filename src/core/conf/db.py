from core.conf.environ import env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB', cast=str, default='postgres'),
        'USER': env('POSTGRES_USER', cast=str, default='postgres'),
        'PASSWORD': env('POSTGRES_PASSWORD', cast=str, default='postgres'),
        'HOST': env('POSTGRES_HOST', cast=str, default='db'),
        "OPTIONS": {"connect_timeout": 1200, "options": "-c statement_timeout=72000"},
        'PORT': env('POSTGRES_PORT', cast=int, default=5432),
    }
}
