<template>
  <div>
    <h2>Los items en cada venta</h2>
    <ButtonComponent :to="{ name: 'itemventas_create' }"
      ><template #pre-icon>
        <Icon
          icon="oui:ml-create-single-metric-job"
          width="28"
          height="28"
          style="color: green"
        /> </template
      >CREAR ITEM</ButtonComponent
    >
    <v-table density="comfortable">
      <thead>
        <tr>
          <th>ID</th>
          <th>ID VENTA</th>
          <th>TOTAL VENTA</th>
          <th>PRODUCTO</th>
          <th>CANTIDAD</th>
          <th>ACCIONES</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="itemventa in itemventas" :key="itemventa.id">
          <td>{{ itemventa.id }}</td>
          <td>{{ itemventa.venta?.id }}</td>
          <td>{{ itemventa.venta?.total }}$</td>
          <td>{{ itemventa.producto?.nombre }}</td>
          <td>{{ itemventa.cantidad }}</td>
          <td class="acciones">
            <ButtonComponent
              :to="{ name: 'itemventas_edit', params: { id: itemventa.id } }"
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
            <ButtonComponent :to="{ name: 'itemventas_show', params: { id: itemventa.id } }">
              <template #post-icon
                ><Icon icon="iconoir:eye" width="28" height="28"></Icon
              ></template>
              MOSTRAR
            </ButtonComponent>
            <ButtonComponent @click="deleteItemVenta(itemventa.id as number)" style="color: red">
              <template #pre-icon
                ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
              ></template>
              Eliminar
            </ButtonComponent>
          </td>
        </tr>
      </tbody>
    </v-table>
    <ButtonComponent :to="{ name: 'itemventasabores_list' }" style="color: #1976d2">MOSTRAR SABOR/ES DE CADA ITEM</ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import useItemVentasStore from '@/stores/itemventas'
import { toRefs, onMounted } from 'vue'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const itemVentasStore = useItemVentasStore()
const { itemventas } = toRefs(itemVentasStore)
const { getAll, destroy } = itemVentasStore

const deleteItemVenta = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este item?')) {
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
