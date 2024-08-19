from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()

def create_app(config_filename=None):
    # Create the Flask app instance
    app = Flask(__name__)

    # Load configuration from config.py if available, otherwise load default settings
    if config_filename:
        app.config.from_pyfile(config_filename)
    else:
        # Default configuration settings
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Initialize Flask-Migrate with the app and SQLAlchemy db
    migrate = Migrate(app, db)

    # Return the app instance
    return app