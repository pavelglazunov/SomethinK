function create_auto_moderation_settings(configurator_content, command_name, automod) {

    if (command_name === "caps" || command_name === "smile") {
        let special_limit_block = div("input_block")
        let min_size_lbl = p("минимальная длина сообщения: ", "configurator_inputs_text")
        let percent_lbl = p(automod + " минимум: ", "configurator_inputs_text")
        let percent_symbol_lbl = p("%", "configurator_inputs_text")
        let input_min_size = input("select_roles", "number", "", "input_min_size")
        let input_percent = input("select_roles", "number", "", "input_percent")

        let min_size_row = div("special_mini_row")
        let percent_row = div("special_mini_row")


        input_min_size.style.margin = "0 1.25vw 0 1vw"
        input_percent.style.margin = "0 0.5vw 0 1vw"

        input_min_size.style.textAlign = "center"
        input_percent.style.textAlign = "center"

        input_min_size.style.alignItems = "center"
        input_percent.style.alignItems = "center"


        input_min_size.style.filter = "none"
        input_min_size.style.maxWidth = "2.5vw"
        input_min_size.style.maxHeight = "1.6vw"
        input_min_size.style.borderRadius = "0.4vw"
        input_percent.style.filter = "none"
        input_percent.style.maxWidth = "2.5vw"
        input_percent.style.maxHeight = "1.6vw"
        input_percent.style.borderRadius = "0.4vw"

        percent_row.style.marginTop = "0.5vw"

        // --- SET VALUE ---
        input_min_size.value = configuration_key[command_name]["min_length"]
        input_percent.value = configuration_key[command_name]["percent"]

        min_size_row.appendChild(min_size_lbl)
        min_size_row.appendChild(input_min_size)

        percent_row.appendChild(percent_lbl)
        percent_row.appendChild(input_percent)
        percent_row.appendChild(percent_symbol_lbl)

        special_limit_block.appendChild(min_size_row)
        special_limit_block.appendChild(percent_row)


        configurator_content.appendChild(special_limit_block)
    }

    if (command_name === "mentions") {
        let mentions_block = div("input_block")

        let mention_lbl = p("количество повторений в одном сообщении", "configurator_inputs_text")
        let mention_input = input("select_roles", "number", "", "input_mentions")

        mention_input.addEventListener("input", () => {
            if (!vld_integer(mention_input.value)) {
                warning("В данное поле можно вводить только числа")
                mention_input.value.slice(0, -1)
            }

        })

        mention_input.style.filter = "none"

        mention_input.value = configuration_key[command_name]["count"]

        mentions_block.appendChild(mention_lbl)
        mentions_block.appendChild(mention_input)

        configurator_content.appendChild(mentions_block)

    }


    let actions_block = div("input_block")
    let action_lbl = p("действие при обнаружении", "configurator_inputs_text")
    let action_select = select("select_roles", "select_action_form")

    action_select.style.filter = "none"

    for (let i of [["отправить на проверку модераторам", "--send"], ["удалить сообщение", "--remove"], ["выдать предупреждение", "--warn"], ["удалить сообщение и выдать предупреждение", "--remove-warn"]]) {
        action_select.appendChild(option(i[0], i[1], i[1] === configuration_key[command_name]["action"]))
    }


    actions_block.appendChild(action_lbl)
    actions_block.appendChild(action_select)


    configurator_content.appendChild(actions_block)


    let roles_and_channels = creat_roles_and_channels_input_blocks(command_name,
        "роли, чьи сообщения бот будет игнорировать",
        "каналы, в которых бот будет игнорировать сообщения")
    configurator_content.appendChild(roles_and_channels[0])
    configurator_content.appendChild(roles_and_channels[1])

}

function reset_key_configurator(show_message = false) {
    for (let i of COMMANDS) {
        for (let j of i) {
            let command_config = {}
            command_config["enable"] = true
            command_config["description"] = COMMANDS_DESCRIPTIONS[j]
            command_config["roles"] = [["Владелец сервера", "-1"]]
            command_config["channels"] = []
            if (j in COMMAND_WITH_SPECIAL_FORM) {
                command_config["special_channel"] = "-1"
            }
            configuration_key[j] = command_config
        }
    }

    for (let i of AUTO_MODERATION) {
        for (let j of i) {
            let auto_mod_config = {}
            auto_mod_config["enable"] = true
            auto_mod_config["roles"] = [["Владелец сервера", "-1"]]
            auto_mod_config["channels"] = []
            auto_mod_config["action"] = "--send"
            auto_mod_config["description"] = COMMANDS_DESCRIPTIONS[j[0]]

            if (j[0] === "caps") {
                auto_mod_config["min_length"] = 20
                auto_mod_config["percent"] = 80
            }
            if (j[0] === "smile") {
                auto_mod_config["min_length"] = 20
                auto_mod_config["percent"] = 80

            }
            if (j[0] === "mentions") {
                auto_mod_config["count"] = 3
            }
            configuration_key[j[0]] = auto_mod_config
        }
    }


    const answer = post_data("moderation", configuration_key)
    answer.then(a => {
        if (a["status"] === "ok") {
            if (show_message) {
                warning("изменения сброшены")
            }

            return 0
        }
        danger(a["message"])
    })
}

