from flask import Flask

from pydantic import BaseModel

from app.error import bp as error_bp
from app.contacts import bp as contacts_bp
from app.news import bp as news_bp
from app.ai import bp as ai_bp


app = Flask(__name__, static_url_path="/static", static_folder="static", template_folder="templates")


class NavigationItem(BaseModel):
    name: str
    url: str


nav_menu: list[NavigationItem] = [
    NavigationItem(name='Нейросети', url='/'),
    NavigationItem(name='Промты', url='#'),
    NavigationItem(name='Статьи', url='/news'),
    NavigationItem(name='Обучение', url='#'),
    NavigationItem(name='Контакты', url='/contacts')
]


@app.context_processor
def inject_nav_menu():
    return dict(nav_menu=nav_menu)


app.register_blueprint(contacts_bp)
app.register_blueprint(news_bp)
app.register_blueprint(error_bp, url_prefix='/error')
app.register_blueprint(ai_bp)
