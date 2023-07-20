const time_messages_block = document.getElementById("time_messages_block")
const events_block = document.getElementById("events_block")
const auto_response_block = document.getElementById("auto_response_block")
const loader = document.getElementsByClassName("loading");

const tm_count = document.getElementById("tm_counter");
const events_counter = document.getElementById("events_counter");
const auto_response_counter = document.getElementById("auto_response_counter");

// time_messages_block.style.height = "100%"
events_block.style.height = "max-content"
// auto_response_block.style.height = "100%"

const limits = {
    "time_message_block": 5,
    "events_block": 2,
    "auto_response_block": 5
}

const no_messages = {
    "time_message_block": "регулярных сообщений",
    "events_block": "событий",
    "auto_response_block": "автоответчиков"
}

update_chapter(2)

let count = 0
let ev_count = 0

let login_discord = null
let user_channels = {}

let configuration_key = {}

displayLoading(document.getElementsByClassName("loading"))
//
fetch('/api/get', {
    method: "GET",
    headers: {
        "configuration_name": "messages",
        "get": "channels|"
    }
})
    .then((response) => response.json())
    .then((data) => {
        login_discord = data["auth_with_discord"]
        // user_roles = data["roles"]
        // console.log(login_discord, "login discord")

        user_channels = data["channels"]

        configuration_key = data["configuration_key"]
        console.log(data["configuration_key"])
        if (data["configuration_key"] === "{}") {
            configuration_key = {}
            reset_message_configuration_key()
        } else {
            configuration_key = JSON.parse(configuration_key)

        }

        // console.log(configuration_key)

        hideLoading(document.getElementsByClassName("loading"))

        main()
    })

function reset_message_configuration_key(show_message = true) {
    configuration_key["time_message"] = {}
    configuration_key["events"] = {}
    configuration_key["auto_response"] = {}

    // for (let tm of document.getElementsByClassName("time_message_block"))
}

function update_counter(type, counter, block) {
    counter.textContent = get_count(type) + "/" + limits[type]
    if (get_count(type) === 0) {
        const no_tm = p("у вас еще нет " + no_messages[type], "configurator_inputs_text")
        no_tm.style.fontSize = "2vw"
        no_tm.style.marginTop = "1vw"

        block.appendChild(no_tm)

        // update_counter("time_message_block", counter)


    }
}

function get_count(type) {
    return document.getElementsByClassName(type).length
}

