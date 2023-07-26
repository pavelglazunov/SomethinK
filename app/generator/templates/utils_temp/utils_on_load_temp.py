UTILS_ON_LOAD_IMPORT_ASYNC_PROCESSES = """
from _____project_name_for_imports_____.regulars import create_all_async_process
 """
UTILS_ON_LOAD_IMPORT_CREATOR = """
from _____project_name_for_imports_____.utils.creator import *

 """
UTILS_ON_LOAD_BASE_IMPORT = """
from disnake.ext import commands


 """
UTILS_ON_LOAD_MAIN_FUNC = """
async def loader(bot: commands.Bot):
     """
UTILS_ON_LOAD_ADD_CREATE_AR = """
    await create_ar(bot)
     """
UTILS_ON_LOAD_ADD_CREATE_REPORT_CHANNEL = """
    await create_report_channel(bot)
     """
UTILS_ON_LOAD_ADD_CREATE_LOGGING_CHANNEL = """
    await create_logging_channel(bot)
     """
UTILS_ON_LOAD_ADD_CREATE_PENDING_MESSAGE_CHANNEL = """
    await create_pending_message_channel(bot)
     """
UTILS_ON_LOAD_ADD_ALL_ASYNC_PROCESS = """
    await create_all_async_process(bot)
"""
