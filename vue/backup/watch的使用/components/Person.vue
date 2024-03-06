<script setup lang="ts" name="Person">
  import {ref} from "vue";

  let name = ref('张三');
  let age = ref(18);
  let email = "2365164682@qq.com";
  let address = "上海市杨浦区军工路516";
  let tel = '18888888888';

  function modifyName() {
    name.value === '张三' ? name.value = '李四' : name.value = '张三';
  }
  function modifyAge() {
    age.value++;
  }

  function showTle() {
    alert(tel);
  }

</script>


<template>
  <div class="person">
    <h1>姓名：{{name}}</h1>
    <h1>年龄：{{age}}</h1>
    <h1>邮箱：{{email}}</h1>
    <h1>地址：{{address}}</h1>
    <button @click="modifyName">修改姓名</button>
    <button @click="modifyAge">修改年龄</button>
    <button @click="showTle">点击查看电话</button>
  </div>

</template>

<style scoped>
  .person{
    background-color: skyblue;
    box-shadow:0 0 10px rgba(0,0,0,0.5);
    border-radius: 10px;
    padding: 20px;
  }

  button{
    margin: 0 10px;
  }


</style>