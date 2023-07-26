# import json
#
# # from shlex import quote
#
"""
Валидация данных, полученных в JSON с сайта

коды ошибок

код  | ошибка
-1  -> неизвестная ошибка

100 -> ошибка преобразования в JSON
101 -> ошибка преобразования в integer
102 -> ошибка преобразования в boolean
103 -> ошибка преобразования в string
104 -> ошибка преобразования в float
105 -> ошибка преобразования в list

200 -> неизвестная команда
201 -> ошибка в описании
202 -> ошибка в списке ролей
203 -> ошибка в списке ролей или каналов, длина != 2
204 -> ошибка в списке ролей или каналов, id < -1
205 -> ошибка в списке автомодерации, значения нет в списке действий: ("--send", "--remove", "--warn", "--remove-warn")
206 -> ошибка в embed, значение не словарь
207 -> ошибка в embed_data, embed не строка
208 -> ошибка в embed_data, color не строка
209 -> ошибка в embed_data, color не HEX
210 -> ошибка в embed_data, footer не строка
211 -> ошибка в embed_data, header не строка
212 -> ошибка в embed_data, header не удовлетворил длине (1-200)
213 -> ошибка в embed_data, image_url не строка
214 -> ошибка в embed_data, image_url не ссылка
215 -> ошибка в embed, content не строка
216 -> ошибка в embed, content не удовлетворил длине (1-3000)
217 -> ошибка в embed, enable_embed не boolean
218 -> ошибка в regular messages, channel не строка
219 -> ошибка в regular messages, channel < -1
220 -> ошибка в regular messages, channel строка, но не число
221 -> ошибка в regular messages, interval не строка
222 -> ошибка в regular messages, interval < 0 or > 1000
223 -> ошибка в regular messages, interval строка, но не число
224 -> ошибка в regular messages, time не строка
225 -> ошибка в regular messages, длина time != 5
226 -> ошибка в regular messages, time строка, но не время
227 -> ошибка в regular messages, units_of_measure не строка
228 -> ошибка в regular messages, units_of_measure нет в допустимых значениях
229 -> ошибка в events, type не строка
230 -> ошибка в events, type нет в допустимых значениях
231 -> ошибка в auto responser, trigger не строка
232 -> ошибка в auto responser, trigger не удовлетворил длине (1-50)
233 -> ошибка в auto responser, trigger type не строка
234 -> ошибка в auto responser, trigger type нет в допустимых значениях
235 -> ошибка в settings, нет logging
236 -> ошибка в settings, нет status
237 -> ошибка в settings, logging не строка
238 -> ошибка в settings, logging < -1
239 -> ошибка в settings, logging не число
240 -> ошибка в settings, enable не boolean
241 -> ошибка в settings, values не list
242 -> ошибка в settings, values нет в допустимых значениях
243 -> ошибка в settings, status text не строка
244 -> ошибка в settings, status text не удовлетворил длине (1-127)
245 -> ошибка в settings, status type не строка
246 -> ошибка в settings, status type нет в допустимых значениях
247 -> ошибка в roles, enable не boolean
248 -> ошибка в roles, start_roles не dict
249 -> ошибка в roles, start_roles.roles не list
250 -> ошибка в roles, значения start_roles.roles
251 -> ошибка в roles, update interval не строка
252 -> ошибка в roles, update interval <0 or >604800
253 -> ошибка в roles, update interval строка, но не число
254 -> ошибка в roles, ar role > color не строка
256 -> ошибка в roles, ar role > color не цвет
257 -> ошибка в sm, youtube не dict
258 -> ошибка в sm, twitch не dict
259 -> ошибка в sm, youtube > channel_id не строка
260 -> ошибка в sm, youtube > channel_id не удовлетворил длине (1-25)
261 -> ошибка в sm, youtube > channel_id <0
262 -> ошибка в sm, youtube > channel_id строка, но не число
263 -> ошибка в sm, youtube > link не строка
264 -> ошибка в sm, youtube > link не ссылка
265 -> ошибка в sm, youtube > message не строка
266 -> ошибка в sm, youtube > message не удовлетворил длине (1-3000)
267 -> ошибка в sm, twitch > channel_id не строка
268 -> ошибка в sm, twitch > channel_id не удовлетворил длине (1-25)
269 -> ошибка в sm, twitch > channel_id <0
270 -> ошибка в sm, twitch > channel_id строка, но не число
271 -> ошибка в sm, twitch > link не строка
272 -> ошибка в sm, twitch > link не ссылка
273 -> ошибка в sm, twitch > message не строка
274 -> ошибка в sm, twitch > message не удовлетворил длине (1-3000)
275 -> ошибка длины ID >25
276 -> ошибка в roles, roles не dict
277 -> ошибка в moderation, moderation не dict
278 -> ошибка в moderation, moderation == {}
279 -> ошибка в messages, messages не dict
280 -> ошибка в another, another не dict
281 -> ошибка в sm, sm не dict
282 -> ошибка в settings, settings не dict

 ->
 ->
 ->

тип данных:
            r'^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$',

"""

