import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from core.handlers import BasicHandler, CoreHandler
from core.utils import set_commands
from core import Config
from core.utils import SystemMessage


os.environ["WORKING_DIR"] = os.getcwd()


async def start_bot(bot: Bot) -> None:
    """
    Runs when your bot started
    May be used to quickly react to incidents
    """
    await set_commands(bot=bot)
    await bot.send_message(chat_id=Config.ADMIN_ID, text=SystemMessage.START_BOT_MESSAGE)


async def stop_bot(bot: Bot) -> None:
    """
    Runs when your bot stopped
    May be used to quickly react to incidents
    """
    await bot.send_message(chat_id=Config.ADMIN_ID, text=SystemMessage.STOP_BOT_MESSAGE)


async def start() -> None:
    """
    Initialize a bot, prepare logging, middlewares, and your handlers
    """
    logging.basicConfig(
        filename="logs/contact_logs",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )

    bot = Bot(token=Config.TOKEN)
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(BasicHandler.get_start, Command(commands=["start", "run"]))
    dp.message.register(BasicHandler.get_help, Command(commands=["help"]))
    dp.message.register(BasicHandler.get_contact, Command(commands=["contact"]))
    dp.message.register(CoreHandler.get_resume, Command(commands=["resume", "cv"]))

    dp.message.register(CoreHandler.route_message_to_admin)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
