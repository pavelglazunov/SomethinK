from disnake_bot.utils.parser import parse_config, edit_config
from disnake.ext import commands

from disnake_bot.regulars import create_all_async_process


async def create_ar(bot: commands.Bot):
    all_ar: dict = parse_config("activity_roles.roles")
    all_guild_roles_name = [r.name for r in bot.guilds[0].roles]
    all_guild_roles_id = []

    for k, v in all_ar.items():
        if (v["role_id"] == 0) or (not (k in all_guild_roles_name)):
            print(k, v)
            role = await bot.guilds[0].create_role(name=k, color=int(v["value"], 16))
            all_ar[k]["role_id"] = role.id

        else:
            role = bot.guilds[0].get_role(v["role_id"])

    print(all_ar)
    edit_config("activity_roles.roles", all_ar)


async def loader(bot: commands.Bot):
    await create_ar(bot)
    ...
    await create_all_async_process(bot)
