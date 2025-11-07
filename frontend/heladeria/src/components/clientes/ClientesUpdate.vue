<template>
  <div>
    <h3>Editar Cliente</h3>
    <form @submit.prevent="actualizar">
      <div>
        <label for="nombre">Nombre:</label>
        <input type="text" name="nombre" v-model="cliente.nombre" />
      </div>
      <div>
        <label for="apellido">Apellido:</label>
        <input type="text" name="apellido" v-model="cliente.apellido" />
      </div>
      <div>
        <label for="telefono">Teléfono:</label>
        <input type="text" name="telefono" v-model="cliente.telefono" />
      </div>
      <div>
        <label for="direccion">Dirección:</label>
        <input type="text" name="direccion" v-model="cliente.direccion" />
      </div>
      <button type="submit">Actualizar Cliente</button>
    </form>

    <RouterLink :to="{ name: 'clientes_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useClientesStore from '@/stores/clientes'

const store = useClientesStore()
const { cliente } = toRefs(store)
const { getOne, update } = store
const route = useRoute()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})

const actualizar = async () => {
  if (!cliente.value.nombre || !cliente.value.apellido || !cliente.value.telefono || !cliente.value.direccion) {
    alert('Por favor, complete los campos.')
    return
  }
  await update(cliente.value)
  alert('Cliente actualizado con éxito.')
}
</script>

<style scoped></style>
