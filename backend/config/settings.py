# backend/config/settings.py
from decouple import config
import dj_database_url

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')  # Ex. "testdeconnection.onrender.com,localhost"
SECRET_KEY = config('SECRET_KEY', default='django-insecure-key')
DATABASE_URL = config('DATABASE_URL', default='sqlite:///db.sqlite3')

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
}