function generate_time_message_block(
    enable_embed = false,
    text_content = "",
    channel_id = "",
    first_send = "12:00",
    interval = "24",
    units_of_measure = "hours",
    embed = {
        "author": "",
        "icon_link": "",
        "header": "",
        "color": "#BEC100",
        "image_url": "",
        "footer_content": ""

    }
) {

    count += 1

    let block = div("time_message_block", "", "_time_message_block_" + count)

    let enable_embed_row = div("mini_row")
    let enable_embed_switcher = input("blue_checkbox", "checkbox", "", "enable_embed_switcher_" + count)
    let enable_embed_lbl = p("embed", "command_name_text")

    enable_embed_switcher.checked = enable_embed

    enable_embed_lbl.style.marginLeft = "0.5vw"


    let block_content = div("input_block_content")
    block_content.style.marginTop = "0.7vw"

    let _input_text_content = document.createElement("textarea")
    _input_text_content.classList.add("select_roles")
    _input_text_content.maxLength = 3000
    _input_text_content.style.resize = "none"
    _input_text_content.style.fontSize = "1.2vw"
    _input_text_content.value = text_content
    _input_text_content.style.height = "6vw"
    _input_text_content.style.width = "40%"
    _input_text_content.placeholder = "введите текст сообщения"
    _input_text_content.id = "_input_text_content_" + count


    let data_block = div("data_block")

    let _input_channel_id
    if (login_discord) {
        _input_channel_id = select("select_roles", "_input_channel_id_" + count)

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
        _input_channel_id = input("select_roles", "number", "", "_input_channel_id_" + count)
        _input_channel_id.value = channel_id
        _input_channel_id.placeholder = "ID канала"
    }

    // _input_channel_id.style.width = "100%"


    let data_row = div("mini_row")
    data_row.style.alignItems = "flex-end"

    let first_time_div = div("data_mimi_block")
    let _input_first_time = input("select_roles", "time", "", "_input_first_time_" + count)
    let _lbl_first_time = p("время отправления", "configurator_inputs_text")

    _input_first_time.value = first_send
    _input_first_time.style.width = "100%"


    let interval_div = div("data_mimi_block")
    let _input_interval = input("select_roles", "number", "", "_input_interval_" + count)
    let _lbl_interval = p("интервал", "configurator_inputs_text")

    _input_interval.value = interval
    _input_interval.max = "1000"
    _input_interval.min = "1"
    _input_interval.style.width = "100%"
    // _input_interval.style.


    let units_of_measure_div = div("data_mimi_block")
    let _input_units_of_measure = select("select_roles", "_input_units_of_measure_" + count, "")
    let _lbl_units_of_measure = p("ед. измерения", "configurator_inputs_text")

    const intervals = [["часы", "hours"], ["дни", "days"], ["недели", "weeks"], ["месяца", "months"], ["года", "years"]]
    for (let i of intervals) {
        let opt = document.createElement("option")
        opt.text = i[0]
        opt.value = i[1]
        if (i[1] === units_of_measure) {
            opt.selected = true
        }

        _input_units_of_measure.appendChild(opt)
    }

    _input_units_of_measure.style.width = "100%"


    let _remove_button = button("remove_button", "❌")
    _remove_button.addEventListener("click", function () {
        block.remove()
        update_counter("time_message_block", tm_count, time_messages_block)

    })


    enable_embed_row.appendChild(enable_embed_switcher)
    enable_embed_row.appendChild(enable_embed_lbl)


    if (enable_embed) {


        let _input_author = input("select_roles", "text")
        _input_author.placeholder = "автор"
        _input_author.style.marginBottom = "0.5vw"
        _input_author.style.marginRight = "0"
        _input_author.style.width = "100%"
        _input_author.style.maxWidth = "100%"
        _input_author.id = "_input_author_" + count
        _input_author.value = embed["author"]

        let _input_header = input("select_roles", "text")
        _input_header.placeholder = "заголовок"
        _input_header.style.marginBottom = "0.5vw"
        _input_header.style.marginRight = "0"
        _input_header.style.width = "100%"
        _input_header.style.maxWidth = "100%"
        _input_header.id = "_input_header_" + count
        _input_header.value = embed["header"]

        let _input_img_url = input("select_roles", "text")
        _input_img_url.placeholder = "ссылка на изображение"
        _input_img_url.style.marginBottom = "0.5vw"
        _input_img_url.style.marginRight = "0"
        _input_img_url.style.width = "100%"
        _input_img_url.style.maxWidth = "100%"
        _input_img_url.id = "_input_img_url_" + count
        _input_img_url.value = embed["image_url"]

        let _input_footer = input("select_roles", "text")
        _input_footer.placeholder = "текст футера"
        // _input_footer.style.marginBottom = "0.5vw"
        _input_footer.style.marginRight = "0"
        _input_footer.style.width = "100%"
        _input_footer.style.maxWidth = "100%"
        _input_footer.id = "_input_footer_" + count
        _input_footer.value = embed["footer_content"]

        let _input_color = input("color_select", "color")
        _input_color.value = embed["color"]
        _input_color.id = "_input_color_" + count

        _input_color.addEventListener("input", function () {
            main_content_block.style.borderLeftColor = _input_color.value
            // console.log("change")
        })

        data_block.appendChild(_input_color)

        let main_content_block = div("main_content_block")

        main_content_block.style.marginLeft = "-0.5vw"
        main_content_block.style.paddingLeft = "0.5vw"

        main_content_block.style.borderLeft = "2px solid " + _input_color.value

        main_content_block.appendChild(_input_author)
        main_content_block.appendChild(_input_header)
        main_content_block.appendChild(_input_text_content)
        main_content_block.appendChild(_input_img_url)
        main_content_block.appendChild(_input_footer)

        block_content.appendChild(main_content_block)

        let channel_and_color_row = div("input_block_content")
        channel_and_color_row.appendChild(_input_channel_id)
        channel_and_color_row.appendChild(_input_color)


        _input_text_content.style.marginBottom = "0.5vw"
        _input_text_content.style.width = "100%"
        _input_text_content.style.maxWidth = "100%"
        _input_text_content.style.marginRight = "0"

        data_block.appendChild(channel_and_color_row)


    } else {
        data_block.appendChild(_input_channel_id)

        block_content.appendChild(_input_text_content)

    }
    _input_channel_id.style.width = "59%"


    first_time_div.appendChild(_lbl_first_time)
    first_time_div.appendChild(_input_first_time)

    interval_div.appendChild(_lbl_interval)
    interval_div.appendChild(_input_interval)

    units_of_measure_div.appendChild(_lbl_units_of_measure)
    units_of_measure_div.appendChild(_input_units_of_measure)

    data_row.appendChild(first_time_div)
    data_row.appendChild(interval_div)
    data_row.appendChild(units_of_measure_div)
    data_row.appendChild(_remove_button)

    data_block.appendChild(data_row)

    block_content.appendChild(data_block)


    block.appendChild(enable_embed_row)
    block.appendChild(block_content)

    enable_embed_switcher.addEventListener("click", function () {
        let data = embed
        let ___id = enable_embed_switcher.id.split("enable_embed_switcher_")[1]

        if (!embed) {
            data = {
                "author": document.getElementById("_input_author_" + ___id).value,
                "header": document.getElementById("_input_header_" + ___id).value,
                "image_url": document.getElementById("_input_img_url_" + ___id).value,
                "footer_content": document.getElementById("_input_footer_" + ___id).value,
                "color": document.getElementById("_input_color_" + ___id).value
            }

        }
        let new_block = generate_time_message_block(
            enable_embed_switcher.checked,
            document.getElementById("_input_text_content_" + ___id).value,
            document.getElementById("_input_channel_id_" + ___id).value,
            document.getElementById("_input_first_time_" + ___id).value,
            document.getElementById("_input_interval_" + ___id).value,
            document.getElementById("_input_units_of_measure_" + ___id).value,
            data
        )

        block.replaceWith(new_block)

    })

    return block
    // time_messages_block.appendChild(block)
}


