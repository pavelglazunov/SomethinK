
import disnake
from disnake.ext import commands
from utils.parser import parse_config, edit_config


 

async def create_report_channel(bot: commands.Bot):
    if parse_config("channels_ID.report_channel_id") > 0:
        return

    channel = await bot.guilds[0].create_text_channel("Жалобы", overwrites={
        bot.guilds[0].default_role: disnake.PermissionOverwrite(read_messages=False),
        bot.guilds[0].owner: disnake.PermissionOverwrite(read_messages=True)
    })
    edit_config("channels_ID.report_channel_id", channel.id)


 


async def create_pending_message_channel(bot: commands.Bot):
    if parse_config("channels_ID.pending_message_channel_id") > 0:
        return

    channel = await bot.guilds[0].create_text_channel("Сообщения для проверки", overwrites={
        bot.guilds[0].default_role: disnake.PermissionOverwrite(read_messages=False),
        bot.guilds[0].owner: disnake.PermissionOverwrite(read_messages=True)
    })
    edit_config("channels_ID.pending_message_channel_id", channel.id)


 

async def create_logging_channel(bot: commands.Bot):
    if parse_config("channels_ID.logging_channel_id") > 0:
        return

    channel = await bot.guilds[0].create_text_channel("Логи", overwrites={
        bot.guilds[0].default_role: disnake.PermissionOverwrite(read_messages=False, ),
        bot.guilds[0].owner: disnake.PermissionOverwrite(read_messages=True),
    })
    await channel.send("Мы рекомендуем отключить уведомления в данном канале, так как в нем будут отображаться логи")

    edit_config("channels_ID.logging_channel_id", channel.id)
