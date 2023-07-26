update_chapter(8)

const letters = "qwertyuiopasdfghjklzxcvbnm_"

function main() {

    // document.getElementById("_input_project_name").addEventListener("input", function () {
    //
    // })

    document.getElementById("save_btn").addEventListener("click", function () {
        let value = document.getElementById("_input_project_name").value

        if (!value) {
            warning("Необходимо указать имя проекта")
            return 0
        }
        if (value.length > 15) {
            warning("Превышена длина имени проекта")
            return 0
        }

        for (let i of value) {
            if (letters.indexOf(i.toLowerCase()) === -1) {
                warning("Имя проекта может содержать только английские буквы и знак _")
                return 0
            }
        }
        const answer = start_creating(value)
        answer.then(a => {
            if (a["status"] === "ok") {
                successText("Поехали!")
                return 0
            }
            danger(a["message"])
        })
    })
}

main()