function generate_events_block(
    enable_embed = false,
    text_content = "",
    channel_id = "",
    event_type = "join",
    embed = {
        "author": "",
        "icon_link": "",
        "header": "",
        "color": "#BEC100",
        "image_url": "",
        "footer_content": ""

    }
) {
    count += 1

    let block = div("events_block", "", "_event_block_" + count)

    let enable_embed_row = div("mini_row")
    let enable_embed_switcher = input("blue_checkbox", "checkbox", "", "enable_embed_switcher_" + count)
    let enable_embed_lbl = p("embed", "command_name_text")

    enable_embed_switcher.checked = enable_embed

    enable_embed_lbl.style.marginLeft = "0.5vw"


    let block_content = div("input_block_content")
    block_content.style.marginTop = "0.7vw"

    let _input_text_content = document.createElement("textarea")
    _input_text_content.classList.add("select_roles")
    _input_text_content.maxLength = 3000
    _input_text_content.style.resize = "none"
    _input_text_content.style.fontSize = "1.2vw"
    _input_text_content.value = text_content
    _input_text_content.style.height = "6vw"
    _input_text_content.style.width = "40%"
    _input_text_content.placeholder = "введите текст сообщения"
    _input_text_content.id = "_input_text_content_" + count


    let data_block = div("data_block")

    let _input_channel_id
    if (login_discord) {
        _input_channel_id = select("select_roles", "_input_channel_id_" + count)

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
        _input_channel_id = input("select_roles", "text", "", "_input_channel_id_" + count)
        _input_channel_id.value = channel_id
        _input_channel_id.placeholder = "ID канала"
    }

    // _input_channel_id.style.width = "100%"


    let data_row = div("mini_row")
    data_row.style.alignItems = "flex-end"

    let _input_event_type = select("select_roles", "_input_event_type_" + count)
    const types = [["участник присоединился", "join"], ["участник вышел", "leave"]]
    for (let i of types) {
        let opt = option(i[0], i[1])
        if (i[1] === event_type) {
            opt.selected = true
        }
        _input_event_type.appendChild(opt)
    }


    let _remove_button = button("remove_button", "❌")
    _remove_button.addEventListener("click", function () {
        block.remove()
        update_counter("events_block", events_counter, events_block)


    })


    enable_embed_row.appendChild(enable_embed_switcher)
    enable_embed_row.appendChild(enable_embed_lbl)


    if (enable_embed) {


        let _input_author = input("select_roles", "text")
        _input_author.placeholder = "автор"
        _input_author.style.marginBottom = "0.5vw"
        _input_author.style.marginRight = "0"
        _input_author.style.width = "100%"
        _input_author.style.maxWidth = "100%"
        _input_author.id = "_input_author_" + count
        _input_author.value = embed["author"]

        let _input_header = input("select_roles", "text")
        _input_header.placeholder = "заголовок"
        _input_header.style.marginBottom = "0.5vw"
        _input_header.style.marginRight = "0"
        _input_header.style.width = "100%"
        _input_header.style.maxWidth = "100%"
        _input_header.id = "_input_header_" + count
        _input_header.value = embed["header"]

        let _input_img_url = input("select_roles", "text")
        _input_img_url.placeholder = "ссылка на изображение"
        _input_img_url.style.marginBottom = "0.5vw"
        _input_img_url.style.marginRight = "0"
        _input_img_url.style.width = "100%"
        _input_img_url.style.maxWidth = "100%"
        _input_img_url.id = "_input_img_url_" + count
        _input_img_url.value = embed["image_url"]

        let _input_footer = input("select_roles", "text")
        _input_footer.placeholder = "текст футера"
        // _input_footer.style.marginBottom = "0.5vw"
        _input_footer.style.marginRight = "0"
        _input_footer.style.width = "100%"
        _input_footer.style.maxWidth = "100%"
        _input_footer.id = "_input_footer_" + count
        _input_footer.value = embed["footer_content"]

        let _input_color = input("color_select", "color")
        _input_color.value = embed["color"]
        _input_color.id = "_input_color_" + count

        _input_color.addEventListener("input", function () {
            main_content_block.style.borderLeftColor = _input_color.value
            // console.log("change")
        })

        data_block.appendChild(_input_color)

        let main_content_block = div("main_content_block")

        main_content_block.style.marginLeft = "-0.5vw"
        main_content_block.style.paddingLeft = "0.5vw"

        main_content_block.style.borderLeft = "2px solid " + _input_color.value

        main_content_block.appendChild(_input_author)
        main_content_block.appendChild(_input_header)
        main_content_block.appendChild(_input_text_content)
        main_content_block.appendChild(_input_img_url)
        main_content_block.appendChild(_input_footer)

        block_content.appendChild(main_content_block)

        let channel_and_color_row = div("input_block_content")
        channel_and_color_row.appendChild(_input_channel_id)
        channel_and_color_row.appendChild(_input_color)


        _input_text_content.style.marginBottom = "0.5vw"
        _input_text_content.style.width = "100%"
        _input_text_content.style.maxWidth = "100%"
        _input_text_content.style.marginRight = "0"

        data_block.appendChild(channel_and_color_row)


    } else {
        data_block.appendChild(_input_channel_id)

        block_content.appendChild(_input_text_content)

    }
    _input_channel_id.style.width = "59%"

    data_row.appendChild(_input_event_type)
    data_row.appendChild(_remove_button)

    data_block.appendChild(data_row)

    block_content.appendChild(data_block)


    block.appendChild(enable_embed_row)
    block.appendChild(block_content)

    enable_embed_switcher.addEventListener("click", function () {
        let data = embed
        let ___id = enable_embed_switcher.id.split("enable_embed_switcher_")[1]

        if (!embed) {
            data = {
                "author": document.getElementById("_input_author_" + ___id).value,
                "header": document.getElementById("_input_header_" + ___id).value,
                "image_url": document.getElementById("_input_img_url_" + ___id).value,
                "footer_content": document.getElementById("_input_footer_" + ___id).value,
                "color": document.getElementById("_input_color_" + ___id).value
            }

        }

        let new_block = generate_events_block(
            enable_embed_switcher.checked,
            document.getElementById("_input_text_content_" + ___id).value,
            document.getElementById("_input_channel_id_" + ___id).value,
            document.getElementById("_input_event_type_" + ___id).value,
            data
        )

        block.replaceWith(new_block)

    })

    return block
}

