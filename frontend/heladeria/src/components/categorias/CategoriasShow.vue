<template>
  <div>
    <h1>CategoriasShow</h1>
    <div>
      <h3>ID: {{ categoria.id }}</h3>
      <h3>NOMBRE: {{ categoria.nombre }}</h3>
      <h3>TIPO: {{ categoria.tipo }}</h3>
      <h3>DESCRIPCIÓN: {{ categoria.descripcion }}</h3>
      <RouterLink :to="{ name: 'categorias_list' }">VOLVER</RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useCategoriasStore from '@/stores/categorias'

const store = useCategoriasStore()
const { categoria } = toRefs(store)
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
