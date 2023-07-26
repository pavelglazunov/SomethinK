AUTOMOD_AUTOMODS_BASE_IMPORTS = """
import disnake
from _____project_name_for_imports_____.utils.parser import parse_config

 """
AUTOMOD_AUTOMODS_IMPORT_RE = """
import re
 """
AUTOMOD_AUTOMODS_IMPORT_EMOJI = """
import emoji

 """
AUTOMOD_AUTOMODS_CONST = """
AUTOMOD_CONFIG: dict = parse_config("automod")


def message_in_ignore_channels(message: disnake.Message, automod_type: str) -> bool:
    if message.channel.id in AUTOMOD_CONFIG.get(f"{automod_type}_ignore_channels", []):
        return True
    return False


def message_author_role_is_allow(message: disnake.Message, automod_type: str):
    author_roles = message.author.roles
    allow_roles = AUTOMOD_CONFIG.get(f"{automod_type}_ignore_roles", [])

    if (message.author.guild.owner.id == message.author.id) and (-1 in allow_roles):
        return True
    for r in author_roles:
        if r.id in allow_roles:
            return True


 """
AUTOMOD_AUTOMODS_LINK = """
def link(message: disnake.Message):
    if message_in_ignore_channels(message, "links") or message_author_role_is_allow(message, "links"):
        return False
    return re.search("(?P<url>https?://(?!.*tenor\.com)[^\s]+)", message.content)


 """
AUTOMOD_AUTOMODS_SMILE = """
def smiles(message: disnake.Message):
    if message_in_ignore_channels(message, "smile") or message_author_role_is_allow(message, "links"):
        return False
    emojis_count = len(re.findall(r':[\w-]+:', emoji.demojize(message.content)))
    message_length = len(message.content) - emojis_count

    if message_length >= parse_config("automod.emoji_min_message_length") and (
            emojis_count / message_length * 100) >= parse_config("automod.emoji_min_percent"):
        return True
    return False


 """
AUTOMOD_AUTOMODS_CAPS = """
def caps(message: disnake.Message):
    if message_in_ignore_channels(message, "caps") or message_author_role_is_allow(message, "links"):
        return False
    message_length = len(message.content)
    caps_count = len([i for i in message.content if i.isupper()])
    if message_length >= parse_config("automod.caps_min_length") and (
            caps_count / message_length * 100) >= parse_config("automod.caps_min_percent"):
        return True
    return False


 """
AUTOMOD_AUTOMODS_MENTIONS = """
def mentions(message: disnake.Message):
    if message_in_ignore_channels(message, "mentions") or message_author_role_is_allow(message, "links"):
        return False
    mentions_count = len(re.findall(r'<@\d+>', emoji.demojize(message.content)))
    if mentions_count >= parse_config("automod.mentions_min_count"):
        return True
    return False


 """
AUTOMOD_AUTOMODS_MAIN_FUNC = """
def automod(message: disnake.Message) -> tuple[str, str, str] | bool:
     """
AUTOMOD_AUTOMODS_LINK_FUNC_CALL = """
    if link(message):
        return "ссылок", AUTOMOD_CONFIG.get("links"), "Использование ссылки в чате"
     """
AUTOMOD_AUTOMODS_SMILES_FUNC_CALL = """
    if smiles(message):
        return "смайликов", AUTOMOD_CONFIG.get("smiles"), "Слишком большая концентрация смайликов на одно сообщение"
     """
AUTOMOD_AUTOMODS_CAPS_FUNC_CALL = """
    if caps(message):
        return "капса", AUTOMOD_CONFIG.get("caps"), "Слишком большая концентрация заглавных букв на одно сообщение"
     """
AUTOMOD_AUTOMODS_MENTIONS_FUNC_CALL = """
    if mentions(message):
        return "упоминаний", AUTOMOD_CONFIG.get("mentions"), "Слишком большая концентрация упоминаний на одно сообщение"
"""
