import os
import pprint

import telebot
from flask import Blueprint, request

from app_config import logger, bot

main = Blueprint('main', __name__)


@main.route('/')
def index():

    if 'APP_URL' in os.environ.keys():

        bot.remove_webhook()
        bot.set_webhook(url=os.environ['APP_URL'] + os.environ['TELEGRAM_BOT_TOKEN'])

    logger.console_logger.info('Reset webhook')
    return '!', 200


@main.route('/' + os.environ['TELEGRAM_BOT_TOKEN'], methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200
