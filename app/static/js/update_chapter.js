function update_chapter(num) {

    let all_chapter = document.getElementsByClassName("select_chapter_menu")
    for (let i of all_chapter) {
        i.classList.remove("active_chapter")

    }
    all_chapter[num].classList.add("active_chapter")
}