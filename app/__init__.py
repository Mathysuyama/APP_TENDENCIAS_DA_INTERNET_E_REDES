from flask import Flask
from config.config import Config
import os

def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Registrar blueprints
    from app.controllers.trends_controller import trends_bp
    app.register_blueprint(trends_bp)
    
    return app