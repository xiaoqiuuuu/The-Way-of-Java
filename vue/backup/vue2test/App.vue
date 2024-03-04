<script lang="ts">
  import Person from "./components/Person.vue";

  export default {
    name: 'App',
    components:{Person}
  }
</script>

<template>
  <div class="app">
    <h1>你好呀，我的第一个vue界面!</h1>
    <Person/>
  </div>
</template>


<style>
  .app {
    background-color: #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    padding: 20px;
  }
</style>