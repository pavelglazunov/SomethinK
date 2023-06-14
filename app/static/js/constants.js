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
    "ar_update": "включить/выключить обновление ролей активности"
}
const ACTIVITY_ROLES = [
    ["cs:go", "visual studio"],
    ["valorant", "PyCharm"],
    ["dota 2", "clion"],
    ["league of legends", "IntelJS"],
    ["minecraft", "WebStorm"],
    ["fortnite", "PhpStorm"]]
const ACTIVITY_ROLES_COLORS = {
    "csgo": "BFC204",
    "visualstudio": "318DFA",
    "valorant": "F44B34",
    "pycharm": "59FA31",
    "dota2": "27A008",
    "clion": "31FABE",
    "leagueoflegends": "1698C1",
    "inteljs": "0048D3",
    "minecraft": "2BF227",
    "webstorm": "0E54DC",
    "fortnite": "EE27F2",
    "phpstorm": "9A0CCC",
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
}
const COMMAND_WITH_SPECIAL_FORM = {
    "afk": ["voice", "канал, куда будет перемещен пользователь"],
    "report": ["text", "канал, куда будут приходить жалобы"]
}
const AUTO_MODERATION = [
    [["links", "ссылки"], ["caps", "капс"]],
    [["smile", "эмодзи"], ["mentions", "упоминания"]]]

