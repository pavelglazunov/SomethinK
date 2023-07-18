from disnake.ext import commands
# from disnake_bot import _message, _errors
# from disnake_bot.config import MESSAGES_CONFIG, MODERATION_COMMANDS, MODERATION_ROLES_ID, EVERYONE_COMMANDS


# class HelpCog(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#
#     @commands.slash_command(name="help", description="Список команд")
#     async def help(self, inter, command: str = ""):
#         if not command:
#             body = "\n".join(
#                 ["**{}** - {}".format(i, MESSAGES_CONFIG["commands"][i]["description"]) for i in EVERYONE_COMMANDS])
#             await _message.send_embed(inter=inter,
#                                       title=MESSAGES_CONFIG["helps"]["help"]["title"],
#                                       body=body,
#                                       color=MESSAGES_CONFIG["helps"]["help"]["color"])
#             return
#         if not (command in MESSAGES_CONFIG["commands"]):
#             await _errors.command_not_found(inter)
#             return
#
#         await inter.response.send_message(MESSAGES_CONFIG["commands"][command]["description"])
#
#     @commands.slash_command(name="helpm", description="Список команд для модераторов")
#     @commands.has_any_role(*MODERATION_ROLES_ID)
#     async def helpm(self, inter, command: str = ""):
#         if not command:
#             body = "\n".join(
#                 ["**{}** - {}".format(i, MESSAGES_CONFIG["commands"][i]["description"]) for i in MODERATION_COMMANDS])
#             await _message.send_embed(inter=inter,
#                                       title=MESSAGES_CONFIG["helps"]["helpm"]["title"],
#                                       body=body,
#                                       color=MESSAGES_CONFIG["helps"]["helpm"]["color"])
#             return
#         if not (command in MESSAGES_CONFIG["commands"]):
#             await _errors.command_not_found(inter)
#             return
#
#         await inter.response.send_message(MESSAGES_CONFIG["commands"][command]["description"])
#
#     @helpm.error
#     async def helpm_error(self, inter, error):
#         if isinstance(error, commands.MissingAnyRole):
#             await _errors.missing_role(inter)
