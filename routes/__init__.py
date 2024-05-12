from flask import Blueprint

# Import the blueprint from region.py
from .region import region_bp

# Initialize the blueprint
def init_app(app):
    app.register_blueprint(region_bp)
