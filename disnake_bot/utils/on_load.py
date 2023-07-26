
from disnake_bot.regulars import create_all_async_process
from disnake_bot.utils.creator import *


async def loader(bot: commands.Bot):
    await create_ar(bot)
    await create_report_channel(bot)
    await create_logging_channel(bot)
    await create_pending_message_channel(bot)

    await create_all_async_process(bot)
