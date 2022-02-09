import logging


class Logger:
    """
    Logger class to log messages to the console and to a file.
    """

    def __init__(self):
        """
        Initialize the logger.
        """
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)

    def get_logger(self, name):
        """
        Get a logger with the given name.
        :param name: The name of the logger.
        :return: The logger.
        """
        logger = logging.getLogger(__name__)
        return logger
