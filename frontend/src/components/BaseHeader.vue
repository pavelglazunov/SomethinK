<template>
  <div class="header">
    <div>
<!--      {% if current_user.is_authenticated %}-->
<!--      <a class="header-text header_text_border_right" href="/user/{{ current_user.id }}">{{ current_user.name-->
<!--        }}</a>-->
<!--      {% else %}-->
<!--      <a class="header-text header_text_border_right" href="/auth">войти</a>-->
<!--      {% endif %}-->
    </div>

    <div class="header_right_texts">
      <a class="header-text header_text_border_left" href="https://www.donationalerts.com/r/somethinkbots"
         target="_blank">Поддержать проект</a>
      <a class="header-text header_text_border_left" href="https://t.me/SomethinKsupportBot" target="_blank">Техподдержка</a>
      <a class="header-text header_text_border_left" style="color: #00FC0A" href="/">SomethinK</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "base_header"
}
</script>

<style scoped>

</style>