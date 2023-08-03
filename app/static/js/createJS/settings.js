update_chapter(6)


const block = document.getElementById("settings")
const loader = document.getElementsByClassName("loading")

const STATUSES = [["playing", "играет в"], ["listening", "слушает"], ["watching", "смотрит"]]
const STATISTIC_LIST = [
    ["text", "текстовые каналы"],
    ["voice", "голосовые каналы"],
    ["member", "участники"],
    ["roles", "роли"],
    ["category", "категории"],
    ["messages", "сообщения"]
]

const LOGGING_EVENTS = [
    ["auto_moderation", "автомодерация"],
    ["commands", "команды"],
    // ["statistic", "обновление статистики"],
    ["auto_response", "автоответчик"],
    ["time_messages", "регулярные сообщения"],
    ["activity_roles", "роли активности"],
    // ["sm", "оповещения ютуб/твич"],
    ["events", "события"],

]

function create_list(name, text, type) {
    let logging_event_block = div("mini_row")
    let cb = input("blue_checkbox", "checkbox", type, type + "_" + name)

    console.log(type, name, configuration_key[type]["values"].indexOf(name) > 0)

    cb.checked = configuration_key[type]["values"].indexOf(name) >= 0;
    cb.classList.add(type)
    logging_event_block.appendChild(cb)
    let _p = p(text, "no_margin")
    _p.style.fontSize = "0.9vw"

    logging_event_block.appendChild(_p)

    logging_event_block.style.minWidth = "11vw"

    return logging_event_block

}

function update_logging_block(value) {


    // if (!value) {
    //     document.getElementById("logging_right_block").classList.add("hide")
    // } else {
    //     document.getElementById("logging_right_block").classList.remove("hide")
    // }
    // document.getElementById("logging_right_block").style.display = !value ? "none" : "flex"
    // document.getElementById("logging_right_block").style.display = !value ? "none" : "flex"

    // for (let set_btn of document.getElementsByClassName("command_block")) {
    //
    //
    //     set_btn.style.display = !value ? "none" : "flex"
    // }


    for (let evt of document.getElementsByClassName("logging")) {
        // console.log(evt)
        evt.style.filter = !value ? "grayscale(50%)" : "grayscale(0)"
        evt.disabled = !value
    }
    // for (let nm of document.getElementsByClassName("no_margin")) {
    //     // console.log(evt)
    //     nm.style.color = !value ? "#aba9a9" : "#dedede"
    // }

    document.getElementById("input_channel_id").style.filter = !value ? "grayscale(50%)" : "grayscale(0)"
    document.getElementById("input_channel_id").style.color = !value ? "#aba9a9" : "#FFFFFF"

    document.getElementsByClassName("part_of_block")[1].style.color = !value ? "#aba9a9" : "#FFFFFF"
}

// function update_statistic_block(value) {
//     if (!value) {
//         document.getElementById("statistic_right_block").classList.add("hide")
//     } else {
//         document.getElementById("statistic_right_block").classList.remove("hide")
//     }
//
//     setTimeout(function () {
//         document.getElementById("statistic_right_block").style.display = !value ? "none" : "flex"
//
//     }, !value ? 200 : 0)
//

// }

// console.log(block)

function reset_settings_configuration_key() {
    configuration_key["logging"] = {
        "enable": true,
        "channel_id": "-1",
        "values": ["commands", "auto_moderation"]
    }
    configuration_key["status"] = {
        "type": "playing",
        "text": "в бота от SomethinK"
    }


    // configuration_key["message_from_dm_switcher_enable"] = false
    // configuration_key["statistic"] = {
    //     "enable": true,
    //     "channel_id": "-1",
    //     "values": ["text", "voice", "member", "roles", "category", "messages"]
    // }

    // for (let cmd of LOGGING_COMMANDS) {
    //     let command_config = {}
    //     command_config["enable"] = true
    //     command_config["description"] = ALL_COMMANDS[cmd]
    //     command_config["roles"] = []
    //     command_config["channels"] = []
    //
    //     configuration_key[cmd] = command_config
    // }
}


