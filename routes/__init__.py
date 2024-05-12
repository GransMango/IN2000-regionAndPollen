from flask import Blueprint

# Import the blueprints from the modules
from .region import region_bp
from .pollen import pollen_bp

# Initialize the blueprints
def init_app(app):
    app.register_blueprint(region_bp)
    app.register_blueprint(pollen_bp)
