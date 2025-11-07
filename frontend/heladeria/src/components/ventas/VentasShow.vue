<template>
  <div>
    <h1>VentasShow</h1>
    <div>
      <h3>ID: {{ venta.id }}</h3>
      <h3>FECHA: {{ venta.fecha }}</h3>
      <h3>TOTAL: {{ venta.total }}</h3>
      <h3>CLIENTE: {{ venta.cliente?.nombre }} {{ venta.cliente?.apellido }}</h3>
      <h3>EMPLEADO: {{ venta.empleado?.nombre }} {{ venta.empleado?.apellido }}</h3>
      <RouterLink :to="{ name: 'ventas_list' }">VOLVER</RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useVentasStore from '@/stores/ventas'

const store = useVentasStore()
const { venta } = toRefs(store)
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
