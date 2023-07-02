import json
from disnake_bot.config import EVERYONE_ID


def get_command_allow_roles(command):
    with open("commands.json") as commands_file:
        commands = json.load(commands_file)
        return [int(i[1]) for i in commands[command]["roles"]] if commands[command]["roles"] else [EVERYONE_ID]


def get_command_allow_channels(command):
    with open("commands.json") as commands_file:
        commands = json.load(commands_file)
        return [int(i[1]) for i in commands[command]["channels"]] if commands[command]["channels"] else []
