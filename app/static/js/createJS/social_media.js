update_chapter(4)

const youtube_blocks = document.getElementById("youtube_blocks")
const twitch_blocks = document.getElementById("twitch_blocks")
const youtube_footer = document.getElementById("youtube_footer")
const twitch_footer = document.getElementById("twitch_footer")
const loader = document.getElementsByClassName("loading")

const youtube_counter = document.getElementById("youtube_counter")
const twitch_counter = document.getElementById("twitch_counter")

let counter = 0

const SM = {
    "youtube": {
        "color": "#C4302B",
        "bg": "#6B1F1D",
        "header": "ютуб",
        "counter": youtube_counter
    },
    "twitch": {
        "color": "#6441A5",
        "bg": "#392A56",
        "header": "твич",
        "counter": twitch_counter
    }
}


function reset_sm_configurator() {
    configuration_key["youtube"] = {}
    configuration_key["twitch"] = {}


    // configuration_key["commands"] = {}

    // for (let i of SM_COMMANDS) {
    //     for (let j of i) {
    //         let command_config = {}
    //         command_config["enable"] = true
    //         command_config["description"] = ALL_COMMANDS[j]
    //         command_config["roles"] = []
    //         command_config["channels"] = []
    //
    //         configuration_key[j] = command_config
    //     }
    // }

}

function update_counter(type) {
    SM[type]["counter"].textContent = get_count(type) + "/3"
}

function get_count(type) {
    return document.getElementsByClassName(type).length
}

function generate_block(
    url = "",
    channel_id = "",
    message = "",
    type = "",
    add_lbl = false
) {
    counter++

    let block = div("block", "", type + "_block_" + counter)
    block.style.borderColor = SM[type]["color"]
    block.style.marginBottom = "1vw"
    block.style.marginTop = "1.5vw"
    block.classList.add(type)
    block.style.padding = "0"

    if (add_lbl) {
        console.log("header")
        block.appendChild(p(SM[type]["header"], "block_header"))
    }
    let block_content = div("block_content")
    block_content.style.minHeight = "10vw"
    block_content.style.marginTop = "1vw"


    block_content.style.alignItems = "center"


    let _input_url = input("select_roles", "text", "", "_input_url_" + counter)
    _input_url.placeholder = "Ссылка на канал"
    _input_url.style.borderColor = SM[type]["color"]
    _input_url.style.marginBottom = "1vw"
    _input_url.value = url


    let _input_channel_id
    if (login_discord) {
        _input_channel_id = select("select_roles", "_input_channel_id_" + counter)

        let opt = document.createElement("option")
        opt.text = "ID канала, куда будут приходить уведомления"
        opt.value = "-1"
        opt.selected = true
        _input_channel_id.appendChild(opt)
        for (let i of user_channels["text"]) {
            let opt = document.createElement("option")
            opt.text = i[1]
            opt.value = i[0]

            if (i[0] === channel_id) {
                opt.selected = true
            }
            _input_channel_id.appendChild(opt)
        }

    } else {
        _input_channel_id = input("select_roles", "number", "", "_input_channel_id_" + counter)
        _input_channel_id.value = channel_id
        _input_channel_id.placeholder = " ID канала, куда будут приходить уведомления"
        _input_channel_id.value = channel_id
    }
    _input_channel_id.style.borderColor = SM[type]["color"]
    _input_channel_id.style.marginBottom = "1vw"


    let _input_message = document.createElement("textarea")
    _input_message.id = "_input_message_" + counter
    _input_message.classList.add("select_roles")
    _input_message.style.resize = "none"
    _input_message.style.height = "3vw"
    _input_message.placeholder = "Введите текст сообщения"
    _input_message.style.borderColor = SM[type]["color"]
    _input_message.maxLength = 3000
    _input_message.value = message

    let __remove_pos_div = div("__pos_div")

    let _remove_block = button("select_roles", "удалить блок", "", type + "_remove_" + counter)
    _remove_block.style.height = "max-content"
    _remove_block.style.width = "max-content"
    _remove_block.style.fontSize = "0.7vw"
    _remove_block.style.padding = "0.3vw"
    _remove_block.style.position = "end"
    _remove_block.style.cursor = "pointer"
    _remove_block.style.borderColor = SM[type]["color"]
    _remove_block.style.borderWidth = "0px"
    _remove_block.addEventListener("click", function () {
        block.remove()
        update_counter(type)
    })


    __remove_pos_div.appendChild(_remove_block)


    block_content.appendChild(_input_url)
    block_content.appendChild(_input_channel_id)
    block_content.appendChild(_input_message)
    block_content.appendChild(__remove_pos_div)

    block.appendChild(block_content)

    return block
}


