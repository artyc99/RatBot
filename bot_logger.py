import logging


class Log:
    def __init__(self, filename, log_level):
        # Initializing logging with config
        self.file_logger = logging.getLogger(__name__)
        self.file_logger.setLevel(log_level)
        self.console_logger = logging.getLogger(__name__)
        self.console_logger.setLevel(log_level)

        # Create handler for file writing
        self.file_logger_handler = logging.FileHandler(filename)
        self.file_logger_handler.setLevel(log_level)
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(log_level)

        # Create Formatter for logs
        self.logger_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add Formatter to handler
        self.file_logger_handler.setFormatter(self.logger_formater)
        self.console_handler.setFormatter(self.logger_formater)

        # Add handler to logger
        self.file_logger.addHandler(self.file_logger_handler)
        self.file_logger.info('Настройка логгирования окончена')
        self.console_logger.addHandler(self.console_handler)
        self.console_logger.info('Настройка логгирования окончена')
