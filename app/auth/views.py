import bcrypt
from flask import Blueprint, render_template, make_response, jsonify, redirect, url_for, session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app import db
from app.auth.forms import LoginForm, RegisterForm
from app.auth.models import User

views_bp = Blueprint('views', __name__, static_folder='static', template_folder='templates',
                     static_url_path='/auth/static')


@views_bp.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data

        user: User = db.session.scalar(select(User).where(User.login == login))

        if not user:
            return redirect(url_for('auth.views.login_page'))

        if not bcrypt.checkpw(password.encode('utf-8'), user.password_hash):
            return redirect(url_for('auth.views.login_page'))
        else:
            response = redirect('/')
            session['user'] = user.login
            session['user_id'] = user.id
            response.set_cookie('AuthToken', user.login)
            return response

    return render_template('login.html', title='Авторизация в нашей системе', form=form)


@views_bp.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(form.password.data.encode('utf-8'), salt)

        try:
            user = User()
            user.email = form.email.data
            user.login = form.login.data
            user.password_hash = hashed

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('auth.views.login_page'))
        except IntegrityError as e:
            db.session.rollback()
            return make_response(jsonify({'msg': str(e)}), 500)

    return render_template('register.html', title='Регистрация в нашей системе', form=form)
