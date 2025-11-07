<template>
  <div>
    <h1>EmpleadosShow</h1>
    <div>
      <h3>ID: {{ empleado.id }}</h3>
      <h3>NOMBRE: {{ empleado.nombre }}</h3>
      <h3>APELLIDO: {{ empleado.apellido }}</h3>
      <h3>TELEFONO: {{ empleado.telefono }}</h3>
      <h3>EMAIL: {{ empleado.email }}</h3>
      <h3>PUESTO: {{ empleado.puesto }}</h3>
      <RouterLink :to="{ name: 'empleados_list' }">VOLVER</RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useEmpleadosStore from '@/stores/empleados'

const store = useEmpleadosStore()
const { empleado } = toRefs(store)
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
