<template>
  <div>
    <h1>
      ProveedoresShow
    </h1>
    <div>
      <h3>ID: {{ proveedor.id }}</h3>
      <h3>NOMBRE: {{ proveedor.nombre }}</h3>
      <h3>TELEFONO: {{ proveedor.telefono }}</h3>
      <h3>EMAIL: {{ proveedor.email }}</h3>
      <RouterLink :to="{ name: 'proveedores_list' }">VOLVER</RouterLink>


    </div>

  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useProveedoresStore from '@/stores/proveedores'

const store = useProveedoresStore()
const { proveedor } = toRefs(store)
const { getOne } = store
const route = useRoute()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})
</script>

<style scoped>

</style>
