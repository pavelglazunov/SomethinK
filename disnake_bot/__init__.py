import datetime

import disnake
from disnake.ext import commands
import disnake_bot.config as cfg

from disnake_bot.utils.parser import parse_config
from disnake_bot.utils.messages import error as send_error_message
# _message = EmbedMessages()
# _errors = ErrorMessages()

intents = disnake.Intents.all()
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = cfg.SYNC_COMMANDS_DEBUG

bot = commands.Bot(command_prefix=cfg.PREFIX,
                   intents=intents,
                   test_guilds=[1076824052007714937],
                   command_sync_flags=command_sync_flags)


@bot.event
async def on_error(ctx: commands.Context, error: commands.CommandError):
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

from cogs.events_handlers import EventsCog
from cogs.moderation import ModerationCog
from cogs.another import AnotherCog
# from cogs.settings import SettingsCog
from disnake_bot.cogs.all_messages import AllMessagesCog

# from cogs.error_handler import ErrorHandlerCog

#
# bot.add_cog(HelpCog(bot))
# bot.add_cog(ErrorHandlerCog(bot))

bot.add_cog(EventsCog(bot))
bot.add_cog(ModerationCog(bot))
bot.add_cog(AnotherCog(bot))
# bot.add_cog(SettingsCog(bot))
bot.add_cog(AllMessagesCog(bot))

if __name__ == '__main__':
    bot.run(cfg.TOKEN)
