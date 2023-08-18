
import datetime
import disnake
from disnake.ext import commands
from utils.parser import get_command_allow_roles, get_command_allow_channels
from utils.decorators import allowed_channels, allowed_roles
from utils.messages import send_message, send_long_message, get_description
from utils.messages import send_error_message, detected_error

 
from modals.feedback_modals import FeedbackTypeSelect

 
class AnotherCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

     
    @commands.slash_command(name="feedback", description=get_description("feedback"))
    @allowed_roles(*get_command_allow_roles("feedback"))
    @allowed_channels(*get_command_allow_channels("feedback"))
    async def feedback(self, inter: disnake.ApplicationCommandInteraction):
        """
        Обратиться к разработчику бота

        Parameters
        ----------
        """
        view = disnake.ui.View()
        view.add_item(FeedbackTypeSelect(self.bot))
        await inter.response.send_message(view=view,
                                          ephemeral=True)

     

    
    @feedback.error
    async def feedback_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    
