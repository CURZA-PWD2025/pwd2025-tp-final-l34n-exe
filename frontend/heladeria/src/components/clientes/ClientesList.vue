<template>
  <div>
    <h2>Los clientes</h2>
    <router-link :to="{name: 'clientes_create'}">Crear cliente </router-link>
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
          <td>{{ cliente.direccion }}</td>
          <td>{{ cliente.telefono }}</td>
          <td>
            <router-link :to="{ name: 'clientes_edit', params: { id: cliente.id}}">Editar</router-link>
            <router-link :to="{ name: 'clientes_show', params: { id: cliente.id}}">Mostrar</router-link>
            <button @click="destroy(cliente.id as number)">Eliminar</button>

          </td>
        </tr>

      </tbody>
    </table>



  </div>
</template>

<script setup lang="ts">
import useClientesStore from '@/stores/clientes';
import { toRefs, onMounted } from 'vue';

const { clientes } = toRefs(useClientesStore())
const { getAll, destroy} = useClientesStore()

onMounted(async()=>{
  await getAll()
})
</script>

<style scoped>

</style>
