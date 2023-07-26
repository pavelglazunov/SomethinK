import json
import os
import shutil

from app.generator.creator import create_file

# from creator import create_file

progres = 0
#
with open("app/generator/templates/data_temp/data_messages_config_temp.json", "r", encoding="utf-8") as file:
    DATA_MESSAGE_CONFIG_TEMP = json.load(file)


#
# with open("templates/data_temp/data_messages_config_temp.json", "r", encoding="utf-8") as file:
#     DATA_MESSAGE_CONFIG_TEMP = json.load(file)


# TODO сравнивание путем сравнивания файлов расширение файла

def create_folder(folder, cfg: dict, project_name, extension="py", not_create=[], **replacement_data):
    for file_name, file_data in cfg.items():

        if f"{folder}.{file_name}.{extension}" in not_create:
            print("CONTINUE", file_name)
            continue
        code_paths = [k for k, v in file_data.items() if v]
        # if code_paths.count(False) == 4:
        #     continue
        json_data = None
        if extension == "json":
            json_data = file_data.get("file_data")
        create_file(
            path=folder,
            filename=f"{file_name}.{extension}",
            code_paths=code_paths,
            project_name=project_name,
            json_data=json_data,
            **replacement_data
        )
    pass


def generate(key: dict):
    os.chdir("app/generator")
    print("START_GENERATING", os.getcwd())

    user_config_file = {
        "channels_ID": {},
        "status": {},
        "roles_ID": {},
        "get_commands_from_direct_message": False,
        "roles_for_new_members": [],
        "automod": {},
        "regular_messages": [],
        "activity_roles": {},
        "events": {},
        "auto_responser": [],
        "social_media_notifications": {},
        "commands": {}
    }

    automod_func_keys = {
        "automod_func_base_imports": True,
        "automod_func_re_import": False,
        "automod_func_emoji_import": False,
        "automod_func_base_funcs": True,
        "automod_func_link": False,
        "automod_func_caps": False,
        "automod_func_mentions": False,
        "automod_func_smiles": False,
        "automod_func_main_func": True
    }
    automod_action_keys = {
        "automod_action_base_imports": True,
        "automod_action_send_import": False,
        "automod_action_send": False,
        "automod_action_remove": False,
        "automod_action_warn": False,
        "automod_action_remove_and_warn": False,
        "automod_action_funcs_list": True
    }

    utils_files_keys = {
        "__init__": {
            'utils_init_file_fun_text': True
        },
        "creator": {
            "utils_creator_imports": True,
            "utils_creator_create_activity_roles": False,
            "utils_creator_create_report_channel": False,
            "utils_creator_create_pending_message_channel": False,
            "utils_creator_create_logging_channel": False,
        },
        "decorators": {
            "utils_decorators_imports": True,
            "utils_decorators_command_allow_channels": False,
            "utils_decorators_base": True,
        },
        "messages": {
            'utils_messages_imports_and_body': True,
            'utils_messages_import_log': False,
            'utils_messages_get_description': False,
            'utils_messages_help_base': True,
            'utils_messages_send_message': False,
            'utils_messages_add_log_message_func_call': False,
            'utils_messages_send_event_message': False,
            'utils_messages_add_log_event_message_func_call': False,
            'utils_messages_error_message_part_1': True,
            'utils_messages_add_log_error_func_call': False,
            'utils_messages_error_message_part_2': True,
            'utils_messages_error_detect': True,

        },
        "parser": {
            "utils_parser_imports": True,
            "utils_parser_get_allow": False,
            "utils_parser_base": True,
        },
        "warnings": {
            "utils_warnings_imports": True,
            "utils_warnings_add_warning": False,
            "utils_warnings_remove_warnings": False,
            "utils_warnings_get_warnings": False,
        },
        "event_logging": {
            "utils_event_logging_file": True,

        },
        "on_load": {
            "utils_on_load_import_async_processes": False,
            "utils_on_load_import_creator": False,
            "utils_on_load_base_import": True,
            "utils_on_load_main_func": True,
            "utils_on_load_add_create_ar": False,
            "utils_on_load_add_create_report_channel": False,
            "utils_on_load_add_create_logging_channel": False,
            "utils_on_load_add_create_pending_message_channel": False,
            "utils_on_load_add_all_async_process": False
        }
    }

    regular_files_keys = {
        "__init__": {
            "regulars_init_base_imports": True,
            "regulars_init_messages_import": False,
            "regulars_init_activity_roles_import": False,
            "regulars_init_social_media_youtube": False,
            "regulars_init_social_media_twitch": False,
            "regulars_init_crate_all_async": True,
            "regulars_init_add_process_regular_message": False,
            "regulars_init_add_process_youtube": False,
            "regulars_init_add_process_twitch": False,
            "regulars_init_add_process_activity_roles_update": False,
            "regulars_init_push_process": True,
        },
        "activity_roles": {
            "regulars_activity_roles_file": False,

        },
        "messages": {
            "regulars_messages_file": False
        },
        "social_medias": {
            "regulars_social_media_imports": True,
            "regulars_social_media_import_youtube_parser": False,
            "regulars_social_media_import_twitch_parser": False,
            "regulars_social_media_youtube": False,
            "regulars_social_media_twitch": False,
        }
    }

    automod_files_keys = {
        "actions": {
            "automod_actions_base_imports": True,
            "automod_actions_warning_import": False,
            "automod_actions_pending_messages_import": False,
            "automod_actions_send_to_command": False,
            "automod_actions_remove": False,
            "automod_actions_warn": False,
            "automod_actions_remove_and_warn": False,
            "automod_actions_actions_list": True,
            "automod_actions_remove_func_call": False,
            "automod_actions_warn_func_call": False,
            "automod_actions_remove_and_warn_func_call": False,
            "automod_actions_send_func_call": False,
        },
        "automods": {
            'automod_automods_base_imports': True,
            'automod_automods_import_re': False,
            'automod_automods_import_emoji': False,
            'automod_automods_const': True,
            'automod_automods_link': False,
            'automod_automods_smile': False,
            'automod_automods_caps': False,
            'automod_automods_mentions': False,
            'automod_automods_main_func': True,
            'automod_automods_link_func_call': False,
            'automod_automods_smiles_func_call': False,
            'automod_automods_caps_func_call': False,
            'automod_automods_mentions_func_call': False,
        }
    }

    modals_files_keys = {
        "__init__": {
            'modals_init_import_embed': False,
            'modals_init_import_feedback': False,
            'modals_init_import_report': False,
        },
        "embed_modals": {
            'modals_modal_embed': False,
        },
        "feedback_modals": {
            'modals_modal_feedback': False,
        },
        "report_modals": {
            'modals_modal_report': False,
        }

    }

    cogs_files_keys = {
        "__init__": {
            'cogs_init_import_another': False,
            'cogs_init_import_all_message': True,
            'cogs_init_import_help': True,
            'cogs_init_import_command': False,
        },
        "all_messages": {
            'cogs_all_messages_base_imports': True,
            'cogs_all_messages_automod_imports': False,
            'cogs_all_messages_logging_import': False,
            'cogs_all_messages_send_event_message_import': False,
            'cogs_all_messages_autoresponse_const': False,
            'cogs_all_messages_cog': True,
            'cogs_all_messages_on_message_edit': False,
            'cogs_all_messages_on_message': False,
            'cogs_all_messages_add_automod_call': False,
            'cogs_all_messages_add_auto_response': False,
            'cogs_all_messages_on_button_click': True,
            'cogs_all_messages_add_send_action_buttons_events': False,
            'cogs_all_messages_add_help_buttons_events': True,
        },
        "another": {
            'cogs_another_commands_base_imports': True,
            'cogs_another_commands_import_gpt': False,
            'cogs_another_commands_import_requests': False,
            'cogs_another_commands_import_embed_modal': False,
            'cogs_another_commands_import_feedback_modal': False,
            'cogs_another_commands_import_weather_api_key': False,
            'cogs_another_commands_import_translate': False,
            'cogs_another_commands_translate_language_list': False,
            'cogs_another_commands_set_openai_token': False,
            'cogs_another_commands_cog': True,
            'cogs_command_color': False,
            'cogs_command_nick': False,
            'cogs_command_joke': False,
            'cogs_command_weather': False,
            'cogs_command_translate': False,
            'cogs_command_say': False,
            'cogs_command_avatar': False,
            'cogs_command_gpt': False,
            'cogs_command_embed': False,
            'cogs_command_feedback': False,
            'cogs_command_errors': True,
        },
        "events_handlers": {
            'cogs_events_handlers_base_imports': True,
            'cogs_events_handlers_events_imports': False,
            'cogs_events_handlers_cog': True,
            'cogs_events_handlers_add_loader': False,
            'cogs_events_handlers_on_member_join': False,
            'cogs_events_handlers_add_auto_role': False,
            'cogs_events_handlers_join_event': False,
            'cogs_events_handlers_on_member_leave': False,
        },
        "help": {
            "cogs_help_base": True
        },
        "moderation": {
            'cogs_command_imports': True,
            'cogs_command_import_add_warning': False,
            'cogs_command_import_get_warnings': False,
            'cogs_command_import_remove_warnings': False,
            'cogs_command_timeout_list': False,
            'cogs_command_cog': True,
            'cogs_command_ban': False,
            'cogs_command_kick': False,
            'cogs_command_unban': False,
            'cogs_command_mute': False,
            'cogs_command_unmute': False,
            'cogs_command_chatmute': False,
            'cogs_command_chatunmute': False,
            'cogs_command_timeout': False,
            'cogs_command_rmtimeout': False,
            'cogs_command_fullban': False,
            'cogs_command_clear': False,
            'cogs_command_afk': False,
            'cogs_command_move': False,
            'cogs_command_deafen': False,
            'cogs_command_undeafen': False,
            'cogs_command_addrole': False,
            'cogs_command_rmrole': False,
            'cogs_command_ping': False,
            'cogs_command_slowmode': False,
            'cogs_command_vkick': False,
            'cogs_command_warn': False,
            'cogs_command_warns': False,
            'cogs_command_rmwarn': False,
            'cogs_command_report': False,
            'cogs_command_errors': True,
        },
    }

    data_files_keys = {
        "config": {
            "add_file": True,
            "file_data": user_config_file
        },
        "messages_config": {
            "add_file": True,
            "file_data": DATA_MESSAGE_CONFIG_TEMP
        },

        "pending_messages": {
            "add_file": False,
            "file_data": {}
        },
        "user_warnings": {
            "add_file": False,
            "file_data": {}
        }
    }

    _bot_metadata = key.get("bot_metadata", {})
    user_config_file["roles_ID"]["everyone_id"] = int(_bot_metadata.get("everyone_id", 0))

    print("PROJECT NAME", _bot_metadata.get("project_name"))

    replacement_config = {
        "_____bot_token_____": _bot_metadata.get("bot_token")
    }
    main_files_keys = {
        "__init__": {
            'bot_init_base_imports': True,
            'bot_init_command_cog_import': False,
            'bot_init_another_cog_import': False,
            'bot_init_body': True,
            'bot_init_add_command_cog': False,
            'bot_init_add_another_cog': False,
        },
        "config": {
            'bot_config_file_base_values': True,
            'bot_config_file_weather_api_key': False,
            'bot_config_file_gpt_api_key': False,
        },
        f"bot": {
            'bot_main_file': True,
        },
    }

    not_bot_files_keys = {
        "requirements": {
            "base": True,
            "openai": False,
            "translate": False,
            "scrapetube": False
        },
        "information": {
            "information": True
        }

    }

    files_flags = {
        "automod.actions.py": False,
        "automod.automods.py": False,

        "cogs.__init__.py": True,
        "cogs.all_messages.py": True,
        "cogs.another.py": False,
        "cogs.event_handlers.py": True,
        "cogs.help.py": True,
        "cogs.moderation.py": False,

        "data.config.json": True,
        "data.messages_config.json": True,
        "data.pending_messages.json": False,
        "data.user_warnings.json": False,

        "modals.__init__.py": False,
        "modals.embed_modals.py": False,
        "modals.feedback_modals.py": False,
        "modals.report_modals.py": False,

        "regulars.__init__.py": False,
        "regulars.activity_roles.py": False,
        "regulars.messages.py": False,
        "regulars.social_medias.py": False,

        "utils.__init__.py": True,
        "utils.creator.py": False,
        "utils.decorators.py": True,
        "utils.event_logging.py": False,
        "utils.messages.py": True,
        "utils.on_load.py": True,
        "utils.parser.py": True,
        "utils.warnings.py": False,  # <-

        ".__init__.py": True,
        ".config.py": True,
        ".runner.py": True,
    }
    # add_automod = False
    add_modals = False

    command_block = key.get("moderation", {})
    commands_cfg_keys = []
    for command, command_data in command_block.items():
        if not command_data.get("enable"):
            continue

        user_config_file["commands"][command] = {
            "channels": [int(i[1]) for i in command_data.get("channels")],
            "roles": [int(i[1]) for i in command_data.get("roles")]
        }
        if command == "warn":
            data_files_keys["user_warnings"]["add_file"] = True
            utils_files_keys["warnings"]["utils_warnings_add_warning"] = True
            cogs_files_keys["moderation"]["cogs_command_import_add_warning"] = True
            files_flags["data.user_warnings.json"] = True
            files_flags["utils.warnings.py"] = True
        if command == "rmwarn":
            data_files_keys["user_warnings"]["add_file"] = True
            utils_files_keys["warnings"]["utils_warnings_remove_warnings"] = True
            cogs_files_keys["moderation"]["cogs_command_import_remove_warnings"] = True
            files_flags["data.user_warnings.json"] = True
            files_flags["utils.warnings.py"] = True
        if command == "warns":
            data_files_keys["user_warnings"]["add_file"] = True
            utils_files_keys["warnings"]["utils_warnings_get_warnings"] = True
            cogs_files_keys["moderation"]["cogs_command_import_get_warnings"] = True
            files_flags["data.user_warnings.json"] = True
            files_flags["utils.warnings.py"] = True

        if command == "report":
            utils_files_keys["creator"]["utils_creator_create_report_channel"] = True
            utils_files_keys["on_load"]["utils_on_load_import_creator"] = True
            utils_files_keys["on_load"]["utils_on_load_add_create_report_channel"] = True
            modals_files_keys["report_modals"]["modals_modal_report"] = True

            modals_files_keys["report_modals"]["modals_modal_report"] = True
            modals_files_keys["__init__"]["modals_init_import_report"] = True

            files_flags["modals.report_modals.py"] = True
            files_flags["modals.__init__.py"] = True

            if command_data.get("special_channel"):
                user_config_file["channels_ID"]["report_channel_id"] = int(command_data.get("special_channel"))
                if user_config_file["channels_ID"]["report_channel_id"] == -1:
                    files_flags["utils.creator.py"] = True

        if command == "timeout":
            cogs_files_keys["moderation"]["cogs_command_timeout_list"] = True
        if act := command_data.get("action"):
            files_flags["automod.actions.py"] = True
            files_flags["automod.automods.py"] = True
            if act == "--send":
                data_files_keys["pending_messages"]["add_file"] = True

                cogs_files_keys["all_messages"]["cogs_all_messages_add_send_action_buttons_events"] = True

                utils_files_keys["creator"]["utils_creator_create_pending_message_channel"] = True
                utils_files_keys["on_load"]["utils_on_load_import_creator"] = True
                utils_files_keys["on_load"]["utils_on_load_add_create_pending_message_channel"] = True

                automod_files_keys["actions"]["automod_actions_pending_messages_import"] = True
                automod_files_keys["actions"]["automod_actions_send_to_command"] = True
                automod_files_keys["actions"]["automod_actions_send_func_call"] = True

                user_config_file["channels_ID"]["pending_message_channel_id"] = -1

                files_flags["data.pending_messages.json"] = True

                files_flags["utils.creator.py"] = True

            if act == "--remove":
                automod_files_keys["actions"]["automod_actions_remove"] = True
                automod_files_keys["actions"]["automod_actions_remove_func_call"] = True
            if act == "--remove-warn":
                automod_files_keys["actions"]["automod_actions_warning_import"] = True
                automod_files_keys["actions"]["automod_actions_remove_and_warn"] = True
                automod_files_keys["actions"]["automod_actions_remove_and_warn_func_call"] = True

                utils_files_keys["warnings"]["utils_warnings_add_warning"] = True

                files_flags["data.user_warnings.json"] = True

            if act == "--warn":
                automod_files_keys["actions"]["automod_actions_warning_import"] = True
                automod_files_keys["actions"]["automod_actions_warn"] = True
                automod_files_keys["actions"]["automod_actions_warn_func_call"] = True

                utils_files_keys["warnings"]["utils_warnings_add_warning"] = True

                files_flags["data.user_warnings.json"] = True

            if command == "links":
                automod_files_keys["automods"]["automod_automods_import_re"] = True
                automod_files_keys["automods"]["automod_automods_link"] = True
                automod_files_keys["automods"]["automod_automods_link_func_call"] = True

                user_config_file["automod"]["links"] = act
                user_config_file["automod"]["links_ignore_channels"] = [int(i[1]) for i in
                                                                        command_data.get("channels", [])]
                user_config_file["automod"]["links_ignore_roles"] = [int(i[1]) for i in command_data.get("roles", [])]

                # automod_func_keys["automod_func_link"] = True
                # automod_func_keys["automod_func_re_import"] = True

            if command == "caps":
                automod_files_keys["automods"]["automod_automods_caps"] = True
                automod_files_keys["automods"]["automod_automods_caps_func_call"] = True

                user_config_file["automod"]["caps"] = act
                user_config_file["automod"]["caps_min_length"] = command_data.get("min_length", 20)
                user_config_file["automod"]["caps_min_percent"] = command_data.get("percent", 80)

                user_config_file["automod"]["caps_ignore_channels"] = [int(i[1]) for i in
                                                                       command_data.get("channels", [])]
                user_config_file["automod"]["caps_ignore_roles"] = [int(i[1]) for i in command_data.get("roles", [])]

                # automod_func_keys["automod_func_caps"] = True
            if command == "mentions":
                automod_files_keys["automods"]["automod_automods_import_re"] = True
                automod_files_keys["automods"]["automod_automods_import_emoji"] = True
                automod_files_keys["automods"]["automod_automods_mentions"] = True
                automod_files_keys["automods"]["automod_automods_mentions_func_call"] = True

                user_config_file["automod"]["mentions"] = act
                user_config_file["automod"]["mentions_min_count"] = command_data.get("count", 3)

                user_config_file["automod"]["mentions_ignore_channels"] = [int(i[1]) for i in
                                                                           command_data.get("channels", [])]
                user_config_file["automod"]["mentions_ignore_roles"] = [int(i[1]) for i in
                                                                        command_data.get("roles", [])]

                # automod_func_keys["automod_func_emoji_import"] = True
                # automod_func_keys["automod_func_mentions"] = True
                # automod_func_keys["automod_func_re_import"] = True

            if command == "smile":
                automod_files_keys["automods"]["automod_automods_import_re"] = True
                automod_files_keys["automods"]["automod_automods_import_emoji"] = True
                automod_files_keys["automods"]["automod_automods_smile"] = True
                automod_files_keys["automods"]["automod_automods_smiles_func_call"] = True

                user_config_file["automod"]["smiles"] = act
                user_config_file["automod"]["emoji_min_message_length"] = command_data.get("min_length", 20)
                user_config_file["automod"]["emoji_min_percent"] = command_data.get("percent", 80)

                user_config_file["automod"]["smile_ignore_channels"] = [int(i[1]) for i in
                                                                        command_data.get("channels", [])]
                user_config_file["automod"]["smile_ignore_roles"] = [int(i[1]) for i in
                                                                     command_data.get("roles", [])]

                # automod_func_keys["automod_func_emoji_import"] = True
                # automod_func_keys["automod_func_re_import"] = True
                # automod_func_keys["automod_func_smiles"] = True

        else:
            DATA_MESSAGE_CONFIG_TEMP["commands"][command]["description"] = command_data.get("description")

            cogs_files_keys["moderation"][f"cogs_command_{command}"] = True
            commands_cfg_keys.append(command)

    _end = len(commands_cfg_keys)
    another_block = key.get("another", {})
    another_commands_cfg_key = []
    for command, command_data in another_block.items():
        if not command_data.get("enable"):
            continue

        user_config_file["commands"][command] = {
            "channels": [int(i[1]) for i in command_data.get("channels")],
            "roles": [int(i[1]) for i in command_data.get("roles")]
        }
        print("ANOTHER_COMMAND:", command)
        DATA_MESSAGE_CONFIG_TEMP["commands"][command]["description"] = command_data.get("description")

        cogs_files_keys["another"][f"cogs_command_{command}"] = True

        if command == "gpt":
            cogs_files_keys["another"]["cogs_another_commands_import_gpt"] = True
            cogs_files_keys["another"]["cogs_another_commands_set_openai_token"] = True

            main_files_keys["config"]["bot_config_file_gpt_api_key"] = True
            replacement_config["_____gpt_api_token_____"] = command_data.get("token")

            not_bot_files_keys["requirements"]["openai"] = True

        if command == "weather":
            cogs_files_keys["another"]["cogs_another_commands_import_requests"] = True
            cogs_files_keys["another"]["cogs_another_commands_import_weather_api_key"] = True
            main_files_keys["config"]["bot_config_file_weather_api_key"] = True
            replacement_config["_____weather_api_token_____"] = command_data.get("token")

        if command == "translate":
            cogs_files_keys["another"]["cogs_another_commands_import_translate"] = True
            cogs_files_keys["another"]["cogs_another_commands_translate_language_list"] = True

            not_bot_files_keys["requirements"]["translate"] = True

        if command == "joke":
            cogs_files_keys["another"]["cogs_another_commands_import_requests"] = True
        if command == "embed":
            cogs_files_keys["another"]["cogs_another_commands_import_embed_modal"] = True

            modals_files_keys["embed_modals"]["modals_modal_embed"] = True
            modals_files_keys["__init__"]["modals_init_import_embed"] = True

            files_flags["modals.embed_modals.py"] = True
            files_flags["modals.__init__.py"] = True
        if command == "feedback":
            cogs_files_keys["another"]["cogs_another_commands_import_feedback_modal"] = True
            modals_files_keys["feedback_modals"]["modals_modal_feedback"] = True
            modals_files_keys["__init__"]["modals_init_import_feedback"] = True

            files_flags["modals.feedback_modals.py"] = True
            files_flags["modals.__init__.py"] = True
        another_commands_cfg_key.append(command)

    if "feedback" in another_commands_cfg_key:
        add_modals = True
    if "embed" in another_commands_cfg_key:
        add_modals = True
    if "report" in commands_cfg_keys:
        add_modals = True

    _settings = key.get("settings", {})
    if _settings.get("logging", {}).get("enable", False):
        logging_events = '("ERRORS", '
        for le in _settings.get("logging", {}).get("values", []):
            logging_events += f'"{le}", '
            if le == "events":
                logging_events += '"leave", "join", '
        logging_events += ')'

        replacement_config["_____logging_events_____"] = logging_events

        utils_files_keys["creator"]["utils_creator_create_logging_channel"] = True
        utils_files_keys["on_load"]["utils_on_load_import_creator"] = True
        utils_files_keys["on_load"]["utils_on_load_add_create_logging_channel"] = True
        cogs_files_keys["all_messages"]["cogs_all_messages_logging_import"] = True

        utils_files_keys["messages"]["utils_messages_import_log"] = True
        utils_files_keys["messages"]["utils_messages_add_log_message_func_call"] = True
        utils_files_keys["messages"]["utils_messages_add_log_event_message_func_call"] = True

        user_config_file["channels_ID"]["logging_channel_id"] = int(_settings.get("logging", {}).get("channel_id", -1))
        if user_config_file["channels_ID"]["logging_channel_id"] == -1:
            files_flags["utils.creator.py"] = True
        files_flags["utils.event_logging.py"] = True

    user_config_file["status"]["type"] = _settings.get("status", {}).get("type", "playing")
    user_config_file["status"]["text"] = _settings.get("status", {}).get("text", "лучшего бота")

    _roles = key.get("roles", {})
    if _roles.get("ar_enable", False):
        user_config_file["ar_update_interval"] = int(_roles.get("update_interval"))
        user_config_file["activity_roles"]["ar_enable"] = True

        utils_files_keys["creator"]["utils_creator_create_activity_roles"] = True
        utils_files_keys["on_load"]["utils_on_load_import_creator"] = True
        utils_files_keys["on_load"]["utils_on_load_add_create_ar"] = True
        regular_files_keys["activity_roles"]["regulars_activity_roles_file"] = True
        regular_files_keys["__init__"]["regulars_init_activity_roles_import"] = True
        regular_files_keys["__init__"]["regulars_init_add_process_activity_roles_update"] = True

        files_flags["regulars.__init__.py"] = True
        files_flags["regulars.activity_roles.py"] = True

        files_flags["utils.creator.py"] = True

        ar_list = {}
        for k, v in _roles.items():
            if k in ("ar_enable", "start_roles", "update_interval"):
                continue
            if v.get("enable"):
                ar_list[k] = {
                    "role_id": 0,
                    "value": v.get("value").replace("#", "")
                }
        user_config_file["activity_roles"]["roles"] = ar_list

    if _roles.get("start_roles", {}):
        user_config_file["roles_for_new_members"] = [int(i[1]) for i in _roles.get("start_roles", {}).get("roles", [])]

        cogs_files_keys["events_handlers"]["cogs_events_handlers_on_member_join"] = True
        cogs_files_keys["events_handlers"]["cogs_events_handlers_add_auto_role"] = True

    _messages = key.get("messages", {})
    if _messages.get("events", {}):
        utils_files_keys["messages"]["utils_messages_send_event_message"] = True
        cogs_files_keys["events_handlers"]["cogs_events_handlers_events_imports"] = True
        __events = _messages.get("events", {})
        _user_events = {}
        _user_events["join"] = []
        _user_events["leave"] = []
        for k, v in __events.items():
            if v.get("type") == "join":
                cogs_files_keys["events_handlers"]["cogs_events_handlers_on_member_join"] = True
                cogs_files_keys["events_handlers"]["cogs_events_handlers_join_event"] = True
                _user_events["join"].append(v)
            if v.get("type") == "leave":
                cogs_files_keys["events_handlers"]["cogs_events_handlers_on_member_leave"] = True
                _user_events["leave"].append(v)
        user_config_file["events"] = _user_events

    if _messages.get("time_message"):
        __regular_messages = _messages.get("time_message", {})
        regular_messages_list = []

        files_flags["regulars.__init__.py"] = True
        files_flags["regulars.messages.py"] = True

        for k, v in __regular_messages.items():
            regular_messages_list.append(v)

        user_config_file["regular_messages"] = regular_messages_list

    if _messages.get("auto_response", {}):
        utils_files_keys["messages"]["utils_messages_send_event_message"] = True
        cogs_files_keys["all_messages"]["cogs_all_messages_send_event_message_import"] = True
        cogs_files_keys["all_messages"]["cogs_all_messages_autoresponse_const"] = True
        cogs_files_keys["all_messages"]["cogs_all_messages_on_message_edit"] = True
        cogs_files_keys["all_messages"]["cogs_all_messages_add_auto_response"] = True

        __auto_response = _messages.get("auto_response", {})
        __auto_response_list = []
        for k, v in __auto_response.items():
            __auto_response_list.append(v)

        user_config_file["auto_responser"] = __auto_response_list

    if _messages.get("time_message"):
        regular_files_keys["messages"]["regulars_messages_file"] = True
        regular_files_keys["__init__"]["regulars_init_messages_import"] = True
        regular_files_keys["__init__"]["regulars_init_add_process_regular_message"] = True

    _social_media = key.get("social_media", {})
    if _social_media:
        files_flags["regulars.__init__.py"] = True
        files_flags["regulars.social_medias.py"] = True

    if _social_media.get("youtube", {}):
        regular_files_keys["social_medias"]["regulars_social_media_import_youtube_parser"] = True
        regular_files_keys["social_medias"]["regulars_social_media_youtube"] = True
        regular_files_keys["__init__"]["regulars_init_social_media_youtube"] = True
        regular_files_keys["__init__"]["regulars_init_add_process_youtube"] = True

        not_bot_files_keys["requirements"]["scrapetube"] = True

        __youtube = _social_media.get("youtube", {})
        __youtube_list = []
        for k, v in __youtube.items():
            __youtube_list.append(v)

        user_config_file["social_media_notifications"]["youtube"] = __youtube_list

    if _social_media.get("twitch", {}):
        regular_files_keys["social_medias"]["regulars_social_media_import_twitch_parser"] = True
        regular_files_keys["social_medias"]["regulars_social_media_twitch"] = True
        regular_files_keys["__init__"]["regulars_init_social_media_twitch"] = True
        regular_files_keys["__init__"]["regulars_init_add_process_twitch"] = True

        __twitch = _social_media.get("twitch", {})
        __twitch_list = []
        for k, v in __twitch.items():
            __twitch_list.append(v)

        user_config_file["social_media_notifications"]["twitch"] = __twitch_list

    if regular_files_keys["__init__"]["regulars_init_crate_all_async"]:
        utils_files_keys["on_load"]["utils_on_load_import_async_processes"] = True
        utils_files_keys["on_load"]["utils_on_load_add_all_async_process"] = True

    if files_flags["utils.on_load.py"]:
        cogs_files_keys["events_handlers"]["cogs_events_handlers_add_loader"] = True

    if files_flags["automod.automods.py"] or files_flags["automod.actions.py"]:
        cogs_files_keys["all_messages"]["cogs_all_messages_automod_imports"] = True
        cogs_files_keys["all_messages"]["cogs_all_messages_on_message_edit"] = True
        cogs_files_keys["all_messages"]["cogs_all_messages_on_message"] = True
        cogs_files_keys["all_messages"]["cogs_all_messages_add_automod_call"] = True

    # if another_block:
    #     generate_another_command(commands_cfg_keys[_end:])
    local_vars = locals()
    print(local_vars)
    # create_data_files([k for k, v in data_file_keys.items() if v])

    if commands_cfg_keys or another_commands_cfg_key:
        utils_files_keys["parser"]["utils_parser_get_allow"] = True
        utils_files_keys["messages"]["utils_messages_get_description"] = True
        utils_files_keys["messages"]["utils_messages_send_message"] = True
        utils_files_keys["decorators"]["utils_decorators_command_allow_channels"] = True

    if commands_cfg_keys:
        cogs_files_keys["__init__"]["cogs_init_import_command"] = True
        main_files_keys["__init__"]["bot_init_command_cog_import"] = True
        main_files_keys["__init__"]["bot_init_add_command_cog"] = True
        files_flags["cogs.moderation.py"] = True
    if another_commands_cfg_key:
        cogs_files_keys["__init__"]["cogs_init_import_another"] = True
        main_files_keys["__init__"]["bot_init_another_cog_import"] = True
        main_files_keys["__init__"]["bot_init_add_another_cog"] = True
        files_flags["cogs.another.py"] = True

        # automod_files_keys["automods"]
        # decorators_file_keys["allowed_channels"] = True

    print(files_flags)
    blocked_files = [k for k, v in files_flags.items() if not v]
    print(f'{blocked_files = }')
    create_folder("automod", automod_files_keys, key.get("bot_metadata", {}).get("project_name"),
                  not_create=blocked_files)
    # create_automod_files(automod_func_keys, automod_action_keys)
    create_folder("cogs", cogs_files_keys, key.get("bot_metadata", {}).get("project_name"), not_create=blocked_files)

    create_folder("data", data_files_keys, key.get("bot_metadata", {}).get("project_name"), extension="json",
                  not_create=blocked_files)
    _modals = []

    # for cmd in ("feedback", "embed", "report"):
    #     if cmd in commands_cfg_keys:
    #         _modals.append(cmd)

    # if add_modals:
    create_folder("modals", modals_files_keys, key.get("bot_metadata", {}).get("project_name"),
                  not_create=blocked_files)

    create_folder("utils", utils_files_keys, key.get("bot_metadata", {}).get("project_name"), not_create=blocked_files)
    create_folder("regulars", regular_files_keys, key.get("bot_metadata", {}).get("project_name"),
                  not_create=blocked_files)
    create_folder(".", main_files_keys, key.get("bot_metadata", {}).get("project_name"), **replacement_config)

    create_folder(".", not_bot_files_keys, key.get("bot_metadata", {}).get("project_name"), extension="txt")
    # create_folder(".", not_bot_files_keys, key.get("bot_metadata", {}).get("project_name"), **replacement_config)

    shutil.make_archive(key.get("bot_metadata", {}).get("project_name"), "zip",
                        key.get("bot_metadata", {}).get("project_name"))
    shutil.rmtree(key.get("bot_metadata", {}).get("project_name"))
    os.chdir("../..")

# if __name__ == "__main__":
#     print(5)
#     with open("../test_json.json", encoding="utf-8") as file:
#         data = json.load(file)
#     # print(os.getcwd())
#
#     if os.path.exists("testbot"):
#         shutil.rmtree("testbot")
#     generate(data)
