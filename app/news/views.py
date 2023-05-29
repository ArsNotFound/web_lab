from flask import render_template, Blueprint
from sqlalchemy import select
from pydantic import parse_obj_as

from app import db
from app.news.models import News, NewsSchema

views_bp = Blueprint('views', __name__, static_folder='static', template_folder='templates')


@views_bp.route('/')
def index():
    news_db = db.session.scalars(select(News)).all()
    news = parse_obj_as(list[NewsSchema], news_db)
    return render_template('news.html', title='Статьи', pname='Статьи', news=news)
