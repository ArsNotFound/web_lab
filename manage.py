# Подключаем приложение Flask из пакета labapp
from app import app

"""

    Этот файл запускает приложение

"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