function generate_base_variant() {
    youtube_blocks.appendChild(generate_block("", "", "", "youtube", get_count("youtube") === 0))
    twitch_blocks.appendChild(generate_block("", "", "", "twitch", get_count("twitch") === 0))

    update_counter("youtube")
    update_counter("twitch")
}


let login_discord = null
let user_channels = {}
let user_roles = {}
let configuration_key = {}


youtube_footer.style.visibility = "hidden"
twitch_footer.style.visibility = "hidden"

displayLoading(loader)

fetch('/api/get', {
    method: "GET",
    headers: {
        "configuration_name": "social_media",
        "get": "roles|channels"
    }
})
    .then((response) => response.json())
    .then((data) => {
        login_discord = data["auth_with_discord"]
        user_channels = data["channels"]
        user_roles = data["roles"]
        configuration_key = data["configuration_key"]

        if (data["configuration_key"] === "{}") {
            console.log(55555)
            configuration_key = {}
            reset_sm_configurator()
            // generate_base_variant()

        } else {
            configuration_key = JSON.parse(configuration_key)

        }

        console.log(configuration_key)


        hideLoading(loader)
        main()

    })


function main() {

    for (let yt of Object.keys(configuration_key.youtube)) {
        console.log(configuration_key["youtube"][yt])
        youtube_blocks.appendChild(generate_block(
            configuration_key["youtube"][yt]["link"],
            configuration_key["youtube"][yt]["channel_id"],
            configuration_key["youtube"][yt]["message"],
            "youtube",
            Object.keys(configuration_key.youtube).indexOf(yt) === 0

        ))
    }
    for (let tw of Object.keys(configuration_key.twitch)) {
        twitch_blocks.appendChild(generate_block(
            configuration_key["twitch"][tw]["link"],
            configuration_key["twitch"][tw]["channel_id"],
            configuration_key["twitch"][tw]["message"],
            "twitch",
            Object.keys(configuration_key.twitch).indexOf(tw) === 0
        ))
    }


    // if (Object.keys(configuration_key.twitch).length === 0 && Object.keys(configuration_key.youtube).length === 0) {
    //     generate_base_variant()
    //
    // }
    // youtube_blocks.appendChild(generate_block(
    //     "", "", "", "youtube", true
    // ))
        // console.log("<<<<<<<<<<<<<<", configuration_key)
    // for (let i of SM_COMMANDS[0]) {
    //     youtube_footer.appendChild(create_command_block(configuration_key, "configurator", base_save_settings, i, {
    //         "slash": true,
    //         "settings": true,
    //         "automod": "",
    //         "remove_after_close": true,
    //         "parent_id": "configurator_parent",
    //     }))
    //     let el = document.getElementsByName(i)[0]
    //     el.style.borderColor = SM["youtube"]["color"]
    //     el.style.backgroundColor = SM["youtube"]["bg"]
    //     el.style.setProperty('--after-color', SM["youtube"]["color"])
    // }
    //
    // for (let i of SM_COMMANDS[1]) {
    //     twitch_footer.appendChild(create_command_block(configuration_key, "configurator", base_save_settings, i, {
    //         "slash": true,
    //         "settings": true,
    //         "automod": "",
    //         "remove_after_close": true,
    //         "parent_id": "configurator_parent",
    //     }))
    //     // cmd.style.borderColor = SM["twitch"]["color"]
    //     let el = document.getElementsByName(i)[0]
    //     el.style.borderColor = SM["twitch"]["color"]
    //     el.style.backgroundColor = SM["twitch"]["bg"]
    //     el.style.setProperty('--after-color', SM["twitch"]["color"])
    //
    // }
    // for (let i of document.getElementsByClassName("command_block")) {
    //     i.style.width = "14vw"
    // }


    document.getElementById("add_youtube_block").addEventListener("click", function () {
        if (get_count("youtube") < 3) {
            youtube_blocks.appendChild(generate_block(
                "", "", "", "youtube", get_count("youtube") === 0
            ))
            update_counter("youtube")
        } else {
            warning("Достигнут лимит ютуб каналов")
        }


    })
    document.getElementById("add_twitch_block").addEventListener("click", function () {
        if (get_count("twitch") < 3) {
            twitch_blocks.appendChild(generate_block(
                "", "", "", "twitch", get_count("twitch") === 0
            ))
            update_counter("twitch")
        } else {
            warning("Достигнут лимит твич каналов")
        }


    })

    update_counter("youtube")
    update_counter("twitch")


    youtube_footer.style.visibility = "visible"
    twitch_footer.style.visibility = "visible"
}

