<template>
  <div>
    <h2>Los empleados</h2>
    <ButtonComponent :to="{ name: 'empleados_create' }"
      ><template #pre-icon>
        <Icon
          icon="oui:ml-create-single-metric-job"
          width="28"
          height="28"
          style="color: green"
        /> </template
      >CREAR EMPLEADO</ButtonComponent
    >
    <v-table density="comfortable">
      <thead>
        <tr>
          <th>ID</th>
          <th>NOMBRE</th>
          <th>APELLIDO</th>
          <th>EMAIL</th>
          <th>TELEFONO</th>
          <th>PUESTO</th>
          <th>ACCIONES</th>
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
          <td class="acciones">
            <ButtonComponent
              :to="{ name: 'empleados_edit', params: { id: empleado.id } }"
              style="color: #1976d2"
            >
              <template #pre-icon
                ><Icon
                  icon="material-symbols:edit-outline"
                  width="28"
                  height="28"
                  style="color: #1976d2"
              /></template>
              EDITAR
            </ButtonComponent>
            <ButtonComponent :to="{ name: 'empleados_show', params: { id: empleado.id } }">
              <template #post-icon
                ><Icon icon="iconoir:eye" width="28" height="28"></Icon
              ></template>
              MOSTRAR
            </ButtonComponent>
            <ButtonComponent @click="deleteEmpleado(empleado.id as number)" style="color: red">
              <template #pre-icon
                ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
              ></template>
              Eliminar
            </ButtonComponent>
          </td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script setup lang="ts">
import useEmpleadosStore from '@/stores/empleados'
import { toRefs, onMounted } from 'vue'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const { empleados } = toRefs(useEmpleadosStore())
const { getAll, destroy } = useEmpleadosStore()

const deleteEmpleado = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este empleado?')) {
    await destroy(id)
    await getAll()
  }
}

onMounted(async () => {
  await getAll()
})
</script>

<style scoped>
h2 {
  margin-bottom: 15px;
  font-size: 26px;
  font-weight: 600;
  color: #333;
  text-align: center;
}

.acciones {
  display: flex;
  gap: 10px;
  align-items: center;
}
</style>
