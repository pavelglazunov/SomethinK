BOT_CONFIG_FILE_BASE_VALUES = """
TOKEN: str = "_____bot_token_____"
SYNC_COMMANDS_DEBUG: bool = False
PREFIX: str = "/"

WARNING_JSON_FILENAME: str = "user_warnings"
CONFIG_JSON_FILENAME: str = "config"
PENDING_MESSAGES_JSON_FILENAME: str = "pending_messages"
MESSAGES_JSON_FILENAME: str = "messages_config"

LOGGING_EVENT_TYPES: tuple = _____logging_events_____

 """
BOT_CONFIG_FILE_WEATHER_API_KEY = """
WEATHER_API_KEY: str = "_____weather_api_token_____"
 """
BOT_CONFIG_FILE_GPT_API_KEY = """
GPT_API_KEY: str = "_____gpt_api_token_____"
"""
