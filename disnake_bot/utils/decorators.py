import json

from disnake.ext import commands
import disnake


def allowed_channels(*channels) -> bool:
    async def predicate(ctx: disnake.ApplicationCommandInteraction):
        print("channels> ", channels)
        if not channels:  # если список каналов пустой, выполняем команду всегда
            return True
        if ctx.channel.id in channels:
            return True
        else:
            return False

    return commands.check(predicate)


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
