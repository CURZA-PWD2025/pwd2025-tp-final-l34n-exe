<template>
  <div>
    <h2>Los empleados</h2>
    <router-link :to="{name: 'empleados_create'}">Crear empleado </router-link>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>NOMBRE</th>
          <th>EMAIL</th>
          <th>TELEFONO</th>
          <th>APELLIDO</th>
          <th>PUESTO</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="empleado in empleados" :key="empleado.id">
          <td>{{ empleado.id }}</td>
          <td>{{ empleado.nombre }}</td>
          <td>{{ empleado.apellido }}</td>
          <td>{{ empleado.email }}</td>
          <td>{{ empleado.telefono }}</td>
          <td>{{ empleado.puesto }}</td>
          <td>
            <router-link :to="{ name: 'empleados_edit', params: { id: empleado.id}}">Editar</router-link>
            <router-link :to="{ name: 'empleados_show', params: { id: empleado.id}}">Mostrar</router-link>
            <button @click="destroy(empleado.id as number)">Eliminar</button>

          </td>
        </tr>

      </tbody>
    </table>



  </div>
</template>

<script setup lang="ts">
import useEmpleadosStore from '@/stores/empleados';
import { toRefs, onMounted } from 'vue';

const { empleados } = toRefs(useEmpleadosStore())
const { getAll, destroy} = useEmpleadosStore()

onMounted(async()=>{
  await getAll()
})
</script>

<style scoped>

</style>
