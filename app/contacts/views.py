from flask import render_template, Blueprint


views_bp = Blueprint('views', __name__, static_folder='static', template_folder='templates')


@views_bp.route('/')
def index():
    return render_template('contacts.html', title='Контакты', pname='Контакты')
