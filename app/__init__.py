from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)
db = SQLAlchemy(app)

def create_app():
    app.config.from_object(Config)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
    