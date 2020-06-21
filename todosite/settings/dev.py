from .base import *

CONFIG_SECRET_DEV_FILE = os.path.join(CONFIG_SECRET_DIR, 'dev.json')
config_secret_dev = json.loads(open(CONFIG_SECRET_DEV_FILE).read())

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.sqlite3'),
    }
}

ALLOWED_HOSTS = config_secret_dev['allowed_hosts']
