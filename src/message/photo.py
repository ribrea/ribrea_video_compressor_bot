"""
Handle for image messages
"""
from telegram import Update

from .base import Message
from telegram.ext import Filters, CallbackContext


class Photo(Message):
    """
    Handle for image messages
    """
    def __init__(self, path: str):
        super().__init__(message_type=Filters.photo)
        self.path = path

    def _execute(self, update: Update, context: CallbackContext) -> None:
        """Stores the photo and asks for a location."""
        user = update.message.from_user
        photo_file = update.message.photo[-1].get_file()
        photo_file.download(self.path+'/'+str(user.id)+'.jpg')
        self.logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
        update.message.reply_photo(
            photo=open(self.path+'/'+str(user.id)+'.jpg', 'rb'), caption='Loved it!'
        )
