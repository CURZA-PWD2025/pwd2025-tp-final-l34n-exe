<template>
  <div>
    <h1>Empleados</h1>
    <RouterView></RouterView>

  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { onMounted } from 'vue';
const route = useRouter()

onMounted(()=>{
  route.push({name:'empleados_list'})
})
</script>

<style scoped>

</style>
