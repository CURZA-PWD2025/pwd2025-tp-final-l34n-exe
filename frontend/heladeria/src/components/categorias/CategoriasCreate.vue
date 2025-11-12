<template>
  <div>
    <h3>CategoriaCreate</h3>
    <form @submit.prevent="crear">
      <div>
        <label for="nombre">Nombre:</label>
        <input type="text" name="nombre" v-model="categoria.nombre" />
      </div>
      <div>
        <label for="apellido">Apellido:</label>
        <input type="text" name="apellido" v-model="categoria.tipo" />
      </div>
      <div>
        <label for="telefono">Teléfono:</label>
        <input type="text" name="telefono" v-model="categoria.descripcion" />
      </div>
      <button type="submit">Crear categoria</button>
    </form>
    <RouterLink :to="{ name: 'categorias_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { toRefs } from 'vue'
import useCategoriasStore from '@/stores/categorias'

const store = useCategoriasStore()
const { categoria } = toRefs(store)
const { create } = store

const crear = async () => {
  if (!categoria.value.nombre || !categoria.value.tipo || !categoria.value.descripcion) {
    alert('Por favor, complete todos los campos.')
    return
  } else {
    await create(categoria.value)
    categoria.value = { nombre: '', tipo: '', descripcion: '' }
    alert('categoria creada con éxito.')
  }
}
</script>

<style scoped></style>
