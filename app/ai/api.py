from flask import Blueprint
from flask_pydantic import validate

from app.ai.content import neural_networks, undefined_category
from app.ai.models import NeuralNetworkIn, NeuralNetwork
from labapp.routes import json_response

api_bp = Blueprint('api', __name__)


@api_bp.route('/ai', methods=['POST'])
@validate()
def post_ai(body: NeuralNetworkIn):
    desc_strip = body.desc.strip()
    neural_networks.append(NeuralNetwork(
        name=body.name,
        category=undefined_category,
        tasks=body.tasks,
        field=body.field,
        url=body.url,
        img="img/logo.png",
        desc=desc_strip,
        short_desc=desc_strip[:100] + "..."
    ))

    msg = f"Ваш запрос на добавление {body.name} получен!"
    return json_response({'msg': msg})
