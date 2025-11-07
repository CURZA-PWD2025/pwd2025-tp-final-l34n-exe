<template>
  <div>
    <h3>Editar Proveedor</h3>
    <form @submit.prevent="actualizar">
      <div>
        <label for="telefono">Teléfono:</label>
        <input type="text" name="telefono" v-model="proveedor.telefono" />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" name="email" v-model="proveedor.email" />
      </div>
      <button type="submit">Actualizar Proveedor</button>
    </form>

    <RouterLink :to="{ name: 'proveedores_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useProveedoresStore from '@/stores/proveedores'

const store = useProveedoresStore()
const { proveedor } = toRefs(store)
const { getOne, update } = store
const route = useRoute()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})

const actualizar = async () => {
  if (!proveedor.value.telefono || !proveedor.value.email) {
    alert('Por favor, complete los campos.')
    return
  }
  await update(proveedor.value)
  alert('Proveedor actualizado con éxito.')
}
</script>

<style scoped></style>
