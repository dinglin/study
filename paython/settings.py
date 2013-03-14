#encoding=utf8
# Django settings for aifangDeploy project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'aifang_deploy',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'aifang',                  # Not used with sqlite3.
        'HOST': '192.168.1.24',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },

}

#shell 路径
SHELL_PATH = "/home/dinglin/python/aifangDeploy/aifangDeploy/shell/"
AIFANG_APP_PATH = "/Users/lenye01/git/aifang-app/"
HOTFIX_PATH = "/Users/lenye01/git/aifang-app/"
TEMP_OP_PATH = "/Users/lenye01/git/aifang-app/"
#puppet server info
PUPPET_SERVER = 'app10-022.i.ajkdns.com'
PUPPET_BASE_DIR = '/etc/puppet'
PUPPET_MODULE_DIR = PUPPET_BASE_DIR + '/modules'
PUPPET_APPS = '18,19,20,21,22,23,24,25'
PUPPET_USER = 'aifang'
#域帐号服务器
CLIENT_ID = 'kyou3'
CLIENT_SECRET = '7cc537e3'
OAUTH_URL = 'https://auth.corp.anjuke.com'
LDAP_URL = 'http://10.11.6.164/ldap/2.1/ldap_anjuke_login.php'
#PMT服务器
PMT_SERVER = 'http://pmt.corp.anjuke.com/api/anjukeinc/projectinfo'
#项目路径
BASE_PATH = "/home/dinglin/python/aifangDeploy/"
#几个变量
PRODUCT_ENV_SSH_USERNAME = "kavin"

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-CN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = BASE_PATH + '/static/compress/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    BASE_PATH + 'static',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#(y1m42m)1t4frjv&amp;(6@3t(h%4=3nd01_7uj4w^q1mwwl7mr22'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aifangDeploy.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'aifangDeploy.wsgi.application'

TEMPLATE_DIRS = (
    BASE_PATH + 'templates'
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'deploy',
    'tools',
    'project',
    'webgit',
    'compare',
    'account',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = {
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request"
                               }

REPORT_SMTP_SERVER = 'smtp.anjuke.com'
REPORT_SMTP_USERNAME = 25
REPORT_SMTP_USERNAME = 'dinglin@anjuke.com'
REPORT_SMTP_PASSWORD = ''
REPORT_SMTP_REPORTER_NAME = 'deploy-system'
REPORT_SMTP_REPORTER_ADDRESS = 'deploy-system@anjuke.com'

OA_MANAGER = ('',
    'kyouzhang',
    'hanjunfeng',
    'andycao',
    'dinglin',
              )
