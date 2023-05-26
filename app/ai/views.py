from flask import render_template, Blueprint
from pydantic import parse_obj_as
from sqlalchemy import select

from app.ai.models import NeuralNetworkSchema, NeuralNetwork
from app.error.views import not_found_html

from app import db

views_bp = Blueprint('views', __name__, static_folder='static', template_folder='templates',
                     static_url_path='/static/ai')


@views_bp.route('/')
def index():
    neural_networks_db = db.session.scalars(select(NeuralNetwork)).all()
    neural_networks = parse_obj_as(list[NeuralNetworkSchema], neural_networks_db)

    return render_template('index.html', title='Нейросети', pname='Нейросети', neural_networks=neural_networks)


@views_bp.route('/ai/add')
def add():
    return render_template('add-ai.html', title='Добавить AI', pname='Добавить AI')


@views_bp.route('/ai/<slug>')
def neural(slug: str):
    neural_networks_db = db.session.scalars(select(NeuralNetwork)).all()
    neural_networks = parse_obj_as(list[NeuralNetworkSchema], neural_networks_db)

    network_db = db.session.scalar(db.select(NeuralNetwork).where(NeuralNetwork.slug == slug))
    if not network_db:
        return not_found_html()

    network = NeuralNetworkSchema.from_orm(network_db)

    return render_template('ai.html', title=network.name, pname=network.name, network=network, networks=neural_networks)
