import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key-for-dev")

DEBUG = True

ALLOWED_HOSTS = [
    "webserver",
    "python-project-52-7l3z.onrender.com",
    ".onrender.com",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_bootstrap5",
    "task_manager",
    "task_manager.users",
    "task_manager.statuses",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "task_manager.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Обратите внимание, что путь к шаблонам – внутри task_manager/
        "DIRS": [BASE_DIR / "task_manager" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "task_manager.wsgi.application"

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', 'postgres://database_name_oqut_user:mRTPazHqUMldeALqN2A0Tr4j2ykqEczL@dpg-d6av3iumcj7s73enf5n0-a.virginia-postgres.render.com/database_name_oqut')
    )
}

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

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Указание папки с переводами - на всякий случай
LOCALE_PATHS = [
    BASE_DIR / "locale",
]