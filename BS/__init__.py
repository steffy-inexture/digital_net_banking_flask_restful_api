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


def create_app(config_class=Config):
    app = Flask(__name__)
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