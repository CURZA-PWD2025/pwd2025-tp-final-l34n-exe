<template>
  <div>
    <h1>Productos</h1>
    <RouterView></RouterView>

  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { onMounted } from 'vue';
const route = useRouter()

onMounted(()=>{
  route.push({name:'productos_list'})
})
</script>

<style scoped>

</style>