function generate_auto_response_block(
    enable_embed = false,
    text_content = "",
    trigger = "",
    event_type = "only",
    embed = {
        "author": "",
        "icon_link": "",
        "header": "",
        "color": "#BEC100",
        "image_url": "",
        "footer_content": ""

    }
) {
    count += 1

    let block = div("auto_response_block", "", "_auto_response_block_" + count)

    let enable_embed_row = div("mini_row")
    let enable_embed_switcher = input("blue_checkbox", "checkbox", "", "enable_embed_switcher_" + count)
    let enable_embed_lbl = p("embed", "command_name_text")

    enable_embed_switcher.checked = enable_embed

    enable_embed_lbl.style.marginLeft = "0.5vw"


    let block_content = div("input_block_content")
    block_content.style.marginTop = "0.7vw"

    let _input_text_content = document.createElement("textarea")
    _input_text_content.classList.add("select_roles")
    _input_text_content.maxLength = 3000
    _input_text_content.style.resize = "none"
    _input_text_content.style.fontSize = "1.2vw"
    _input_text_content.value = text_content
    _input_text_content.style.height = "6vw"
    _input_text_content.style.width = "40%"
    _input_text_content.placeholder = "введите текст сообщения"
    _input_text_content.id = "_input_text_content_" + count


    let data_block = div("data_block")

    let _input_trigger = input("select_roles", "text", "", "_input_trigger_" + count)

    _input_trigger.maxLength = 50
    // _input_channel_id.style.width = "100%"

    let data_row = div("mini_row")
    data_row.style.alignItems = "flex-end"

    let _input_trigger_type = select("select_roles", "_input_trigger_type_" + count)
    const types = [["в начале сообщения", "start"], ["в любом месте сообщения", "inside"], ["только триггер", "only"]]
    for (let i of types) {
        let opt = option(i[0], i[1])
        if (i[1] === event_type) {
            opt.selected = true
        }
        _input_trigger_type.appendChild(opt)
    }

    let _remove_button = button("remove_button", "❌")
    _remove_button.addEventListener("click", function () {
        block.remove()
        update_counter("auto_response_block", auto_response_counter, auto_response_block)


    })


    enable_embed_row.appendChild(enable_embed_switcher)
    enable_embed_row.appendChild(enable_embed_lbl)


    if (enable_embed) {


        let _input_author = input("select_roles", "text")
        _input_author.placeholder = "автор"
        _input_author.style.marginBottom = "0.5vw"
        _input_author.style.marginRight = "0"
        _input_author.style.width = "100%"
        _input_author.style.maxWidth = "100%"
        _input_author.id = "_input_author_" + count
        _input_author.value = embed["author"]

        let _input_header = input("select_roles", "text")
        _input_header.placeholder = "заголовок"
        _input_header.style.marginBottom = "0.5vw"
        _input_header.style.marginRight = "0"
        _input_header.style.width = "100%"
        _input_header.style.maxWidth = "100%"
        _input_header.id = "_input_header_" + count
        _input_header.value = embed["header"]

        let _input_img_url = input("select_roles", "text")
        _input_img_url.placeholder = "ссылка на изображение"
        _input_img_url.style.marginBottom = "0.5vw"
        _input_img_url.style.marginRight = "0"
        _input_img_url.style.width = "100%"
        _input_img_url.style.maxWidth = "100%"
        _input_img_url.id = "_input_img_url_" + count
        _input_img_url.value = embed["image_url"]

        let _input_footer = input("select_roles", "text")
        _input_footer.placeholder = "текст футера"
        // _input_footer.style.marginBottom = "0.5vw"
        _input_footer.style.marginRight = "0"
        _input_footer.style.width = "100%"
        _input_footer.style.maxWidth = "100%"
        _input_footer.id = "_input_footer_" + count
        _input_footer.value = embed["footer_content"]

        let _input_color = input("color_select", "color")
        _input_color.value = embed["color"]
        _input_color.id = "_input_color_" + count

        _input_color.addEventListener("input", function () {
            main_content_block.style.borderLeftColor = _input_color.value
            // console.log("change")
        })

        data_block.appendChild(_input_color)

        let main_content_block = div("main_content_block")

        main_content_block.style.marginLeft = "-0.5vw"
        main_content_block.style.paddingLeft = "0.5vw"

        main_content_block.style.borderLeft = "2px solid " + _input_color.value

        main_content_block.appendChild(_input_author)
        main_content_block.appendChild(_input_header)
        main_content_block.appendChild(_input_text_content)
        main_content_block.appendChild(_input_img_url)
        main_content_block.appendChild(_input_footer)

        block_content.appendChild(main_content_block)

        let channel_and_color_row = div("input_block_content")
        channel_and_color_row.appendChild(_input_trigger)
        channel_and_color_row.appendChild(_input_color)


        _input_text_content.style.marginBottom = "0.5vw"
        _input_text_content.style.width = "100%"
        _input_text_content.style.maxWidth = "100%"
        _input_text_content.style.marginRight = "0"

        data_block.appendChild(channel_and_color_row)


    } else {
        data_block.appendChild(_input_trigger)

        block_content.appendChild(_input_text_content)

    }
    _input_trigger.style.width = "59%"

    data_row.appendChild(_input_trigger_type)
    data_row.appendChild(_remove_button)

    data_block.appendChild(data_row)

    block_content.appendChild(data_block)


    block.appendChild(enable_embed_row)
    block.appendChild(block_content)

    enable_embed_switcher.addEventListener("click", function () {
        let data = embed
        let ___id = enable_embed_switcher.id.split("enable_embed_switcher_")[1]

        if (!embed) {
            data = {
                "author": document.getElementById("_input_author_" + ___id).value,
                "header": document.getElementById("_input_header_" + ___id).value,
                "image_url": document.getElementById("_input_img_url_" + ___id).value,
                "footer_content": document.getElementById("_input_footer_" + ___id).value,
                "color": document.getElementById("_input_color_" + ___id).value
            }

        }

        let new_block = generate_auto_response_block(
            enable_embed_switcher.checked,
            document.getElementById("_input_text_content_" + ___id).value,
            document.getElementById("_input_trigger_" + ___id).value,
            document.getElementById("_input_trigger_type_" + ___id).value,
            data
        )

        block.replaceWith(new_block)

    })

    return block
}

