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
    GET_ABOUT_MESSAGE_EN = (
        "🌐 My name is Valerii Chirkov, and I'm a 24-year-old professional with a passion "
        "for web development and system architecture. 🏙️ Originally from Russia, "
        "I currently reside in the vibrant city of Saint-Petersburg.\n\n"
        "💻 With over 4 years of experience in developing web products and designing "
        "system architectures, I have honed my skills in backend development using "
        "Python as my primary language. Additionally, I have had the opportunity to "
        "work on enterprise-level projects using Java EE while employed at the largest "
        "telecom company in Russia.\n\n"
        "💼 However, my expertise extends beyond the realm of IT. I have a keen interest "
        "in finance and management, which led me to complete a business school program "
        "in South Korea. In fact, I even have experience running a small construction "
        "business, showcasing my entrepreneurial spirit.\n\n"
        "🤼‍ Sports play a significant role in my life, and I have achieved the impressive "
        "feat of becoming a candidate for the title of Master of Sports in Greco-Roman "
        "wrestling before my 15th birthday. I also enjoy boxing and participating in "
        "extreme sports, as they provide an outlet for my adventurous side.\n\n"
        "👫💍 While I am not currently married, my aspirations for the near future "
        "include finding a compatible partner with whom I can build a healthy "
        "and financially independent family.\n\n"
        "🌍 In addition to my professional pursuits, I have a passion for travel. "
        "Exploring new cultures and experiencing different environments is a source "
        "of inspiration for me. As such, I am open to relocation opportunities that "
        "align with my career goals.\n\n"
        "🚀 I hope this glimpse into my background and interests has piqued your curiosity. "
        "If you have an exciting opportunity that matches my skill set and ambitions, "
        "I eagerly await your best offer. Let's embark on a journey of growth and success together!\n\n"
        'Code of this bot <a href="https://github.com/valerii-chirkov/tg_anime_bot">here</a>'
    )
    GET_ABOUT_MESSAGE_RU = (
        "🌐 Меня зовут Валерий Чирков, мне 24 года, увлекаюсь "
        "веб-разработкой и архитектурой систем. 🏙 Родом из России, в настоящее время "
        "живу в живописном городе Санкт-Петербурге.\n\n"
        "💻 У меня более 4 лет опыта разработки веб-продуктов и проектирования системных "
        "архитектур, за это время я отточил свои навыки в разработке бэкэнда с использованием Python в "
        "качестве основного языка программирования. Кроме того, у меня была возможность "
        "работать над проектами корпоративного уровня с использованием Java EE, будучи "
        "сотрудником крупнейшей телекоммуникационной компании в России.\n\n"
        "💼 Однако, мои навыки не ограничиваются только IT-сферой. У меня большой интерес "
        "к финансам и управлению, что привело меня к прохождению программы бизнес-школы "
        "в Южной Корее. Также, у меня есть опыт ведения небольшого строительного "
        "бизнеса, что подчеркивает мой предпринимательский и творческий дух.\n\n"
        "🤼‍ Спорт играет значительную роль в моей жизни, и я достиг впечатляющего результата, "
        "став кандидатом в мастера спорта по греко-римской борьбе до своего 15-летия. "
        "Я также увлекаюсь боксом и занимаюсь экстремальными видами спорта, так "
        "как они позволяют мне проявить свою авантюрную сторону.\n\n"
        "👫💍 В настоящее время я не женат, и мои планы на ближайшее будущее включают в "
        "себя поиск подходящего партнера, с которым я смогу построить здоровую и "
        "финансово независимую семью.\n\n"
        "🌍 Помимо профессиональных достижений, у меня есть страсть к путешествиям. "
        "Исследование новых культур и погружение в различные среды являются "
        "источником вдохновения для меня. Поэтому я открыт для возможностей переезда, "
        "соответствующих моим карьерным целям.\n\n"
        "🚀 Я надеюсь, что эта небольшая информация о моем опыте и интересах вызвала ваше "
        "любопытство. Если у вас есть интересное предложение, соответствующее моим "
        "навыкам и амбициям, я с нетерпением жду вашего лучшего предложения. Давайте "
        "вместе начнем путь к росту и успеху!\n\n"
        'Код этого бота <a href="https://github.com/valerii-chirkov/tg_anime_bot">здесь</a>'
    )


class CoreMessage:
    GET_MESSAGE_ROUTED_TO_ADMIN_EN = "Your message successfully sent to the admin!"
    GET_MESSAGE_TEXT = "User: @{username}\n" "Sent message: {text}"
    GET_USER_REQUEST_CV = "User: @{username} requested cv"
