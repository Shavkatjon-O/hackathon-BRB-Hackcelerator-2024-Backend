import environ

from pathlib import Path
from django.utils.translation import gettext_lazy as _
from datetime import timedelta

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = [
    "apps.anons",
    "apps.applications",
    "apps.approvals",
    "apps.assistants",
    "apps.borrowers",
    "apps.cards",
    "apps.chats",
    "apps.clients",
    "apps.common",
    "apps.events",
    "apps.loans",
    "apps.meetings",
    "apps.notifications",
    "apps.payments",
    "apps.planners",
    "apps.users",
]

THIRD_PARTY_APPS = [
    "drf_yasg",
    "rest_framework",
    "rest_framework_simplejwt",
    "modeltranslation",
    "rosetta",
    "corsheaders",
    "channels",
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "core.middlewares.ErrorHandlerMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "core.wsgi.application"
ASGI_APPLICATION = "core.asgi.application"

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

TIME_ZONE = "Asia/Tashkent"

USE_L10N = True
USE_I18N = True
USE_TZ = True

LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
    ("uz", _("Uzbek")),
)
LOCALE_PATHS = (BASE_DIR / "locales/",)

STATICFILES_DIRS = (BASE_DIR / "staticfiles",)

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

JAZZMIN_SETTINGS = {
    # Site
    "site_title": "BRB Titans",
    "site_header": "BRB Titans",
    "site_brand": "BRB Titans",
    "site_logo": "brb-titans-logo.png",
    # Welcome
    "welcome_sign": "Welcome to BRB Titans admin panel!",
    "welcome_panel_logo": "brb-titans-logo.png",
    # Login
    "login_logo": "brb-titans-logo.png",
}


REST_FRAMEWORK = {
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# EMAIL_HOST = env.str("EMAIL_HOST")
# EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = env.int("EMAIL_PORT")
# EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
# EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL")

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}
