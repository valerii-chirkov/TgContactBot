from core import Config


class SystemMessage:
    """
    System messages that are visible to admin only
    """

    START_BOT_MESSAGE = f"☄️ {Config.BOT_NAME} started"
    STOP_BOT_MESSAGE = f"🙊 {Config.BOT_NAME} stopped"


class BasicMessage:
    """
    Basic messages that are visible to users
    """

    GET_START_MESSAGE_EN = (
        "<b>Hi!</b>\n"
        "This bot helps me to stay organized and productive.\n"
        "Hope you also find it convenient to use!\n"
        "Try it and write your first message!\n"
    )
    GET_START_MESSAGE_RU = (
        "<b>Привет!</b>\n"
        "Этот бот помогает мне оставаться организованным и продуктивным.\n"
        "Надеюсь вам тоже понравится им пользоваться!\n"
        "Скорее пиши первое сообщение!"
    )
    GET_HELP_MESSAGE_EN = (
        "This bot helps me to stay organized and productive.\n"
        "That's why there are several convenient commands:\n"
        "<b>/contact</b> - to contact me, I will soon text you back\n"
        "<b>/resume</b> - to get my current CV\n"
        "<b>/about</b> - to get to know me better\n"
    )
    GET_HELP_MESSAGE_RU = (
        "Этот бот помогает мне оставаться организованным и продуктивным.\n"
        "Поэтому бот поддерживает следующие команды:\n"
        "<b>/contact</b> - связаться со мной, я отвечу в лс\n"
        "<b>/resume</b> - получить мое текущее резюме\n"
        "<b>/about</b> - узнать меня получше\n"
    )
    GET_CONTACT_MESSAGE_EN = (
        "To contact me just write messages like you usually do.\n" "You may also send me any type of files or links."
    )
    GET_CONTACT_MESSAGE_RU = (
        "Для связи со мной - просто напишите в этот чат.\n" "Вы также можете отправлять любые файлы и ссылки."
    )


class CoreMessage:
    GET_MESSAGE_ROUTED_TO_ADMIN_EN = "Your message successfully sent to the admin!"
    GET_MESSAGE_TEXT = "User: @{username}\n" "Sent message: {text}"
    GET_USER_REQUEST_CV = "User: @{username} requested cv"
