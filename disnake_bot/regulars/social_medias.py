import asyncio
import scrapetube
import requests

from disnake.ext import commands


async def check_youtube(bot: commands.Bot, yt_data: dict):
    url = yt_data.get("link")
    channel = bot.guilds[0].get_channel(int(yt_data.get("channel_id")))
    message = yt_data.get("message")
    iteration = 0
    start_videos = []
    while not bot.is_closed():
        videos = scrapetube.get_channel(channel_url=url, limit=5)
        video_ids = [video["videoId"] for video in videos]

        if iteration == 0:
            start_videos = video_ids
            iteration += 1
            continue

        for video_id in video_ids:
            if video_id not in start_videos:
                video_url = f"https://youtu.be/{video_id}"
                await channel.send(message.replace("{url}", video_url))

        start_videos = video_ids

        await asyncio.sleep(60)
        pass


async def check_twitch(bot: commands.Bot, tw_data: dict, delay):
    url = tw_data.get("link")
    channel = bot.guilds[0].get_channel(int(tw_data.get("channel_id")))
    message = tw_data.get("message")
    await asyncio.sleep(delay)

    is_online = False
    while not bot.is_closed():
        response = requests.get(url).content.decode()

        if "isLiveBroadcast" in response:
            if not is_online:
                await channel.send(message.replace("{url}", url))

            is_online = True
        else:
            is_online = False

        await asyncio.sleep(60)
        pass
