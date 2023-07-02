import json
# from shlex import quote

"""
Валидация данных, полученных в JSON с сайта

коды ошибок

код  | ошибка
100 -> ошибка преобразования в JSON  
101 -> неизвестная команда
102 -> ошибка преобразования в boolean
103 -> ошибка в описании
104 -> ошибка в списке ролей
 ->   
 ->   
 ->   

тип данных: 

"""
ALL_COMMANDS = ['ban', 'unban', 'mute', 'unmute', 'chatmute', 'chatunmute', 'timeout', 'rmtimeout', 'fullban', 'clear',
                'afk', 'warn', 'report', 'warns', 'move', 'rmwarn', 'deafen', 'addrole', 'undeafen', 'rmrole', 'ping',
                'slowmode', 'kick', 'vkick', 'links', 'smile', 'caps', 'mentions', 'ar_update', 'add_yt', 'rm_yt',
                'add_tw', 'rm_tw', "ignore_admin", "ignore_bot"]


def _json(data):
    try:
        json.dumps(data)
        return True
    except Exception:
        return False


def _boolean(data):
    try:
        bool(data)
        return True
    except TypeError:
        return False


def _int(data):
    try:
        int(data)
        return True
    except Exception:
        return False


def _length(data, length):
    return len(data) <= length


def moderation(data: dict):
    if not _json(data): return 100
    # data = json.dumps(data)
    # data = dict(data)
    print(all([i in ALL_COMMANDS for i in data.keys()]), [i in ALL_COMMANDS for i in data.keys()])
    print(data.keys())
    print(data)
    print("==== START VALIDATION ====")
    if not all([i in ALL_COMMANDS for i in data.keys()]): return 101
    for k, v in data.items():
        print(v)
        if not _boolean(v["enable"]): return 102
        print(">>", k)
        print(k, "|", v["description"], len(v["description"].split()), _length(v["description"], 200))
        if not (v["description"] or len(v["description"].split()) != 0 or _length(v["description"], 200)): return 103
        if not all([_int(i[1]) for i in v["roles"]]) and v["roles"]: return

        # v["description"] = quote(v["description"])
        print(v["description"])


def roles(data):
    return False


def messages(data):
    return False


def another(data):
    return False


def social_media(data):
    return False


def customization(data):
    return False


def settings(data):
    return False

VALIDATION = {
    "moderation": moderation,
    "roles": roles,
    "messages": messages,
    "another": another,
    "social_media": social_media,
    "customization": customization,
    "settings": settings
}
