"""
Handler for /start command
"""
from telegram import Update
from telegram.ext import CallbackContext
from .base import Command


class Start(Command):
    """
    Handler for /start command
    """
    def __init__(self):
        super(Start, self).__init__(message="Hello, I'm a bot. I'm here to help . @ribrea", command='start')

    def _execute(self, update: Update, context: CallbackContext):
        """
        Handler for /start command
        :param update: message update
        :param context: request context
        """
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.message)

