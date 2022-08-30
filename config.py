from datetime import timedelta


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:harsh2022@localhost:5432/db_for_bs'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = 'sdfghjjjjjjjjjjjjjjjjjj'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'steffykhristi.18.ce@iite.indusuni.ac.in'
    MAIL_PASSWORD = 'rpmvdxckolclxdos'

class CeleryConfig:
    CELERY_IMPORTS = ('BS.tasks')
    # CELERY_TASK_RESULT_EXPIRES = 30
    CELERY_TIMEZONE = 'UTC'

    CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'

    CELERYBEAT_SCHEDULE = {
        'loan-mail-celery': {
            'task': 'BS.tasks.loan_detail',
            # Every minute
            'schedule': timedelta(seconds=60),
        },
        'insurance-mail-celery': {
            'task': 'BS.tasks.insurance_detail',
            # Every minute
            'schedule': timedelta(seconds=60),
        }

    }
