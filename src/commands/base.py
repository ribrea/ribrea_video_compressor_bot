"""
Command Base
"""
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from src.logger import Logger


class Command:
    """
    Base class for all commands.
    """

    def __init__(self, command: str, message: str):
        self.command: str = command
        self.message: str = message
        self.logger = Logger().get_logger("Command")

    def _execute(self, update: Update, context: CallbackContext) -> None:
        """
        Execute the command.
        """
        raise NotImplementedError("execute() not implemented.")

    def handle(self) -> CommandHandler:
        """
        Return the command handler.
        :return: CommandHandler
        """
        return CommandHandler(self.command, self._execute)
