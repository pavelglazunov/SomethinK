// import ALL_COMMANDS from "./constants"


function div(classes = "_", name = "", id = null) {
    let d = document.createElement("div")
    d.name = name
    d.classList.add(classes)
    if (id) {
        d.id = id
    }
    return d
}

function p(text, classes, id = null) {
    let p = document.createElement("p")
    p.textContent = text
    p.classList.add(classes)
    if (id) {
        p.id = id
    }

    return p

}

function input(classes, type, name = "", id = null, placeholder = "") {
    let input = document.createElement("input")
    input.type = type
    input.name = name
    input.placeholder = placeholder
    input.classList.add(classes)
    if (id) {
        input.id = id
    }

    return input
}

function button(classes, text, name = "", id = null) {
    let btn = document.createElement("button")
    if (name) {
        btn.name = name
    }
    btn.textContent = text
    btn.classList.add(classes)
    if (id) {
        input.id = id
    }

    return btn
}

function select(classes, id, name = "") {
    let sl = document.createElement("select")
    sl.name = name
    sl.classList.add(classes)
    sl.id = id

    return sl
}

function restart_configurator(configurator) {
    configurator.innerHTML = ""
    configurator.name = ""
    configurator.style.paddingBottom = "1vw"
    configurator.appendChild(p("В этом блоке вы сможете настроить выбранные команды", "about_configurator"))
    configurator.appendChild(p("Данный блок не является обязательным для заполнения", "about_configurator"))
    configurator.appendChild(p("Если вы не заполните поля связанные с ролями или каналами, к ним автоматически будет применено значение \"все\"", "about_configurator"))
    configurator.appendChild(p("Если вы не заполните поле \"описание\", в команде будет установлено базовое значение (указано в заголовке каждой команды)", "about_configurator"))
    let ir = p("<span style=\"color: #dc3545\">*</span> - обязательно для заполнения", "about_configurator")
    ir.innerHTML = "<span style=\"color: #dc3545\">*</span> - обязательно для заполнения"
    configurator.appendChild(ir)
}

function create_roles_input_block(command_name, configuration_key, login_discord, roles_description) {
    let roles_block = div("input_block")
    let roles_mini_block = div("mini_row")
    let roles_inputs = div("select_roles_div", "", "input_roles_block")
    let roles_add_btn = button("add_role_btn", "+")

    let role_input_form = null
    if (login_discord) {
        role_input_form = select("select_roles", "roles_input_form")
        // let opt = document.createElement("option")
        // opt.text = "Владелец сервера"
        // opt.value = "-1"
        // opt.selected = true
        // role_input_form.appendChild(opt)
        for (let i = 0; i < user_roles.length; i++) {
            let opt = document.createElement("option")
            opt.text = user_roles[i][1]
            opt.value = user_roles[i][0]

            role_input_form.appendChild(opt)

        }
        // let users_channel =
    } else {
        role_input_form = input("select_roles", "text", "", "roles_input_form", " ID роли")
    }

    console.log(command_name)
    console.log(configuration_key[command_name])
    for (let i of configuration_key[command_name]["roles"]) {
        roles_inputs.appendChild(generate_added_object("role", i[0], i[1]))
    }

    roles_add_btn.addEventListener("click", function () {
        let role_value = ""
        let role_text = ""
        if (login_discord) {
            let roles_selector = document.getElementById("roles_input_form")
            role_value = roles_selector.value
            role_text = roles_selector[roles_selector.selectedIndex].text

        } else {
            let roles_input = document.getElementById("roles_input_form")
            role_value = roles_input.value
            role_text = roles_input.value
        }


        roles_inputs.appendChild(generate_added_object("role", role_text, role_value))

    })


    let roles_add_lbl = p("Добавить роль", "configurator_inputs_text")
    let roles_input_lbl = p(roles_description, "configurator_inputs_text")

    roles_mini_block.style.display = "flex"
    roles_mini_block.style.marginTop = "0.3vw"
    roles_inputs.style.filter = "none"
    roles_inputs.style.display = "flex"
    roles_add_btn.style.filter = "none"
    role_input_form.style.filter = "none"

    role_input_form.style.height = "1.5vw"
    role_input_form.style.width = "48%"

    roles_add_lbl.style.marginRight = "1.5vw"

    // roles_mini_block.appendChild(roles_input_form)
    roles_mini_block.appendChild(roles_add_lbl)
    roles_mini_block.appendChild(role_input_form)
    roles_mini_block.appendChild(roles_add_btn)

    roles_block.appendChild(roles_input_lbl)
    roles_block.appendChild(roles_inputs)
    roles_block.appendChild(roles_mini_block)


    roles_block.appendChild(roles_mini_block)

    return roles_block
}

