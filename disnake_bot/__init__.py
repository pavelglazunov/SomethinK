import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction as Inter
import disnake_bot.config as cfg
from enum import Enum

from disnake_bot.utils.embed_messages import EmbedMessages, ErrorMessages

_message = EmbedMessages()
_errors = ErrorMessages()

intents = disnake.Intents.all()
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = cfg.sync_commands_debug

bot = commands.Bot(command_prefix="/",
                   intents=intents,
                   test_guilds=[1076824052007714937],
                   command_sync_flags=command_sync_flags)


@bot.slash_command(description="amogus////////")
async def buttons(inter: Inter):
    embed = disnake.Embed(

    )

    await inter.response.send_message(
        embed=embed,
        components=[

            disnake.ui.Button(label="первая", style=disnake.ButtonStyle.success, custom_id="_help_first",
                              disabled=True),
            disnake.ui.Button(label="следующая", style=disnake.ButtonStyle.success, custom_id="_help_next",
                              disabled=True),
            disnake.ui.Button(label="1/9", style=disnake.ButtonStyle.gray, custom_id="_help_page", disabled=True),
            disnake.ui.Button(label="предыдущая", style=disnake.ButtonStyle.success, custom_id="_help_previous"),
            disnake.ui.Button(label="последняя", style=disnake.ButtonStyle.success, custom_id="_help_last"),
        ]
    )


@bot.listen("on_button_click")
async def help_listener(inter: Inter):
    if inter.component.custom_id.startWith("_help"):
        if inter.component.custom_id == "_help_previous":
            await inter.response.send_message("Contact us at https://discord.gg/disnake!")
        elif inter.component.custom_id == "_help_last":
            await inter.response.send_message("Got it. Signing off!")


@bot.event
async def on_ready():
    # Получаем объекты серверов, на которых находится бот
    for guild in bot.guilds:
        # Получаем объект бота на сервере
        bot_member = guild.get_member(bot.user.id)

        # Получаем все права бота на сервере
        bot_permissions = bot_member.guild_permissions

        # Выводим все права бота на сервере в консоль
        print(f'Права бота на сервере {guild.name}:')
        for perm, value in bot_permissions:
            if value:
                print(f'{perm}: {value}')
# @bot.check
# async def global_guild_only(ctx):
#     if not ctx.guild:
#         raise commands.NoPrivateMessage  # replicating guild_only check: https://github.com/Rapptz/discord.py/blob/42a538edda79f92a26afe0ac902b45c1ea20154d/discord/ext/commands/core.py#L1832-L1846
#     return True
# async def on_ready():
#     print("Connected")
# from cogs.cog_help import HelpCog
from cogs.moderation import ModerationCog

from cogs.error_handler import ErrorHandlerCog

#
# bot.add_cog(HelpCog(bot))
bot.add_cog(ModerationCog(bot))
bot.add_cog(ErrorHandlerCog(bot))

if __name__ == '__main__':
    bot.run(cfg.token)
