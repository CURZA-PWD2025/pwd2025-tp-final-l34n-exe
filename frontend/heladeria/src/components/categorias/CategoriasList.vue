<template>
  <div>
    <h2>Las categorias</h2>
    <router-link :to="{ name: 'categorias_create' }">Crear categoria </router-link>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>NOMBRE</th>
          <th>TIPO</th>
          <th>DESCRIPCIÓN</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="categoria in categorias" :key="categoria.id">
          <td>{{ categoria.id }}</td>
          <td>{{ categoria.nombre }}</td>
          <td>{{ categoria.tipo }}</td>
          <td>{{ categoria.descripcion }}</td>
          <td>
            <router-link :to="{ name: 'categorias_edit', params: { id: categoria.id } }"
              >Editar</router-link
            >
            <router-link :to="{ name: 'categorias_show', params: { id: categoria.id } }"
              >Mostrar</router-link
            >
            <button @click="deleteCategoria(categoria.id as number)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import useCategoriasStore from '@/stores/categorias'
import { toRefs, onMounted } from 'vue'

const { categorias } = toRefs(useCategoriasStore())
const { getAll, destroy } = useCategoriasStore()

onMounted(async () => {
  await getAll()
})

const deleteCategoria = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar esta categoria?')) {
    await destroy(id)
    await getAll()
  }
}
</script>

<style scoped></style>
