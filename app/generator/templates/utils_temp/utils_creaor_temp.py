UTILS_CREATOR_IMPORTS = """
import disnake
from disnake.ext import commands
from _____project_name_for_imports_____.utils.parser import parse_config, edit_config


 """
UTILS_CREATOR_CREATE_ACTIVITY_ROLES = """

async def create_ar(bot: commands.Bot):
    all_ar: dict = parse_config("activity_roles.roles")
    all_guild_roles_name = [r.name for r in bot.guilds[0].roles]

    for k, v in all_ar.items():
        if (v["role_id"] == 0) or (not (k in all_guild_roles_name)):
            role = await bot.guilds[0].create_role(name=k, color=int(v["value"], 16))
            all_ar[k]["role_id"] = role.id

        else:
            role = bot.guilds[0].get_role(v["role_id"])

    edit_config("activity_roles.roles", all_ar)


 """
UTILS_CREATOR_CREATE_REPORT_CHANNEL = """

async def create_report_channel(bot: commands.Bot):
    if parse_config("channels_ID.report_channel_id") > 0:
        return

    channel = await bot.guilds[0].create_text_channel("Жалобы", overwrites={
        bot.guilds[0].default_role: disnake.PermissionOverwrite(read_messages=False),
        bot.guilds[0].owner: disnake.PermissionOverwrite(read_messages=True)
    })
    edit_config("channels_ID.report_channel_id", channel.id)


 """
UTILS_CREATOR_CREATE_PENDING_MESSAGE_CHANNEL = """


async def create_pending_message_channel(bot: commands.Bot):
    if parse_config("channels_ID.pending_message_channel_id") > 0:
        return

    channel = await bot.guilds[0].create_text_channel("Сообщения для проверки", overwrites={
        bot.guilds[0].default_role: disnake.PermissionOverwrite(read_messages=False),
        bot.guilds[0].owner: disnake.PermissionOverwrite(read_messages=True)
    })
    edit_config("channels_ID.pending_message_channel_id", channel.id)


 """
UTILS_CREATOR_CREATE_LOGGING_CHANNEL = """

async def create_logging_channel(bot: commands.Bot):
    if parse_config("channels_ID.logging_channel_id") > 0:
        return

    channel = await bot.guilds[0].create_text_channel("Логи", overwrites={
        bot.guilds[0].default_role: disnake.PermissionOverwrite(read_messages=False, ),
        bot.guilds[0].owner: disnake.PermissionOverwrite(read_messages=True),
    })
    await channel.send("Мы рекомендуем отключить уведомления в данном канале, так как в нем будут отображаться логи")

    edit_config("channels_ID.logging_channel_id", channel.id)
"""
