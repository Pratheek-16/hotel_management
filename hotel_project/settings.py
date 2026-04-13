from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-xw(q^(zrft%f+1x4ifr1j1l$soruk5^j-=iquzcecxe)5b#pc3'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hotel_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hotel_project.urls'

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

WSGI_APPLICATION = 'hotel_project.wsgi.application'

# ── SQLite Database ──
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# ──────────────────────────────────────────────────────────────
# ✉️  EMAIL CONFIGURATION
# ──────────────────────────────────────────────────────────────
# Option 1 ── Gmail SMTP (recommended for production)
# Step 1: Enable 2-Factor Authentication on your Google account.
# Step 2: Go to Google Account → Security → App Passwords.
# Step 3: Generate an App Password for "Mail" on "Other device".
# Step 4: Replace the values below with your credentials.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sreepratheekpotnuru@gmail.com'     
EMAIL_HOST_PASSWORD = 'lgsb azcp ljbu tgqo' 
DEFAULT_FROM_EMAIL = 'Hotel Aurum <sreepratheekpotnuru@gmail.com>'  

# ──────────────────────────────────────────────────────────────
# Option 2 ── Console backend (for local development/testing)
# Emails will be printed to the terminal instead of actually sent.
# Uncomment the line below and comment out the Gmail settings above.
# ──────────────────────────────────────────────────────────────
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'