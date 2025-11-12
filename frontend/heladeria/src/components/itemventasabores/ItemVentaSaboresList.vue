<template>
  <div>
    <h2>Sabores en cada item</h2>
    <router-link :to="{ name: 'itemventasabores_create' }">Crear item </router-link>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>ID ITEM</th>
          <th>SABOR</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="itemventasabor in itemventasabores" :key="itemventasabor.id">
          <td>{{ itemventasabor.id }}</td>
          <td>{{ itemventasabor.itemventa?.id }}</td>
          <td>{{ itemventasabor.sabor?.nombre }}</td>
          <td>
            <router-link :to="{ name: 'itemventasabores_edit', params: { id: itemventasabor.id } }"
              >Editar</router-link
            >
            <router-link :to="{ name: 'itemventasabores_show', params: { id: itemventasabor.id } }"
              >Mostrar</router-link
            >
            <button @click="deleteItemVentaSabor(itemventasabor.id as number)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import useItemVentaSaboresStore from '@/stores/itemventasabores'
import { toRefs, onMounted } from 'vue'

const { itemventasabores } = toRefs(useItemVentaSaboresStore())
const { getAll, destroy } = useItemVentaSaboresStore()

const deleteItemVentaSabor = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este producto?')) {
    await destroy(id)
    await getAll()
  }
}

onMounted(async () => {
  await getAll()
})
</script>

<style scoped></style>
