from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        from BS.User.routes import user
        from BS.Bank.routes import bank_detail
        from BS.Officers.routes import officers
        from BS.Admin.routes import admin

        app.register_blueprint(user)
        app.register_blueprint(bank_detail)
        app.register_blueprint(officers)
        app.register_blueprint(admin)

        return app
