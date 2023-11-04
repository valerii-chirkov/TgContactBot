from aiogram import Bot
from aiogram.types import Message

from core import Config
from core.utils import CoreMessage


class CoreHandler:
    @staticmethod
    async def route_message_to_admin(message: Message, bot: Bot) -> None:
        """
        User type any message or sends any file
        User gets a message of sent status
        Admin gets a forwarded message from user
        """
        await bot.send_message(
            chat_id=message.from_user.id, text=CoreMessage.GET_MESSAGE_ROUTED_TO_ADMIN_EN, parse_mode="HTML"
        )

        await bot.forward_message(
            chat_id=Config.ADMIN_ID, from_chat_id=message.from_user.id, message_id=message.message_id
        )
