from core.conf.boilerplate import BASE_DIR


STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR.parent / 'static',  # /app/src/static
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR.parent / 'media'

