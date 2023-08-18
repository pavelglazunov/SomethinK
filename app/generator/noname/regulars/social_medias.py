
import asyncio
from disnake.ext import commands

 
import scrapetube

 

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

 