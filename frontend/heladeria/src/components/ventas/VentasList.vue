<template>
  <div>
    <h2>Las ventas</h2>
    <ButtonComponent :to="{ name: 'ventas_create' }"
      ><template #pre-icon>
        <Icon
          icon="oui:ml-create-single-metric-job"
          width="28"
          height="28"
          style="color: green"
        /> </template
      >CREAR VENTA</ButtonComponent
    >
    <v-table density="comfortable">
      <thead>
        <tr>
          <th>ID</th>
          <th>FECHA</th>
          <th>TOTAL</th>
          <th>CLIENTE</th>
          <th>EMPLEADO</th>
          <th>ACCIONES</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="venta in ventas" :key="venta.id">
          <td>{{ venta.id }}</td>
          <td>{{ venta.fecha }}</td>
          <td>{{ venta.total }}$</td>
          <td>{{ venta.cliente?.nombre }} {{ venta.cliente?.apellido }}</td>
          <td>{{ venta.empleado?.nombre }} {{ venta.empleado?.apellido }}</td>
          <td class="acciones">
            <ButtonComponent
              :to="{ name: 'ventas_edit', params: { id: venta.id } }"
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
            <ButtonComponent :to="{ name: 'ventas_show', params: { id: venta.id } }">
              <template #post-icon
                ><Icon icon="iconoir:eye" width="28" height="28"></Icon
              ></template>
              MOSTRAR
            </ButtonComponent>
            <ButtonComponent @click="deleteVenta(venta.id as number)" style="color: red">
              <template #pre-icon
                ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
              ></template>
              Eliminar
            </ButtonComponent>
          </td>
        </tr>
      </tbody>
    </v-table>
    <ButtonComponent :to="{ name: 'itemventas_list' }" style="color: #1976d2">
      <template #post-icon></template>
      MOSTRAR ITEMS</ButtonComponent
    >
  </div>
</template>

<script setup lang="ts">
import useVentasStore from '@/stores/ventas'
import { toRefs, onMounted } from 'vue'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const ventasStore = useVentasStore()
const { ventas } = toRefs(ventasStore)
const { getAll, destroy } = ventasStore

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
