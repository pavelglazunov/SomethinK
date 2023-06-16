// optimize code in this file


function swap(id, status) {
    console.log(id, status)
    status ? document.getElementById("__tm_inputs_block_" + id).classList.add("visible") : document.getElementById("__tm_inputs_block_" + id).classList.remove("visible")
    status ? document.getElementById("__tm_embed_inputs_block_" + id).classList.remove("visible") : document.getElementById("__tm_embed_inputs_block_" + id).classList.add("visible")
}

class MessagesForm {
    constructor(discord_auth, content_id, channels) {
        this.discord_auth = discord_auth
        this.content_id = content_id
        this.counter = 0
        this.channels = channels
    }


    _timeMessageDataBlock(id, add_color = false) {
        let time_message_data_block = document.createElement("div")
        time_message_data_block.classList.add("input_time_message_data_block")

        let channel_id = document.createElement(discord_auth ? "select" : "input")

        channel_id.classList.add("select_roles")
        channel_id.classList.add("___widht_control")
        channel_id.classList.add("___noMargin")
        channel_id.placeholder = "Введите ID канала"
        if (this.discord_auth) {
            for (let i = 0; i < this.channels.length; i++) {
                let opt = document.createElement("option")
                opt.text = this.channels[i][1]
                opt.value = this.channels[i][0]

                channel_id.appendChild(opt)

            }
        }

        if (add_color) {
            let color_and_channels = document.createElement("div")
            color_and_channels.classList.add("color_and_channels")

            let _color = document.createElement("input")
            _color.type = "color"
            _color.classList.add("color_select")
            _color.value = "#FFF200"
            _color.addEventListener("change", function () {
                console.log(_color.value)
            })
            color_and_channels.appendChild(_color)
            color_and_channels.appendChild(channel_id)

            time_message_data_block.appendChild(color_and_channels)


        }

        else {
            time_message_data_block.appendChild(channel_id)

        }




        // ===========================================================
        // ===========================================================
        // ===========================================================

        let __data_block = document.createElement("div")
        __data_block.classList.add("data_block")

        let data_time_block = document.createElement("div")
        let _input_time = document.createElement("input")
        let _text_time = document.createElement("p")
        _text_time.classList.add("data_text")
        _text_time.textContent = "время отправки"

        _input_time.type = "time"
        _input_time.classList.add("select_roles")
        _input_time.classList.add("___noMargin")
        

        data_time_block.classList.add("colon")
        data_time_block.classList.add("time_input")
        data_time_block.appendChild(_text_time)
        data_time_block.appendChild(_input_time)


        // -----------------------------------------------------------------------


        let data_interval_block = document.createElement("div")
        let _text_interval = document.createElement("p")
        let _input_interval = document.createElement("input")
        _text_interval.classList.add("data_text")
        _text_interval.textContent = "интервал"

        _input_interval.type = "text"
        _input_interval.classList.add("select_roles")
        _input_interval.classList.add("___noMargin")
        
        _input_interval.value = "24"

        data_interval_block.classList.add("colon")
        data_interval_block.classList.add("interval_input")
        data_interval_block.appendChild(_text_interval)
        data_interval_block.appendChild(_input_interval)

        // -----------------------------------------------------------------------

        let data_units_block = document.createElement("div")
        let _text_units = document.createElement("p")
        let _input_units = document.createElement("select")
        _text_units.classList.add("data_text")
        _text_units.textContent = "единицы измерения"

        _input_units.classList.add("select_roles")
         _input_units.classList.add("___noMargin")
        
        let params = [["minutes", "минуты"], ["hours", "часы"], ["days", "дни"], ["weeks", "недели"], ["months", "месяцы"]]
        for (let i in params) {
            console.log(i)
            let opt = document.createElement("option")
            opt.value = params[i][0]
            opt.text = params[i][1]

            _input_units.appendChild(opt)
        }

        data_units_block.classList.add("colon")
        data_units_block.classList.add("time_units")
        data_units_block.appendChild(_text_units)
        data_units_block.appendChild(_input_units)

        // -----------------------------------------------------------------------

        let data_rm_block = document.createElement("div")
        data_rm_block.id = "__tm_rm_block_" + id
        data_rm_block.textContent = "❌"
        data_rm_block.classList.add("rm_block")
        data_rm_block.classList.add("data_text")
        data_rm_block.addEventListener("click", function () {
            if (confirm("Удалить данное сообщение по времени?")) {
                document.getElementById("__time_message_block_" + id).remove()
            }
        })


        __data_block.appendChild(data_time_block)
        __data_block.appendChild(data_interval_block)
        __data_block.appendChild(data_units_block)
        __data_block.appendChild(data_rm_block)

        time_message_data_block.appendChild(__data_block)

        return time_message_data_block
    }
    
