<template>
  <div>
    <h2>Los items en cada venta</h2>
    <router-link :to="{name: 'itemventas_create'}">Crear item </router-link>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>VENTA</th>
          <th>PRODUCTO</th>
          <th>CANTIDAD</th>

        </tr>
      </thead>
      <tbody>
        <tr v-for="itemventa in itemventas" :key="itemventa.id">
          <td>{{ itemventa.id }}</td>
          <td>{{ itemventa.venta?.total }}</td>
          <td>{{ itemventa.producto?.nombre }}</td>
          <td>{{ itemventa.cantidad }}</td>
          <td>
            <router-link :to="{ name: 'itemventas_edit', params: { id: itemventa.id}}">Editar</router-link>
            <router-link :to="{ name: 'itemventas_show', params: { id: itemventa.id}}">Mostrar</router-link>
            <button @click="destroy(itemventa.id as number)">Eliminar</button>
          </td>
        </tr>

      </tbody>
    </table>



  </div>
</template>

<script setup lang="ts">
import useItemVentasStore from '@/stores/itemventas';
import { toRefs, onMounted } from 'vue';

const { itemventas } = toRefs(useItemVentasStore())
const { getAll, destroy} = useItemVentasStore()

onMounted(async()=>{
  await getAll()
})
</script>

<style scoped>

</style>
