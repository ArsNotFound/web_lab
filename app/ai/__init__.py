from flask import Blueprint

from app.ai.api import api_bp
from app.ai.views import views_bp

bp = Blueprint('ai', __name__)
bp.register_blueprint(views_bp)
bp.register_blueprint(api_bp, url_prefix='/api')
