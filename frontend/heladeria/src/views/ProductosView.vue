<template>
  <div>
    <h1>Productos</h1>
    <button @click="volverAlInicio">VOLVER AL INICIO</button>
    <RouterView></RouterView>

  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
const router = useRouter()

const volverAlInicio = () => {
  router.push({name:'HomeView'})
}

</script>

<style scoped>

</style>
