import disnake
from disnake.ext import commands

from disnake_bot.utils.parser import parse_config
from disnake_bot.utils.messages import send_event_message


class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self, ):
        print(f"Бот {self.bot.user.name} готов к работе!")

        from disnake_bot.on_load import loader

        await loader(self.bot)

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):
        for role_id in parse_config("roles_for_new_members"):
            role = self.bot.guilds[0].get_role(role_id)
            await member.add_roles(role)

        join_events = parse_config("events.join")

        for ev in join_events:
            channel = self.bot.get_channel(int(ev.get("channel")))
            await send_event_message(channel, ev, member, "join")

    @commands.Cog.listener()
    async def on_member_remove(self, member: disnake.Member):
        leave_events = parse_config("events.leave")

        for ev in leave_events:
            channel = self.bot.get_channel(int(ev.get("channel")))
            await send_event_message(channel, ev, member, "leave")
