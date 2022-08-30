from BS import celery
from BS.celery_utils import init_celery
from BS.factory import create_app

app = create_app()
init_celery(celery,app)