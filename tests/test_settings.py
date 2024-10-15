SECRET_KEY = 'fake-key-for-test'
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django_queryset_erd',
    'tests',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
USE_TZ = True

