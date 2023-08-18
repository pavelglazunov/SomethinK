
import asyncio
from disnake.ext import commands
from utils.parser import parse_config

 
from .activity_roles import start_activity_roles_updating

 
async def create_all_async_process(bot: commands.Bot):
    tasks = []
     
    tasks.append(asyncio.create_task(start_activity_roles_updating(bot=bot)))

     
    await asyncio.gather(*tasks)
