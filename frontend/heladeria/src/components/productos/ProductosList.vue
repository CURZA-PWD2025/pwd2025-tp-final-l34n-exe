<template>
  <div>
    <h2>Los productos</h2>
    <ButtonComponent :to="{ name: 'productos_create' }"
      ><template #pre-icon>
        <Icon
          icon="oui:ml-create-single-metric-job"
          width="28"
          height="28"
          style="color: green"
        /> </template
      >CREAR PRODUCTO</ButtonComponent
    >
    <v-table density="comfortable">
      <thead>
        <tr>
          <th>ID</th>
          <th>NOMBRE</th>
          <th>PRECIO</th>
          <th>STOCK</th>
          <th>MAX_SABORES</th>
          <th>PROVEEDOR</th>
          <th>CATEGORIA</th>
          <th>ACCIONES</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto in productos" :key="producto.id">
          <td>{{ producto.id }}</td>
          <td>{{ producto.nombre }}</td>
          <td>{{ producto.precio }}</td>
          <td>{{ producto.stock }}</td>
          <td>{{ producto.max_sabores }}</td>
          <td>{{ producto.proveedor?.nombre }}</td>
          <td>{{ producto.categoria?.nombre }}</td>
          <td class="acciones">
            <ButtonComponent
              :to="{ name: 'productos_edit', params: { id: producto.id } }"
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
            <ButtonComponent :to="{ name: 'productos_show', params: { id: producto.id } }">
              <template #post-icon
                ><Icon icon="iconoir:eye" width="28" height="28"></Icon
              ></template>
              MOSTRAR
            </ButtonComponent>
            <ButtonComponent @click="deleteProducto(producto.id as number)" style="color: red">
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
import useProductosStore from '@/stores/productos'
import { toRefs, onMounted } from 'vue'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const { productos } = toRefs(useProductosStore())
const { getAll, destroy } = useProductosStore()

const deleteProducto = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este producto?')) {
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
