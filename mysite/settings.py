import os

gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Application definition

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'mysite', 'static'),
)
SITE_ID = 1

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors':
                (
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django.core.context_processors.i18n',
                    'django.core.context_processors.debug',
                    'django.core.context_processors.request',
                    'django.core.context_processors.media',
                    'django.core.context_processors.csrf',
                    'django.core.context_processors.tz',
                    'sekizai.context_processors.sekizai',
                    'django.core.context_processors.static',
                    'cms.context_processors.cms_settings',
                )
        }
    },
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'mysite', 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_style',
    'djangocms_column',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'reversion',
    'mysite',
    'top_gallery',
    'top_gallery_plugin',
    'core',
    'call_to_action_plugin',
    'clients_plugin',
    'debug_toolbar',
    'djangocms_blog',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'meta_mixin',
    'send_email',
    'adminsortable',
    'eav',
    'questionary',
)

LANGUAGES = (
    ## Customize this
    ('ru', gettext('ru')),
    ('ua', gettext('ua')),
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
    1: [
        {
            'name': gettext('ru'),
            'code': 'ru',
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
        {
            'name': gettext('ua'),
            'code': 'ua',
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
        {
            'name': gettext('en'),
            'code': 'en',
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature'),
    ('header.html', 'Header'),
    ('home_page.html', 'Home page'),
    ('contact_us.html', 'Contact us'),
    ('feature_bread.html', 'Page with Feature (breadcrumbs)')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

MIGRATION_MODULES = {
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
    'djangocms_column': 'djangocms_column.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

# Blog settings

BLOG_PAGINATION = 4
BLOG_USE_PLACEHOLDER = False
BLOG_USE_ABSTRACT = False
BLOG_ENABLE_COMMENTS = False
BLOG_POSTS_LIST_TRUNCWORDS_COUNT = 50
BLOG_IMAGE_THUMBNAIL_SIZE = {'size': '900x350', 'crop': True, 'upscale': False}
BLOG_IMAGE_FULL_SIZE = {'size': '900x350', 'crop': True, 'upscale': False}
BLOG_AUTHOR_DEFAULT = False

META_SITE_PROTOCOL = 'http'
META_USE_SITES = True
PARLER_LANGUAGES = {
    1: (
        {'code': 'en'},
        {'code': 'ru'},
        {'code': 'ua'},
    ),
}
# Ckeditor settings

CKEDITOR_UPLOAD_PATH = "uploads/"


try:
    from local_settings import *
except ImportError:
    print ('Local settings import error')
