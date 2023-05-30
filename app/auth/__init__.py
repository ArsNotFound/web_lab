from flask import Blueprint

from .views import views_bp

bp = Blueprint('auth', __name__)
bp.register_blueprint(views_bp)
