<template>
  <div>
    <h3>Editar categoria</h3>
    <form @submit.prevent="actualizar">
      <div>
        <label for="nombre">Nombre:</label>
        <input type="text" name="nombre" v-model="categoria.nombre" />
      </div>
      <div>
        <label for="tipo">Tipo:</label>
        <input type="text" name="tipo" v-model="categoria.tipo" />
      </div>
      <div>
        <label for="descripcion">Descripción:</label>
        <input type="text" name="descripcion" v-model="categoria.descripcion" />
      </div>
      <button type="submit">Actualizar categoria</button>
    </form>

    <RouterLink :to="{ name: 'categorias_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useCategoriasStore from '@/stores/categorias'

const store = useCategoriasStore()
const { categoria } = toRefs(store)
const { getOne, update } = store
const route = useRoute()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})

const actualizar = async () => {
  if (!categoria.value.nombre || !categoria.value.tipo || !categoria.value.descripcion) {
    alert('Por favor, complete los campos.')
    return
  }
  await update(categoria.value)
  alert('categoria actualizado con éxito.')
}
</script>

<style scoped></style>
