from disnake import ApplicationCommandInteraction as Inter
from disnake_bot.utils.parse_commands import get_command_allow_channels
from disnake.ext import commands
import disnake


def allowed_channels(*channels):
    async def predicate(ctx: disnake.ApplicationCommandInteraction):
        if not channels:  # если список каналов пустой, выполняем команду всегда
            return True
        if ctx.channel.id in channels:
            return True
        else:
            await ctx.response.send_message("Команда может быть выполнена только в разрешенных каналах.")
            return False

    return commands.check(predicate)
