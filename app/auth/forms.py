from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(),
                                                   Length(min=8, message='Пароль должен иметь минимум 8 символов')])
    password_confirm = PasswordField('Подтверждение', validators=[EqualTo('password', message='Пароли не совпадают')])