# ALL_COMMANDS = ['ban', 'unban', 'mute', 'unmute', 'chatmute', 'chatunmute', 'timeout', 'rmtimeout', 'fullban', 'clear',
#                 'afk', 'warn', 'report', 'warns', 'move', 'rmwarn', 'deafen', 'addrole', 'undeafen', 'rmrole', 'ping',
#                 'slowmode', 'kick', 'vkick', 'links', 'smile', 'caps', 'mentions', 'ar_update', 'add_yt', 'rm_yt',
#                 'add_tw', 'rm_tw', "ignore_admin", "ignore_bot"]
#
#
# def on_error(error_code):
#     def decorator(func):
#         def wrapper(*args):
#             try:
#                 func(*args)
#                 return 0
#             except Exception:
#                 return error_code
#
#         return wrapper
#
#     return decorator
#
#
# @on_error(100)
# def _json(data):
#     json.dumps(data)
#
#
# @on_error(101)
# def _int(data):
#     int(data)
#
#
# @on_error(102)
# def _boolean(data):
#     bool(data)
#
#
# @on_error(103)
# def _string(data):
#     str(data)
#
#
# @on_error(104)
# def _float(data):
#     float(data)
#
#
# def _length(data, length):
#     return len(data) <= length
#
#
import datetime
import json
import re


def moderation(data: dict):
    if not isinstance(data, dict):
        return 277

    if not data.get("moderation"):
        return 278
    for _command in data["moderation"].values():
        print(_command)
        if _command.get("action"):
            continue
        if error_code := valid_command_data(_command):
            return error_code
    return False


def roles(data: dict):
    if not isinstance(data, dict):
        return 276
    if error_code := validate_roles_data(data):
        return error_code
    return False


def messages(data: dict):
    if not isinstance(data, dict):
        return 279
    # if not (data["messages"].get("auto_response"))
    for _command in [*data["messages"]["auto_response"].values()] + [*data["messages"]["events"].values()] + [
        *data["messages"]["time_message"].values()]:
        if error_code := validate_message_data(_command):
            return error_code
    return False


def another(data: dict):
    if not isinstance(data, dict):
        return 280
    for _command in data["another"].values():
        if error_code := valid_command_data(_command):
            return error_code
    return False


def social_media(data: dict):
    if not isinstance(data, dict):
        return 281
    if error_code := validate_social_media(data.get("social_media", {})):
        return error_code
    return False


def customization(data):
    return False


def settings(data: dict):
    if not isinstance(data, dict):
        return 282
    if error_code := validate_settings_data(data.get("settings", {})):
        return error_code
    return False


def _is_valid_list_of_lists(lst: list) -> int or bool:
    for item in lst:
        if not isinstance(item, list):
            return 105
        if len(item) != 2:
            return 203
        if not isinstance(item[0], str):
            return 103
        if not isinstance(item[1], str):
            return 103
        if len(item[1]) > 25:
            return 275
        try:
            num = int(item[1])
            if num < -1:
                return 204
        except ValueError:
            return 101
    return False


