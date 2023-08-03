UTILS_PARSER_IMPORTS = """
from config import CONFIG_JSON_FILENAME, MESSAGES_JSON_FILENAME
from utils.decorators import edit_json


 """
UTILS_PARSER_GET_ALLOW = """
def get_command_allow_roles(command):
    allowed_roles = parse_config(f"commands.{command}.roles")
    return allowed_roles if allowed_roles else [everyone_id]


def get_command_allow_channels(command):
    allowed_channels = parse_config(f"commands.{command}.channels")
    return allowed_channels if allowed_channels else []


 """
UTILS_PARSER_BASE = """

@edit_json(CONFIG_JSON_FILENAME)
def parse_config(key: str, data: dict):
    value = data
    for i in key.split("."):
        value = value[i]
    return value


@edit_json(CONFIG_JSON_FILENAME)
def edit_config(key: str, value, data: dict):
    keys = key.split('.')
    current = data
    for k in keys[:-1]:
        current = current[k]
    current[keys[-1]] = value
    return 0


@edit_json(MESSAGES_JSON_FILENAME)
def load_messages(data):
    return data
    
everyone_id = parse_config("roles_ID.everyone_id")
"""