function main() {
    // time_messages_block.appendChild(gene(true))
    // console.log(0)
    // events_block.appendChild(generate_events_block())
    document.getElementById("tm_block_footer").style.visibility = "visible"
    document.getElementById("events_block_footer").style.visibility = "visible"
    document.getElementById("auto_response_block_footer").style.visibility = "visible"


    update_counter("time_message_block", tm_count, time_messages_block)
    update_counter("events_block", events_counter, events_block)
    update_counter("auto_response_block", auto_response_counter, auto_response_block)


    if (Object.keys(configuration_key).length !== 0) {
        // console.log("here")
        // console.log(configuration_key.time_message)
        time_messages_block.innerHTML = ""
        for (let i of Object.keys(configuration_key.time_message)) {
            // console.log(">>", i)

            time_messages_block.appendChild(generate_time_message_block(
                configuration_key.time_message[i]["enable_embed"],
                configuration_key.time_message[i]["content"],
                configuration_key.time_message[i]["channel"],
                configuration_key.time_message[i]["time"],
                configuration_key.time_message[i]["interval"],
                configuration_key.time_message[i]["units_of_measure"],
                configuration_key.time_message[i]["embed"]
            ))
            update_counter("time_message_block", tm_count, time_messages_block)
        }
    }


    if (Object.keys(configuration_key).length !== 0) {
        // console.log("here")
        // console.log(configuration_key.events)
        events_block.innerHTML = ""
        for (let i of Object.keys(configuration_key.events)) {

            events_block.appendChild(generate_events_block(
                configuration_key.events[i]["enable_embed"],
                configuration_key.events[i]["content"],
                configuration_key.events[i]["channel"],
                configuration_key.events[i]["type"],
                configuration_key.events[i]["embed"]
            ))
            update_counter("events_block", events_counter, events_block)

        }
    }


    if (Object.keys(configuration_key).length !== 0) {
        // console.log(configuration_key.auto_response)
        auto_response_block.innerHTML = ""
        for (let i of Object.keys(configuration_key.auto_response)) {

            auto_response_block.appendChild(generate_auto_response_block(
                configuration_key.auto_response[i]["enable_embed"],
                configuration_key.auto_response[i]["content"],
                configuration_key.auto_response[i]["channel"],
                configuration_key.auto_response[i]["trigger"],
                configuration_key.auto_response[i]["trigger_type"],
                configuration_key.auto_response[i]["embed"]
            ))
            update_counter("auto_response_block", auto_response_counter, auto_response_block)


        }
    }

    update_counter("time_message_block", tm_count, time_messages_block)
    update_counter("events_block", events_counter, events_block)
    update_counter("auto_response_block", auto_response_counter, auto_response_block)


}


