import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    """
    Use your sensitive data from .env file
    """

    BOT_NAME: str = os.getenv("BOT_NAME")
    ADMIN_ID: str = os.getenv("ADMIN_ID")
    TOKEN: str = os.getenv("BOT_TOKEN")
    DB_URL: str = os.getenv("DB_URL")
