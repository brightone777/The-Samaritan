import os
import mimetypes
from pathlib import Path
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = 'django-insecure-y4!a(37wk_3e!hd(33sx7!3oq*2r!o9&717h-ixf)g2#*^_uar'
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'the-samaritann.onrender.com']

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'posts.apps.PostsConfig',
    'cloudinary',
    'cloudinary_storage',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs and templates
ROOT_URLCONF = 'anonymous_posting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'anonymous_posting.wsgi.application'

# Database (default fallback is SQLite)
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
    )
}

# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Time zone and localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# Static files (Render-friendly)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ✅ Cloudinary media storage
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': os.environ.get("CLOUDINARY_API_KEY"),
    'API_SECRET': os.environ.get("CLOUDINARY_API_SECRET"),
}

# Email setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ochiengbrightone777@gmail.com'
EMAIL_HOST_PASSWORD = 'brightt777...'  # Use app password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
ADMINS = [('Admin', 'ochiengbrightone777@gmail.com')]

# MIME types for images
mimetypes.add_type("image/png", ".png", True)
mimetypes.add_type("image/jpeg", ".jpg", True)
mimetypes.add_type("image/jpeg", ".jpeg", True)

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
