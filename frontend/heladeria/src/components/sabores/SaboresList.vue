<template>
  <div>
    <h2>Los sabores</h2>
    <router-link :to="{name: 'sabores_create'}">Crear sabor </router-link>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>NOMBRE</th>
          <th>STOCK</th>
          <th>DISPONIBLE</th>
          <th>CATEGORIA</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="sabor in sabores" :key="sabor.id">
          <td>{{ sabor.id }}</td>
          <td>{{ sabor.nombre }}</td>
          <td>{{ sabor.stock }}</td>
          <td>{{ sabor.disponible ? 'Sí' : 'No' }}</td>
          <td>{{ sabor.categoria?.nombre }}</td>
          <td>
            <router-link :to="{ name: 'sabores_edit', params: { id: sabor.id}}">Editar</router-link>
            <router-link :to="{ name: 'sabores_show', params: { id: sabor.id}}">Mostrar</router-link>
            <button @click="destroy(sabor.id as number)">Eliminar</button>

          </td>
        </tr>

      </tbody>
    </table>



  </div>
</template>

<script setup lang="ts">
import useSaboresStore from '@/stores/sabores';
import { toRefs, onMounted } from 'vue';

const { sabores } = toRefs(useSaboresStore())
const { getAll, destroy} = useSaboresStore()

onMounted(async()=>{
  await getAll()
})
</script>

<style scoped>

</style>