function create_channels_input_block(command_name, configuration_key, login_discord, channels_description) {
    let channels_block = div("input_block")
    let channels_mini_block = div("mini_row")
    let channels_inputs = div("select_roles_div")
    let channels_add_btn = button("add_role_btn", "+")

    let channel_input_form = null
    if (login_discord) {
        channel_input_form = select("select_roles", "channels_input_form")

        for (let i = 0; i < user_channels["text"].length; i++) {
            let opt = document.createElement("option")
            opt.text = user_channels["text"][i][1]
            opt.value = user_channels["text"][i][0]


            channel_input_form.appendChild(opt)

        }
    } else {
        channel_input_form = input("select_roles", "text", "", "channels_input_form", " ID канала")
    }

    let channels_add_lbl = p("Добавить канал", "configurator_inputs_text")
    let channels_input_lbl = p(channels_description, "configurator_inputs_text")

    channels_mini_block.style.display = "flex"
    channels_mini_block.style.marginTop = "0.3vw"
    channels_inputs.style.filter = "none"
    channels_inputs.style.display = "flex"
    channels_add_btn.style.filter = "none"
    channel_input_form.style.filter = "none"
    channel_input_form.style.height = "1.5vw"
    channel_input_form.style.width = "48%"
    channels_add_lbl.style.marginRight = "0.8vw"

    for (let i of configuration_key[command_name]["channels"]) {
        channels_inputs.appendChild(generate_added_object("channel", i[0], i[1]))
    }

    channels_add_btn.addEventListener("click", function () {
        let channel_value = ""
        let channel_text = ""
        if (login_discord) {
            let channels_selector = document.getElementById("channels_input_form")
            channel_value = channels_selector.value
            channel_text = channels_selector[channels_selector.selectedIndex].text


        } else {
            let channels_input = document.getElementById("channels_input_form")
            channel_value = channels_input.value
            channel_text = channels_input.value
        }


        channels_inputs.appendChild(generate_added_object("channel", channel_text, channel_value))

    })

    channels_mini_block.appendChild(channels_add_lbl)
    channels_mini_block.appendChild(channel_input_form)
    channels_mini_block.appendChild(channels_add_btn)

    channels_block.appendChild(channels_input_lbl)
    channels_block.appendChild(channels_inputs)
    channels_block.appendChild(channels_mini_block)


    channels_block.appendChild(channels_mini_block)

    return channels_block
}

function fake() {
    return document.createElement("div")
}
function creat_roles_and_channels_input_blocks(command_name,
                                               roles_description = "роли, которые могут использовать эту команду",
                                               channels_description = "каналы, где бот будет видеть эту команду") {
    return [create_roles_input_block(command_name, configuration_key, login_discord, roles_description),
        create_channels_input_block(command_name, configuration_key, login_discord, channels_description)]
}

function generate_added_object(type, text, value) {
    let actual_added_block_count = document.getElementsByClassName("added_" + type + "s_block").length
    if (actual_added_block_count === 15) {
        warning("Достигнул лимит " + {"role": "ролей", "channel": "каналов"}[type])
        return fake()
    }
    if (!value) {
        warning("Введите ID " + {"role": "роли", "channel": "канала"}[type])
        return fake()
    }
    if (!vld_integer(value)) {
        warning("Некорректное значение ID " + {"role": "роли", "channel": "канала"}[type])
        return fake()
    }

    // console.log(parseInt(value))

    let role_remove_button = button("role_remove_button", "✖")
    let added_block = div("added_" + type + "s_block", "selected_roles")
    let block_text = p(text, "role_block_text")

    added_block.setAttribute(type + "_data", value)
    added_block.setAttribute(type + "_name", text)
    added_block.appendChild(block_text)
    added_block.appendChild(role_remove_button)

    role_remove_button.addEventListener("click", function () {
        let all_selected = document.getElementsByClassName("added_" + type + "s_block")
        for (let i = 0; i < all_selected.length; i++) {
            if (value === all_selected[i].getAttribute(type + "_data")) {
                added_block.remove()
            }
        }
    })

    return added_block

}