def valid_command_data(data: dict) -> bool or int:
    if error_code := _is_valid_list_of_lists(data['channels']):
        return error_code

    # description =
    if not isinstance(data.get("description", None), str):
        print(data)
        return 103
    if not isinstance(data['enable'], bool):
        return 102
    if error_code := _is_valid_list_of_lists(data['roles']):
        return error_code
    if 'special_channel' in data:
        special_channel = data['special_channel']
        if not isinstance(special_channel, str):
            return 103
        try:
            num = int(special_channel)
            if num < -1:
                return 204
        except ValueError:
            return 101
    if 'token' in data:
        token = data['token']
        if not isinstance(token, str):
            return 103
    if 'action' in data:
        action = data['action']
        if not isinstance(action, str):
            return 103
        if not (action in ("--send", "--remove", "--warn", "--remove-warn")):
            return 205
    if 'min_length' in data:
        min_length = data['min_length']
        if not isinstance(min_length, int):
            return 101
    if 'percent' in data:
        percent = data['percent']
        if not isinstance(percent, int):
            return 101
    if 'count' in data:
        count = data['count']
        if not isinstance(count, int):
            return 101

    return False


def _validate_embed(embed_data: dict) -> bool or int:
    if not isinstance(embed_data, dict):
        return 206
    if not isinstance(embed_data.get("author"), str):
        return 207
    if not isinstance(embed_data.get("color"), str):
        return 208
    if not re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', embed_data.get("color")):
        return 209
    if not isinstance(embed_data.get("footer_content"), str):
        return 210
    if not isinstance(embed_data.get("header"), str):
        return 211
    if not (1 <= len(embed_data.get("header")) <= 200):
        return 212
    if not isinstance(embed_data.get("image_url"), str):
        return 213
    if not embed_data.get("image_url"):
        return False
    if not re.match(
            r'^((http|https)://)',
            embed_data.get("image_url")):
        return 214
    return False


def validate_message_data(data: dict) -> bool or int:
    if not isinstance(data, dict):
        return True
    if not isinstance(data.get('content'), str):
        return 215
    if not (1 <= len(data.get("content")) <= 3000):
        return 216
    if not isinstance(data.get('enable_embed'), bool):
        return 217
    if data.get('enable_embed'):
        if error_code := _validate_embed(data["embed"]):
            return error_code

    channel = data.get("channel")
    if channel:
        if not isinstance(channel, str):
            return 218
        try:
            num = int(channel)
            if num < -1:
                return 219
        except ValueError:
            return 220

    interval = data.get("interval")
    if interval:
        if not isinstance(interval, str):
            return 221
        try:
            num = int(interval)
            if not (1 <= num <= 1000):
                return 222
        except ValueError:
            return 223

    time = data.get("time")
    if time:
        if not isinstance(time, str):
            return 224
        if len(time) != 5:
            return 225
        try:
            datetime.datetime.strptime(time, '%H:%M')
        except ValueError:
            return 226

    units_of_measure = data.get("units_of_measure")
    if units_of_measure:
        if not isinstance(units_of_measure, str):
            return 227
        if not (units_of_measure in ("hours", "days", "weeks", "months", "years")):
            return 228

    _type = data.get("type")
    if _type:
        if not isinstance(_type, str):
            return 229
        if not (_type in ("join", "leave")):
            return 230

    trigger = data.get("trigger")
    if trigger:
        if not isinstance(trigger, str):
            return 231
        if not (1 <= len(trigger) <= 50):
            return 232

    trigger_type = data.get("trigger_type")
    if trigger_type:
        if not isinstance(trigger_type, str):
            return 233
        if not (trigger_type in ("start", "inside", "only")):
            return 234

    return False


def validate_settings_data(data: dict) -> bool or int:
    if not data.get("logging"):
        return 235

    if not data.get("status"):
        return 236

    logging = data.get("logging")

    channel = logging.get("channel_id")
    if not isinstance(channel, str):
        return 237
    try:
        num = int(channel)
        if num < -1:
            return 238
    except ValueError:
        return 239

    channel = logging.get("enable")
    if not isinstance(channel, bool):
        return 240

    values = logging.get("values")
    if not isinstance(values, list):
        return 241

    for i in values:
        if not (i in (
                "auto_moderation", "commands", "statistic", "auto_response", "time_messages", "activity_roles", "sm",
                "events")):
            return 242

    status = data.get("status")
    if not isinstance(status.get("text"), str):
        return 243
    if not (1 <= len(status.get("text")) <= 127):
        return 244

    if not isinstance(status.get("type"), str):
        return 245
    if not (status.get("type") in ("playing", "listening", "watching", "streaming")):
        return 246

    return False


