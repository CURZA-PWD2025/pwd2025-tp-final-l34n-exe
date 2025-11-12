<template>
  <div>
    <h2>Los productos</h2>
    <router-link :to="{ name: 'productos_create' }">Crear producto </router-link>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>NOMBRE</th>
          <th>PRECIO</th>
          <th>STOCK</th>
          <th>MAX_SABORES</th>
          <th>PROVEEDOR</th>
          <th>CATEGORIA</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto in productos" :key="producto.id">
          <td>{{ producto.id }}</td>
          <td>{{ producto.nombre }}</td>
          <td>{{ producto.precio }}</td>
          <td>{{ producto.stock }}</td>
          <td>{{ producto.max_sabores }}</td>
          <td>{{ producto.proveedor?.nombre }}</td>
          <td>{{ producto.categoria?.nombre }}</td>
          <td>
            <router-link :to="{ name: 'productos_edit', params: { id: producto.id } }"
              >Editar</router-link
            >
            <router-link :to="{ name: 'productos_show', params: { id: producto.id } }"
              >Mostrar</router-link
            >
            <button @click="deleteProducto(producto.id as number)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import useProductosStore from '@/stores/productos'
import { toRefs, onMounted } from 'vue'

const { productos } = toRefs(useProductosStore())
const { getAll, destroy } = useProductosStore()

const deleteProducto = async (id: number) => {
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
