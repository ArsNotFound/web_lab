import os

"""

Модуль с описанием конфигурации для приложения Flask

"""


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg://postgres:postgres@localhost:5432/web"
