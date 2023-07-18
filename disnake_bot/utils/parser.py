import json
from disnake_bot.config import EVERYONE_ID, CONFIG_JSON_FILENAME, MESSAGES_JSON_FILENAME
from disnake_bot.utils.decorators import edit_json


def get_command_allow_roles(command):
    with open("commands.json") as commands_file:
        commands = json.load(commands_file)
        return [int(i[1]) for i in commands[command]["roles"]] if commands[command]["roles"] else [EVERYONE_ID]


def get_command_allow_channels(command):
    with open("commands.json") as commands_file:
        commands = json.load(commands_file)
        return [int(i[1]) for i in commands[command]["channels"]] if commands[command]["channels"] else []


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
