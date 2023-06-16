
"""


- help                                      -       зависит от сборки
- helpmoder (при необходимости)             -       зависит от сборки
- helpadmin (при необходимости)             -       зависит от сборки
- SomethinK                                 +

Административные команды
- ban                                       +
- unban                                     +
- kick                                      +
- mute                                      +
- unmute                                    +
- chatmute                                  +
- chatunmute                                +
- report                                    -
- clear                                     +
- afk                                       -
- warn                                      +
- warnings                                  +
- warnclear                                 +
- addrole                                   -
- rmrole                                    -
- ping                                      -
- fullban
- timeout
- rmtimeout
- deafen/undeafen
- move
- vkick
- slowmode

Отправка сообщений
- отправка по времени                       -
- кастомные триггеры
- фильтрация чата                           -
- обработчик событий    (join, leave)



Социальные сети
- подключение твич/ютуб                     -

Дополнительный команды
- color                                     -
- nick                                      -
- mem - случайный мем                       - ?????
- joke - случайная шутка                    -
- поиск в интернете                         -
- погода                                    -
- переводчик                                -
- say
- invite
- avatar
- распознавание математических действий     -
- chatGPT
- статистика сервера


настройки
- status (установка статуса бота)
- логирование                               -
-- logging_on                               +
-- logging_off                              +

Авто-выдача ролей
- при заходе на сервер                      -
- при какой-нибудь активности               -

# Игры с ботом
# - загадки                                   -
# - камень, ножницы, бумага                   -
# -

?
 /activedevbadge - включение режима разработчика

==========================================================
заносить новых пользователей в варн лист









{
    "user_id": {

                }
}
"""
json_format = {
    "user_id":
        {
            "bot_settings": {
                "name": "name",
                "token": "token",
                "status": "status",
                "prefix": "prefix"
            },
            "channels_id": {
                "moderation": "id",
                "logging": "id",
                "afk": "id",
                "warnings": "id"
            },
            "roles_id": {
                "moderation": "id",
            },
            "commands":
                {
                    "moderation": {
                        "logging_commands": True,
                        "command_name": {
                            "trigger": "trigger",
                            "description": "description",
                            "allowed_roles": ["role1", "role2"],
                            "allowed_channels": ["channel1", "channel2"],

                        }
                    },
                    "messages": {
                        "time_messages": {
                            "id1": {
                                "text": "text",
                                "time": "time",
                                "delta": "delta"
                            },
                            "id2": {...}
                        },
                        "autoresponder": {
                            "id1_text": {
                                "trigger": "trigger",
                                "trigger_type": "START WITH",
                                "message_type": "message",
                                "message_data": {
                                    "text": "text",
                                    "author": "",
                                    "thumbnail_url": "",
                                    "title": "",
                                    "image_url": "",
                                    "footer": "",
                                    "embed_url": ""
                                }
                            },
                            "id2_embed": {
                                "trigger": "trigger",
                                "trigger_type": "START WITH",
                                "message_type": "embed",
                                "message_data": {
                                    "text": "text",
                                    "author": "author",
                                    "thumbnail_url": "url",
                                    "title": "title",
                                    "image_url": "url",
                                    "footer": "footer",
                                    "embed_url": "url"
                                }

                            }
                        }
                    },

                }
        }
}


url = """
https://ru.stackoverflow.com/questions/1496542/python-disnake-%D0%B4%D0%B8%D1%81%D0%BA%D0%BE%D1%80%D0%B4-%D0%B1%D0%BE%D1%82

"""



