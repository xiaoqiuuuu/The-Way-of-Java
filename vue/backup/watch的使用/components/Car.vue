<script setup lang="ts" name="Car">
import {reactive, ref, toRef, toRefs, watch} from "vue";

  let car = ref({brand:"奔驰" , price:100000});

  function modifyBrand(){
    car.value.brand = car.value.brand==="奔驰"?"宝马":"奔驰";
  }
  function modifyPrice(){
    car.value.price ++ ;
  }

  function modifyCar(){
    car.value = {brand:"沃尔沃",price:114123};
  }

  // watch(brand,(newValue,oldValue)=>{
  //   console.log("brand变化了",newValue,oldValue);
  // });
  //
  // watch(price,(newValue,oldValue)=>{
  //   console.log("price变化了",newValue,oldValue);
  // });
  // watch(car,(newValue,oldValue)=>{
  //   console.log("car变化了",newValue,oldValue);
  // } , {deep:true});

</script>

<template>
  <div class="car">
    <h1>我是一辆汽车</h1>
    <h1>品牌：{{car.brand}}</h1>
    <h1>价格：{{car.price}}</h1>
    <button @click="modifyBrand">点我修改品牌</button>
    <button @click="modifyPrice">点我修改价格</button>
    <button @click="modifyCar">点我修改汽车</button>
  </div>
</template>

<style scoped>
  .car{
    margin-top: 20px;
    background-color: lightblue;
    box-shadow:0 0 10px rgba(0,0,0,0.5);
    border-radius: 10px;
    padding: 20px;
  }

  button{
    margin: 0 10px;
  }


</style>