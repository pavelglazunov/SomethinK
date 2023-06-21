update_chapter(6)


const block = document.getElementById("settings")
const loader = document.getElementsByClassName("loading")

const STATUSES = [["playing", "играет"], ["listening", "слушает"], ["watching", "смотрит"], ["streaming ", "стримит"]]

function create_logging_event(name, text) {
    let logging_event_block = div("mini_row")

    logging_event_block.appendChild(input("blue_checkbox", "checkbox", "logging_event", "le_" + name))
    let _p = p(text, "no_margin")
    _p.style.fontSize = "0.9vw"

    logging_event_block.appendChild(_p)

    logging_event_block.style.minWidth = "11vw"

    return logging_event_block

}

function update_logging_block(value) {
    for (let set_btn of document.getElementsByClassName("settings_button")) {
        console.log(set_btn)
        set_btn.style.filter = !value ? "grayscale(50%)" : "grayscale(0)"
    }
    for (let evt of document.getElementsByClassName("mini_row")) {
        // console.log(evt)
        evt.style.filter = !value ? "grayscale(50%)" : "grayscale(0)"
    }
    // for (let nm of document.getElementsByClassName("no_margin")) {
    //     // console.log(evt)
    //     nm.style.color = !value ? "#aba9a9" : "#dedede"
    // }
    document.getElementsByName("logon")[0].style.filter = !value ? "grayscale(50%)" : "grayscale(0)"
    document.getElementsByName("logoff")[0].style.filter = !value ? "grayscale(50%)" : "grayscale(0)"

    document.getElementById("input_channel_id").style.filter = !value ? "grayscale(50%)" : "grayscale(0)"
    document.getElementById("input_channel_id").style.color = !value ? "#aba9a9" : "#FFFFFF"

    document.getElementsByClassName("part_of_block")[1].style.color = !value ? "#aba9a9" : "#FFFFFF"
}


console.log(block)

function reset_settings_configuration_key() {
    configuration_key["logging"] = {
        "enable": true,
        "channel_id": "-1",
        "logging_events": ["command", "auto_moderation"]
    }
    configuration_key["status"] = ["play", ""]
    configuration_key["statistic"] = {
        "enable": true,
        "channel_id": "-1",
        "stats": ["text", "voice", "member", "roles", "category", "messages"],
        "interval": 5
    }

    for (let cmd of LOGGING_COMMANDS) {
        let command_config = {}
        command_config["enable"] = false
        command_config["description"] = ALL_COMMANDS[cmd]
        command_config["roles"] = []
        command_config["channels"] = []

        configuration_key[cmd] = command_config
    }
}


let login_discord = null
let user_roles = []
let user_channels = {}

// displayLoading(loader)
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

        if (Object.keys(configuration_key).length === 0) {
            configuration_key = {}
            reset_settings_configuration_key()
        } else {
            configuration_key = JSON.parse(configuration_key)

        }


        // hideLoading(loader)
        main()

    })

const LOGGING_EVENTS = [
    ["time_messages", "регулярные сообщения"],
    ["commands", "команды"],
    ["statistic", "обновление статистики"],
    ["auto_response", "автоответчик"],
    ["youtube", "оповещения ютуб"],
    ["activity_roles", "роли активности"],
    ["twitch", "оповещения твич"],
    ["events", "события"],

]

function main() {
    console.log(block)
    block.innerHTML = ""

    let logging_block = div("input_block")
    logging_block.style.width = "100%"
    logging_block.style.display = "flex"
    logging_block.style.flexDirection = "row"

    let logging_lbl = p("логирование", "no_margin")
    logging_lbl.style.marginLeft = "0.9vw"
    let logging_switcher = input("active_checkbox", "checkbox", "", "logging_enable")
    let logging_left_block = div("part_of_block")

    logging_switcher.addEventListener("click", function () {
        // console.log(logging_switcher.checked)
        update_logging_block(logging_switcher.checked)
    })

    let logging_row = div("mini_row")

    logging_left_block.style.minWidth = "20vw"

    logging_row.appendChild(logging_lbl)
    logging_row.appendChild(logging_switcher)

    logging_left_block.appendChild(logging_row)
    logging_left_block.appendChild(create_command_block(
        configuration_key,
        "configurator",
        base_save_settings,
        "logon",
    ))
    logging_left_block.appendChild(create_command_block(
        configuration_key,
        "configurator",
        base_save_settings,
        "logoff",
    ))

    let logging_right_block = div("part_of_block")
    logging_right_block.style.width = "20vw"

    let create_channel_lbl = p("канал, куда будут отправляться логи", "configurator_inputs_text")

    let _input_channel_id
    if (login_discord) {
        _input_channel_id = select("select_roles", "input_channel_id")

        _input_channel_id.appendChild(option("создать канал автоматически", "-1", true))

        for (let i of user_channels["text"]) {
            let opt = document.createElement("option")
            opt.text = i[1]
            opt.value = i[0]

            if (i[0] === configuration_key["logging"]["channel_id"]) {
                opt.selected = true
            }
            _input_channel_id.appendChild(opt)
        }

    } else {
        _input_channel_id = input("select_roles", "number", "", "input_channel_id")
        _input_channel_id.value = configuration_key["logging"]["channel_id"]
        _input_channel_id.placeholder = "ID канала"
    }
    let logging_event_lbl = p("логирование:", "configurator_inputs_text")


    logging_right_block.style.paddingTop = "2vw"
    logging_right_block.appendChild(create_channel_lbl)
    logging_right_block.appendChild(_input_channel_id)
    logging_right_block.appendChild(logging_event_lbl)


    for (let cmd = 0; cmd < 8; cmd += 2) {
        let row = div("mimi_wor")
        row.style.display = "flex"
        row.style.flexDirection = "row"
        row.appendChild(create_logging_event(LOGGING_EVENTS[cmd][0], LOGGING_EVENTS[cmd][1]))
        row.appendChild(create_logging_event(LOGGING_EVENTS[cmd + 1][0], LOGGING_EVENTS[cmd + 1][1]))

        logging_right_block.appendChild(row)
    }


    // logging_right_block.appendChild(input("select_roles", "text", "", "logging_channel_id"))

    // let logging_content = div("")

    logging_block.appendChild(logging_left_block)
    logging_block.appendChild(logging_right_block)

    let status_block = div("input_block")
    let status_lbl = p("статус бота", "no_margin")

    status_block.style.textAlign = "left"
    status_block.style.marginBottom = "1vw"

    let input_row = div("mini_row")

    let select_type = select("select_roles", "_input_bot_status_type")
    select_type.style.width = "max-content"
    for (let st of STATUSES) {
        select_type.appendChild(option(st[1], st[0]))

    }

    let input_status_text = input("select_roles", "text", "", "_input_status_text")
    input_status_text.maxLength = 127
    input_status_text.onerror = function () {
        warning("test warning")
    }
    input_status_text.style.width = "50%"
    // update_logging_block(logging_switcher.checked)

    input_row.appendChild(select_type)
    input_row.appendChild(input_status_text)


    status_block.appendChild(status_lbl)
    status_block.appendChild(input_row)



    block.appendChild(logging_block)
    block.appendChild(status_block)
}