function create_command_block(
    configuration_key,
    configuration_id,
    save_func,
    name,
    kwargs={
        "slash": true,
        "settings": true,
        "automod": "",
        "remove_after_close": false,
        "parent_id": "",
    }
) {

    // console.log(name)

    let text = p(kwargs.slash ? "/" + name : name, "command_name_text")
    let cb = input("active_checkbox", "checkbox", name)
    let command_block = div("command_block")


    if (kwargs.automod) {
        text.textContent = kwargs.automod
    }

    if (kwargs.fontsize) {
        text.style.fontSize = kwargs.fontsize

    }

    cb.checked = configuration_key[name]["enable"]
    cb.addEventListener("click", function () {
        configuration_key[name]["enable"] = cb.checked
    })

    command_block.appendChild(text)
    command_block.appendChild(cb)


    if (kwargs.settings) {
        console.log(">>")
        let setting = div("settings_button", name)
        setting.addEventListener("click", function () {
            let configurator = document.getElementById(configuration_id)
            if (!configurator) {
                document.getElementById(kwargs.parent_id).appendChild(div("block", "", configuration_id))
            }
            let last = save_func(configuration_key)
            console.log(last)
            if (last === name) {
                console.log(">>>>>>>>>>>>>>>")
                if (kwargs.remove_after_close) {
                    configurator.remove()
                    return 0
                }
                else {
                    restart_configurator(configurator)
                    return 0
                }


            }
            open_settings(configuration_key, configuration_id, name, kwargs)
        })
        command_block.appendChild(setting)

    }


    return command_block
}


function open_settings(configuration_key, configuration_id, name, kwargs) {
    let configurator = document.getElementById(configuration_id)

    configurator.innerHTML = ""
    configurator.name = name
    configurator.style.paddingBottom = "0"

    let configurator_name = p(kwargs.slash ? "/" + name : name, "block_header")
    if (kwargs.automod) {
        configurator_name.textContent = kwargs.automod
    }

    let configurator_description = p(configuration_key[name]["description"], "configurator_inputs_text", "__description")
    configurator_description.style.justifyContent = "center"

    configurator_name.appendChild(configurator_description)
    configurator_name.style.fontSize = "1.2vw"


    let configurator_content = div("configurator_content")
    configurator_content.appendChild(configurator_name)

    if (kwargs.automod) {
        create_auto_moderation_settings(configurator_content, name, kwargs.automod)
        configurator.appendChild(configurator_content)
        return 0
    }

    let description_block = div("input_block")
    let description_input = input("select_roles", "text", "", "__description_input", " Описание")


    if (configuration_key[name]["description"] !== ALL_COMMANDS[name]) {
        console.log(configuration_key[name])
        description_input.value = configuration_key[name]["description"]
    }


    let description_lbl = p("данный текст будет отображаться в /help", "configurator_inputs_text")
    description_input.addEventListener("input", function () {
        let actual_description = document.getElementById("__description")
        let actual_description_input = document.getElementById("__description_input")
        if (actual_description_input.value.length === 200) {
            warning("Достигнут лимит в 200 символов, если вам необходимо больше, напишите нам в телеграм по ссылке")
        }
        actual_description.textContent = actual_description_input.value ? actual_description_input.value : ALL_COMMANDS[name]


    })


    description_input.maxLength = 200
    description_input.style.filter = "none"

    description_block.appendChild(description_lbl)
    description_block.appendChild(description_input)


    // ----------------- INPUT ROLES -----------------

    let roles_and_channels = creat_roles_and_channels_input_blocks(name)

    configurator_content.appendChild(description_block)
    configurator_content.appendChild(roles_and_channels[0])
    configurator_content.appendChild(roles_and_channels[1])


    // ----------------- ADD SPECIAL FORM -----------------

    if (name in COMMAND_WITH_SPECIAL_FORM) {
        let specials_block = div("input_block")
        let specials_mini_block = div("mini_row")
        let create_special_channel_cb = input("blue_checkbox", "checkbox", "", "auto_channel_cb")
        let create_special_channel_lbl = p("создать канал автоматически", "configurator_inputs_text")

        let special_input_form = null
        if (login_discord) {
            special_input_form = select("select_roles", "specials_input_form")
            let opt = document.createElement("option")
            opt.text = ""
            opt.value = " "
            opt.selected = true
            special_input_form.appendChild(opt)
            for (let i of user_channels[COMMAND_WITH_SPECIAL_FORM[name][0]]) {
                let opt = document.createElement("option")
                opt.text = i[1]
                opt.value = i[0]
                if (i[0] === configuration_key[name]["special_channel"]) {
                    opt.selected = true
                }
                special_input_form.appendChild(opt)

            }
        } else {
            special_input_form = input("select_roles", "text", "", "specials_input_form", " ID канала")
            if (configuration_key[name]["special_channel"] in ["-1", " "]) {
                special_input_form.value = configuration_key[name]["special_channel"]
            }
        }

        create_special_channel_cb.checked = Boolean(configuration_key[name]["special_channel"] === "-1")
        special_input_form.disabled = create_special_channel_cb.checked

        let specials_input_lbl = p(COMMAND_WITH_SPECIAL_FORM[name][1], "configurator_inputs_text")
        specials_input_lbl.innerHTML = COMMAND_WITH_SPECIAL_FORM[name][1] + "<span style=\"color: #dc3545\">*</span>"
        create_special_channel_cb.addEventListener("click", function () {
            special_input_form.disabled = create_special_channel_cb.checked
        })

        specials_mini_block.style.display = "flex"
        specials_mini_block.style.alignItems = "center"
        specials_mini_block.style.marginTop = "0.3vw"
        special_input_form.style.filter = "none"
        special_input_form.style.height = "1.5vw"
        create_special_channel_lbl.style.textAlignLas = "center"
        create_special_channel_lbl.style.marginLeft = "0.5vw"

        specials_mini_block.appendChild(create_special_channel_cb)
        specials_mini_block.appendChild(create_special_channel_lbl)

        specials_block.appendChild(specials_input_lbl)
        specials_block.appendChild(special_input_form)
        specials_block.appendChild(specials_mini_block)

        configurator_content.appendChild(specials_block)
    }


    // configurator_content.appendChild(footer)

    configurator.appendChild(configurator_content)


}

