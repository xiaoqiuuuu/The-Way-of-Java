<script lang="ts">
  import Person from "./components/Person.vue";
  import Car from "./components/Car.vue";

  export default {
    name: 'App',
    components:{Person,Car}
  }
</script>

<template>
  <div class="app">
    <h1>你好呀，我的第一个vue界面!</h1>
    <Person/>
    <Car/>


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