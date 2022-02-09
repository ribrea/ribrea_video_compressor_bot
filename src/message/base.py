"""
Base for handle Message
"""
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, MessageFilter, CallbackContext
from src.commands import Command
from src.logger import Logger


class Message:
    """
    Base for handle Message
    """

    def __init__(self, message_type: MessageFilter):
        self.message_type: MessageFilter = message_type
        self.logger = Logger().get_logger("Message")

    def handle(self) -> MessageHandler:
        """
        Handle Message
        """
        return MessageHandler(self.message_type, self._execute)

    def _execute(self, update: Update, context: CallbackContext) -> None:
        """
        Execute
        :param update:
        :param context:
        """
        raise NotImplementedError()
