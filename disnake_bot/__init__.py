import disnake
from disnake.ext import commands
import disnake_bot.config as cfg

from disnake_bot.utils.parser import parse_config
from disnake_bot.utils.messages import send_error_message as send_error_message

from cogs.events_handlers import EventsCog
from cogs.moderation import ModerationCog
from cogs.another import AnotherCog
from cogs.help import HelpCog
from disnake_bot.cogs.all_messages import AllMessagesCog

intents = disnake.Intents.all()
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = cfg.SYNC_COMMANDS_DEBUG

bot = commands.Bot(command_prefix=cfg.PREFIX,
                   intents=intents,
                   command_sync_flags=command_sync_flags)

bot.add_cog(HelpCog(bot))

bot.add_cog(EventsCog(bot))
bot.add_cog(ModerationCog(bot))
bot.add_cog(AnotherCog(bot))
bot.add_cog(AllMessagesCog(bot))