    timeMessageBase(id) {
        // MAIN BLOCK (need ID)
        let block = document.createElement("div")
        block.id = "__time_message_block_" + id
        block.classList.add("block")


        let swap_row = document.createElement("div")
        swap_row.classList.add("swap_row")


        let base_text = document.createElement("p")
        base_text.classList.add("___noMargin")
        base_text.textContent = "обычный"

        let embed_text = document.createElement("p")
        embed_text.classList.add("base_embed_text")
        embed_text.textContent = "embed"

        

        let swap_checkbox = document.createElement("input")
        swap_checkbox.type = "checkbox"
        swap_checkbox.classList.add("active_checkbox")
        swap_checkbox.classList.add("___noMargin")
        swap_checkbox.id = "swap_checkbox_id_" + block.id.split("__time_message_block_")[1]
        swap_checkbox.addEventListener("click", function () {
            swap(id, swap_checkbox.checked)
        })
        console.log("hereeeee");
        // swap_checkbox.onclick(this._swap(id))
        swap_row.appendChild(base_text)
        swap_row.appendChild(swap_checkbox)
        swap_row.appendChild(embed_text)

        block.appendChild(swap_row)

        let __tm_inputs_block = document.createElement("div")
        __tm_inputs_block.classList.add("base_input__base_block")
        __tm_inputs_block.id = "__tm_inputs_block_" + block.id.split("__time_message_block_")[1]

        let input_text_block_div = document.createElement("div")
        input_text_block_div.classList.add("input_text_block")


        let main_text = document.createElement("input")
        main_text.type = "text"
        main_text.placeholder = "Введите текст сообщения"
        main_text.classList.add("embed_fields")
        main_text.classList.add("___h100")
        // main_text.classList.add("input_text")
        main_text.classList.add("___noMargin")


        input_text_block_div.appendChild(main_text)
        __tm_inputs_block.appendChild(input_text_block_div)
        __tm_inputs_block.appendChild(this._timeMessageDataBlock(id))

        block.appendChild(__tm_inputs_block)
        block.appendChild(this.timeMessageEmbed(id))
        document.getElementById(this.content_id).appendChild(block)
    }

    timeMessageEmbed(id) {

        let __tm_embed_inputs_block = document.createElement("div")
        __tm_embed_inputs_block.id = "__tm_embed_inputs_block_" + id
        __tm_embed_inputs_block.classList.add("base_input__base_block")
        __tm_embed_inputs_block.classList.add("visible")


        let embed_texts_data = document.createElement("div")
        embed_texts_data.classList.add("input_text_block")
        embed_texts_data.id = "__tm_embed_inputs_text_block_" + id


        let input_first_line = document.createElement("div")
        input_first_line.classList.add("first_line_embed")

        let _author = document.createElement("input")
        _author.classList.add("embed_fields")
        _author.classList.add("half")
        _author.placeholder = "автор"

        let _author_url = document.createElement("input")
        _author_url.classList.add("embed_fields")
        _author_url.classList.add("half")
        _author_url.placeholder = "ссылка на иконку"

        input_first_line.appendChild(_author)
        input_first_line.appendChild(_author_url)

        let _header = document.createElement("input")
        _header.classList.add("embed_fields")
        _header.classList.add("___margin_0-5")
        _header.placeholder = "заголовок"

        let _text = document.createElement("input")
        _text.classList.add("embed_fields")
        _text.classList.add("___margin_0-5")
        _text.classList.add("input_text")
        _text.placeholder = "текст (обязательно для заполнения)"

        let _img_url = document.createElement("input")
        _img_url.classList.add("embed_fields")
        _img_url.classList.add("___margin_0-5")
        _img_url.placeholder = "ссылка на изображение"

        let _footer = document.createElement("input")
        _footer.classList.add("embed_fields")
        _footer.classList.add("___margin_0-5")
        _footer.placeholder = "текст футера"

        embed_texts_data.appendChild(input_first_line)
        embed_texts_data.appendChild(_header)
        embed_texts_data.appendChild(_text)
        embed_texts_data.appendChild(_img_url)
        embed_texts_data.appendChild(_footer)

        // write function to create html div with given class


        __tm_embed_inputs_block.appendChild(embed_texts_data)


        // let __ = this._timeMessageDataBlock(id)
        // __.insertBefore()
        // __tm_embed_inputs_block.appendChild(_color)
        __tm_embed_inputs_block.appendChild(this._timeMessageDataBlock(id, true))


        return __tm_embed_inputs_block
    }


}