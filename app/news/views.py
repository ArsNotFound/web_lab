from flask import render_template, Blueprint

from app.news.content import news

views_bp = Blueprint('views', __name__, static_folder='static', template_folder='templates')


@views_bp.route('/')
def index():
    return render_template('news.html', title='Статьи', pname='Статьи', news=news)
