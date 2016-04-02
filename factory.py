"""
factory.py
"""

from flask import Flask

def create_app(app_name,config_obj):
    """
    Create the flask application
    """
    # Initialize app object
    app = Flask(app_name)

    app.config.from_object(config_obj)

    return app

def register_blueprints(app,*blueprints):
    """
    Registers blueprints for the application
    """
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
