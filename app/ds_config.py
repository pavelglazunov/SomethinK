from urllib import parse

# TOKEN = "MTA4MzI5MTA0NzkwNTQ4MDcyNQ.Gi4fGJ.J823SdFEcaHLQ-KuQcIxoQO7C83K-WfnSyLPl8"  # SomethinK Auth App
TOKEN = "MTA4MzI5MTA0NzkwNTQ4MDcyNQ.GMEuAa.I5Y52PipzTPDRsmT-vZ7UnHzyDOTs3GIBjC7Q0"
TEST_BOT_TOKEN = "MTA4MzQxMDA4NjAyMzY3NjAxNA.G7rxTw.qmXKjgTRwZByKF2wefqYP9jKhN4xmUNmNSzDHk"
REDIRECT_URL = "http://127.0.0.1:8080/auth/discord"
API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_SECRET = "gHWYL7QL5uo1WesVOyV-BX687yxHQ_Rb"
APPLICATION_ID = "1083291047905480725"
# OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id=1083291047905480725&redirect_uri={parse.quote(REDIRECT_URL)}&response_type=code&scope=identify"
# OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id=1083291047905480725&redirect_uri={parse.quote(REDIRECT_URL)}&response_type=code&scope=identify&"
# OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id=1083291047905480725&redirect_uri={parse.quote(REDIRECT_URL)}&response_type=code&scope=identify%20guilds%20email%20guilds.join%20guilds.members.read"
# OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id=1083291047905480725&redirect_uri={parse.quote(REDIRECT_URL)}&response_type=code&scope=email%20guilds.join%20guilds%20identify"


OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id=1083291047905480725&redirect_uri={parse.quote(REDIRECT_URL)}&response_type=code&scope=identify%20guilds%20email%20role_connections.write%20guilds.join%20guilds.members.read"
