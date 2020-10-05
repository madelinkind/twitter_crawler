import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'twitter_db',
        'USER': 'root',
        'PASSWORD':'root',
        'HOST':'raspberry.home',
        'PORT':'5432',
    }
}

INSTALLED_APPS = (
    'db',
)

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = 'jwb#whr6=1n&nkd^zzj89da(_-3mjbs77jc#rp(s)k&!ru-8_g'
