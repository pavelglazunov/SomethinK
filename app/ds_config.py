import os
from urllib import parse

TOKEN = os.getenv("SK_DISCORD_TOKEN") or "discord application token"
TEST_BOT_TOKEN = os.getenv("SK_DISCORD_TEST_TOKEN") or "discord test application token"
REDIRECT_URL = "http://127.0.0.1:8080/auth/discord"
API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_SECRET = os.getenv("SK_DISCORD_CLIENT_SECRET") or "discord application secret key"
APPLICATION_ID = os.getenv("SK_DISCORD_CLIENT_ID") or "discord application ID"

OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id={APPLICATION_ID}&redirect_uri={parse.quote(REDIRECT_URL)}&response_type=code&scope=identify%20guilds%20email%20role_connections.write%20guilds.join%20guilds.members.read"
