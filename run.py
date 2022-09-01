from flask_migrate import Migrate

from BS import create_app, db
from BS.factory import celery

app = create_app(celery=celery)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
