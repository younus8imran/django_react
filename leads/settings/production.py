import os 
from . import BASE_DIR 
import dj_database_url


##  SECRET KEY settings
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['.herokuapp.com']

DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')
CORS_ORIGIN_ALLOW_ALL = (os.environ.get('CORS_ORIGIN_ALLOW_ALL') == 'True')


DATABASES = { 
    'default': dj_database_url.config(
        default= os.environ.get('DATABASE_URL')
    )
}


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None 

AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')