let login_discord = null
let user_roles = []
let user_channels = {}

displayLoading(loader)
let configuration_key = {}
fetch('/api/get', {
    method: "GET",
    headers: {
        "configuration_name": "settings",
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
            reset_settings_configuration_key()
        } else {
            configuration_key = JSON.parse(configuration_key)

        }


        hideLoading(loader)
        main()

    })


function main() {
    block.innerHTML = ""

    let logging_block = div("input_block")
    logging_block.style.width = "100%"
    logging_block.style.display = "flex"
    logging_block.style.flexDirection = "row"

    let logging_lbl = p("логирование", "no_margin")
    logging_lbl.style.marginLeft = "0.9vw"
    let logging_switcher = input("active_checkbox", "checkbox", "", "logging_enable")
    let logging_left_block = div("part_of_block")

    logging_switcher.checked = configuration_key["logging"]["enable"]

    logging_switcher.addEventListener("change", function () {
        // console.log(logging_switcher.checked)
        configuration_key["logging"]["enable"] = logging_switcher.checked
        update_logging_block(logging_switcher.checked)

        // logging_left_block.style.visibility = logging_switcher.checked ? "hidden" : "visible"
        // logging_right_block.style.visibility = logging_switcher.checked ? "hidden" : "visible"
    })


    let logging_row = div("mini_row")

    logging_left_block.style.minWidth = "20vw"

    logging_row.appendChild(logging_lbl)
    logging_row.appendChild(logging_switcher)

    logging_left_block.appendChild(logging_row)
    // logging_left_block.appendChild(create_command_block(
    //     configuration_key,
    //     "configurator",
    //     base_save_settings,
    //     "logon",
    // ))
    // logging_left_block.appendChild(create_command_block(
    //     configuration_key,
    //     "configurator",
    //     base_save_settings,
    //     "logoff",
    // ))

    let logging_right_block = div("part_of_block", "", "logging_right_block")
    logging_right_block.style.width = "20vw"

    let create_channel_lbl = p("канал, куда будут отправляться логи", "configurator_inputs_text")
    if (!login_discord) {
        create_channel_lbl.innerHTML += '<span style="color: #65e025">*</span>'

    }
    let _input_channel_id
    if (login_discord) {
        _input_channel_id = select("select_roles", "input_channel_id")

        _input_channel_id.appendChild(option("создать канал автоматически", "-1", true))

        for (let i of user_channels["text"]) {
            let opt = document.createElement("option")
            opt.text = i[1]
            opt.value = i[0]
            console.log(i[0])
            if (i[0] === configuration_key["logging"]["channel_id"]) {
                opt.selected = true
            }
            _input_channel_id.appendChild(opt)
        }

    } else {
        _input_channel_id = input("select_roles", "number", "", "input_channel_id")
        _input_channel_id.value = configuration_key["logging"]["channel_id"]
        _input_channel_id.placeholder = "ID канала"
        _input_channel_id.min = "-1"
        _input_channel_id.maxLength = 25
    }
    let logging_event_lbl = p("логирование:", "configurator_inputs_text")


    // logging_right_block.style.paddingTop = "2vw"
    logging_right_block.appendChild(create_channel_lbl)
    logging_right_block.appendChild(_input_channel_id)
    logging_right_block.appendChild(logging_event_lbl)


    for (let cmd = 0; cmd < 6; cmd += 2) {
        let row = div("mimi_wor")
        row.style.display = "flex"
        row.style.flexDirection = "row"
        row.appendChild(create_list(LOGGING_EVENTS[cmd][0], LOGGING_EVENTS[cmd][1], "logging"))
        row.appendChild(create_list(LOGGING_EVENTS[cmd + 1][0], LOGGING_EVENTS[cmd + 1][1], "logging"))

        logging_right_block.appendChild(row)
    }


    // logging_right_block.appendChild(input("select_roles", "text", "", "logging_channel_id"))

    // let logging_content = div("")

    logging_block.appendChild(logging_left_block)
    logging_block.appendChild(logging_right_block)


    let status_block = div("input_block")
    let status_lbl = p("статус бота", "no_margin")

    status_lbl.style.marginLeft = "0.9vw"

    status_block.style.textAlign = "left"
    status_block.style.marginBottom = "1vw"
    // status_block.style.marginLeft = "0.9vw"

    let input_row = div("mini_row")

    let select_type = select("select_roles", "_input_bot_status_type")
    select_type.style.width = "max-content"
    for (let st of STATUSES) {
        select_type.appendChild(option(st[1], st[0], st[0] === configuration_key["status"]["type"]))

    }

    select_type.style.marginLeft = "0.9vw"

    let input_status_text = input("select_roles", "text", "", "_input_status_text")
    input_status_text.maxLength = 127
    input_status_text.placeholder = "текст статуса"
    input_status_text.onerror = function () {
        warning("test warning")
    }
    input_status_text.style.width = "50%"
    // input_status_text.required = true


    input_status_text.value = configuration_key["status"]["text"]
    // select_type.value = configuration_key["status"]["type"]
    // update_logging_block(logging_switcher.checked)

    input_row.appendChild(select_type)
    input_row.appendChild(input_status_text)


    status_block.appendChild(status_lbl)
    status_block.appendChild(input_row)

    // let message_from_dm_switcher = input("active_checkbox", "checkbox", "", "logging_enable")
    // let message_from_dm_switcher_lbl = p("реагировать на команды мз личных сообщений", "no_margin")
    //
    // let message_from_dm_switcher_row = div("mini_row")
    //
    // message_from_dm_switcher_row.appendChild(message_from_dm_switcher)
    // message_from_dm_switcher_row.appendChild(message_from_dm_switcher_lbl)



    // message_from_dm_switcher.checked = configuration_key["message_from_dm_switcher_enable"]
    // message_from_dm_switcher.addEventListener("change", function () {
    //     // console.log(logging_switcher.checked)
    //     configuration_key["message_from_dm_switcher_enable"] = message_from_dm_switcher.checked
    //     // update_logging_block(logging_switcher.checked)
    //
    //     // logging_left_block.style.visibility = logging_switcher.checked ? "hidden" : "visible"
    //     // logging_right_block.style.visibility = logging_switcher.checked ? "hidden" : "visible"
    // })


    // let statistic_block = div("input_block")
    // statistic_block.style.width = "100%"
    // statistic_block.style.display = "flex"
    // statistic_block.style.flexDirection = "row"
    //
    // let statistic_lbl = p("статистика", "no_margin")
    // statistic_lbl.style.marginLeft = "0.9vw"
    // let statistic_switcher = input("active_checkbox", "checkbox", "", "statistic_enable")
    // let statistic_left_block = div("part_of_block")
    //
    //
    // statistic_switcher.checked = configuration_key["statistic"]["enable"]
    // statistic_switcher.addEventListener("click", function () {
    //     update_statistic_block(statistic_switcher.checked)
    // })
    //
    // let statistic_row = div("mini_row")
    //
    // statistic_left_block.style.minWidth = "20vw"
    //
    // statistic_row.appendChild(statistic_lbl)
    // statistic_row.appendChild(statistic_switcher)
    //
    // statistic_left_block.appendChild(statistic_row)
    //
    //
    // let statistic_right_block = div("part_of_block", "", "statistic_right_block")
    // statistic_right_block.style.width = "20vw"
    //
    // let statistic_channel_lbl = p("канал, где будет статистика", "configurator_inputs_text")
    // if (!login_discord) {
    //     statistic_channel_lbl.innerHTML += '<span style="color: #65e025">*</span>'
    //
    // }
    //
    // let statistic_input_channel_id
    // if (login_discord) {
    //     statistic_input_channel_id = select("select_roles", "statistic_input_channel_id")
    //
    //     statistic_input_channel_id.appendChild(option("создать канал автоматически", "-1", true))
    //
    //     for (let i of user_channels["text"]) {
    //         let opt = document.createElement("option")
    //         opt.text = i[1]
    //         opt.value = i[0]
    //
    //         if (i[0] === configuration_key["statistic"]["channel_id"]) {
    //             opt.selected = true
    //         }
    //         statistic_input_channel_id.appendChild(opt)
    //     }
    //
    // } else {
    //     statistic_input_channel_id = input("select_roles", "number", "", "statistic_input_channel_id")
    //     statistic_input_channel_id.value = configuration_key["statistic"]["channel_id"]
    //     statistic_input_channel_id.placeholder = "ID канала"
    // }
    // // let statistic_event_lbl = p("логирование:", "configurator_inputs_text")
    //
    //
    // statistic_right_block.style.paddingTop = "2vw"
    // statistic_right_block.appendChild(statistic_channel_lbl)
    // statistic_right_block.appendChild(statistic_input_channel_id)
    // // logging_right_block.appendChild(statistic_event_lbl)
    //
    //
    // for (let cmd = 0; cmd < 6; cmd += 2) {
    //     let row = div("mimi_wor")
    //     row.style.display = "flex"
    //     row.style.flexDirection = "row"
    //     row.appendChild(create_list(STATISTIC_LIST[cmd][0], STATISTIC_LIST[cmd][1], "statistic"))
    //     row.appendChild(create_list(STATISTIC_LIST[cmd + 1][0], STATISTIC_LIST[cmd + 1][1], "statistic"))
    //
    //     statistic_right_block.appendChild(row)
    // }
    //
    //
    // // logging_right_block.appendChild(input("select_roles", "text", "", "logging_channel_id"))
    //
    // // let logging_content = div("")
    //
    // statistic_block.appendChild(statistic_left_block)
    // statistic_block.appendChild(statistic_right_block)


    block.appendChild(logging_block)
    block.appendChild(status_block)
    // block.appendChild(message_from_dm_switcher_row)
    // block.appendChild(statistic_block)

    let _p = p("используйте -1, чтобы создать канал автоматически", "configurator_inputs_text")
    _p.innerHTML = '<span style="color: #65e025">*</span>' + _p.textContent

    _p.style.marginTop = "1vw"

    if (!login_discord) {
        block.appendChild(_p)

    }

    // update_logging_block(logging_switcher.checked)
    // update_statistic_block(statistic_switcher.checked)

}


