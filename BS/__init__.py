import os

from BS.celery_utils import init_celery
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_marshmallow import Marshmallow
from flask_mail import Mail

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
mail = Mail()

PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]


def create_app(app_name=PKG_NAME, **kwargs):
    app = Flask(app_name)
    if kwargs.get("celery"):
        init_celery(kwargs.get("celery"), app)

    # app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from BS.User.routes import user
        from BS.Bank.routes import bank_detail
        from BS.Officers.routes import officers
        from BS.Admin.routes import admin
        from BS.Authentication.routes import auth

        app.register_blueprint(user)
        app.register_blueprint(bank_detail)
        app.register_blueprint(officers)
        app.register_blueprint(admin)
        app.register_blueprint(auth)

        return app
