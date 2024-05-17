<template>
  <div class="container">
    <column-list :list="list"></column-list>

  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue"
import 'bootstrap/dist/css/bootstrap.min.css';
import ColumnList , {ColumnProps} from "./components/ColumnList.vue";

const testData: ColumnProps[] = [
  {
    id: 1,
    title: 'test1专栏',
    description: 'test1专栏描述',
    avatar: 'https://picsum.photos/id/237/200/300',
  },
  {
    id: 2,
    title: 'test2专栏',
    description: 'test2专栏描述',
    avatar: 'https://picsum.photos/id/237/200/300',
  }
]

export default defineComponent({
  name: 'App',
  components: {
    ColumnList
  },
  setup() {
    return {
      list: testData
    }
  }
})


</script>


<style>


</style>
