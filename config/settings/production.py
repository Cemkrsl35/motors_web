"""
Django production settings.

Usage:
    DJANGO_SETTINGS_MODULE=config.settings.production
"""

import os

from .base import *  # noqa: F401, F403
from .base import get_env

# --- Security ---

DEBUG = False

SECRET_KEY = get_env("DJANGO_SECRET_KEY", required=True)

ALLOWED_HOSTS = [
    host.strip()
    for host in get_env("DJANGO_ALLOWED_HOSTS", required=True).split(",")
    if host.strip()
]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True


# --- Database (override with env-based config in production) ---

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", ""),
        "USER": os.getenv("DB_USER", ""),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": os.getenv("DB_PORT", ""),
    }
}


# --- Static files ---

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"


# --- Logging ---

LOGGING["loggers"]["django"]["level"] = "WARNING"  # noqa: F405