function base_save_settings(configuration_key) {
    console.log(configuration_key)
    let configurator = document.getElementById("configurator")
    let actual_name = configurator.name
    let data = {}

    if (!actual_name) {
        return 0
    }

    data["enable"] = document.getElementsByName(actual_name)[0].checked

    let roles = []
    for (let role of document.getElementsByClassName("added_roles_block")) {
        roles.push([role.getAttribute("role_name"), role.getAttribute("role_data")])
    }
    data["roles"] = roles

    let channels = []
    for (let channel of document.getElementsByClassName("added_channels_block")) {
        channels.push([channel.getAttribute("channel_name"), channel.getAttribute("channel_data")])
    }
    data["channels"] = channels

    if (["smile", "mentions", "links", "caps"].indexOf(actual_name) !== -1) {
        let action = document.getElementById("select_action_form")
        data["action"] = action.value

        if (["caps", "smile"].indexOf(actual_name) !== -1) {
            let text_men_length = document.getElementById("input_min_size")
            let percent = document.getElementById("input_percent")

            data["min_length"] = text_men_length.value
            data["percent"] = percent.value
        }

        if (actual_name === "mentions") {
            let mentions = document.getElementById("input_mentions")

            data["mentions"] = mentions.value
        }

        updateLS(actual_name, data)
        return actual_name
    }


    let description = document.getElementById("__description_input")
    data["description"] = description.value ? description.value : ALL_COMMANDS[actual_name]

    if (actual_name in COMMAND_WITH_SPECIAL_FORM) {
        let special_form = document.getElementById("specials_input_form")
        let auto_create_cb = document.getElementById("auto_channel_cb")
        if (!auto_create_cb.checked) {
            data["special_channel"] = special_form.value
        } else {
            data["special_channel"] = "-1"

        }
        // data.set("special_channel", "-1")
    }
    // console.log(data)

    // return data
    // postUserChanges(data).then((return_data) => {
    // })
    // updateLS(actual_name, data)
    configuration_key[actual_name] = data

    return actual_name

}

function displayLoading(loader) {

    // for (let loader of document.getElementsByClassName("__loading")) {

        // console.log(loader)
        // loader.classList.add("display");
        // loader.style.visibility = "visible"

    // }
    // loader = document.getElementById("loading")

    console.log(loader)
    for (let l of loader) {
        l.classList.add("display");
        console.log(">>>>>>>>>>>", l)
    }

    console.log("loading")
    // to stop loading after some time
    // setTimeout(() => {
    //     loader.classList.remove("display");
    // }, 5000);
}

// hiding loading
function hideLoading(loader) {

    console.log(loader)
    let loader_list = document.getElementsByClassName("loading")
    while (loader_list.length >= 1) {
        loader_list[0].remove()
    }

    // for (let i = 0; i <= loader.length / 2 + 1; i++){
    //     loader[0].remove()
    // }

    // while () {
        // loader[0].remove()
    // }
    // for (let l of loader) {
    //     console.log(l)
    //     // l.remove()
    //     l.cl
    // }
    // for (let loader of document.getElementsByClassName("__loading")) {
    //     loader.remove()
    //
    //
    // }
}
