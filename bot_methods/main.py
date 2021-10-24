from app_config import bot, logger


@bot.message_handler(commands=['start'])
def start(message):
    # bot.reply_to(message, 'Hello, ' + message.from_user.first_name)
    logger.console_logger.info('Start message')
    bot.reply_to('Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)
