
import asyncio
from disnake.ext import commands
from utils.parser import parse_config

 
from .social_medias import check_youtube

 
async def create_all_async_process(bot: commands.Bot):
    tasks = []
     
    for yt in parse_config("social_media_notifications.youtube"):
        tasks.append(asyncio.create_task(check_youtube(bot=bot, yt_data=yt)))

     
    await asyncio.gather(*tasks)
