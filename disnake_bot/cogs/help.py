import disnake
from disnake.ext import commands

from disnake_bot.utils.messages import edit_help_page, get_full_description


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="help", description="Список команд")
    async def help(self, inter: disnake.ApplicationCommandInteraction, command: str = ""):
        if command:
            await inter.response.send_message(get_full_description(command))
            return

        await edit_help_page(inter, 0)
