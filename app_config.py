import os

from bot_logger import Log

if 'LOG_LEVEL' in os.environ.keys():
    if 'LOGGER' in os.environ.keys():
        logger = Log('logs/bot.log', os.environ['LOG_LEVEL'], os.environ['LOGGER'])
    else:
        logger = Log('logs/bot.log', os.environ['LOG_LEVEL'])
else:
    raise EnvironmentError

logger.console_logger.info('Starting app')

def configurate(app):

    app.config['SECRET_KEY'] = 'Some-my-very-secret-key'

    # blueprints
    from blueprints.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
