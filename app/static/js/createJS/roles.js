update_chapter(3)


async function api_post_key(data) {
    const response = await fetch("../api/save", {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
            "config_name": "roles"
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(Object.fromEntries(data))


    })
    return await response.json()
}


const roles_content = document.getElementById("roles_content")
roles_content.style.minWidth = "40vw"

function updateAR(value) {
    for (let i of Object.keys(ACTIVITY_ROLES_COLORS)) {
        // console.log(i)


        let _color = document.getElementById("color_" + i)
        let _cb = document.getElementById("cb_" + i)
        let _lbl = document.getElementById("lbl_" + i)

        _color.disabled = !value
        _cb.disabled = !value

        _color.style.filter = !value ? "grayscale(50%)" : "grayscale(0)"
        _cb.style.filter = !value ? "grayscale(50%)" : "grayscale(0)"
        _lbl.style.color = !value ? "#aba9a9" : "#dedede"


    }
    let _interval = document.getElementById("input_interval")
    let _interval_lbl = document.getElementById("interval_lbl")
    let _interval_lbl_m = document.getElementById("interval_lbl_minutes")

    _interval.disabled = !value
    _interval.style.filter = !value ? "grayscale(50%)" : "grayscale(0)"

    _interval_lbl.style.color = !value ? "#aba9a9" : "#dedede"
    _interval_lbl_m.style.color = !value ? "#aba9a9" : "#dedede"

}

function create_activity_roles_element(el_name, title) {
    let active_roles_row = div("active_roles_row", el_name)
    let color_select = input("color_select", "color", "role_color", "color_" + el_name)
    let role_add_cb = input("blue_checkbox", "checkbox", "role_cb", "cb_" + el_name)
    let lbl = p(title, "configurator_inputs_text", "lbl_" + el_name)

    color_select.value = configuration_key[el_name]["value"]
    role_add_cb.checked = configuration_key[el_name]["enable"]

    role_add_cb.addEventListener("click", function () {
        configuration_key[el_name]["enable"] = role_add_cb.checked
    })

    color_select.addEventListener("change", function () {
        console.log(color_select.value)
        configuration_key[el_name]["value"] = color_select.value

    })
    // color_select.disabled = !configuration_key["ar_enable"]
    // role_add_cb.disabled = !configuration_key["ar_enable"]

    lbl.style.color = "#CDCDCD"
    color_select.style.height = "1.7vw"
    // console.log(el_name, ACTIVITY_ROLES_COLORS[el_name])

    active_roles_row.appendChild(color_select)
    active_roles_row.appendChild(role_add_cb)
    active_roles_row.appendChild(lbl)


    return active_roles_row
}

function save_command() {
    console.log("saving")
}


function reset_configuration_key() {
    // console.log(5)
    configuration_key["start_roles"] = {
        "roles": []
    }
    // configuration_key["start_roles"]["roles"] = []

    for (let _r of ACTIVITY_ROLES) {
        for (let r of _r) {
            r = r.replace(" ", "").replace(":", "").replace(" ", "").toLowerCase()
            // console.log(r)

            configuration_key[r] = {
                "enable": false,
                "value": "#" + ACTIVITY_ROLES_COLORS[r]
            }
            // configuration_key[r.toLocaleLowerCase()]
        }
    }
    configuration_key["update_interval"] = 5
    configuration_key["ar_enable"] = false

    // configuration_key["ar_update"] = {
    //     "enable": true,
    //     "description": "включить/выключить обновление ролей активности",
    //     "roles": [],
    //     "channels": []
    // }

}

function displayLoading() {
    loader.classList.add("display");
    // to stop loading after some time
    setTimeout(() => {
        loader.classList.remove("display");
    }, 5000);
}

// hiding loading
function hideLoading() {
    loader.remove()
}

let login_discord = null
let user_roles = []
const loader = document.getElementById("loading");
let user_channels = {}

