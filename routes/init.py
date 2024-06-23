from flask import Blueprint

# Initialize blueprints
bp = Blueprint('main', __name__)

from . import image
