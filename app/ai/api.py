from flask import Blueprint, jsonify, make_response
from flask_pydantic import validate
from pydantic import parse_obj_as
from sqlalchemy import select

from app import db
from app.ai.models import NeuralNetworkSchemaIn, NeuralNetwork, NeuralNetworkCategory, NeuralNetworkSchema

api_bp = Blueprint('api', __name__)


def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@api_bp.route('/ai', methods=['GET'])
@validate(response_many=True)
def get_all_ai():
    neural_networks_db = db.session.scalars(select(NeuralNetwork)).all()
    neural_networks = parse_obj_as(list[NeuralNetworkSchema], neural_networks_db)
    return neural_networks


@api_bp.route('/ai/<string:slug>', methods=['GET'])
@validate()
def get_ai(slug: str):
    neural_network_db = db.session.scalar(select(NeuralNetwork).where(NeuralNetwork.slug == slug))
    if not neural_network_db:
        return not_found()
    neural_network = NeuralNetworkSchema.from_orm(neural_network_db)
    return neural_network


@api_bp.route('/ai', methods=['POST'])
@validate()
def create_ai(body: NeuralNetworkSchemaIn):
    desc_strip = body.desc.strip()

    d = body.dict()
    d["slug"] = body.name.strip().lower().replace(" ", "_")
    d["img"] = "img/logo.png"
    d["desc"] = desc_strip
    d["short_desc"] = desc_strip[:100] + "..."
    d["category"] = db.session.scalar(
        select(NeuralNetworkCategory).where(NeuralNetworkCategory.name == "Без категории"))

    neural_network = NeuralNetwork(
        **d
    )

    db.session.add(neural_network)
    db.session.commit()

    msg = f"Ваш запрос на добавление {body.name} получен!"
    return make_response(jsonify({'msg': msg}))


@api_bp.route('/ai/<string:slug>', methods=['PUT'])
@validate()
def update_ai(slug: str, body: NeuralNetworkSchemaIn):
    neural_network_db: NeuralNetwork = db.session.scalar(select(NeuralNetwork).where(NeuralNetwork.slug == slug))
    if not neural_network_db:
        return not_found()

    desc_strip = body.desc.strip()

    neural_network_db.name = body.name.strip()
    neural_network_db.url = body.url
    neural_network_db.tasks = body.tasks
    neural_network_db.field = body.field
    neural_network_db.short_desc = desc_strip[:100] + "..."
    neural_network_db.desc = desc_strip

    db.session.commit()

    return make_response(jsonify({"msg": "Данные успешно обновлены"}))


@api_bp.route('/ai/<string:slug>', methods=['DELETE'])
def delete_ai(slug: str):
    neural_network_db: NeuralNetwork = db.session.scalar(select(NeuralNetwork).where(NeuralNetwork.slug == slug))
    if not neural_network_db:
        return not_found()

    db.session.delete(neural_network_db)
    db.session.commit()

    return make_response(jsonify({"msg": "Данные успешно удалены"}))