let configuration_key = {}
displayLoading()
fetch('/api/all', {
    method: "GET",
    headers: {
        "configuration_name": "roles"
    }
})
    .then((response) => response.json())
    .then((data) => {
        login_discord = data["auth_with_discord"]
        user_roles = data["roles"]
        console.log(login_discord, "login discord")

        user_channels = data["channels"]

        configuration_key = data["configuration_key"]

        console.log(">>", configuration_key)
        console.log(">>", typeof configuration_key)


        if (Object.keys(configuration_key).length === 0) {
            console.log(55555)
            configuration_key = {}
            reset_configuration_key()
        }
        else {
            configuration_key = JSON.parse(configuration_key)

        }

        console.log(configuration_key)

        hideLoading()

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

// let configuration_key = get_configuration_key("roles")
// console.log(configuration_key)
// reset_configuration_key()

// console.log(configuration_key)


function main() {
    roles_content.appendChild(create_roles_input_block(
        "start_roles", configuration_key,
        login_discord, "роли, которые будут выданы при первом заходе на сервер"
    ))

    let activity_roles_row = div("mini_row")
    let activity_role_switcher = input("active_checkbox", "checkbox")

    activity_role_switcher.checked = configuration_key["ar_enable"]
    activity_role_switcher.addEventListener("click", function () {
        updateAR(activity_role_switcher.checked)
        configuration_key["ar_enable"] = activity_role_switcher.checked
    })

    activity_roles_row.appendChild(p("роли активности", "configurator_inputs_text"))
    activity_roles_row.appendChild(activity_role_switcher)

    activity_roles_row.style.padding = "0 2vw"
    activity_roles_row.style.marginTop = "2vw"

    roles_content.appendChild(activity_roles_row)


    let activity_roles_block = div("active_roles_block")

    activity_roles_block.style.padding = "0 2.5vw"
    activity_roles_block.style.marginTop = "1vw"

    for (let i of ACTIVITY_ROLES) {
        let _ar_row = div("row")
        _ar_row.style.marginTop = "0"
        for (let j of i) {

            let _ar_name = j.replace(" ", "").replace(":", "").replace(" ", "").toLowerCase()
            _ar_row.appendChild(create_activity_roles_element(_ar_name, j))

        }
        activity_roles_block.appendChild(_ar_row)

    }


    let interval_row = div("row")
    interval_row.appendChild(p("интервал обновления ролей:", "configurator_inputs_text", "interval_lbl"))
    let input_interval_form = input("select_roles", "text", "", "input_interval")
    input_interval_form.style.width = "2vw"
    input_interval_form.style.height = "1.5vw"
    input_interval_form.style.margin = "0 1vw"
    input_interval_form.style.filter = "none"
    input_interval_form.style.textAlign = "center"

    input_interval_form.value = configuration_key["update_interval"]

    interval_row.appendChild(input_interval_form)
    interval_row.appendChild(p("минут", "configurator_inputs_text", "interval_lbl_minutes"))
    interval_row.style.justifyContent = "flex-start"
    interval_row.style.alignItems = "center"
    // interval_row.appendChild(input("интервал обновления ролей:", "configurator_inputs_text"))
    activity_roles_block.appendChild(interval_row)

    roles_content.appendChild(activity_roles_block)

    updateAR(configuration_key["ar_enable"])

    // let ar_command_block = create_command_block(
    //     configuration_key,
    //     "configurator",
    //     base_save_settings,
    //     "ar_update",
    //     {
    //         "slash": true,
    //         "settings": true,
    //         "automod": "",
    //         "remove_after_close": true,
    //         "parent_id": "configurator_parent",
    //         "fontsize": "1.1vw"
    //     }
    // )
    //
    // ar_command_block.style.marginTop = "2vw"
    // ar_command_block.style.paddingRight = "3vw"
    //
    //
    // roles_content.appendChild(ar_command_block)
}


document.getElementById("save_btn").addEventListener("click", function () {
    // console.log(configuration_key)
    // base_save_settings(configuration_key)

    let roles_list = []
    for (let role of document.getElementsByClassName("added_roles_block")) {
        // console.log(i.getAttribute("role_name"), i.getAttribute("role_name"))
        roles_list.push([role.getAttribute("role_name"), role.getAttribute("role_data")])
    }
    configuration_key["start_roles"]["roles"] = roles_list
    configuration_key["update_interval"] = document.getElementById("input_interval").value
    // console.log(configuration_key)
    //
    // console.log(typeof configuration_key)
    // console.log(JSON.stringify(configuration_key))
    const answer = post_data("roles", configuration_key)
    answer.then(a => {
        if (a["status"] === "ok") {
            success()
            return 0
        }
        danger(a["message"])
    })



})

// reset_configuration_key()


// document.getElementById("roles_input_form").style.w