// console.log(1)
document.getElementById("tm_block_footer").style.visibility = "hidden"
document.getElementById("events_block_footer").style.visibility = "hidden"
document.getElementById("auto_response_block_footer").style.visibility = "hidden"


document.getElementById("add_tm_block").addEventListener("click", function () {
    if (document.getElementsByClassName("time_message_block").length === 0) {
        time_messages_block.innerHTML = ""
        console.log(55555)
    }
    if (get_count("time_message_block") === 5) {
        warning("Достигнут лимит регулярных сообщений")
        return
    }
    time_messages_block.appendChild(generate_time_message_block())
    update_counter("time_message_block", tm_count, time_messages_block)

})
document.getElementById("add_events_block").addEventListener("click", function () {
    if (get_count("events_block") === 0) {
        events_block.innerHTML = ""
        console.log(666666)
    }
    if (get_count("events_block") === 2) {
        warning("Достигнут лимит событий")
        return
    }
    events_block.appendChild(generate_events_block())
    update_counter("events_block", events_counter, events_block)

})


document.getElementById("add_auto_response_block").addEventListener("click", function () {
    if (get_count("auto_response_block") === 0) {
        auto_response_block.innerHTML = ""
        console.log(777777)
    }
    if (get_count("auto_response_block") === 5) {
        warning("Достигнут лимит автоответчиков")
        return
    }
    auto_response_block.appendChild(generate_auto_response_block())
    update_counter("auto_response_block", auto_response_counter, auto_response_block)

})


