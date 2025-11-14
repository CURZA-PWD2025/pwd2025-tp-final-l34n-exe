<template>
  <div>
    <h3>ProveedorCreate</h3>
    <form @submit.prevent="crear">
      <div>
        <label for="nombre">Nombre:</label>
        <input type="text" name="nombre" v-model="proveedor.nombre" />
      </div>
      <div>
        <label for="telefono">Teléfono:</label>
        <input type="text" name="telefono" v-model="proveedor.telefono" />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" name="email" v-model="proveedor.email" />
      </div>
      <button type="submit">Crear Proveedor</button>
    </form>
    <RouterLink :to="{ name: 'proveedores_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { toRefs } from 'vue'
import useProveedoresStore from '@/stores/proveedores'

const store = useProveedoresStore()
const { proveedor } = toRefs(store)
const { create } = store

const crear = async () => {
  if (!proveedor.value.nombre || !proveedor.value.telefono || !proveedor.value.email) {
    alert('Por favor, complete todos los campos.')
    return
  } else {
    await create(proveedor.value)
    proveedor.value = { nombre: '', telefono: '', email: '' }
    alert('Proveedor creado con éxito.')
  }
}
</script>

<style scoped></style>
