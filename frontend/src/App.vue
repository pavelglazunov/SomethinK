<template>
  <base_header></base_header>
  <router-view></router-view>
</template>

<script>

import base_header from "@/components/BaseHeader";

export default {
  name: 'App',
  components: {base_header}
}
</script>

<style src="./assets/css/main.css"></style>
<style>

/*#app {*/
/*  font-family: Avenir, Helvetica, Arial, sans-serif;*/
/*  -webkit-font-smoothing: antialiased;*/
/*  -moz-osx-font-smoothing: grayscale;*/
/*  text-align: center;*/
/*  color: #2c3e50;*/
/*  margin-top: 60px;*/
/*}*/

</style>
