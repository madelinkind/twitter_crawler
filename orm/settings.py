import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        # Database driver
        'ENGINE': 'django.db.backends.sqlite3',
        # Replace below with Database Name if using other database engines
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = (
    'db',
)

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = 'jwb#whr6=1n&nkd^zzj89da(_-3mjbs77jc#rp(s)k&!ru-8_g'
