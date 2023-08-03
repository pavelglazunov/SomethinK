COGS_ALL_MESSAGES_BASE_IMPORTS = """
import disnake
from disnake.ext import commands
from utils.messages import edit_help_page
from utils.parser import parse_config

 """
COGS_ALL_MESSAGES_AUTOMOD_IMPORTS = """
from automod.automods import automod
from automod.actions import ACTIONS, remove_pending_message

 """
COGS_ALL_MESSAGES_LOGGING_IMPORT = """
from utils.event_logging import log

 """
COGS_ALL_MESSAGES_SEND_EVENT_MESSAGE_IMPORT = """
from utils.messages import send_event_message

 """
COGS_ALL_MESSAGES_AUTORESPONSE_CONST = """
auto_responses = parse_config("auto_responser")
detect_trigger = {
    "inside": lambda x, m: x in m,
    "start": lambda x, m: m.startswith(x),
    "only": lambda x, m: x == m,
}


 """
COGS_ALL_MESSAGES_COG = """
class AllMessagesCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

     """
COGS_ALL_MESSAGES_ON_MESSAGE_EDIT = """
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if mod := automod(after):
            await log(after, mod[0], "auto_moderation")
            await ACTIONS[mod[1]](after, mod[2], mod[0])

     """
COGS_ALL_MESSAGES_ON_MESSAGE = """
    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if message.author.bot:
            return

         """
COGS_ALL_MESSAGES_ADD_AUTOMOD_CALL = """
        if mod := automod(message):
            await log(message, mod[0], "auto_moderation")
            await ACTIONS[mod[1]](message, mod[2], mod[0])

         """
COGS_ALL_MESSAGES_ADD_AUTO_RESPONSE = """
        for response in auto_responses:
            trigger_type = response["trigger_type"]
            trigger = response["trigger"]
            if detect_trigger[trigger_type](trigger, message.content):
                channel = message.channel
                await send_event_message(channel, response, message.author, "auto_response")

     """
COGS_ALL_MESSAGES_ON_BUTTON_CLICK = """
    @commands.Cog.listener("on_button_click")
    async def button_listener(self, inter: disnake.MessageInteraction):
        custom_id: str = inter.component.custom_id

         """
COGS_ALL_MESSAGES_ADD_SEND_ACTION_BUTTONS_EVENTS = """
        if custom_id.startswith("r_"):
            data = remove_pending_message(custom_id.split("_")[1])
            embed = disnake.Embed(title="Новое сообщение для проверки (отклонено)")
            embed.add_field(name="Текст сообщения", value=data['message_content'], inline=False)
            embed.add_field(name="Информация", value=f"ID сообщения: {data['message_id']}\\n"
                                                     f"Сообщение получено от: {data['from_user_mention']}\\n"
                                                     f"Сообщение получено в канале: {data['message_channel_mention']}\\n"
                                                     f"Сообщение получено в: {data['message_send_time']}", inline=False)
            embed.color = int("FF0000", 16)
            embed.set_footer(text=f"Отклонено модератором: {inter.user.mention}")
            await inter.message.edit(embed=embed, components=[])

        if custom_id.startswith("a_"):
            data = remove_pending_message(custom_id.split("_")[1])
            embed = disnake.Embed(title="Новое сообщение для проверки (одобрено)")
            embed.add_field(name="Текст сообщения", value=data['message_content'], inline=False)
            embed.add_field(name="Информация", value=f"ID сообщения: {data['message_id']}\\n"
                                                     f"Сообщение получено от: {data['from_user_mention']}\\n"
                                                     f"Сообщение получено в канале: {data['message_channel_mention']}\\n"
                                                     f"Сообщение получено в: {data['message_send_time']}", inline=False)
            embed.color = int("00FF00", 16)
            embed.set_footer(text=f"Одобрено модератором: {inter.user.mention}")
            await inter.message.edit(embed=embed, components=[])
            channel = inter.guild.get_channel(data["message_channel_id"])
            await channel.send(f"**Сообщение прошло проверку**\\n{data['message_content']}\\n"
                               f"*от: {data['from_user_mention']}*")

         """
COGS_ALL_MESSAGES_ADD_HELP_BUTTONS_EVENTS = """
        if custom_id == "help_next":
            actual_page = int(inter.message.components[0].children[2].label.split("/")[0])
            await edit_help_page(inter, actual_page, inter.message)

        if custom_id == "help_previous":
            actual_page = int(inter.message.components[0].children[2].label.split("/")[0])
            await edit_help_page(inter, actual_page - 2, inter.message)

        if custom_id == "help_last":
            actual_page = int(inter.message.components[0].children[2].label.split("/")[0])
            await edit_help_page(inter, actual_page + 1001, inter.message)

        if custom_id == "help_first":
            await edit_help_page(inter, 0, inter.message)
"""
