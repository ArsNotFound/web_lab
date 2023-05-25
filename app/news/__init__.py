from flask import Blueprint

from app.news.views import views_bp

bp = Blueprint('news', __name__)

bp.register_blueprint(views_bp, url_prefix='/news')
