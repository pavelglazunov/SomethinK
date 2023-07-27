BASE_CONFIG = {
    "another": {
        "avatar": {
            "channels": [],
            "description": "получить аватар пользователя",
            "enable": False,
            "roles": []
        },
        "color": {
            "channels": [],
            "description": "поменять цвет имени на сервере",
            "enable": False,
            "roles": []
        },
        "embed": {
            "channels": [],
            "description": "создать embed",
            "enable": False,
            "roles": []
        },
        "feedback": {
            "channels": [],
            "description": "создать приглашение на сервер",
            "enable": True,
            "roles": []
        },
        "gpt": {
            "channels": [],
            "description": "общения с chatGPT",
            "enable": False,
            "roles": [],
            "token": ""
        },
        "joke": {
            "channels": [],
            "description": "случайная шутка",
            "enable": False,
            "roles": []
        },
        "nick": {
            "channels": [],
            "description": "поменять имя на сервере",
            "enable": False,
            "roles": []
        },
        "say": {
            "channels": [],
            "description": "написать сообщения от имени бота",
            "enable": False,
            "roles": []
        },
        "translate": {
            "channels": [],
            "description": "перевести текст",
            "enable": False,
            "roles": []
        },
        "weather": {
            "channels": [],
            "description": "актуальная погода",
            "enable": False,
            "roles": [],
            "token": ""
        }
    },
    "customization": {},
    "messages": {
        "auto_response": {},
        "events": {},
        "time_message": {}
    },
    "moderation": {
        "addrole": {
            "channels": [],
            "description": "выдать роль пользователю",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "afk": {
            "channels": [],
            "description": "переместить пользователя в AFK канал",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "ban": {
            "channels": [],
            "description": "заблокировать пользователя",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "caps": {
            "action": "--send",
            "channels": [],
            "description": "бот будет реагировать на сообщения с капсом, если выполняются условия, указанные ниже",
            "enable": True,
            "min_length": 20,
            "percent": 80,
            "roles": []
        },
        "chatmute": {
            "channels": [],
            "description": "выключить пользователю возможность писать в чат",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "chatunmute": {
            "channels": [],
            "description": "включить пользователю возможность писать в чат",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "clear": {
            "channels": [],
            "description": "удалить сообщения",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "deafen": {
            "channels": [],
            "description": "выключить звук пользователю",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "fullban": {
            "channels": [],
            "description": "заблокировать пользователя и удалить все его сообщения",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "kick": {
            "channels": [],
            "description": "выгнать пользователя",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "links": {
            "action": "--send",
            "channels": [],
            "description": "бот будет реагировать на сообщения с ссылками",
            "enable": True,
            "roles": []
        },
        "mentions": {
            "action": "--send",
            "channels": [],
            "count": 3,
            "description": "бот будет реагировать на сообщения с повторяющимися упоминаниями, если выполняются условия, указанные ниже",
            "enable": True,
            "roles": []
        },
        "move": {
            "channels": [],
            "description": "переместить пользователя в другой голосовой канал",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "mute": {
            "channels": [],
            "description": "выключить микрофон пользователю",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "ping": {
            "channels": [],
            "description": "посмотреть пинг сервера и бота",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "report": {
            "channels": [],
            "description": "отправить жалобу на пользователя",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ],
            "special_channel": "-1"
        },
        "rmrole": {
            "channels": [],
            "description": "забрать роль у пользователя",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "rmtimeout": {
            "channels": [],
            "description": "удалить таймаут у пользователя",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "rmwarn": {
            "channels": [],
            "description": "снять предупреждение с пользователя",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "slowmode": {
            "channels": [],
            "description": "включить/выключить медленный режим",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "smile": {
            "action": "--send",
            "channels": [],
            "description": "бот будет реагировать на сообщения со смайликами, если выполняются условия, указанные ниже",
            "enable": True,
            "min_length": 20,
            "percent": 80,
            "roles": []
        },
        "timeout": {
            "channels": [],
            "description": "выдать пользователю таймаут",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "unban": {
            "channels": [],
            "description": "разблокировать пользователя",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "undeafen": {
            "channels": [],
            "description": "включить звук у пользователя",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "unmute": {
            "channels": [],
            "description": "включить микрофон пользователю",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "vkick": {
            "channels": [],
            "description": "отключить пользователя от голосового канала",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "warn": {
            "channels": [],
            "description": "выдать предупреждение пользователю",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        },
        "warns": {
            "channels": [],
            "description": "посмотреть список предупреждений пользователя",
            "enable": True,
            "roles": [
                [
                    "Владелец сервера",
                    "-1"
                ]
            ]
        }
    },
    "roles": {
        "Counter-Strike: Global Offensive": {
            "enable": False,
            "value": "#BFC204"
        },
        "Dota 2": {
            "enable": False,
            "value": "#27A008"
        },
        "Fortnite": {
            "enable": False,
            "value": "#EE27F2"
        },
        "League of Legends": {
            "enable": False,
            "value": "#1698C1"
        },
        "Minecraft": {
            "enable": False,
            "value": "#2BF227"
        },
        "VALORANT": {
            "enable": False,
            "value": "#F44B34"
        },
        "ar_enable": False,
        "start_roles": {
            "roles": []
        },
        "update_interval": "5"
    },
    "settings": {
        "logging": {
            "channel_id": "-1",
            "enable": True,
            "values": [
                "auto_moderation",
                "commands"
            ]
        },
        "status": {
            "text": "в бота от SomethinK",
            "type": "playing"
        }
    },
    "social_media": {
        "twitch": {},
        "youtube": {}
    }
}