def validate_roles_data(data: dict) -> bool or int:
    if not isinstance(data.get("ar_enable"), bool):
        return 247
    if not isinstance(data.get("start_roles"), dict):
        return 248
    if not isinstance(data.get("start_roles").get("roles"), list):
        return 249
    if _is_valid_list_of_lists(data.get("start_roles").get("roles")):
        return 250
    if not isinstance(data.get("update_interval"), str):
        return 251

    try:
        num = int(data.get("update_interval"))
        if not (1 <= num <= 604800):
            return 252
    except ValueError:
        return 253

    for i in data:
        if i in ("ar_enable", "start_roles", "update_interval"):
            continue
        if not isinstance(data.get(i).get("enable"), bool):
            return 254
        if not isinstance(data.get(i).get("value"), str):
            return 255
        if not re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', data.get(i).get("value")):
            return 256

    return False


def validate_social_media(data: dict) -> bool or int:
    if not isinstance(data.get("youtube"), dict):
        return 257
    if not isinstance(data.get("twitch"), dict):
        return 258

    youtube = data.get("youtube", {})
    for yt in youtube:
        if not isinstance(youtube[yt].get("channel_id"), str):
            return 259
        if not (1 <= len(youtube[yt].get("channel_id")) <= 25):
            return 260
        try:
            num = int(youtube[yt].get("channel_id"))
            if num < 0:
                return 261
        except ValueError:
            return 262

        if not isinstance(youtube[yt].get("link"), str):
            return 263

        if not re.match(
                r'^((http|https)://)',
                youtube[yt].get("link")):
            return 264

        if not isinstance(youtube[yt].get("message"), str):
            return 265

        if not (1 <= len(youtube[yt].get("message")) <= 3000):
            return 266

    twitch = data.get("twitch", {})
    for tw in twitch:
        if not isinstance(twitch[tw].get("channel_id"), str):
            return 267
        if not (1 <= len(twitch[tw].get("channel_id")) <= 25):
            return 268
        try:
            num = int(twitch[tw].get("channel_id"))
            if num < 0:
                return 269
        except ValueError:
            return 270

        if not isinstance(twitch[tw].get("link"), str):
            return 271

        if not re.match(
                r'^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$',
                twitch[tw].get("link")):
            return 272

        if not isinstance(twitch[tw].get("message"), str):
            return 273

        if not (1 <= len(twitch[tw].get("message")) <= 3000):
            return 274

    return False


def validation(data) -> bool or int:
    print(data)
    try:
        if data["another"] != {}:
            for _command in data["another"].values():
                if _command.get("action"):
                    _command["description"] = "_"
                if error_code := valid_command_data(_command):
                    return error_code

        if data["moderation"] != {}:
            for _command in data["moderation"].values():
                if _command.get("action"):
                    _command["description"] = "_"
                if error_code := valid_command_data(_command):
                    return error_code
        # print(*data["messages"]["time_message"].values())
        if data["messages"] != {}:
            for _command in [*data["messages"]["auto_response"].values()] + [*data["messages"]["events"].values()] + [
                *data["messages"]["time_message"].values()]:
                if error_code := validate_message_data(_command):
                    return error_code

        if error_code := validate_settings_data(data.get("settings", {})):
            return error_code

        if error_code := validate_roles_data(data.get("roles", {})):
            return error_code

        if error_code := validate_social_media(data.get("social_media", {})):
            return error_code

        return False
    except Exception as e:
        print(e)
        return -1


# if __name__ == '__main__':
#     with open("../test_json.json", encoding="utf-8") as file:
#         _data: dict = json.load(file)
#
#         print(validation(_data))
# print(_data["moderation"])
# for i in _data:
#     if _code := VALIDATION[i](_data[i]):
#         print(_code)
# VALIDATION = {
#     "moderation": moderation,
#     "roles": roles,
#     "messages": messages,
#     "another": another,
#     "social_media": social_media,
#     "customization": customization,
#     "settings": settings
# }
