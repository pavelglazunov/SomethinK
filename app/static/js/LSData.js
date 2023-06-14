function SaveDateToLocalStorage(key, value) {
    console.log(value)
    localStorage.setItem(key, JSON.stringify(value))
}

function get_configuration_key(key) {
    console.log(key)
    let cfg_key = {}
    if (localStorage.getItem(key)) {
        cfg_key = JSON.parse(localStorage.getItem(key))
    }
    return cfg_key
}