document.getElementById("save_btn").addEventListener("click", function () {


    let new_data = {
        "time_message": {},
        "events": {},
        "auto_response": {},
    }
    for (let tm of document.getElementsByClassName("time_message_block")) {
        let data = {}
        let embed = {}
        let id = tm.id.split("_time_message_block_")[1]
        let active_embed = document.getElementById("enable_embed_switcher_" + id)

        if (!document.getElementById("_input_channel_id_" + id).value) {
            danger("Введите ID канала в регулярных сообщениях")
            return 0
        }


        if (active_embed.checked) {
            if (!document.getElementById("_input_header_" + id).value) {
                danger("Введите текст заголовка embed в регулярных сообщениях")
                return 0
            }
        }


        if (!document.getElementById("_input_text_content_" + id).value) {
            danger("Введите текст embed в регулярных сообщениях")
            return 0
        }

        embed = active_embed.checked ? {
            "author": document.getElementById("_input_author_" + id).value,
            "header": document.getElementById("_input_header_" + id).value,
            "image_url": document.getElementById("_input_img_url_" + id).value,
            "footer_content": document.getElementById("_input_footer_" + id).value,
            "color": document.getElementById("_input_color_" + id).value
        } : {
            "author": "",
            "header": "",
            "image_url": "",
            "footer_content": "",
            "color": "#BEC100",
        }

        data = {
            "enable_embed": active_embed.checked,
            "content": document.getElementById("_input_text_content_" + id).value,
            "channel": document.getElementById("_input_channel_id_" + id).value,
            "time": document.getElementById("_input_first_time_" + id).value,
            "interval": document.getElementById("_input_interval_" + id).value,
            "units_of_measure": document.getElementById("_input_units_of_measure_" + id).value,
            "embed": embed

        }

        new_data["time_message"][id] = data

    }


    for (let ev of document.getElementsByClassName("events_block")) {
        let data = {}
        let embed = {}
        let id = ev.id.split("_event_block_")[1]
        let active_embed = document.getElementById("enable_embed_switcher_" + id)


        if (!document.getElementById("_input_channel_id_" + id).value) {
            danger("Введите ID канала в событиях")
            return 0
        }


        if (active_embed.checked) {
            if (!document.getElementById("_input_header_" + id).value) {
                danger("Введите текст заголовка embed в событиях")
                return 0
            }
        }

        if (!document.getElementById("_input_text_content_" + id).value) {
            danger("Введите текст embed в событиях")
            return 0
        }

        embed = active_embed.checked ? {
            "author": document.getElementById("_input_author_" + id).value,
            "header": document.getElementById("_input_header_" + id).value,
            "image_url": document.getElementById("_input_img_url_" + id).value,
            "footer_content": document.getElementById("_input_footer_" + id).value,
            "color": document.getElementById("_input_color_" + id).value
        } : {
            "author": "",
            "header": "",
            "image_url": "",
            "footer_content": "",
            "color": "#BEC100",
        }

        data = {
            "enable_embed": active_embed.checked,
            "content": document.getElementById("_input_text_content_" + id).value,
            "channel": document.getElementById("_input_channel_id_" + id).value,
            "type": document.getElementById("_input_event_type_" + id).value,
            "embed": embed

        }

        new_data["events"][id] = data

    }


    for (let ar of document.getElementsByClassName("auto_response_block")) {
        let data = {}
        let embed = {}
        let id = ar.id.split("_auto_response_block_")[1]
        let active_embed = document.getElementById("enable_embed_switcher_" + id)

        if (active_embed.checked) {
            if (!document.getElementById("_input_header_" + id).value) {
                danger("Введите текст заголовка embed в автоответчике")
                return 0
            }
        }

        if (!document.getElementById("_input_text_content_" + id).value) {
            danger("Введите текст embed в автоответчике")
            return 0
        }

        if (!document.getElementById("_input_trigger_" + id).value) {
            danger("Введите триггер в автоответчике")
            return 0
        }

        embed = active_embed.checked ? {
            "author": document.getElementById("_input_author_" + id).value,
            "header": document.getElementById("_input_header_" + id).value,
            "image_url": document.getElementById("_input_img_url_" + id).value,
            "footer_content": document.getElementById("_input_footer_" + id).value,
            "color": document.getElementById("_input_color_" + id).value
        } : {
            "author": "",
            "header": "",
            "image_url": "",
            "footer_content": "",
            "color": "#BEC100",
        }

        data = {
            "enable_embed": active_embed.checked,
            "content": document.getElementById("_input_text_content_" + id).value,
            "trigger": document.getElementById("_input_trigger_" + id).value,
            "trigger_type": document.getElementById("_input_trigger_type_" + id).value,
            "embed": embed

        }

        new_data["auto_response"][id] = data

    }
    reset_message_configuration_key()
    configuration_key = new_data
    console.log(configuration_key)

    const answer = post_data("messages", configuration_key)
    answer.then(a => {
        if (a["status"] === "ok") {
            success()
            return 0
        }
        else {
            danger(a["message"])
            console.log(a, a["message"], 5555555555555555555)
        }
    })


})


document.getElementById("reset_btn").addEventListener("click", function () {
    if (confirm("Вы уверены, что хотите сбросить все изменения?")) {
        reset_message_configuration_key()

        main()
        // update_counter("time_message_block", tm_count, time_messages_block)
        // update_counter("events_block", events_counter, events_block)
        // update_counter("auto_response_block", auto_response_counter, auto_response_block)

        const answer = post_data("messages", configuration_key)
        answer.then(a => {
            if (a["status"] === "ok") {
                warning("изменения сброшены")
                return 0
            }
            danger(a["message"])
        })
    }
})