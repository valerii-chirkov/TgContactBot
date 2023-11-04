from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot) -> None:
    """
    Commands your users would execute in your bot
    """
    commands = [
        BotCommand(command="help", description="How to use/Как пользоваться"),
        BotCommand(command="about", description="About me/Обо мне"),
        BotCommand(command="contact", description="Contact me/Связаться со мной"),
        BotCommand(command="resume", description="Get my CV/Получить мое резюме"),
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
