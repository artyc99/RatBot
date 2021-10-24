import os

import telebot
from telebot import apihelper

from bot_logger import Log

if 'LOG_LEVEL' in os.environ.keys():
    if 'LOGGER' in os.environ.keys():
        logger = Log('logs/bot.log', os.environ['LOG_LEVEL'], os.environ['LOGGER'])
    else:
        logger = Log('logs/bot.log', os.environ['LOG_LEVEL'])
else:
    raise EnvironmentError

logger.console_logger.info('Starting app')

if 'TELEGRAM_BOT_TOKEN' in os.environ.keys():
    bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'], threaded=False)

else:
    raise EnvironmentError

logger.console_logger.info('Bot token set')


def configurate(app):

    app.config['SECRET_KEY'] = 'Some-my-very-secret-key'

    # blueprints
    from blueprints.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
