"""
Video Compressor
"""
import subprocess

from telegram import Update

from .base import Message
from telegram.ext import Filters, CallbackContext
from src.run.video_compressor import compress_video


class VidoCompressor(Message):
    """
    Video Compressor
    """

    def __init__(self):
        super().__init__(message_type=Filters.video)
        self.type = Filters.video
        self.path = "/tmp/video_compressor"

    def _execute(self, update: Update, context: CallbackContext) -> None:
        """
        Run
        """

        response = update.message.reply_text(f"Gotta compress that video!")
        user = update.message.from_user
        video = update.message.video.get_file()
        response.delete()
        response = update.message.reply_text(f"Downloading video...")
        video.download(f"{self.path}/{user.id}.mp4")
        response.delete()
        response = update.message.reply_text(f"Start Compressing {user.id}.mp4")
        compress_video(f"{self.path}/{user.id}.mp4", f"{self.path}/{user.id}(1).mp4")
        response.delete()
        response = update.message.reply_text(f"Compressed video sent to {user.id}")
        response.delete()
        update.message.reply_text("Done!")
        update.message.reply_video(
            video=open(f"{self.path}/{user.id}(1).mp4", "rb"),
        )
        if subprocess.call(['bash', 'src/run/cleaner.sh', self.path]) != 0:
            print("Error cleaning up")