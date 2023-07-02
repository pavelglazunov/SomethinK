import disnake
from disnake.ext import commands


class ErrorHandlerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Команда не найдена.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Отсутствует обязательный аргумент.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Неверный аргумент.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("Вы не можете использовать эту команду.")
        # добавьте другие обработчики ошибок, если это необходимо
