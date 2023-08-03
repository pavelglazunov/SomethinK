COGS_EVENTS_HANDLERS_BASE_IMPORTS = """
import disnake
from disnake.ext import commands
from utils.parser import parse_config

 """
COGS_EVENTS_HANDLERS_EVENTS_IMPORTS = """
from utils.messages import send_event_message


 """
COGS_EVENTS_HANDLERS_COG = """
class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Бот {self.bot.user.name} готов к работе!")
         """
COGS_EVENTS_HANDLERS_ADD_LOADER = """
        from utils.on_load import loader
        await loader(self.bot)

     """
COGS_EVENTS_HANDLERS_ON_MEMBER_JOIN = """
    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):
         """
COGS_EVENTS_HANDLERS_ADD_AUTO_ROLE = """
        for role_id in parse_config("roles_for_new_members"):
            role = self.bot.guilds[0].get_role(role_id)
            await member.add_roles(role)

         """
COGS_EVENTS_HANDLERS_JOIN_EVENT = """
        join_events = parse_config("events.join")
        for ev in join_events:
            channel = self.bot.get_channel(int(ev.get("channel")))
            await send_event_message(channel, ev, member, "join")

     """
COGS_EVENTS_HANDLERS_ON_MEMBER_LEAVE = """
    @commands.Cog.listener()
    async def on_member_remove(self, member: disnake.Member):
        leave_events = parse_config("events.leave")

        for ev in leave_events:
            channel = self.bot.get_channel(int(ev.get("channel")))
            await send_event_message(channel, ev, member, "leave")
"""
