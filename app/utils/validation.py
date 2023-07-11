import json

# from shlex import quote

"""
Валидация данных, полученных в JSON с сайта

коды ошибок

код  | ошибка
100 -> ошибка преобразования в JSON  
101 -> ошибка преобразования в integer
102 -> ошибка преобразования в boolean
103 -> ошибка преобразования в string
104 -> ошибка преобразования в float

200 -> неизвестная команда
201 -> ошибка в описании
202 -> ошибка в списке ролей
 ->   
 ->   
 ->   

тип данных: 

"""
ALL_COMMANDS = ['ban', 'unban', 'mute', 'unmute', 'chatmute', 'chatunmute', 'timeout', 'rmtimeout', 'fullban', 'clear',
                'afk', 'warn', 'report', 'warns', 'move', 'rmwarn', 'deafen', 'addrole', 'undeafen', 'rmrole', 'ping',
                'slowmode', 'kick', 'vkick', 'links', 'smile', 'caps', 'mentions', 'ar_update', 'add_yt', 'rm_yt',
                'add_tw', 'rm_tw', "ignore_admin", "ignore_bot"]


def on_error(error_code):
    def decorator(func):
        def wrapper(*args):
            try:
                func(*args)
                return 0
            except Exception:
                return error_code

        return wrapper

    return decorator


@on_error(100)
def _json(data):
    json.dumps(data)


@on_error(101)
def _int(data):
    int(data)


@on_error(102)
def _boolean(data):
    bool(data)


@on_error(103)
def _string(data):
    str(data)


@on_error(104)
def _float(data):
    float(data)


def _length(data, length):
    return len(data) <= length


def moderation(data: dict):
    if code := _json(data) != 0: return code
    # data = json.dumps(data)
    # data = dict(data)

    print("==== START MODERATION VALIDATION ====")
    if not all([i in ALL_COMMANDS for i in data.keys()]): return 101
    for k, v in data.items():
        if code := _boolean(data) != 0: return code
        # if not (v["description"] or len(v["description"].split()) != 0 or _length(v["description"], 200)): return 103
        # if not all([_int(i[1]) for i in v["roles"]]) and v["roles"]: return


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

if __name__ == '__main__':
    with open("../test_json1.json", encoding="utf-8") as file:
        _data: dict = json.load(file)

        print(_data["moderation"])
        for i in _data:
            if _code := VALIDATION[i](_data[i]):
                print(_code)
