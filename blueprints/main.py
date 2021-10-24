from flask import Blueprint

from app_config import logger

main = Blueprint('main', __name__)


@main.route('/')
def index():
    logger.console_logger.info('Index hello logs')
    return 'Hello'
