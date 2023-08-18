
from regulars import create_all_async_process
 
from utils.creator import *

 
from disnake.ext import commands


 
async def loader(bot: commands.Bot):
     
    await create_report_channel(bot)
     
    await create_logging_channel(bot)
     
    await create_pending_message_channel(bot)
     
    await create_all_async_process(bot)
