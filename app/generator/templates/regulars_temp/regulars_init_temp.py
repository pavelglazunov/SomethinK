REGULARS_INIT_BASE_IMPORTS = """
import asyncio
from disnake.ext import commands
from _____project_name_for_imports_____.utils.parser import parse_config

 """
REGULARS_INIT_MESSAGES_IMPORT = """
from .messages import regular_message

 """
REGULARS_INIT_ACTIVITY_ROLES_IMPORT = """
from .activity_roles import start_activity_roles_updating

 """
REGULARS_INIT_SOCIAL_MEDIA_YOUTUBE = """
from .social_medias import check_youtube

 """
REGULARS_INIT_SOCIAL_MEDIA_TWITCH = """
from .social_medias import check_twitch


 """
REGULARS_INIT_CRATE_ALL_ASYNC = """
async def create_all_async_process(bot: commands.Bot):
    tasks = []
     """
REGULARS_INIT_ADD_PROCESS_REGULAR_MESSAGE = """
    for r_message in parse_config("regular_messages"):
        tasks.append(asyncio.create_task(regular_message(bot=bot, message_data=r_message)))

     """
REGULARS_INIT_ADD_PROCESS_YOUTUBE = """
    for yt in parse_config("social_media_notifications.youtube"):
        tasks.append(asyncio.create_task(check_youtube(bot=bot, yt_data=yt)))

     """
REGULARS_INIT_ADD_PROCESS_TWITCH = """
    delay = 0
    for tw in parse_config("social_media_notifications.twitch"):
        tasks.append(asyncio.create_task(check_twitch(bot=bot, tw_data=tw, delay=delay)))
        delay += 2

     """
REGULARS_INIT_ADD_PROCESS_ACTIVITY_ROLES_UPDATE = """
    tasks.append(asyncio.create_task(start_activity_roles_updating(bot=bot)))

     """
REGULARS_INIT_PUSH_PROCESS = """
    await asyncio.gather(*tasks)
"""
