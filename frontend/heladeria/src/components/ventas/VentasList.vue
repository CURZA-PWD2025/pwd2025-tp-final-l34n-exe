<template>
  <div>
    <h2>Las ventas</h2>
    <router-link :to="{name: 'ventas_create'}">Crear venta </router-link>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>FECHA</th>
          <th>TOTAL</th>
          <th>NOMBRE CLIENTE</th>
          <th>/APELLIDO CLIENTE</th>
          <th>/NOMBRE EMPLEADO</th>
          <th>/APELLIDO EMPLEADO</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="venta in ventas" :key="venta.id">
          <td>{{ venta.id }}</td>
          <td>{{ venta.fecha }}</td>
          <td>{{ venta.total }}</td>
          <td>{{ venta.cliente?.nombre }}</td>
          <td>{{ venta.cliente?.apellido }}</td>
          <td>{{ venta.empleado?.nombre }}</td>
          <td>{{ venta.empleado?.apellido }}</td>
          <td>
            <router-link :to="{ name: 'ventas_edit', params: { id: venta.id}}">Editar</router-link>
            <router-link :to="{ name: 'ventas_show', params: { id: venta.id}}">Mostrar</router-link>
            <button @click="deleteVenta(venta.id as number)">Eliminar</button>

          </td>
        </tr>

      </tbody>
    </table>



  </div>
</template>

<script setup lang="ts">
import useVentasStore from '@/stores/ventas';
import { toRefs, onMounted } from 'vue';

const { ventas } = toRefs(useVentasStore())
const { getAll, destroy} = useVentasStore()

const deleteVenta = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar esta venta?')) {
    await destroy(id)
    await getAll()
  }
}

onMounted(async () => {
  await getAll()
})
</script>

<style scoped>

</style>
