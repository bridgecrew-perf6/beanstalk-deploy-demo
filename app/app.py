from flask import Flask
from .api.base import api_bp

def create_app(settings=None):
    app = Flask(__name__)

    app.register_blueprint(api_bp, url_prefix='/api')
    return app
