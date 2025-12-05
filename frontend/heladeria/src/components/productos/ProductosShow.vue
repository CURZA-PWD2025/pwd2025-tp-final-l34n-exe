<template>
  <div class="container">
    <v-card class="mx-auto my-8" variant="outlined" elevation="16" max-width="300">
      <v-card-title class="text-h6 text-center">Detalle del producto</v-card-title>
      <v-card-text>
        <p><strong>ID:</strong> {{ producto.id }}</p>
        <p><strong>NOMBRE:</strong> {{ producto.nombre }}</p>
        <p><strong>PRECIO:</strong> {{ producto.precio }}</p>
        <p><strong>STOCK:</strong> {{ producto.stock }}</p>
        <p><strong>MAXIMO DE SABORES:</strong> {{ producto.max_sabores }}</p>
        <p><strong>PROVEEDOR:</strong> {{ producto.proveedor?.nombre }}</p>
        <p><strong>CATEGORIA:</strong> {{ producto.categoria?.nombre }}</p>
        <div class="acciones">
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
          <ButtonComponent @click="deleteProducto(producto.id as number)" style="color: red">
            <template #pre-icon
              ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
            ></template>
            Eliminar
          </ButtonComponent>
        </div>
      </v-card-text>
    </v-card>
    <ButtonComponent class="volver" :to="{ name: 'productos_list' }">
      <template #pre-icon><Icon icon="ic:twotone-list" width="28" height="28"  style="color: black" /></template>
      VOLVER A LA LISTA
  </ButtonComponent>
  </div>

</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import useProductosStore from '@/stores/productos'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const store = useProductosStore()
const { producto } = toRefs(store)
const { getOne, destroy } = store
const route = useRoute()
const router = useRouter()
const deleteProducto = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este producto?')) {
    await destroy(id)
    router.push({ name: 'productos_list' })
  }
}

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})
</script>

<style scoped>
.acciones{
  display: flex;
}
</style>
