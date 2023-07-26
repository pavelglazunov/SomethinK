UTILS_DECORATORS_IMPORTS = """
import json

from disnake.ext import commands
import disnake


 """
UTILS_DECORATORS_COMMAND_ALLOW_CHANNELS = """

def allowed_channels(*channels):
    async def predicate(ctx: disnake.ApplicationCommandInteraction):
        if not channels:
            return True
        if ctx.channel.id in channels:
            return True
        else:
            return False

    return commands.check(predicate)


def allowed_roles(*roles):
    async def predicate(ctx: disnake.ApplicationCommandInteraction):
        if not roles:
            return True
        if -1 in roles and (ctx.guild.owner == ctx.author):
            return True
        for r in ctx.user.roles:
            if r.id in roles:
                return True
        else:
            return False

    return commands.check(predicate)

 """
UTILS_DECORATORS_BASE = """

def edit_json(json_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(f"data/{json_name}.json", encoding="utf-8") as file:
                data = json.load(file)

            result = func(*args, data)

            with open(f"data/{json_name}.json", mode="w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False)

            return result

        return wrapper

    return decorator
"""
