import json
import os

from app.generator.templates.modals_temp import *
from app.generator.templates.cogs_temp import *
from app.generator.templates.another_commands_temp import *
from app.generator.templates.base_temp import *
from app.generator.templates.utils_temp import *
from app.generator.templates.regulars_temp import *
from app.generator.templates.automod_temp import *
from app.generator.templates.main_temp import *

# from templates.modals_temp import *
# from templates.cogs_temp import *
# from templates.another_commands_temp import *
# from templates.base_temp import *
# from templates.utils_temp import *
# from templates.regulars_temp import *
# from templates.automod_temp import *
# from templates.main_temp import *

TEMPLATES = {
    'cogs_command_imports': COGS_COMMAND_IMPORTS,
    'cogs_command_import_add_warning': COGS_COMMAND_IMPORT_ADD_WARNING,
    'cogs_command_import_get_warnings': COGS_COMMAND_IMPORT_GET_WARNINGS,
    'cogs_command_import_remove_warnings': COGS_COMMAND_IMPORT_REMOVE_WARNINGS,
    'cogs_command_timeout_list': COGS_COMMAND_TIMEOUT_LIST,
    'cogs_command_cog': COGS_COMMAND_COG,
    'cogs_command_ban': COGS_COMMAND_BAN,
    'cogs_command_kick': COGS_COMMAND_KICK,
    'cogs_command_unban': COGS_COMMAND_UNBAN,
    'cogs_command_mute': COGS_COMMAND_MUTE,
    'cogs_command_unmute': COGS_COMMAND_UNMUTE,
    'cogs_command_chatmute': COGS_COMMAND_CHATMUTE,
    'cogs_command_chatunmute': COGS_COMMAND_CHATUNMUTE,
    'cogs_command_timeout': COGS_COMMAND_TIMEOUT,
    'cogs_command_rmtimeout': COGS_COMMAND_RMTIMEOUT,
    'cogs_command_fullban': COGS_COMMAND_FULLBAN,
    'cogs_command_clear': COGS_COMMAND_CLEAR,
    'cogs_command_afk': COGS_COMMAND_AFK,
    'cogs_command_move': COGS_COMMAND_MOVE,
    'cogs_command_deafen': COGS_COMMAND_DEAFEN,
    'cogs_command_undeafen': COGS_COMMAND_UNDEAFEN,
    'cogs_command_addrole': COGS_COMMAND_ADDROLE,
    'cogs_command_rmrole': COGS_COMMAND_RMROLE,
    'cogs_command_ping': COGS_COMMAND_PING,
    'cogs_command_slowmode': COGS_COMMAND_SLOWMODE,
    'cogs_command_vkick': COGS_COMMAND_VKICK,
    'cogs_command_warn': COGS_COMMAND_WARN,
    'cogs_command_warns': COGS_COMMAND_WARNS,
    'cogs_command_rmwarn': COGS_COMMAND_RMWARN,
    'cogs_command_report': COGS_COMMAND_REPORT,
    'cogs_command_errors': COGS_COMMAND_ERRORS,

    # 'cogs_command_embed': COGS_COMMAND_EMBED,
    # 'cogs_command_feedback': COGS_COMMAND_FEEDBACK,

    'cogs_another_commands_base_imports': COGS_ANOTHER_COMMANDS_BASE_IMPORTS,
    'cogs_another_commands_import_gpt': COGS_ANOTHER_COMMANDS_IMPORT_GPT,
    'cogs_another_commands_import_requests': COGS_ANOTHER_COMMANDS_IMPORT_REQUESTS,
    'cogs_another_commands_import_embed_modal': COGS_ANOTHER_COMMANDS_IMPORT_EMBED_MODAL,
    'cogs_another_commands_import_feedback_modal': COGS_ANOTHER_COMMANDS_IMPORT_FEEDBACK_MODAL,
    'cogs_another_commands_import_weather_api_key': COGS_ANOTHER_COMMANDS_IMPORT_WEATHER_API_KEY,
    'cogs_another_commands_import_translate': COGS_ANOTHER_COMMANDS_IMPORT_TRANSLATE,
    'cogs_another_commands_translate_language_list': COGS_ANOTHER_COMMANDS_TRANSLATE_LANGUAGE_LIST,
    'cogs_another_commands_set_openai_token': COGS_ANOTHER_COMMANDS_SET_OPENAI_TOKEN,
    'cogs_another_commands_cog': COGS_ANOTHER_COMMANDS_COG,
    'cogs_command_color': COGS_COMMAND_COLOR,
    'cogs_command_nick': COGS_COMMAND_NICK,
    'cogs_command_joke': COGS_COMMAND_JOKE,
    'cogs_command_weather': COGS_COMMAND_WEATHER,
    'cogs_command_translate': COGS_COMMAND_TRANSLATE,
    'cogs_command_say': COGS_COMMAND_SAY,
    'cogs_command_avatar': COGS_COMMAND_AVATAR,
    'cogs_command_gpt': COGS_COMMAND_GPT,
    'cogs_command_embed': COGS_COMMAND_EMBED,
    'cogs_command_feedback': COGS_COMMAND_FEEDBACK,

    'cogs_help_base': COGS_HELP_BASE,

    'cogs_events_handlers_base_imports': COGS_EVENTS_HANDLERS_BASE_IMPORTS,
    'cogs_events_handlers_events_imports': COGS_EVENTS_HANDLERS_EVENTS_IMPORTS,
    'cogs_events_handlers_cog': COGS_EVENTS_HANDLERS_COG,
    'cogs_events_handlers_add_loader': COGS_EVENTS_HANDLERS_ADD_LOADER,
    'cogs_events_handlers_on_member_join': COGS_EVENTS_HANDLERS_ON_MEMBER_JOIN,
    'cogs_events_handlers_add_auto_role': COGS_EVENTS_HANDLERS_ADD_AUTO_ROLE,
    'cogs_events_handlers_join_event': COGS_EVENTS_HANDLERS_JOIN_EVENT,
    'cogs_events_handlers_on_member_leave': COGS_EVENTS_HANDLERS_ON_MEMBER_LEAVE,

    'cogs_all_messages_base_imports': COGS_ALL_MESSAGES_BASE_IMPORTS,
    'cogs_all_messages_automod_imports': COGS_ALL_MESSAGES_AUTOMOD_IMPORTS,
    'cogs_all_messages_logging_import': COGS_ALL_MESSAGES_LOGGING_IMPORT,
    'cogs_all_messages_send_event_message_import': COGS_ALL_MESSAGES_SEND_EVENT_MESSAGE_IMPORT,
    'cogs_all_messages_autoresponse_const': COGS_ALL_MESSAGES_AUTORESPONSE_CONST,
    'cogs_all_messages_cog': COGS_ALL_MESSAGES_COG,
    'cogs_all_messages_on_message_edit': COGS_ALL_MESSAGES_ON_MESSAGE_EDIT,
    'cogs_all_messages_on_message': COGS_ALL_MESSAGES_ON_MESSAGE,
    'cogs_all_messages_add_automod_call': COGS_ALL_MESSAGES_ADD_AUTOMOD_CALL,
    'cogs_all_messages_add_auto_response': COGS_ALL_MESSAGES_ADD_AUTO_RESPONSE,
    'cogs_all_messages_on_button_click': COGS_ALL_MESSAGES_ON_BUTTON_CLICK,
    'cogs_all_messages_add_send_action_buttons_events': COGS_ALL_MESSAGES_ADD_SEND_ACTION_BUTTONS_EVENTS,
    'cogs_all_messages_add_help_buttons_events': COGS_ALL_MESSAGES_ADD_HELP_BUTTONS_EVENTS,

    'cogs_init_import_another': COGS_INIT_IMPORT_ANOTHER,
    'cogs_init_import_all_message': COGS_INIT_IMPORT_ALL_MESSAGE,
    'cogs_init_import_help': COGS_INIT_IMPORT_HELP,
    'cogs_init_import_command': COGS_INIT_IMPORT_COMMAND,

    'empty_json': EMPTY_JSON,
    'utils_messages_imports_and_body': UTILS_MESSAGES_IMPORTS_AND_BODY,
    'utils_messages_import_log': UTILS_MESSAGES_IMPORT_LOG,
    'utils_messages_get_description': UTILS_MESSAGES_GET_DESCRIPTION,
    'utils_messages_help_base': UTILS_MESSAGES_HELP_BASE,
    'utils_messages_send_message': UTILS_MESSAGES_SEND_MESSAGE,
    'utils_messages_add_log_message_func_call': UTILS_MESSAGES_ADD_LOG_MESSAGE_FUNC_CALL,
    'utils_messages_send_event_message': UTILS_MESSAGES_SEND_EVENT_MESSAGE,
    'utils_messages_add_log_event_message_func_call': UTILS_MESSAGES_ADD_LOG_EVENT_MESSAGE_FUNC_CALL,
    'utils_messages_error_message_part_1': UTILS_MESSAGES_ERROR_MESSAGE_PART_1,
    'utils_messages_add_log_error_func_call': UTILS_MESSAGES_ADD_LOG_ERROR_FUNC_CALL,
    'utils_messages_error_message_part_2': UTILS_MESSAGES_ERROR_MESSAGE_PART_2,

    'utils_messages_error_detect': UTILS_MESSAGES_ERROR_DETECT,

    'utils_parser_imports': UTILS_PARSER_IMPORTS,
    'utils_parser_get_allow': UTILS_PARSER_GET_ALLOW,
    'utils_parser_base': UTILS_PARSER_BASE,
    'utils_warnings_imports': UTILS_WARNINGS_IMPORTS,
    'utils_warnings_add_warning': UTILS_WARNINGS_ADD_WARNING,
    'utils_warnings_remove_warnings': UTILS_WARNINGS_REMOVE_WARNINGS,
    'utils_warnings_get_warnings': UTILS_WARNINGS_GET_WARNINGS,
    'utils_decorators_imports': UTILS_DECORATORS_IMPORTS,
    'utils_decorators_command_allow_channels': UTILS_DECORATORS_COMMAND_ALLOW_CHANNELS,
    'utils_decorators_base': UTILS_DECORATORS_BASE,
    'utils_creator_imports': UTILS_CREATOR_IMPORTS,
    'utils_creator_create_activity_roles': UTILS_CREATOR_CREATE_ACTIVITY_ROLES,
    'utils_creator_create_report_channel': UTILS_CREATOR_CREATE_REPORT_CHANNEL,
    'utils_creator_create_pending_message_channel': UTILS_CREATOR_CREATE_PENDING_MESSAGE_CHANNEL,
    'utils_creator_create_logging_channel': UTILS_CREATOR_CREATE_LOGGING_CHANNEL,
    'utils_event_logging_file': UTILS_EVENT_LOGGING_FILE,
    'utils_on_load_import_async_processes': UTILS_ON_LOAD_IMPORT_ASYNC_PROCESSES,
    'utils_on_load_import_creator': UTILS_ON_LOAD_IMPORT_CREATOR,
    'utils_on_load_base_import': UTILS_ON_LOAD_BASE_IMPORT,
    'utils_on_load_main_func': UTILS_ON_LOAD_MAIN_FUNC,
    'utils_on_load_add_create_ar': UTILS_ON_LOAD_ADD_CREATE_AR,
    'utils_on_load_add_create_report_channel': UTILS_ON_LOAD_ADD_CREATE_REPORT_CHANNEL,
    'utils_on_load_add_create_logging_channel': UTILS_ON_LOAD_ADD_CREATE_LOGGING_CHANNEL,
    'utils_on_load_add_create_pending_message_channel': UTILS_ON_LOAD_ADD_CREATE_PENDING_MESSAGE_CHANNEL,
    'utils_on_load_add_all_async_process': UTILS_ON_LOAD_ADD_ALL_ASYNC_PROCESS,

    'regulars_activity_roles_file': REGULARS_ACTIVITY_ROLES_FILE,
    'regulars_messages_file': REGULAR_MESSAGES_FILE,
    'regulars_social_media_imports': REGULARS_SOCIAL_MEDIA_IMPORTS,
    'regulars_social_media_import_youtube_parser': REGULARS_SOCIAL_MEDIA_IMPORT_YOUTUBE_PARSER,
    'regulars_social_media_import_twitch_parser': REGULARS_SOCIAL_MEDIA_IMPORT_TWITCH_PARSER,
    'regulars_social_media_youtube': REGULARS_SOCIAL_MEDIA_YOUTUBE,
    'regulars_social_media_twitch': REGULARS_SOCIAL_MEDIA_TWITCH,
    'regulars_init_base_imports': REGULARS_INIT_BASE_IMPORTS,
    'regulars_init_messages_import': REGULARS_INIT_MESSAGES_IMPORT,
    'regulars_init_activity_roles_import': REGULARS_INIT_ACTIVITY_ROLES_IMPORT,
    'regulars_init_social_media_youtube': REGULARS_INIT_SOCIAL_MEDIA_YOUTUBE,
    'regulars_init_social_media_twitch': REGULARS_INIT_SOCIAL_MEDIA_TWITCH,
    'regulars_init_crate_all_async': REGULARS_INIT_CRATE_ALL_ASYNC,
    'regulars_init_add_process_regular_message': REGULARS_INIT_ADD_PROCESS_REGULAR_MESSAGE,
    'regulars_init_add_process_youtube': REGULARS_INIT_ADD_PROCESS_YOUTUBE,
    'regulars_init_add_process_twitch': REGULARS_INIT_ADD_PROCESS_TWITCH,
    'regulars_init_add_process_activity_roles_update': REGULARS_INIT_ADD_PROCESS_ACTIVITY_ROLES_UPDATE,
    'regulars_init_push_process': REGULARS_INIT_PUSH_PROCESS,
    'automod_actions_base_imports': AUTOMOD_ACTIONS_BASE_IMPORTS,
    'automod_actions_warning_import': AUTOMOD_ACTIONS_WARNING_IMPORT,
    'automod_actions_pending_messages_import': AUTOMOD_ACTIONS_PENDING_MESSAGES_IMPORT,
    'automod_actions_send_to_command': AUTOMOD_ACTIONS_SEND_TO_COMMAND,
    'automod_actions_remove': AUTOMOD_ACTIONS_REMOVE,
    'automod_actions_warn': AUTOMOD_ACTIONS_WARN,
    'automod_actions_remove_and_warn': AUTOMOD_ACTIONS_REMOVE_AND_WARN,
    'automod_actions_actions_list': AUTOMOD_ACTIONS_ACTIONS_LIST,
    'automod_actions_remove_func_call': AUTOMOD_ACTIONS_REMOVE_FUNC_CALL,
    'automod_actions_warn_func_call': AUTOMOD_ACTIONS_WARN_FUNC_CALL,
    'automod_actions_remove_and_warn_func_call': AUTOMOD_ACTIONS_REMOVE_AND_WARN_FUNC_CALL,
    'automod_actions_send_func_call': AUTOMOD_ACTIONS_SEND_FUNC_CALL,
    'automod_automods_base_imports': AUTOMOD_AUTOMODS_BASE_IMPORTS,
    'automod_automods_import_re': AUTOMOD_AUTOMODS_IMPORT_RE,
    'automod_automods_import_emoji': AUTOMOD_AUTOMODS_IMPORT_EMOJI,
    'automod_automods_const': AUTOMOD_AUTOMODS_CONST,
    'automod_automods_link': AUTOMOD_AUTOMODS_LINK,
    'automod_automods_smile': AUTOMOD_AUTOMODS_SMILE,
    'automod_automods_caps': AUTOMOD_AUTOMODS_CAPS,
    'automod_automods_mentions': AUTOMOD_AUTOMODS_MENTIONS,
    'automod_automods_main_func': AUTOMOD_AUTOMODS_MAIN_FUNC,
    'automod_automods_link_func_call': AUTOMOD_AUTOMODS_LINK_FUNC_CALL,
    'automod_automods_smiles_func_call': AUTOMOD_AUTOMODS_SMILES_FUNC_CALL,
    'automod_automods_caps_func_call': AUTOMOD_AUTOMODS_CAPS_FUNC_CALL,
    'automod_automods_mentions_func_call': AUTOMOD_AUTOMODS_MENTIONS_FUNC_CALL,
    'modals_init_import_embed': MODALS_INIT_IMPORT_EMBED,
    'modals_init_import_feedback': MODALS_INIT_IMPORT_FEEDBACK,
    'modals_init_import_report': MODALS_INIT_IMPORT_REPORT,
    'modals_modal_embed': MODAL_EMBED,
    'modals_modal_feedback': MODAL_FEEDBACK,
    'modals_modal_report': MODAL_REPORT,

    'utils_init_file_fun_text': UTILS_INIT_FILE_FUN_TEXT,
    'bot_main_file': BOT_MAIN_FILE,
    'bot_init_base_imports': BOT_INIT_BASE_IMPORTS,
    'bot_init_command_cog_import': BOT_INIT_COMMAND_COG_IMPORT,
    'bot_init_another_cog_import': BOT_INIT_ANOTHER_COG_IMPORT,
    'bot_init_body': BOT_INIT_BODY,
    'bot_init_add_command_cog': BOT_INIT_ADD_COMMAND_COG,
    'bot_init_add_another_cog': BOT_INIT_ADD_ANOTHER_COG,
    'bot_config_file_base_values': BOT_CONFIG_FILE_BASE_VALUES,
    'bot_config_file_weather_api_key': BOT_CONFIG_FILE_WEATHER_API_KEY,
    'bot_config_file_gpt_api_key': BOT_CONFIG_FILE_GPT_API_KEY,
}