update_chapter(1)

let login_discord = null
let user_roles = []
let user_channels = {}
const loader = document.getElementsByClassName("loading")

displayLoading(loader)
let configuration_key = {}
fetch('/api/get', {
    method: "GET",
    headers: {
        "configuration_name": "moderation",
        "get": "roles|channels"
    }
})
    .then((response) => response.json())
    .then((data) => {
        login_discord = data["auth_with_discord"]
        user_roles = data["roles"]

        user_channels = data["channels"]

        configuration_key = data["configuration_key"]

        if (data["configuration_key"] === "{}") {
            configuration_key = {}
            reset_key_configurator()
        } else {
            configuration_key = JSON.parse(configuration_key)

        }

        hideLoading(loader)
        main()

    })

const main_block = document.getElementById("main_command")
const another_block = document.getElementById("another_command")
const auto_moderation_block = document.getElementById("auto_moderation")


function main() {
    main_block.innerHTML = ""
    another_block.innerHTML = ""
    auto_moderation_block.innerHTML = ""

    restart_configurator(document.getElementById("configurator"))


    for (let i = 0; i < 6; i++) {
        let row = div("row")

        row.appendChild(create_command_block(
            configuration_key,
            "configurator",
            base_save_settings,
            COMMANDS[i][0],
        ))
        row.appendChild(create_command_block(
            configuration_key,
            "configurator",
            base_save_settings,
            COMMANDS[i][1],
        ))

        main_block.appendChild(row)

    }

    for (let i = 6; i < COMMANDS.length; i++) {
        let row = div("row")

        row.appendChild(create_command_block(
            configuration_key,
            "configurator",
            base_save_settings,
            COMMANDS[i][0],
        ))
        row.appendChild(create_command_block(
            configuration_key,
            "configurator",
            base_save_settings,
            COMMANDS[i][1],
        ))
        another_block.appendChild(row)

    }

    for (let command of AUTO_MODERATION) {
        let row = div("row")

        row.appendChild(create_command_block(
            configuration_key,
            "configurator",
            base_save_settings,
            command[0][0],
            {
                "slash": false,
                "settings": true,
                "automod": command[0][1],
                "remove_after_close": false,
                "parent_id": ""
            }
        ))
        row.appendChild(create_command_block(
            configuration_key,
            "configurator",
            base_save_settings,
            command[1][0],
            {
                "slash": false,
                "settings": true,
                "automod": command[1][1],
                "remove_after_close": false,
                "parent_id": ""
            }
        ))

        auto_moderation_block.appendChild(row)
    }
}

document.getElementById("add_base_role_button").addEventListener("click", function () {
    let base_input_form = document.getElementById("base_role_input")
    let base_role_value, base_role_text
    if (login_discord) {

        base_role_value = base_input_form.value
        base_role_text = base_input_form[base_input_form.selectedIndex].text
    } else {
        base_role_value = base_input_form.value
        base_role_text = base_input_form.value
    }

    console.log(base_role_value, base_role_text)
    const last = base_save_settings(configuration_key)

    for (let cm in configuration_key) {
        let actual_roles = configuration_key[cm]["roles"]
        actual_roles.push([base_role_text, base_role_value])
        configuration_key[cm]["roles"] = actual_roles
    }
    console.log(last, configuration_key)
    open_settings(configuration_key, "configurator", last, {
        "slash": true,
        "settings": true,
        "automod": "",
        "remove_after_close": false,
        "parent_id": "",
    })
})
document.getElementById("another_save_btn").addEventListener("click", function () {
    base_save_settings(configuration_key)

    if (!login_discord) {
        if (((configuration_key["afk"]["special_channel"] === "") && (configuration_key["afk"]["enable"])) || ((configuration_key["report"]["special_channel"] === " ") && (configuration_key["report"]["enable"]))) {

        }
    }

    const answer = post_data("moderation", configuration_key)
    answer.then(a => {
        if (a["status"] === "ok") {
            success()
            return 0
        }
        danger(a["message"])
    })
})
document.getElementById("another_reset_btn").addEventListener("click", function () {
    if (confirm("Вы уверены, что хотите сбросить все изменения?")) {
        reset_key_configurator(true)

        main()

    }
})

