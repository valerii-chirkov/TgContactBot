from aiogram import Bot
from aiogram.types import Message

from core import Config
from core.utils import CoreMessage
from core.handlers.utils import get_cv


class CoreHandler:
    @staticmethod
    async def route_message_to_admin(message: Message, bot: Bot) -> None:
        """
        User type any message or sends any file
        User gets a message of sent status
        Admin gets a forwarded message from user
        """
        # User gets a message of sent status
        await bot.send_message(
            chat_id=message.from_user.id, text=CoreMessage.GET_MESSAGE_ROUTED_TO_ADMIN_EN, parse_mode="HTML"
        )
        # Admin gets a forwarded message from user
        await bot.forward_message(
            chat_id=Config.ADMIN_ID, from_chat_id=message.from_user.id, message_id=message.message_id
        )

    @staticmethod
    async def get_resume(message: Message, bot: Bot) -> None:
        """
        User request a resume
        CV from Config.CV_PATH sends to a user
        Admin get a message that the user requested the CV
        """
        # CV from Config.CV_PATH sends to a user
        document = await get_cv()
        await bot.send_document(chat_id=message.from_user.id, document=document)

        # Admin get a message that the user requested the CV
        text = CoreMessage.GET_USER_REQUEST_CV.format(username=message.from_user.username)
        await bot.send_message(chat_id=Config.ADMIN_ID, text=text, parse_mode="HTML")
