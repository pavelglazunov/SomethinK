from disnake_bot.utils.parser import parse_config
import re
import disnake
import emoji


def link(message: str):
    return re.search("(?P<url>https?://[^\s]+)", message)


def smiles(message: str):
    emojis_count = len(re.findall(r':[\w-]+:', emoji.demojize(message)))
    message_length = len(message) - emojis_count

    if message_length >= parse_config("automod.emoji_min_message_length") and (
            emojis_count / message_length * 100) >= parse_config("automod.emoji_min_percent"):
        return True
    return False


def caps(message: str):
    message_length = len(message)
    caps_count = len([i for i in message if i.isupper()])
    if message_length >= parse_config("automod.caps_min_length") and (
            caps_count / message_length * 100) >= parse_config("automod.caps_min_percent"):
        return True
    return False


def mentions(message: str):
    mentions_count = len(re.findall(r'<@\d+>', emoji.demojize(message)))
    print(mentions_count)

    if mentions_count >= parse_config("automod.mentions_min_count"):
        return True
    return False


def automod(message) -> tuple[str, str, str] | bool:
    if link(message): return "ссылки", parse_config("automod.links"), "Использование ссылки в чате"
    if smiles(message): return "смайлики", parse_config(
        "automod.smiles"), "Слишком большая концентрация смайликов на одно сообщение"
    if caps(message): return "капс", parse_config(
        "automod.caps"), "Слишком большая концентрация заглавных букв на одно сообщение"
    if mentions(message): return "упоминания", parse_config(
        "automod.mentions"), "Слишком большая концентрация упоминаний на одно сообщение"
    return False