document.getElementById("save_btn").addEventListener("click", function () {
    // base_save_settings(configuration_key)

    let new_yt_data = {}
    for (let yt of document.getElementsByClassName("youtube")) {
        let id = yt.id.split("_block_")[1]
        let link = document.getElementById("_input_url_" + id).value
        let channel_id = document.getElementById("_input_channel_id_" + id).value
        let message = document.getElementById("_input_message_" + id).value

        console.log(id)
        console.log(link)
        console.log(channel_id)
        console.log(message)
        console.log("////////")
        if (!link) {
            danger("Необходимо ввести ссылку на ютуб канал")
            return
        }
        if (Number(channel_id) < 1) {
            danger("Необходимо указать канал, куда будут приходить уведомления")

            return
        }
        if (!message) {
            danger("Необходимо ввести текст сообщения")
            return
        }

        data = {
            "link": link,
            "channel_id": channel_id,
            "message": message


        }

        new_yt_data[id] = data
    }


    let new_tw_data = {}
    for (let tw of document.getElementsByClassName("twitch")) {
        let id = tw.id.split("_block_")[1]
        let link = document.getElementById("_input_url_" + id).value
        let channel_id = document.getElementById("_input_channel_id_" + id).value
        let message = document.getElementById("_input_message_" + id).value

        console.log(id)
        if (!link) {
            danger("Необходимо ввести ссылку на твич канал")
            return
        }
        if (Number(channel_id) < 1) {
            danger("Необходимо указать канал, куда будут приходить уведомления о прямой трансляции")

            return
        }
        if (!message) {
            danger("Необходимо ввести текст сообщения")
            return
        }

        data = {
            "link": link,
            "channel_id": channel_id,
            "message": message


        }

        new_tw_data[id] = data
    }

    configuration_key["youtube"] = new_yt_data
    configuration_key["twitch"] = new_tw_data

    const answer = post_data("social_media", configuration_key)
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
        reset_sm_configurator()


        // const answer = post_data("messages", configuration_key)
        // console.log(configuration_key)

        // while (document.getElementsByClassName("command_block")) {
        //     document.getElementsByClassName("command_block")[0].remove()
        //     console.log(1)
        // }
        const command_blocks = document.getElementsByClassName("command_block")

        for (let i = 0; i < 4; i++) {
            command_blocks[0].remove()
        }

        youtube_blocks.innerHTML = ""
        twitch_blocks.innerHTML = ""
        // for (let i of document.getElementsByClassName("command_block")) {
        //     i.remove()
        // }
        // document.getElementById("youtube_footer").innerHTML = ""
        // document.getElementById("twitch_footer").innerHTML = ""

        // generate_base_variant()
        const answer = post_data("social_media", configuration_key)
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