REPLACEMENT = dict()
# REPLACEMENT.update(AUTOMOD_FUNCS_REPLACEMENT)

REPLACEMENT_WITH_GENERATE_DATA = dict()
# REPLACEMENT_WITH_GENERATE_DATA.update(AUTOMOD_ACTION_REPLACEMENT_WITH_GENERATED_DATA)
REPLACEMENT_WITH_GENERATE_DATA.update(COMMAND_REPLACEMENT_WITH_GENERATED_DATA)


# REPLACEMENT_WITH_GENERATE_DATA.update(MODALS_REPLACEMENT_WITH_GENERATE_DATA)


# def update_all_mini_generators(_key):
#     mg_generate_actions_list(_key)


def create_file(
        path,
        filename,
        code_paths,
        project_name,
        json_data=None,
        **replacement_data
):
    REPLACEMENT["_____project_name_for_imports_____"] = project_name

    for k, v in replacement_data.items():
        REPLACEMENT[k] = v

    # print(os.getcwd())
    if not os.path.exists(project_name):
        os.mkdir(project_name)
    os.chdir(project_name)
    # print(os.getcwd())

    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    # print(os.getcwd())

    with open(filename, mode="w", encoding="utf-8") as file:

        # print(">>>>>>>>>", json_data, json_data is None)
        if not (json_data is None):
            json.dump(json_data, file, ensure_ascii=False)
            os.chdir("../..")
            return

        file_code = ""
        for code_path_name in code_paths:
            if not code_path_name:
                continue
            code_path = TEMPLATES[code_path_name]
            for replace_key, replace_value in REPLACEMENT.items():
                if replace_key in code_path:
                    code_path = code_path.replace(replace_key, replace_value)
            for replace_with_gd_key, replace_with_gd_value in REPLACEMENT_WITH_GENERATE_DATA.items():
                if replace_with_gd_key in code_path:
                    code_path = code_path.replace(replace_with_gd_key, replace_with_gd_value(code_paths))

            file_code += code_path
        file.write(file_code)

    pass

    # print(">>>", os.getcwd())
    os.chdir("..")
    if path != ".":
        os.chdir("..")
    # print(">>>", os.getcwd())
