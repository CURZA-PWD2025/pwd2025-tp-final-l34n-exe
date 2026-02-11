<template>
  <div>
    <h2>Las categorias</h2>
    <!--AÑADIR ALERTAS SI UNA CATEGORIA NO SE PUEDE ELIMINAR-->
    <ButtonComponent :to="{ name: 'categorias_create' }"
      ><template #pre-icon>
        <Icon
          icon="oui:ml-create-single-metric-job"
          width="28"
          height="28"
          style="color: green"
        /> </template
      >CREAR CATEGORIA</ButtonComponent
    >
    <v-table density="comfortable">
      <thead>
        <tr>
          <th>ID</th>
          <th>NOMBRE</th>
          <th>TIPO</th>
          <th>DESCRIPCIÓN</th>
          <th>ACCIONES</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="categoria in categorias" :key="categoria.id">
          <td>{{ categoria.id }}</td>
          <td>{{ categoria.nombre }}</td>
          <td>{{ categoria.tipo }}</td>
          <td>{{ categoria.descripcion }}</td>

          <td class="acciones">
            <ButtonComponent
              :to="{ name: 'categorias_edit', params: { id: categoria.id } }"
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

            <ButtonComponent :to="{ name: 'categorias_show', params: { id: categoria.id } }">
              <template #post-icon
                ><Icon icon="iconoir:eye" width="28" height="28"></Icon
              ></template>
              MOSTRAR
            </ButtonComponent>

            <ButtonComponent @click="deleteCategoria(categoria.id as number)" style="color: red">
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
import useCategoriasStore from '@/stores/categorias'
import useProductosStore from '@/stores/productos'
import useSaboresStore from '@/stores/sabores'
import useItemVentasStore from '@/stores/itemventas'
import useItemVentasSaboresStore from '@/stores/itemventasabores'
import type { ItemVenta } from '@/interfaces/ItemVenta'
import type { ItemVentaSabor } from '@/interfaces/ItemVentaSabor'
import { toRefs, onMounted } from 'vue'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const store = useCategoriasStore()
const { categorias } = toRefs(store)
const productoStore = useProductosStore()
const { productos } = toRefs(productoStore)
const saborStore = useSaboresStore()
const { sabores } = toRefs(saborStore)
const itemVentasStore = useItemVentasStore()
const { itemventas } = toRefs(itemVentasStore)
const itemVentasSaboresStore = useItemVentasSaboresStore()
const { itemventasabores } = toRefs(itemVentasSaboresStore)
const { getAll, destroy } = store

onMounted(async () => {
  await getAll()
  await productoStore.getAll()
  await saborStore.getAll()
  await itemVentasStore.getAll()
  await itemVentasSaboresStore.getAll()
})

const deleteCategoria = async (id: number) => {
  if (confirm('¿Está seguro de que desea eliminar esta categoría?')) {
    if (
      productos.value.some((p) => p.categoria?.id === id) ||
      sabores.value.some((s) => s.categoria?.id === id) ||
      itemventas.value.some((iv: ItemVenta) => iv.producto?.categoria?.id === id) ||
      itemventasabores.value.some((ivs: ItemVentaSabor) => ivs.sabor?.categoria?.id === id)
    ) {
      alert('No se puede eliminar una categoría que tiene productos, sabores o ventas asociadas.')
      return
    }
    await destroy(id)
    await getAll()
  }
}
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
