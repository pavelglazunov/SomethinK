<template>
  <title>Выберите способ авторизации</title>

  <h1 class="main_header">выберите способ авторизации</h1>
  <div class="content">
    <div class="auth_block">
      <div class="block_header">Discord</div>
      <div class="block_content">
        <p class="block_text">При данном способе входа, сайт получит доступ к вашим серверам и сможет автоматически
          заполнять ID каналов и ролей</p>
        <img class="block_image" src="../assets/images/auth/icons8-discord-96.svg">
      </div>
      <a class="auth_button" :href="this.discord_url">Войти</a>

    </div>
    <div class="auth_block">
      <div class="block_header">Почта</div>
      <div class="block_content">
        <p class="block_text">При данном способе входа, сайт не сможет получить доступ к вашим серверам поэтому Вам
          придется переносить ID каналов и ролей вручную <br>PS это очень просто)</p>
        <img class="block_image" src="../assets/images/auth/icons8-mail-96.svg">
      </div>
      <a class="auth_button" href="/auth/login">Войти</a>
    </div>
  </div>


</template>

<script>
export default {
  name: "AuthPage",
  data() {
    return {
      redirect_url: "https://",
      discord_url: "auth"
    }
  },
  async created() {
    const resp = await fetch(`http://${process.env.VUE_APP_SERVER_IP}:${process.env.VUE_APP_SERVER_PORT}/api/discord_url`)
    const respJson = await resp.json()

    this.discord_url = respJson["url"]
    // console.log(respJson)



  }
}
</script>

<style src="./../assets/css/auth/auth.css"></style>
<style src="./../assets/css/auth/select_auth_type.css"></style>