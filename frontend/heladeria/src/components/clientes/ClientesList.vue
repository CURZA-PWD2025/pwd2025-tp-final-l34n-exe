<template>
  <div>
    <h2>Los clientes</h2>
    <router-link :to="{ name: 'clientes_create' }">Crear cliente </router-link>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>NOMBRE</th>
          <th>APELLIDO</th>
          <th>TELEFONO</th>
          <th>DIRECCION</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="cliente in clientes" :key="cliente.id">
          <td>{{ cliente.id }}</td>
          <td>{{ cliente.nombre }}</td>
          <td>{{ cliente.apellido }}</td>
          <td>{{ cliente.telefono }}</td>
          <td>{{ cliente.direccion }}</td>
          <td>
            <router-link :to="{ name: 'clientes_edit', params: { id: cliente.id ?? 0 } }"
              >Editar</router-link
            >
            <router-link :to="{ name: 'clientes_show', params: { id: cliente.id ?? 0 } }"
              >Mostrar</router-link
            >
            <button @click="deleteCliente(cliente.id ? cliente.id : 0)" class="btn-delete">
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import useClientesStore from '@/stores/clientes'
import { toRefs, onMounted } from 'vue'

const { clientes } = toRefs(useClientesStore())
const { getAll, destroy } = useClientesStore()

const deleteCliente = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este cliente?')) {
    await destroy(id)
    await getAll()
  }
}

onMounted(async () => {
  await getAll()
})
</script>

<style scoped></style>
