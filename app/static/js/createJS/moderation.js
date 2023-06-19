function updateLS(key, value) {
    configuration_key[key] = value
}


function create_auto_moderation_settings(configurator_content, command_name, automod) {

    console.log(command_name)
    console.log("caps" === "caps", "caps" === "smile")
    if (command_name === "caps" || command_name === "smile") {
        let special_limit_block = div("input_block")
        let min_size_lbl = p("минимальная длина сообщения: ", "configurator_inputs_text")
        let percent_lbl = p(automod + " минимум: ", "configurator_inputs_text")
        let percent_symbol_lbl = p("%", "configurator_inputs_text")
        let input_min_size = input("select_roles", "text", "", "input_min_size")
        let input_percent = input("select_roles", "text", "", "input_percent")

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
        let mention_input = input("select_roles", "text", "", "input_mentions")

        mention_input.addEventListener("input", function () {
            if (!vld_integer(mention_input.value)) {
                warning("В данное поле можно вводить только числа")
                mention_input.value.slice(0, -1)
            }

        })

        // mention_input.validity

        mention_input.style.filter = "none"

        console.log(configuration_key[command_name])
        mention_input.value = configuration_key[command_name]["count"]

        // let mentions_row = div("mini_row")
        mentions_block.appendChild(mention_lbl)
        mentions_block.appendChild(mention_input)

        configurator_content.appendChild(mentions_block)

    }


    let actions_block = div("input_block")
    let action_lbl = p("действие при обнаружении", "configurator_inputs_text")
    let action_select = select("select_roles", "select_action_form")

    action_select.style.filter = "none"

    for (let i of [["удалить сообщение", "--remove"], ["выдать предупреждение", "--warn"], ["удалить сообщение и выдать предупреждение", "--remove-warn"]]) {
        let opt = document.createElement("option")

        opt.text = i[0]
        opt.value = i[1]

        action_select.appendChild(opt)
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

function reset_key_configurator(show_message=false) {
    for (let i of COMMANDS) {
        for (let j of i) {
            let command_config = {}
            command_config["enable"] = true
            command_config["description"] = COMMANDS_DESCRIPTIONS[j]
            command_config["roles"] = []
            command_config["channels"] = []
            if (j in COMMAND_WITH_SPECIAL_FORM) {
                command_config["special_channel"] = "-1"
            }
            configuration_key[j] = command_config
        }
    }
    //"ссылки", "капс"],
    //     ["эмодзи", "упоминания"
    // let auto_mod = {}
    for (let i of AUTO_MODERATION) {
        for (let j of i) {
            let auto_mod_config = {}
            auto_mod_config["enable"] = true
            auto_mod_config["roles"] = []
            auto_mod_config["channels"] = []
            auto_mod_config["action"] = 0
            auto_mod_config["description"] = COMMANDS_DESCRIPTIONS[j[0]]

            if (j[0] === "caps") {
                auto_mod_config["min_length"] = 20
                auto_mod_config["percent"] = 80
                // auto_mod["caps"] = auto_mod_config
            }
            if (j[0] === "smile") {
                auto_mod_config["min_length"] = 20
                auto_mod_config["percent"] = 80

            }
            if (j[0] === "mentions") {
                auto_mod_config["count"] = 3
            }
            configuration_key[j[0]] = auto_mod_config

            // if (j === "ссылки") {
            //     auto_mod["links"] = auto_mod_config
            // }
            // if (j === "mentions") {
            //     auto_mod["mentions"] = auto_mod_config
            //
            // }

            // let _type
            // for (let t of AUTO_MODERATION_TRANSLATION) {
            //     console.log(t)
            // if (AUTO_MODERATION_TRANSLATION[t] === j) {
            //     auto_mod[AUTO_MODERATION_TRANSLATION[t]] = auto_mod_config
            // }
            // }
            // configuration_key[j] = command_config
        }
    }

    configuration_key["ignore_admin"] = {
        "enable": true
    }
    configuration_key["ignore_bot"] = {
        "enable": true
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
    // configuration_key["auto_moderation"] = auto_mod
}

update_chapter(1)

// let data = api_all().then(json => json)
// console.log("data", data.)
let login_discord = null
let user_roles = []
let user_channels = {}
// fetch('/api/all')
//     .then((response) => response.json())
//     .then((data) => {
//         login_discord = data["auth_with_discord"]
//         user_roles = data["roles"]
//         user_channels = data["channels"]
//         console.log(login_discord, "login discord")
//         // {title: "foo", body: "bar", userId: 1, id: 101}
//     })


// let configuration_key = get_configuration_key("moderation", reset_key_configurator)

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

        // console.log(login_discord, "login discord")
        user_channels = data["channels"]

        configuration_key = data["configuration_key"]

        // console.log(">>", configuration_key)
        // console.log(">>", typeof configuration_key)

        if (Object.keys(configuration_key).length === 0) {
            console.log(55555)
            configuration_key = {}
            reset_key_configurator()
        } else {
            configuration_key = JSON.parse(configuration_key)

        }

        console.log(configuration_key)

        // hideLoading()

        hideLoading(loader)
        main()

        // roles_content.appendChild(create_roles_input_block(
        //     "start_roles",
        //     configuration_key,
        //     login_discord,
        //     "роли, которые будут выданы при первом заходе на сервер",
        // ))
        // document.getElementById("input_roles_block").style.width = "78.1%"
        // document.getElementById("input_roles_block").style.maxWidth = "32vw"
        // {title: "foo", body: "bar", userId: 1, id: 101}
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
        // row.appendChild(create_command_block(COMMANDS[i][0], configuration_key))
        // row.appendChild(create_command_block(COMMANDS[i][1], configuration_key))

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
        // row.appendChild(create_command_block(command[0][0], configuration_key, command[0][1]))
        // row.appendChild(create_command_block(command[1][0], configuration_key, command[1][1]))

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

    for (let cm in configuration_key) {
        // console.log(cm)
        // continue
        let actual_roles = configuration_key[cm]["roles"]
        actual_roles.push([base_role_text, base_role_value])
        configuration_key[cm]["roles"] = actual_roles
        // console.log(cm)
    }
})
document.getElementById("another_save_btn").addEventListener("click", function () {
    base_save_settings(configuration_key)
    if (((configuration_key["afk"]["special_channel"] === " ") && (configuration_key["afk"]["enable"])) || ((configuration_key["report"]["special_channel"] === " ") && (configuration_key["report"]["enable"]))) {


        if ((configuration_key["afk"]["special_channel"] === " ") && (configuration_key["afk"]["enable"])) {
            danger("Необходимо указать канал или поставить авто-создание в команде /afk")


        }
        console.log(configuration_key["report"])
        if ((configuration_key["report"]["special_channel"] === " ") && (configuration_key["report"]["enable"])) {
            danger("Необходимо указать канал или поставить авто-создание в команде /report")

        }

        return 0
    }

    // SaveDateToLocalStorage("moderation", configuration_key)

    const answer = post_data("moderation", configuration_key)
    answer.then(a => {
        if (a["status"] === "ok") {
            success()
            return 0
        }
        danger(a["message"])
    })
    // success()
})
document.getElementById("another_reset_btn").addEventListener("click", function () {
    if (confirm("Вы уверены, что хотите сбросить все изменения?")) {
        reset_key_configurator(true)

        main()
        // SaveDateToLocalStorage("moderation", configuration_key)

        // location.reload()

        // warning("изменения сброшены")

    }
})

