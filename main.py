#!/usr/bin/python3.9

Token: str = ""

from telegram.ext import Updater

from src.commands import Start
from src.message import Photo, VidoCompressor
from src.logger import Logger

# Initialize the logger
logger = Logger()

# Initialize the updater and dispatcher
updater = Updater(token=Token)
dispatcher = updater.dispatcher

dispatcher.add_handler(Start().handle())
dispatcher.add_handler(VidoCompressor().handle())
dispatcher.add_handler(Photo('./stack').handle())
updater.start_polling()
