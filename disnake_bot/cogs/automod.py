import datetime

import disnake
from disnake.ext import commands
from disnake_bot.automod.automods import automod
from disnake_bot.automod.actions import ACTIONS, remove_pending_message
from disnake_bot.event_logging import log

from disnake_bot.utils.parser import get_command_allow_roles, get_command_allow_channels
from disnake_bot.utils.decorators import allowed_channels

from disnake_bot import _message


class AutomodCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if message.author.bot:
            return
        if mod := automod(message.content):
            log(message, mod[0], "commands")
            await ACTIONS[mod[1]](message, mod[2])

    @commands.Cog.listener("on_button_click")
    async def button_listener(self, inter: disnake.MessageInteraction):
        custom_id: str = inter.component.custom_id
        if custom_id.startswith("r_"):
            data = remove_pending_message(custom_id.split("_")[1])
            embed = disnake.Embed(title="Новое сообщение для проверки (отклонено)")
            embed.add_field(name="Текст сообщения", value=data['message_content'], inline=False)
            embed.add_field(name="Информация", value=f"ID сообщения: {data['message_id']}\n"
                                                     f"Сообщение получено от: {data['from_user_mention']}\n"
                                                     f"Сообщение получено в канале: {data['message_channel_mention']}\n"
                                                     f"Сообщение получено в: {data['message_send_time']}", inline=False)
            embed.color = int("FF0000", 16)
            embed.footer.text = f"Отклонено модератором: {inter.user.mention}"
            await inter.message.edit(embed=embed, components=[])

        if custom_id.startswith("a_"):
            data = remove_pending_message(custom_id.split("_")[1])
            embed = disnake.Embed(title="Новое сообщение для проверки (одобрено)")
            embed.add_field(name="Текст сообщения", value=data['message_content'], inline=False)
            embed.add_field(name="Информация", value=f"ID сообщения: {data['message_id']}\n"
                                                     f"Сообщение получено от: {data['from_user_mention']}\n"
                                                     f"Сообщение получено в канале: {data['message_channel_mention']}\n"
                                                     f"Сообщение получено в: {data['message_send_time']}", inline=False)
            embed.color = int("00FF00", 16)
            embed.footer.text = f"Одобрено модератором: {inter.user.mention}"
            await inter.message.edit(embed=embed, components=[])
            channel = inter.guild.get_channel(data["message_channel_id"])
            await channel.send(f"**Сообщение прошло проверку**\n{data['message_content']}\n"
                               f"*от: {data['from_user_mention']}*")