import os

from flask import Flask

from app_config import configurate

from bot_logger import Log

app = Flask(__name__)

app = configurate(app)


if __name__ == '__main__':

    if 'LOG_LEVEL' in os.environ.keys():
        logger = Log('./Logs/bot.log', os.environ['LOG_LEVEL'])
        if 'LOGGER' in os.environ.keys():
            logger = Log('./Logs/bot.log', os.environ['LOG_LEVEL'], os.environ['LOGGER'])
    else:
        raise EnvironmentError

    logger.console_logger.info('Starting app')

    app.run()
