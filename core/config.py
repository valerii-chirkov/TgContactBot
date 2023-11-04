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
    CV_FILENAME: str = os.getenv("CV_FILENAME")
    WORKING_DIR: str = os.getenv("WORKING_DIR") or ""  # initialized in main.py
    CV_PATH: str = os.path.join(WORKING_DIR, "files", CV_FILENAME)
