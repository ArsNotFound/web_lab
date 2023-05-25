from flask import render_template, Blueprint

from app.ai.content import neural_networks
from app.ai.models import NeuralNetwork
from app.error.views import not_found_html


views_bp = Blueprint('views', __name__, static_folder='static', template_folder='templates', static_url_path='/static/ai')


@views_bp.route('/')
def index():
    return render_template('index.html', title='Нейросети', pname='Нейросети', neural_networks=neural_networks)


@views_bp.route('/ai/add')
def add():
    return render_template('add-ai.html', title='Добавить AI', pname='Добавить AI')


@views_bp.route('/ai/<slug>')
def neural(slug: str):
    network: NeuralNetwork = next(filter(lambda n: n.slug == slug, neural_networks))
    if not network:
        return not_found_html()
    return render_template('ai.html', title=network.name, pname=network.name, network=network, networks=neural_networks)
