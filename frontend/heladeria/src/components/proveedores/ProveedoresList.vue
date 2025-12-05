<template>
  <div>
    <h2>Los proveedores</h2>
    <ButtonComponent :to="{ name: 'proveedores_create' }"
      ><template #pre-icon>
        <Icon
          icon="oui:ml-create-single-metric-job"
          width="28"
          height="28"
          style="color: green"
        /> </template
      >CREAR PROVEEDOR</ButtonComponent
    >
    <v-table density="comfortable">
      <thead>
        <tr>
          <th>ID</th>
          <th>NOMBRE</th>
          <th>EMAIL</th>
          <th>TELEFONO</th>
          <th>ACCIONES</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="proveedor in proveedores" :key="proveedor.id">
          <td>{{ proveedor.id }}</td>
          <td>{{ proveedor.nombre }}</td>
          <td>{{ proveedor.email }}</td>
          <td>{{ proveedor.telefono }}</td>
          <td class="acciones">
            <ButtonComponent
              :to="{ name: 'proveedores_edit', params: { id: proveedor.id } }"
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
            <ButtonComponent :to="{ name: 'proveedores_show', params: { id: proveedor.id } }">
              <template #post-icon
                ><Icon icon="iconoir:eye" width="28" height="28"></Icon
              ></template>
              MOSTRAR
            </ButtonComponent>
            <ButtonComponent @click="deleteProveedor(proveedor.id as number)" style="color: red">
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
import useProveedoresStore from '@/stores/proveedores'
import { toRefs, onMounted } from 'vue'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const { proveedores } = toRefs(useProveedoresStore())
const { getAll, destroy } = useProveedoresStore()

const deleteProveedor = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este proveedor?')) {
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
