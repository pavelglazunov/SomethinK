UTILS_WARNINGS_IMPORTS = """

import datetime

from utils.decorators import edit_json
from config import WARNING_JSON_FILENAME


 """
UTILS_WARNINGS_ADD_WARNING = """

@edit_json(WARNING_JSON_FILENAME)
def add_warning(user, author, reason, data: dict):
    user_warnings = data.get(user, [])
    user_warnings.append({
        "id": len(user_warnings),
        "reason": reason,
        "from": author,
        "time": str(datetime.datetime.now())
    })
    data[user] = user_warnings


 """
UTILS_WARNINGS_REMOVE_WARNINGS = """

@edit_json(WARNING_JSON_FILENAME)
def remove_warnings(user, index, data):
    index -= 1
    user_warns: list = data.get(user, [])
    if index == -1:
        user_warns.clear()
        warn = "Все предупреждения успешно сняты"
    else:
        w = user_warns.pop(index)
        warn = f"Предупреждение {w['id']} ({w['reason']}) успешно удалено"

    data[user] = user_warns
    return warn


 """
UTILS_WARNINGS_GET_WARNINGS = """

@edit_json(WARNING_JSON_FILENAME)
def get_user_warnings(user, data):
    return data.get(user, [])
"""
