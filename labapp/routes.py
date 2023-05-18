# -*- coding: utf-8 -*-
from labapp import app, db
from flask import render_template, make_response,  Response, jsonify, json
from flask_pydantic import validate
from labapp.content import nav_menu, neural_networks, news, undefined_category
from labapp.model import NeuralNetwork, NeuralNetworkIn

"""

    Модуль регистрации маршрутов для запросов к серверу, т.е.
    здесь реализуется обработка запросов при переходе пользователя на определенные адреса веб-приложения

"""


@app.route('/')
@app.route('/index')
def index_route():
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    return render_template('index.html', title='Нейросети', pname='Нейросети', nav_menu=nav_menu,
                           neural_networks=neural_networks)


@app.route('/contacts')
def contact_route():
    return render_template('contacts.html', title='Контакты', pname='Контакты', nav_menu=nav_menu)


@app.route('/neural/<slug>')
def neural_route(slug: str):
    network: NeuralNetwork = next(filter(lambda n: n.slug == slug, neural_networks))
    if not network:
        return not_found()
    return render_template('neural.html', title=network.name, pname=network.name, nav_menu=nav_menu, network=network,
                           networks=neural_networks)


@app.route('/news')
def news_route():
    return render_template('news.html', title='Статьи', pname='Статьи', nav_menu=nav_menu, news=news)


@app.route('/add-ai')
def add_ai_route():
    return render_template('add-ai.html', title='Добавить AI', pname='Добавить AI', nav_menu=nav_menu, )


@app.route('/api/ai', methods=['POST'])
@validate()
def post_ai(body: NeuralNetworkIn):
    desc_strip = body.desc.strip()
    neural_networks.append(NeuralNetwork(
        name=body.name,
        category=undefined_category,
        tasks=body.tasks,
        field=body.field,
        url=body.url,
        img="img/AI.png",
        desc=desc_strip,
        short_desc=desc_strip[:100] + "..."
    ))

    msg = f"Ваш запрос на добавление {body.name} получен!"
    return json_response({'msg': msg})


"""

    Реализация response-методов, возвращающих клиенту стандартные коды протокола HTTP

"""


# Возврат html-страницы с кодом 404 (Не найдено)
@app.route('/notfound')
def not_found_html():
    return render_template('404.html', title='404', err={'error': 'Not found', 'code': 404})


# Формирование json-ответа. Если в метод передается только data (dict-объект), то по-умолчанию устанавливаем код возврата code = 200
# В Flask есть встроенный метод jsonify(dict), который также реализует данный метод (см. пример метода not_found())
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))


# Пример формирования json-ответа с использованием встроенного метода jsonify()
# Обработка ошибки 404 протокола HTTP (Данные/страница не найдены)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


# Обработка ошибки 400 протокола HTTP (Неверный запрос)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)
