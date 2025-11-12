<template>
  <div>
    <h1>ClientesShow</h1>
    <div>
      <h3>ID: {{ cliente.id }}</h3>
      <h3>NOMBRE: {{ cliente.nombre }}</h3>
      <h3>APELLIDO: {{ cliente.apellido }}</h3>
      <h3>TELEFONO: {{ cliente.telefono }}</h3>
      <h3>EMAIL: {{ cliente.direccion }}</h3>
      <RouterLink :to="{ name: 'clientes_list' }">VOLVER</RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useClientesStore from '@/stores/clientes'

const store = useClientesStore()
const { cliente } = toRefs(store)
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
