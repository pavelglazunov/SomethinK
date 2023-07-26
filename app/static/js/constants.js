const ALL_COMMANDS = {
    "ban": "заблокировать пользователя",
    "unban": "разблокировать пользователя",
    "mute": "выключить микрофон пользователю",
    "unmute": "включить микрофон пользователю",
    "chatmute": "выключить пользователю возможность писать в чат",
    "chatunmute": "включить пользователю возможность писать в чат",
    "timeout": "выдать пользователю таймаут",
    "rmtimeout": "удалить таймаут у пользователя",
    "fullban": "заблокировать пользователя и удалить все его сообщения",
    "clear": "удалить сообщения",
    "afk": "переместить пользователя в AFK канал",
    "warn": "выдать предупреждение пользователю",
    "report": "отправить жалобу на пользователя",
    "warns": "посмотреть список предупреждений пользователя",
    "move": "переместить пользователя в другой голосовой канал",
    "rmwarn": "снять предупреждение с пользователя",
    "deafen": "выключить звук пользователю",
    "addrole": "выдать роль пользователю",
    "undeafen": "включить звук у пользователя",
    "rmrole": "забрать роль у пользователя",
    "ping": "посмотреть пинг сервера и бота",
    "slowmode": "включить/выключить медленный режим",
    "kick": "выгнать пользователя",
    "vkick": "отключить пользователя от голосового канала",
    "links": "бот будет реагировать на сообщения с ссылками",
    "smile": "бот будет реагировать на сообщения со смайликами, если выполняются условия, указанные ниже",
    "caps": "бот будет реагировать на сообщения с капсом, если выполняются условия, указанные ниже",
    "mentions": "бот будет реагировать на сообщения с повторяющимися упоминаниями, если выполняются условия, указанные ниже",
    "ar_update": "включить/выключить обновление ролей активности",
    "add_yt": "добавить отслеживание ютуб канала",
    "rm_yt": "удалить отслеживание ютуб канала",
    "add_tw": "добавить отслеживание твич канала",
    "rm_tw": "удалить отслеживание твич канала",
    "color": "поменять цвет имени на сервере",
    "nick": "поменять имя на сервере",
    "joke": "случайная шутка",
    "weather": "актуальная погода",
    "translate": "перевести текст",
    "say": "написать сообщения от имени бота",
    "avatar": "получить аватар пользователя",
    "gpt": "общения с chatGPT",
    "embed": "создать embed",
    "feedback": "создать приглашение на сервер",
}
const ACTIVITY_ROLES = [
    ["Dota 2", "Counter-Strike: Global Offensive"],
    ["VALORANT", "Minecraft"],
    ["League of Legends", "Fortnite"]]
    // ["league of legends", "IntelJS"],
    // ["minecraft", "WebStorm"],
    // ["fortnite", "PhpStorm"]]
const ACTIVITY_ROLES_COLORS = {
    "Counter-Strike: Global Offensive": "BFC204",
    "VALORANT": "F44B34",
    "Dota 2": "27A008",
    "League of Legends": "1698C1",
    "Minecraft": "2BF227",
    "Fortnite": "EE27F2",
}
const COMMANDS = [
    ["ban", "unban"],
    ["kick", "vkick"],
    ["mute", "unmute"],
    ["chatmute", "chatunmute"],
    ["timeout", "rmtimeout"],
    ["fullban", "clear"],
    ["afk", "warn"],
    ["report", "warns"],
    ["move", "rmwarn"],
    ["deafen", "addrole"],
    ["undeafen", "rmrole"],
    ["ping", "slowmode"],
]
const COMMANDS_DESCRIPTIONS = {
    "ban": "заблокировать пользователя",
    "unban": "разблокировать пользователя",
    "mute": "выключить микрофон пользователю",
    "unmute": "включить микрофон пользователю",
    "chatmute": "выключить пользователю возможность писать в чат",
    "chatunmute": "включить пользователю возможность писать в чат",
    "timeout": "выдать пользователю таймаут",
    "rmtimeout": "удалить таймаут у пользователя",
    "fullban": "заблокировать пользователя и удалить все его сообщения",
    "clear": "удалить сообщения",
    "afk": "переместить пользователя в AFK канал",
    "warn": "выдать предупреждение пользователю",
    "report": "отправить жалобу на пользователя",
    "warns": "посмотреть список предупреждений пользователя",
    "move": "переместить пользователя в другой голосовой канал",
    "rmwarn": "снять предупреждение с пользователя",
    "deafen": "выключить звук пользователю",
    "addrole": "выдать роль пользователю",
    "undeafen": "включить звук у пользователя",
    "rmrole": "забрать роль у пользователя",
    "ping": "посмотреть пинг сервера и бота",
    "slowmode": "включить/выключить медленный режим",
    "kick": "выгнать пользователя",
    "vkick": "отключить пользователя от голосового канала",
    "links": "бот будет реагировать на сообщения с ссылками",
    "smile": "бот будет реагировать на сообщения со смайликами, если выполняются условия, указанные ниже",
    "caps": "бот будет реагировать на сообщения с капсом, если выполняются условия, указанные ниже",
    "mentions": "бот будет реагировать на сообщения с повторяющимися упоминаниями, если выполняются условия, указанные ниже",
    "logon": "включить логирование",
    "logoff": "выключить логирование",
}
const COMMANDS_WITH_API_TOKEN = {
    "gpt": ["для работы этой команды нужен API токен openAI", "https://ai-journal.ru/chatgpt-api-%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%BA%D0%BB%D1%8E%D1%87/"],
    "weather": ["для работы этой команды нужен API токен Weather", "https://www.weatherapi.com/"]
}

const COMMAND_WITH_SPECIAL_FORM = {
    // "afk": ["voice", "канал, куда будет перемещен пользователь"],
    "report": ["text", "канал, куда будут приходить жалобы"]
}
const AUTO_MODERATION = [
    [["links", "ссылки"], ["caps", "капс"]],
    [["smile", "эмодзи"], ["mentions", "упоминания"]]]


const SM_COMMANDS = [
    ["add_yt", "rm_yt"],
    ["add_tw", "rm_tw"]
]

const LOGGING_COMMANDS = ["logon", "logoff"]