import asyncio
import datetime

import disnake
from disnake.ext import commands

INTERVAL_COEFFICIENT = {
    "minutes": 60,
    "hours": 60 * 60,
    "days": 60 * 60 * 24,
    "weeks": 60 * 60 * 24 * 7,
    "months": 60 * 60 * 24 * 7 * 30,
    "years": 60 * 60 * 24 * 365
}


async def regular_message(bot: commands.Bot, message_data: dict):
    message_time = datetime.time(*list(map(int, message_data["time"].split(":"))))
    now = datetime.datetime.now()
    dt = datetime.datetime.combine(now.date(), message_time)

    if dt < now:
        dt += datetime.timedelta(days=1)

    diff = (dt - now).total_seconds()
    await asyncio.sleep(int(diff))
    while not bot.is_closed():
        channel = bot.get_channel(int(message_data["channel"]))
        interval = int(message_data["interval"]) * INTERVAL_COEFFICIENT[message_data["units_of_measure"]]

        if message_data["enable_embed"]:
            embed = disnake.Embed()
            embed.title = message_data["embed"]["author"]
            embed.description = message_data["content"]
            embed.set_footer(text=message_data["embed"]["footer_content"])
            embed.set_image(message_data["embed"]["image_url"])
            embed.color = int(message_data["embed"]["color"][1:], 16)

            await channel.send(embed=embed)
        else:
            await channel.send(message_data["content"])
        await asyncio.sleep(interval)
