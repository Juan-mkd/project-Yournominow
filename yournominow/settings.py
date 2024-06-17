"""
Django settings for yournominow project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os



BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'empleado', 'static'),
    os.path.join(BASE_DIR, 'login', 'static'),
    os.path.join(BASE_DIR, 'usuario', 'static'),
    os.path.join(BASE_DIR, 'administrador', 'static'),
    
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (Uploaded by users)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--yv@emsjzu0edu)q@@9@(=+)1h3cd4)3q_x3#w@j009g13$jz)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



ALLOWED_HOSTS = ['*']


# ALLOWED_HOSTS = ['3.91.9.201', 'localhost',]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'usuario',
    'administrador',
    'empleado',
    'desprendible',
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

ROOT_URLCONF = 'yournominow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yournominow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yournominow',
        'USER': 'admin',
        'PASSWORD': 'YourNomiNow123',
        'HOST': 'databasenomi.c7g4qsk2wmfp.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/







# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




AUTHENTICATION_BACKENDS = [
    'login.CedulaBackend',  # Cambia 'myapp' 
    'django.contrib.auth.backends.ModelBackend',
]



# Asegúrate de tener estas configuraciones adecuadas
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Por ejemplo, 'smtp.gmail.com'
EMAIL_PORT = 587  # Puerto de tu servidor de correo (ejemplo: 587 para TLS en Gmail)
EMAIL_USE_TLS = True  # O False si no estás utilizando TLS
EMAIL_HOST_USER = 'one2023123@gmail.com'  # Tu dirección de correo electrónico
EMAIL_HOST_PASSWORD = 'hubn ktge kjzb ckgi'  # Tu contraseña de correo electrónico
DEFAULT_FROM_EMAIL = 'one2023123@gmail.com'  # Tu dirección de correo electrónico predeterminada



AUTHENTICATION_BACKENDS = [
    'login.backends.CedulaBackend',  # Reemplaza 'myapp' con el nombre de tu aplicación
    'django.contrib.auth.backends.ModelBackend',  # Mantén el backend de autenticación predeterminado
]



LOGIN_REDIRECT_URL = 'login'
