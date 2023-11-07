<template>

  <title>Создайте своего бота для Discord онлайн без единой строчки кода абсолютно бесплатно | SomethinK</title>


  <div class="main-block-content">

    <h1 class="main_text">
      Создайте своего бота для Discord онлайн без единой строчки кода абсолютно бесплатно
    </h1>

    <div class="button-row">
      <div class="line" style="width: 4vw"></div>
      <router-link class="button-start" to="auth" @click="console.log(this.current_user)">создать</router-link>
      <!--            {% if current_user.is_authenticated %}-->
      <!--            <a href="/create/token" v-if="current_user.status === 'unauthorized' class="button-start">начать</a>-->
      <!--            {% else %}-->
      <!--            <a href="/auth" class="button-start">создать</a>-->
      <!--            {% endif %}-->

      <a class="button-more" id="view_more_button" @click="scroll_to_about_block()">подробнее</a>


    </div>


  </div>

  <section class="section" style="margin-top: 10vw" id="about_section">
    <div class="section_header">
      <div class="line" style="width: 30vw"></div>
      <div class="section_name">немного о SomethinK</div>
      <div class="line" style="width: 15vw"></div>

    </div>

    <div class="section_data" style="width: 65vw; border-right: 1px #52565F solid">
      <p class="section_text">
        SomethinK - это веб-фреймворк, с удобным и понятным интерфейсом,
        разработанный специально для создания Discord ботов.
      </p>
    </div>
  </section>

  <section class="section_center">

    <div class="section_header">
      <div class="line" style="width: 42.5vw; border-bottom:#23272A "></div>
      <div class="section_name">возможности</div>

      <div class="line" style="width: 8.5vw"></div>
    </div>

    <div class="section_body">
      <div class="section_description">
        <p>Используйте любые комбинации команд, для создания своего бота!</p>
      </div>

      <div class="icons_block">
        <div class="icons_row">
          <div class="icon_block">
            <img class="icon_image" alt="icon" src="./../assets/mainPageImages/icon_moder.svg">
            <p class="icon_header">модерация</p>
            <p class="icon_text">базовый набор команд, позволяющий управлять вашим сервером
            </p>
          </div>
          <div class="icon_block">
            <img class="icon_image" alt="icon" src="./../assets/mainPageImages/icon_messages.svg">
            <p class="icon_header">анонсы</p>
            <p class="icon_text">автоматическое оповещение о событиях на сервере или вне него
            </p>
          </div>
          <div class="icon_block">
            <img class="icon_image" alt="icon" src="./../assets/mainPageImages/icon_autorole.svg">
            <p class="icon_header">авто-роль</p>
            <p class="icon_text">автоматическая выдача роли, когда к серверу присоединяется новый участник

            </p>
          </div>
          <div class="icon_block">
            <img class="icon_image" alt="icon" src="./../assets/mainPageImages/icon_automod.svg">
            <p class="icon_header">авто-модерация</p>
            <p class="icon_text">автоматическая модерация вашего сервера
            </p>
          </div>
        </div>
        <div class="icons_row">
          <div class="icon_block">
            <img class="icon_image" alt="icon" src="./../assets/mainPageImages/icon_color.svg">
            <p class="icon_header">цвета</p>
            <p class="icon_text">позволяет участникам выбрать цвет никнейма на сервере</p>
          </div>
          <div class="icon_block">
            <img class="icon_image" alt="icon" src="./../assets/mainPageImages/icon_joke.svg">
            <p class="icon_header">шутки</p>
            <p class="icon_text">случайная шутка от бота
            </p>
          </div>
          <div class="icon_block">
            <img class="icon_image" alt="icon" src="./../assets/mainPageImages/icon_translate.svg">
            <p class="icon_header">переводчик</p>
            <p class="icon_text">перевод слов или предложений с восьми разных языков

            </p>
          </div>
          <div class="icon_block">
            <img class="icon_image" alt="icon" src="./../assets/mainPageImages/icon_gpt.svg">
            <p class="icon_header">chatGPT</p>
            <p class="icon_text">общайтесь с chatGPT прямо со своего сервера дискорд
            </p>
          </div>
        </div>
      </div>

    </div>

  </section>


  <section class="section_center" style="margin-top: 7vw">
    <div class="section_header">
      <div class="line" style="width: 30vw"></div>
      <div class="section_name">интеграция с социальными сетями</div>


    </div>

    <div class="section_row_body">
      <div class="icon_block">
        <img class="icon_image" alt="icon" src="./../assets/mainPageImages/icon_youtube.svg">
        <p class="icon_header">ютуб</p>
        <p class="icon_text">Получайте уведомления, с ютуб каналов о новых видео </p>
      </div>
      <div class="icon_block">
        <img class="icon_image" alt="icon" src="./../assets/mainPageImages/icon_twitch.svg">
        <p class="icon_header">твич</p>
        <p class="icon_text">Настройте уведомления о стримах, чтобы участники сервера никогда не пропускали ваши
          трансляции
        </p>
      </div>
      <p class="section_text" style="max-width: 40vw">
        Добавляет ссылки на каналы любимых авторов, чтобы получать уведомления о новых публикациях
      </p>
    </div>

  </section>

  <section class="section_center" style="margin-top: 7vw; margin-bottom: 5vw">
    <div class="section_header">
      <div class="line" style="width: 22vw"></div>
      <div class="section_name">часто задаваемые вопросы</div>

    </div>

    <div class="questions">
      <div class="question_block">
        <p class="question_header_text">“Сколько времени займет сборка бота?”</p>
        <p class="icon_text">Предположительное время создания от 10 до 25 минут.</p>
      </div>

      <div class="question_block">
        <p class="question_header_text">“Что я получу после создания бота?”</p>
        <p class="icon_text">Вы получите архив, с готовым кодом и инструкцией по установке бота на хостинг.</p>
      </div>

      <div class="question_block">
        <p class="question_header_text">“На каком языке будет написан бот?”</p>
        <p class="icon_text">Проект будет написан на языке программирования Python с использованием библиотеки
          Disnake.</p>
      </div>

      <div class="question_block">
        <p class="question_header_text">“Есть ли на сайте платный функционал?”</p>
        <p class="icon_text">Нет, наш сайт полностью бесплатный для всех пользователей. Однако, если вы хотите
          поддержать проект и помочь нам развиваться, вы можете воспользоваться <a
              href="https://www.donationalerts.com/r/somethinkbots"
              style="color: #4A74C6; text-decoration: none" target="_blank">ссылкой</a>.</p>
      </div>
    </div>


  </section>

  <!--    <script>-->
  <!--      const button = document.getElementById('view_more_button');-->

  <!--      button.addEventListener('click', function () {-->

  <!--      });-->

  <!--    </script>-->
  <!--  <script>-->
  <!--    document.getElementById("github_url").addEventListener("click", () => {-->
  <!--      const url = document.createElement("a")-->
  <!--      url.href = "https://github.com/pavelglazunov/SomethinK"-->
  <!--      url.target = "_blank"-->
  <!--      url.click()-->
  <!--    })-->
  <!--  </script>-->

</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      current_user: {
        'status': 'response'
      }
    }
  },
  async mounted() {
    await fetch('http://127.0.0.1:8080/api/get_current_user')
        .then(response => {
          return response.json();
        })
        .then(data => {
          this.current_user = data.target;
          // console.log(this.current_user)
        })
        .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
        });
  },
  methods: {
    scroll_to_about_block() {

      const targetElement = document.getElementById('about_section');
      const targetPosition = targetElement.offsetTop;
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }
  }

}
</script>

<style src="./../assets/css/index.css"></style>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!--<style scoped>-->
