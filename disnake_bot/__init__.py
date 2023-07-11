import disnake
from disnake.ext import commands
import disnake_bot.config as cfg

from disnake_bot.utils.embed_messages import EmbedMessages, ErrorMessages

_message = EmbedMessages()
_errors = ErrorMessages()

intents = disnake.Intents.all()
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = cfg.SYNC_COMMANDS_DEBUG

bot = commands.Bot(command_prefix=cfg.PREFIX,
                   intents=intents,
                   test_guilds=[1076824052007714937],
                   command_sync_flags=command_sync_flags)


@bot.event
async def on_ready():
    print(f"Бот {bot.user.name} готов к работе!")

    from on_load import loader

    await loader(bot)

    # await channel.send("Сообщение раз в 10 секунд")
    # from regulars import create_all_async_process
    #
    # await create_all_async_process(bot)
    print("here XD")
    # bot.loop.create_task(send_regular_message(bot=bot))


# @bot.check
# async def global_guild_only(ctx):
#     if not ctx.guild:
#         raise commands.NoPrivateMessage  # replicating guild_only check: https://github.com/Rapptz/discord.py/blob/42a538edda79f92a26afe0ac902b45c1ea20154d/discord/ext/commands/core.py#L1832-L1846
#     return True
# async def on_ready():
#     print("Connected")
# from cogs.cog_help import HelpCog
from cogs.moderation import ModerationCog
from cogs.another import AnotherCog
from cogs.settings import SettingsCog
from disnake_bot.cogs.automod import AutomodCog

from cogs.error_handler import ErrorHandlerCog

#
# bot.add_cog(HelpCog(bot))
bot.add_cog(ModerationCog(bot))
bot.add_cog(AnotherCog(bot))
bot.add_cog(ErrorHandlerCog(bot))
bot.add_cog(SettingsCog(bot))
bot.add_cog(AutomodCog(bot))

if __name__ == '__main__':
    bot.run(cfg.TOKEN)
