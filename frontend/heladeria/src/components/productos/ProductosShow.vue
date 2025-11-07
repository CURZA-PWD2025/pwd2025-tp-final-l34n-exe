<template>
  <div>
    <h1>ProductosShow</h1>
    <div>
      <h3>ID: {{ producto.id }}</h3>
      <h3>NOMBRE: {{ producto.nombre }}</h3>
      <h3>PRECIO: {{ producto.precio }}</h3>
      <h3>STOCK: {{ producto.stock }}</h3>
      <h3>MAXIMO DE SABORES: {{ producto.max_sabores }}</h3>
      <h3>PROVEEDOR: {{ producto.proveedor?.nombre }}</h3>
      <h3>CATEGORIA: {{ producto.categoria?.nombre }}</h3>
      <RouterLink :to="{ name: 'productos_list' }">VOLVER</RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useProductosStore from '@/stores/productos'

const store = useProductosStore()
const { producto } = toRefs(store)
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
