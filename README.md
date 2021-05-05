# Coin Transaction (backend)

## Run Project 

### Change in ./settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

### Run following commands:

- py manage.py migrate
- py manage.py createsuperuser
- py manage.py runserver
