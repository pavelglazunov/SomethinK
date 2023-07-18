import disnake
from disnake.ext import commands

from disnake_bot.utils.messages import error as send_error_message


class ErrorHandlerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_error(self, ctx: commands.Context, error: commands.CommandError):
        print(error, type(error))

        if isinstance(error, commands.CommandNotFound):
            await send_error_message(ctx, "command_not_found")
            # await ctx.send("Команда не найдена.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await send_error_message(ctx, "missing_argument")
            # await ctx.send("Отсутствует обязательный аргумент.")
        elif isinstance(error, commands.BadArgument):
            await send_error_message(ctx, "incorrect_argument")
        elif isinstance(error, commands.MissingPermissions):
            await send_error_message(ctx, "bot_missing_permission")
            # await ctx.send("Неверный аргумент.")
        elif isinstance(error, commands.CheckFailure):
            await send_error_message(ctx, "missing_permission")
        elif isinstance(error, commands.CommandInvokeError) or isinstance(error, disnake.InteractionTimedOut):
            await ctx.send("Команда превысила лимит по времени, пожалуйста повторит попытку")
        else:
            await ctx.send("ERROR")
        # добавьте другие обработчики ошибок, если это необходимо
