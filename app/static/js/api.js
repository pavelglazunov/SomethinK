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
    try {
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
            body: JSON.stringify({ project_name: project_name }),
        });

        if (response.status === 429) {
            danger("Слишком много запросов в минуту");
            return;
        }

        // Получаем ответ в виде blob-объекта
        const blob = await response.blob();

        if (blob.type === "application/json") {
            // Если ответ в виде JSON
            const json = await blob.text();
            const data = JSON.parse(json);

            if (data.status !== "ok") {
                // Если статус не 'ok' - показываем ошибку
                danger(data.message);
                return 0;
            }
        } else {
            // Если ответ не в виде JSON - скачиваем файл
            const url = URL.createObjectURL(blob);

            // Создаем ссылку для скачивания файла
            const link = document.createElement("a");
            link.href = url;
            link.download = project_name + ".zip"; // Указываем имя файла
            document.body.appendChild(link);

            // Кликаем по ссылке для скачивания файла
            link.click();

            // Удаляем ссылку
            document.body.removeChild(link);

            // Освобождаем ресурсы
            URL.revokeObjectURL(url);
        }
    } catch (error) {
        danger("Произошла ошибка: " + error.message);
    }
}
