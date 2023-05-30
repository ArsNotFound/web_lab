from datetime import timedelta

"""

Модуль с описанием конфигурации для приложения Flask

"""


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg://postgres:postgres@localhost:5432/web"
    SECRET_KEY = 'bdgfbneibieRIGOWEFSD'
    SESSION_COOKIE_NAME = 'user_id'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)
