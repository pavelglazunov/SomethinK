update_chapter(5)

const block = document.getElementById("commands")
const loader = document.getElementsByClassName("loading")



function reset_another_configuration_key() {
    for (let i of ANOTHER_COMMANDS) {
        for (let j of i) {
            let command_config = {}
            command_config["enable"] = false
            command_config["description"] = ALL_COMMANDS[j]
            command_config["roles"] = []
            command_config["channels"] = []
            if (j in COMMANDS_WITH_API_TOKEN) {
                command_config["token"] = ""
            }
            configuration_key[j] = command_config
        }
    }
}



let login_discord = null
let user_roles = []
let user_channels = {}

displayLoading(loader)
let configuration_key = {}
fetch('/api/get', {
    method: "GET",
    headers: {
        "configuration_name": "another",
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
            reset_another_configuration_key()
        } else {
            configuration_key = JSON.parse(configuration_key)

        }



        hideLoading(loader)
        main()

    })

ANOTHER_COMMANDS = [
    ["color", "nick"],
    ["joke", "weather"],
    ["translate", "say"],
    ["avatar", "gpt"],
    ["embed", "invite"]
]

function main() {
    block.innerHTML = ""

    restart_configurator(document.getElementById("configurator"))

    console.log(configuration_key)
    for (let cmd of ANOTHER_COMMANDS) {
        let row = div("row")

        row.appendChild(create_command_block(
            configuration_key,
            "configurator",
            base_save_settings,
            cmd[0],
        ))
        row.appendChild(create_command_block(
            configuration_key,
            "configurator",
            base_save_settings,
            cmd[1],
        ))

        block.appendChild(row)
    }


}

document.getElementById("save_btn").addEventListener("click", function () {
    base_save_settings(configuration_key)

    if (configuration_key["gpt"]["enable"] && !configuration_key["gpt"]["token"]) {
        danger("Необходимо ввести API токен от openAI")
        return 0
    }

    if (configuration_key["weather"]["enable"] && !configuration_key["weather"]["token"]) {
        danger("Необходимо ввести API токен от Weather")
        return 0
    }

    const answer = post_data("another", configuration_key)
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
        reset_another_configuration_key()

        main()
        // update_counter("time_message_block", tm_count, time_messages_block)
        // update_counter("events_block", events_counter, events_block)
        // update_counter("auto_response_block", auto_response_counter, auto_response_block)

        const answer = post_data("another", configuration_key)
        answer.then(a => {
            if (a["status"] === "ok") {
                warning("изменения сброшены")
                return 0
            }
            danger(a["message"])
        })
    }
})