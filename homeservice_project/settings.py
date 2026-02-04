"""
Django settings for homeservice_project project.
Production-ready for Railway.app
"""

from pathlib import Path
import os
import dj_database_url

# Load .env locally (Railway ignores this)
if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

# ============================
# BASE DIRECTORY
# ============================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================
# SECURITY
# ============================

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-dev-only-change-this"
)

DEBUG = True  # Set to False in production

ALLOWED_HOSTS = ["*"]  # Safe for Railway (domain changes dynamically)


# ============================
# APPLICATION DEFINITION
# ============================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Your apps
    "admin_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "homeservice_project.urls"

# ============================
# TEMPLATES
# ============================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Look inside BASE_DIR/templates AND app/templates
        "DIRS": [BASE_DIR / "templates"],  
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "homeservice_project.wsgi.application"


# ============================
# DATABASE
# ============================

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=False,
    )
}


# ============================
# PASSWORD VALIDATION
# ============================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ============================
# INTERNATIONALIZATION
# ============================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True


# ============================
# STATIC FILES
# ============================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Optional: additional folders to search during development
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Whitenoise for production
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ============================
# DEFAULT PRIMARY KEY
# ============================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ============================
# AUTH
# ============================

LOGIN_URL = "login"
