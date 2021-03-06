r"""

    occupywallst.settings
    ~~~~~~~~~~~~~~~~~~~~~

    This file is used to configure Django.

"""

import os
from os.path import abspath, dirname, join
project_root = dirname(abspath(__file__))

DEBUG = False
PAYPAL_DEBUG = DEBUG
AUTHNET_DEBUG = DEBUG
TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = join(project_root, 'media')
GEOIP_PATH = join(project_root, 'data')
SHP_PATH = join(project_root, 'data')

ADMINS = (
    ('', 'errors@occupywallst.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': 'occupywallst.db',
    }
}

SITE_ID = 1
USE_I18N = True
USE_L10N = False
USE_THOUSAND_SEPARATOR = True
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
DEFAULT_CHARSET = 'utf-8'
ROOT_URLCONF = 'occupywallst.urls'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

# change me in production
SECRET_KEY = 'oek(taazh36*h939oau#$%()dhueha39h(3zhc3##ev_jpfyd2'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'occupywallst',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.comments',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.gis',
)
