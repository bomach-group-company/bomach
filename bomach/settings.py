"""
Django settings for bomach project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""



from pathlib import Path
from decouple import config


TRY_LOCAL_DB = False
TRY_MYSQL = True

if not TRY_LOCAL_DB and TRY_MYSQL:
    import pymysql

    pymysql.install_as_MySQLdb()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^=k8^m1m@gdhgg&+a@g6up*tfi^67g^e%8uv0yhhj!sqzc()$=dw03gb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# use local db, storage, email config create be me
TRY_LOCAL_STORAGE = False
TRY_LOCAL_EMAIL = False

ALLOWED_HOSTS = ['yuhga.org', 'www.yuhga.org', '127.0.0.1', 'localhost']

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')
# SECURE_SSL_REDIRECT = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_summernote',
    'ckeditor', 
    'django.contrib.staticfiles',
    'main',
]
    
if not TRY_LOCAL_STORAGE:
    INSTALLED_APPS.insert(7, 'cloudinary_storage')
    INSTALLED_APPS.insert(9, 'cloudinary')
 
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    # STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': 'dervdezl1',
        'API_KEY': '174652233732241',
        'API_SECRET': 'KRbKr774gQtrYuy2FPKfDnW3qsE',
    }

    # CKEDITOR_IMAGE_BACKEND = 'cloudinary_storage.storage.CloudinaryMediaBackend'
    # CKEDITOR_CLOUDINARY_OPTIONS = {
    #     'cloud_name': config('CLOUDINARY_STORAGE_CLOUD_NAME'),
    #     'api_key': config('CLOUDINARY_STORAGE_API_KEY'),
    #     'api_secret': config('CLOUDINARY_STORAGE_API_SECRET'),
    #     'overwrite': True,  # Set this to True if you want to overwrite existing files
    # }

SUMMERNOTE_THEME = 'bs4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bomach.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'bomach.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if TRY_LOCAL_DB:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

elif TRY_MYSQL:
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bomaoqrt_bomach_db',
            'HOST': '127.0.0.1',
            'PORT': 3306,
            'USER': 'bomaoqrt_emma',
            'PASSWORD': '#56S6Ehh_f])_',
            'OPTIONS': {
                'charset': 'utf8mb4',
                'sql_mode': 'strict_trans_tables',
            },
        }
    }
    
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bomaoqrt_bomach_db',
            'HOST': '127.0.0.1',
            'PORT': 3306,
            'USER': 'bomaoqrt_emma',
            'PASSWORD': '#56S6Ehh_f])_',
        }
    }



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
   BASE_DIR / 'static'
]

MEDIA_URL = '/media/'    

MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

###DEVELOPMENT

if TRY_LOCAL_EMAIL:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = '1025'

###PRODUCTION

else:
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'maxzenorhymegod@gmail.com'
    EMAIL_HOST_PASSWORD = 'piztddphatcsnbtm'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

# required cause i used CKEDITOR previously then switched the field to SUMMERNOTE because of bug in debug=False
CKEDITOR_UPLOAD_PATH = 'uploads/'

SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'toolbar': [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['para', ['ul', 'ol']],
            ['insert', ['link']],
            ['view', ['fullscreen']],
        ],
        'disable_upload': True,
        'disable_attachment': True,
    },
}


# # CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js' 
# CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
# # CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'

# # CKEDITOR_ALLOW_NONIMAGE_FILES = False
# # CKEDITOR_RESTRICT_BY_USER = False
# # CKEDITOR_BROWSE_SHOW_DIRS = True

# CKEDITOR_CONFIGS = {
#     'default': {
     
#         'toolbar_Custom': [
#             {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
#             {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
#             {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
#             {'name': 'forms',
#              'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
#                        'HiddenField']},
#             '/',
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
#             {'name': 'paragraph',
#              'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#                        'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
#                        'Language']},
#             {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#             {'name': 'insert',
#              'items': ['Image', 'Youtube','Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
#             '/',
#             {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#             {'name': 'about', 'items': ['CodeSnippet']},
#             {'name': 'about', 'items': ['About']},
#             '/',  # put this to force next toolbar on new line
#             {'name': 'yourcustomtools', 'items': [
#                 # put the name of your editor.ui.addButton here
#                 'Preview',
#                 'Maximize',

#             ]},
#         ],
#         'toolbar': 'Custom',  # put selected toolbar config here
#         'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
#         'height': 400,
#         # 'width': '100%',
#         'filebrowserWindowHeight': 725,
#         'filebrowserWindowWidth': 940,
#         'toolbarCanCollapse': True,
#         'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
#         'tabSpaces': 4,
#         'extraPlugins': ','.join([
#             'uploadimage', # the upload image feature
#             # your extra plugins here
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             'devtools',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath',
#             'codesnippet',
#         ]),
#     }
# }


