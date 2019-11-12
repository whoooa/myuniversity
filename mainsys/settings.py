"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1-es+1&96*tx)f8&^u1g0rg13#*n7s+*@i5rx^)tgf$ox40&fg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "myxy.site", "www.myxy.site"]

# Application definition




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mainsys.urls'

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
            'builtins': ['django.templatetags.static'],
        },
    },
]

WSGI_APPLICATION = 'mainsys.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "nnpro",
#         "USER": "root",
#         "PASSWORD": "niu123",
#     },
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'

MEDIA_URL = "/media/"

STATICFILES_DIRS = (os.path.join('static'), )

##################
# 导入数据库配置
##################

try:
    from .dbconfig import *
except ImportError as e:
    if "dbconfig" not in str(e):
        raise e

##################
# 导入网站个性化配置
##################

try:
    from .webconfig import *
except ImportError as e:
    if "webconfig" not in str(e):
        raise e



##################
# 额外目录添加
##################

APPS_CANNOT_INTSALL = ["utils", ]  # 禁止作为app安装的目录



APP_ROOT = os.path.join(BASE_DIR, "./xyapps")
APP_MODELS = os.path.join(BASE_DIR, "./xymodels")
APP_VIEWS = os.path.join(BASE_DIR, "./xyviews")
sys.path.insert(0, APP_ROOT)
sys.path.insert(0, APP_MODELS)
sys.path.insert(0, APP_VIEWS)


# 根据wlapps里的目录进行动态设置
for ap in os.listdir(APP_ROOT):
    if ap not in APPS_CANNOT_INTSALL and os.path.isdir(os.path.join(APP_ROOT, ap)) and \
            os.path.exists(os.path.join(os.path.join(APP_ROOT, ap), "__init__.py")):
        INSTALLED_APPS += ("xyapps." + ap,)

# 根据wlmodels里的目录进行动态设置
if os.path.exists(APP_MODELS):
    for ap in os.listdir(APP_MODELS):
        if ap not in APPS_CANNOT_INTSALL and os.path.isdir(os.path.join(APP_MODELS, ap)) and \
                os.path.exists(os.path.join(os.path.join(APP_MODELS, ap), "__init__.py")):
            INSTALLED_APPS += ("xymodels." + ap,)

if os.path.exists(APP_VIEWS):
    for ap in os.listdir(APP_VIEWS):
        if ap not in APPS_CANNOT_INTSALL and os.path.isdir(os.path.join(APP_VIEWS, ap)) and \
                os.path.exists(os.path.join(os.path.join(APP_VIEWS, ap), "__init__.py")):
            INSTALLED_APPS += ("xyviews." + ap,)

