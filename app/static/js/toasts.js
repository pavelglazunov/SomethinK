// import HELP_URL from "./constants"

function _toast_call(text, theme) {
    new Toast({
        title: false,
        text: text,
        theme: theme,
        autohide: true,
        interval: parseInt("3000")
    })
}

function warning(text) {
    _toast_call(text, "warning")
}
function success() {
    _toast_call("изменения сохранены", "success")
}
function successText(text) {
    _toast_call(text, "success")
}
function danger(text) {
    _toast_call(text, "danger")
}

