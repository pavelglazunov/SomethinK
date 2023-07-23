import disnake
from disnake.ext import commands
import disnake_bot.config as cfg

from disnake_bot.utils.parser import parse_config
from disnake_bot.utils.messages import send_error_message as send_error_message

intents = disnake.Intents.all()
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = cfg.SYNC_COMMANDS_DEBUG

bot = commands.Bot(command_prefix=cfg.PREFIX,
                   intents=intents,
                   test_guilds=[1076824052007714937],
                   command_sync_flags=command_sync_flags)


# async def on_command_error(ctx: commands.Context, error: commands.CommandError):
#     print(error, type(error))


from cogs.events_handlers import EventsCog
from cogs.moderation import ModerationCog
from cogs.another import AnotherCog
from cogs.help import HelpCog
from disnake_bot.cogs.all_messages import AllMessagesCog

# from cogs.error_handler import ErrorHandlerCog

#
bot.add_cog(HelpCog(bot))
# bot.add_cog(ErrorHandlerCog(bot))

bot.add_cog(EventsCog(bot))
bot.add_cog(ModerationCog(bot))
bot.add_cog(AnotherCog(bot))
bot.add_cog(AllMessagesCog(bot))

if __name__ == '__main__':
    bot.run(cfg.TOKEN)
