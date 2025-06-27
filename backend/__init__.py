from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    Migrate(app, db)

    from backend.routes.auth import auth_bp
    from backend.routes.test import test_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(test_bp)

    return app
