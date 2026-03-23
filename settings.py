from os import getenv
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': getenv('DB_ENGINE'),
        'HOST': getenv('DB_HOST'),
        'PORT': getenv('DB_PORT'),
        'NAME': getenv('DB_NAME'),
        'USER': getenv('DB_USER'),
        'PASSWORD': getenv('DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = getenv('SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