document.getElementById("save_btn").addEventListener("click", function () {

    const status_value = document.getElementById("_input_status_text").value

    if (status_value.length === 0) {
        danger("Необходимо указать статус бота")
        return 0
    }

    // base_save_settings(configuration_key)

    configuration_key["status"]["type"] = document.getElementById("_input_bot_status_type").value
    configuration_key["status"]["text"] = status_value


    let logging_events = []
    for (let i of LOGGING_EVENTS) {
        console.log(i)
        if (document.getElementById("logging_" + i[0]).checked) {
            logging_events.push(i[0])
        }
    }

    configuration_key["logging"]["values"] = logging_events

    // let statistic_types = []
    // for (let i of STATISTIC_LIST) {
    //     if (document.getElementById("statistic_" + i[0]).checked) {
    //         statistic_types.push(i[0])
    //     }
    // }
    //
    // configuration_key["statistic"]["values"] = statistic_types


    configuration_key["logging"]["channel_id"] = document.getElementById("input_channel_id").value
    // configuration_key["statistic"]["channel_id"] = document.getElementById("statistic_input_channel_id").value
    // console.log(logging_events)

    configuration_key["logging"]["enable"] = document.getElementById("logging_enable").checked
    // configuration_key["statistic"]["enable"] = document.getElementById("statistic_enable").checked


    const answer = post_data("settings", configuration_key)
    console.log(configuration_key)
    answer.then(a => {
        if (a["status"] === "ok") {
            success()
            return 0
        }
        danger(a["message"])
    })

})

document.getElementById("reset_btn").addEventListener("click", function () {
    if (confirm("Вы уверены, что хотите сбросить все изменения?")) {
        reset_settings_configuration_key()


        const answer = post_data("settings", configuration_key)
        answer.then(a => {
            if (a["status"] === "ok") {
                warning("изменения сброшены")
                return 0
            }
            danger(a["message"])
        })

        main()


    }
})