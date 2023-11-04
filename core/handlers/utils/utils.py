from aiogram.types import FSInputFile
from core import Config


async def get_cv() -> FSInputFile:
    """
    Gets your cv filename from .env
    And returns an FSInputFile object to pass it to bot.send_document
    """
    document = FSInputFile(Config.CV_PATH)
    return document
