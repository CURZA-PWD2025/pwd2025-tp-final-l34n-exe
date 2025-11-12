<template>
  <div>
    <h1>SaboresShow</h1>
    <div>
      <h3>ID: {{ sabor.id }}</h3>
      <h3>NOMBRE: {{ sabor.nombre }}</h3>
      <h3>STOCK: {{ sabor.stock }}</h3>
      <h3>CATEGORIA: {{ sabor.categoria?.nombre }}</h3>
      <h3>DISPONIBLE: {{ sabor.disponible ? 'Sí' : 'No' }}</h3>
      <RouterLink :to="{ name: 'sabores_list' }">VOLVER</RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useSaboresStore from '@/stores/sabores'

const store = useSaboresStore()
const { sabor } = toRefs(store)
const { getOne } = store
const route = useRoute()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})
</script>

<style scoped></style>
