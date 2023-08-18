

import asyncio

from disnake.ext import commands
from utils.parser import parse_config


async def start_activity_roles_updating(bot: commands.Bot):
    while not bot.is_closed():
        all_activity_roles: dict = parse_config("activity_roles.roles")
        interval = int(parse_config("ar_update_interval")) * 60
        enable = parse_config("activity_roles.ar_enable")
        if not enable:
            await asyncio.sleep(interval)
            continue
        for user in bot.guilds[0].members:
            for r in all_activity_roles.values():
                role = bot.guilds[0].get_role(r["role_id"])
                if role in user.roles:
                    await user.remove_roles(role)

            if act := user.activity:

                if act.name.lower() in all_activity_roles.keys():
                    role = bot.guilds[0].get_role(all_activity_roles[act.name.lower()]["role_id"])
                    await user.add_roles(role)

        await asyncio.sleep(interval)

