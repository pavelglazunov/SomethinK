import asyncio

from disnake.ext import commands

from .messages import regular_message
from .activity_roles import start_activity_roles_updating
from .social_medias import check_youtube, check_twitch

from disnake_bot.utils.parser import parse_config


async def create_all_async_process(bot: commands.Bot):
    tasks = []
    for r_message in parse_config("regular_messages"):
        tasks.append(asyncio.create_task(regular_message(bot=bot, message_data=r_message)))

    for yt in parse_config("social_media_notifications.youtube"):
        tasks.append(asyncio.create_task(check_youtube(bot=bot, yt_data=yt)))

    delay = 0
    for tw in parse_config("social_media_notifications.twitch"):
        tasks.append(asyncio.create_task(check_twitch(bot=bot, tw_data=tw, delay=delay)))
        delay += 2

    tasks.append(asyncio.create_task(start_activity_roles_updating(bot=bot)))

    await asyncio.gather(*tasks)
