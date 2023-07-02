async function api_all() {
    let login_discord
    let user_roles
    let user_channels
    let status

    fetch('/api/all').then(response => response.json())
        .then(json => {
            login_discord = json["auth_with_discord"]
            user_roles = json["roles"]
            user_channels = json["channels"]
            status = json["user_bot_token"]
        })
    console.log("IAM HERE")
    return {
        "login_discord": login_discord,
        "user_roles": user_roles,
        "user_channels": user_channels,
        "status": status
    }
    // return await response.json()
}

async function post_data(type, data) {
    const response = await fetch("../api/save", {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
            "configuration_name": type
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data)


    })
    if (response.status === 429) {
        danger("Слишком много запросов в минуту")
        return
    }
    return await response.json()
}

async function start_creating(project_name) {
    const response = await fetch("../api/start_creating", {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify({"project_name": project_name})


    })
    if (response.status === 429) {
        danger("Слишком много запросов в минуту")
        return
    }
    return await response.json()
}

async function api_submit_token() {
    let response = await fetch("/api/")
}
