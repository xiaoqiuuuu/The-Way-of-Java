<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Person",
  data() {
    return {
      name: "张三",
      age:18,
      tel:18123456789,
      email:"123@qq.com",
      address:"北京市朝阳区"
    }
  },
  methods:{
    modifyName(){
      if (this.name=="张三"){
          this.name="李四";
      } else {
        this.name="张三";
      }
    },
    modifyAge(){
      this.age+=1;
    },
    showTle(){
      alert(this.tel);
    }
  }
})
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