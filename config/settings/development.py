"""
Django development settings.

Usage:
    DJANGO_SETTINGS_MODULE=config.settings.development
"""

from .base import *  # noqa: F401, F403

# --- Debug ---

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# --- Database ---

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}


# --- Email (console backend for development) ---

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# --- Logging ---

LOGGING["loggers"]["django"]["level"] = "INFO"  # noqa: F405
