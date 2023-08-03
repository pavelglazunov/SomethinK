UTILS_EVENT_LOGGING_FILE = """

import datetime

from config import LOGGING_EVENT_TYPES
import disnake


async def log(ctx: disnake.ApplicationCommandInteraction, event_name, event_type, error=None, **kwargs):
    if not (event_type in LOGGING_EVENT_TYPES):
        return
    from utils.parser import parse_config

    if event_type in ("commands", "auto_response", "ERROR"):
        author = f"{ctx.author.name} ({ctx.author.id})"
        channel = f"{ctx.channel.name} ({ctx.channel.id})"
    else:
        author = "bot"
        channel = "None (const from config)"

    if event_type in ("join", "leave", "auto_response"):
        channel_to_send = ctx
    else:
        channel_to_send = ctx.guild.get_channel(parse_config("channels_ID.logging_channel_id"))

    log_data = f"{datetime.datetime.now()} -- " \
               f"type: {event_type} | " \
               f"name: {event_name} | " \
               f"author: {author} | " \
               f"channel: {channel} | "

    for i in kwargs:
        log_data += f"Argument: {i} = {kwargs[i]} | "

    log_data += f"errors: {error}"

    await channel_to_send.send(log_data)
    print(log_data)
    return True
"""
