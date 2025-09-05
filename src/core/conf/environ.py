import os

ENVIRONMENT = os.getenv('ENVIRONMENT', 'develop')
SECRET_KEY = os.getenv('SECRET_KEY', 'insecure-secret-key')
DEBUG = ENVIRONMENT == 'develop'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
