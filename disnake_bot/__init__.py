import disnake
from disnake.ext import commands
from disnake import app_commands
import disnake_bot.config as cfg

from disnake_bot.utils.embed_messages import EmbedMessages, ErrorMessages


_message = EmbedMessages()
_errors = ErrorMessages()

intents = disnake.Intents.all()
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

bot = commands.Bot(command_prefix="!",
                   intents=intents,
                   test_guilds=[1076824052007714937],
                   command_sync_flags=command_sync_flags)

# async def on_ready():
#     print("Connected")
from cogs.cog_help import HelpCog
from cogs.cog_moderation import ModerationCog

bot.add_cog(HelpCog(bot))
bot.add_cog(ModerationCog(bot))

if __name__ == '__main__':
    bot.run(cfg.token)
