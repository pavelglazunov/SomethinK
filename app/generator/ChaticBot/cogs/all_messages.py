
import disnake
from disnake.ext import commands
from utils.messages import edit_help_page
from utils.parser import parse_config

 
from utils.event_logging import log

 
class AllMessagesCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

     
    @commands.Cog.listener("on_button_click")
    async def button_listener(self, inter: disnake.MessageInteraction):
        custom_id: str = inter.component.custom_id

         
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
