# TODO добавить ограничение на запросы save в минут


# TODO валидация данных
# TODO отсеивание команд
# TODO исправить регистрацию через тг, добавить лимит по времени
# TODO добавить команду выключатель отслеживания команд в личных сообщениях
# TODO добавить команду feedback для обратной связи
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



все команды нужно реализовать через слэш -> @bot.slash_command(name="command", description="amogus")
в команды могут передаваться аргументы, если перед аргументом стоит ?, то от считается необязательным

-- отдельные команды с обычным вводом/выводом --
/ban <member> <?reason> -> бан участника
/unban <member> <?reason> -> снять бан с участника
/mute <member> <?reason> -> мут участника
/unmute <member> <?reason> -> снять мут участника
/chatmute <member> <?reason> -> мут участника вс чате
/chatunmute <member> <?reason> -> снять мут участника вс чате
/timeout <member> <time> <?reason> -> выдать таймаут участнику
/rmtimeout <member> <?reason> -> удалить таймаут у участнику
/fullban <member> <?reason> -> бан + удалить все сообщения пользователя
/clear <count>  -> удалить count сообщений
/afk <member> -> переместить участника в афк канал (id афк канала находиться в файле config.py в переменной AFK_CHANNEL_ID)
/move <member> <channel> ->  переместить участника в указанный канал
/deafen <member> <?reason> -> выключить звук пользователю
/undeafen <member> <?reason> -> включить звук пользователю
/addrole <member> <role> -> выдать роль пользователю
/rmrole <member> <role> -> забрать роль у пользователя
/ping -> вывести ping сервера и бота
/slowmode <status> -> включить/выключить медленный режим в статусе реализовать выбор on/off соответственно
/vkick <member> <?reason> -> исключить пользователя из голосового канала
/ar_update <interval: int>  -> изменить значение ar_interval в файле data/config.json на введенное, сохранить изменения
/color <color> -> изменить цвет имени в чате (выдача (при необходимости создание) роли с указанным цветом)
/nick <name> -> изменить имя в чате
/joke -> случайная шутка
/weather <city> -> получение погоды из указанного города через сайты с открытым API, API ключ храниться в файле config.py в переменной WEATHER_API_KEY
/gpt <text> -> обращение к chatGPT, API ключ храниться в файле config.py в переменной CHATGPT_API_KEY
/translate <from> <to> <text> -> перевод текста с языка from на to, при необходимости можно использовать API
/say <text> -> написать текст от имени бота
/avatar <member> -> получить аватар пользователя


-- команды, которые взаимодействуют друг с другом --
/warn <member> <?reason> -> выдать предупреждение пользователю, все предупреждения хранятся в data/user_warnings.json в формате:
    {
        user1: [
            {
                "text": "текст предупреждения",
                "time": "точное время выдачи",
                "from": "кем выдано"
            }]
    }
/warns <member> -> просмотр всех предупреждений пользователя
/rmwarn <member> -> снять все предупреждения с пользователя

-- команды с окном ввода --
команды ниже использую всплывающие окна для ввода информации, документация по таким окнам: https://guide.disnake.dev/interactions/modals
/report -> в всплывающем окне запрашиваются: имя отправителя, на кого отправить жалобу и текст сообщения, после этого оформленный embed с этими данными отправляется в специальный канал (id канала находиться в файле config.py в переменной REPORT_CHANNEL_ID)
/embed -> в всплывающем окне запрашиваются: заголовок, тело, автор, цвет (в любом формате), текст футера, после чего команда отправляет готовый embed


-- не команды --
нужно реализовать функционал авто модерации, при обнаружении выполнять одно из действий ниже
возможные действия:
--send -> удалить сообщение, сохранив его текст в data/waiting_messages.json, отправить сообщение в специальный канал (ID канала находиться в файле config.py в переменной WAITING_MESSAGES_CHANNEL_ID),
к сообщению добавить кнопки "удалить" и "одобрить", которые будут удалять сообщение из waiting_messages.json или отправлять сообщения в первоначальный канал, удаляя из waiting_messages.json соответственно
--remove -> удалить сообщение
--warn -> выдать предупреждение пользователю
--remove-warn -> удалить сообщение и выдать предупреждение пользователю

авто модерация:
1) проверка всех сообщений на наличие ссылок в них. При обнаружение ссылки выполнить одно из действий выше, действие указанно в config.py в переменной LINKS_DETECT_ACTION
игнорировать сообщения из каналов, указанных в config.py в списке IGNORE_LINKS_CHANNELS
игнорировать сообщения пользователей, указанных в config.py в списке IGNORE_LINKS_ROLES
2) проверка всех сообщений на наличие смайликов в них. Если длина сообщения больше EMOJI_MIN_MESSAGE_LENGTH (config.py) и процент эмодзи больше чем EMOJI_MIN_PERCENT (config.py) выполнить одно из действий выше, действие указанно в config.py в переменной EMOJI_DETECT_ACTION
игнорировать сообщения из каналов, указанных в config.py в списке IGNORE_EMOJI_CHANNELS
игнорировать сообщения пользователей, указанных в config.py в списке IGNORE_EMOJI_ROLES
3) проверка всех сообщений на наличие капса в них. Если длина сообщения больше CAPS_MIN_MESSAGE_LENGTH (config.py) и процент эмодзи больше чем CAPS_MIN_PERCENT (config.py) выполнить одно из действий выше, действие указанно в config.py в переменной CAPS_DETECT_ACTION
игнорировать сообщения из каналов, указанных в config.py в списке IGNORE_CAPS_CHANNELS
игнорировать сообщения пользователей, указанных в config.py в списке IGNORE_CAPS_ROLES
4) проверка всех сообщений на наличие упоминаний пользователей или каналов в них. Если количество упоминаний больше чем MENTIONS_MIN_COUNT (config.py) выполнить одно из действий выше, действие указанно в config.py в переменной MENTION_DETECT_ACTION
игнорировать сообщения из каналов, указанных в config.py в списке IGNORE_MENTIONS_CHANNELS
игнорировать сообщения пользователей, указанных в config.py в списке IGNORE_MENTIONS_ROLES





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



