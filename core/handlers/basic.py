from aiogram import Bot
from aiogram.types import Message
from core.utils import BasicMessage


class BasicHandler:
    @staticmethod
    async def get_start(message: Message, bot: Bot) -> None:
        """
        Sends a message GET_START_MESSAGE_EN
        """
        await bot.send_message(chat_id=message.from_user.id, text=BasicMessage.GET_START_MESSAGE_EN, parse_mode="HTML")

    @staticmethod
    async def get_help(message: Message, bot: Bot) -> None:
        """
        Sends a message triggered by /help command
        """
        await bot.send_message(chat_id=message.from_user.id, text=BasicMessage.GET_HELP_MESSAGE_EN, parse_mode="HTML")

    @staticmethod
    async def get_contact(message: Message, bot: Bot) -> None:
        """
        Sends a message triggered by /contact command
        """
        await bot.send_message(
            chat_id=message.from_user.id, text=BasicMessage.GET_CONTACT_MESSAGE_EN, parse_mode="HTML"
        )
