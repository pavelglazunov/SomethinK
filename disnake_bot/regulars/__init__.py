import asyncio
import concurrent.futures
import threading

from .messages import regular_message
from .activity_roles import start_activity_roles_updating
from disnake.ext import commands
from disnake_bot.utils.parser import parse_config
from threading import Thread


async def create_all_async_process(bot: commands.Bot):
    tasks = []
    for r_message in parse_config("regular_messages"):
        tasks.append(asyncio.create_task(regular_message(bot=bot, message_data=r_message)))
        print("task added")
    # print(bot.guilds[0].members)
    tasks.append(asyncio.create_task(start_activity_roles_updating(bot=bot)))

    await asyncio.gather(*tasks)


# async def generate_regular_messages(bot: commands.Bot):
#
#
# async def start_activity_role_update(bot: commands.Bot):
#     tasks = []
#
#     await asyncio.gather(*tasks)
