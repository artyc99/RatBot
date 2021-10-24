import os

from flask import Flask

from app_config import configurate

from bot_logger import Log

app = Flask(__name__)

app = configurate(app)


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 443)))
