import datetime

from disnake_bot.config import LOGGING_EVENT_TYPES
import disnake


def logging_to_file(data):
    pass


def logging_to_special_channel(data):
    pass


def logging_to_audit(data):
    pass


LOGGING_TYPES = {
    "audit": logging_to_audit,
    "file": logging_to_file,
    "channel": logging_to_special_channel
}


def log(ctx, event_name, event_type, error=None):
    if not (event_type in LOGGING_EVENT_TYPES):
        return
    from disnake_bot.utils.parser import parse_config

    logging_type = parse_config("logging")
    if logging_type == "off":
        return

    if event_type in ("commands", "auto_response"):
        author = f"{ctx.author.name} ({ctx.author.id})"
        channel = f"{ctx.channel.name} ({ctx.channel.id})"
    else:
        author = "bot"
        channel = "None (const from config)"
    # for logg_type in logging_type.split("+"):
    log_data = f"{datetime.datetime.now()} -- " \
               f"type: {event_type} | " \
               f"name: {event_name} | " \
               f"author: {author} | " \
               f"channel: {channel} | " \
               f"errors: {error}"

    print(log_data)
    return True
