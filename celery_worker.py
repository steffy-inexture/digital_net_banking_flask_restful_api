from BS import create_app
from BS.celery_utils import init_celery
from BS.factory import celery

app = create_app()
init_celery(celery, app)
