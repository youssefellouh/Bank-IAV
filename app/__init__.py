from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    Migrate(app, db)

    from app.api.auth import auth_bp

    app.register_blueprint(auth_bp)
    # app.register_blueprint(user.bp)
    # app.register_blueprint(account.bp)

    return app