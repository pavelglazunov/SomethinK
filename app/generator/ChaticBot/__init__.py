
import disnake
from disnake.ext import commands
import config as cfg
from utils.parser import parse_config
from utils.messages import send_error_message
from cogs.events_handlers import EventsCog
from cogs.help import HelpCog
from cogs.all_messages import AllMessagesCog


from cogs.moderation import ModerationCog
 
from cogs.another import AnotherCog
 


intents = disnake.Intents.all()
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = cfg.SYNC_COMMANDS_DEBUG

activity_text = parse_config("status.text")
ACTIVITIES = {
    "playing": disnake.Game(name=activity_text),
    "listening": disnake.Activity(type=disnake.ActivityType.listening, name=activity_text),
    "watching": disnake.Activity(type=disnake.ActivityType.watching, name=activity_text)
}


bot = commands.Bot(command_prefix=cfg.PREFIX,
                   intents=intents,
                   command_sync_flags=command_sync_flags,
                   activity=ACTIVITIES[parse_config("status.type")])

bot.add_cog(HelpCog(bot))
bot.add_cog(EventsCog(bot))
bot.add_cog(AllMessagesCog(bot))

bot.add_cog(ModerationCog(bot))

bot.add_cog(AnotherCog(bot))
