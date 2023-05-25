from flask import Blueprint

from app.contacts.views import views_bp

bp = Blueprint('contacts', __name__)
bp.register_blueprint(views_bp, url_prefix='/contacts')
