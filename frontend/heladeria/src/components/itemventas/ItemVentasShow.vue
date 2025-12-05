<template>
  <div>
    <v-card class="mx-auto my-8" variant="outlined" elevation="16" max-width="300">
      <v-card-title class="text-h6 text-center">Detalle del item</v-card-title>
      <v-card-text>
        <p><strong>ID: {{ itemventa.id }}</strong></p>
        <p><strong>VENTA ID: {{ itemventa.venta?.id }}</strong></p>
        <p><strong>FECHA VENTA: {{ itemventa.venta?.fecha }}</strong></p>
        <p><strong>PRODUCTO: {{ itemventa.producto?.nombre }}</strong></p>
        <p><strong>CANTIDAD: {{ itemventa.cantidad }}</strong></p>
        <div class="acciones">
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
          <ButtonComponent @click="deleteItemVenta(itemventa.id as number)" style="color: red">
            <template #pre-icon
              ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
            ></template>
            Eliminar
          </ButtonComponent>
        </div>
      </v-card-text>
    </v-card>
  </div>
  <ButtonComponent :to="{ name: 'itemventas_list' }">
      <template #pre-icon><Icon icon="ic:twotone-list" width="28" height="28"  style="color: black" /></template>
      VOLVER A LA LISTA
  </ButtonComponent>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import useItemVentasStore from '@/stores/itemventas'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const store = useItemVentasStore()
const { itemventa } = toRefs(store)
const { getOne, destroy } = store
const route = useRoute()
const router = useRouter()

const deleteItemVenta = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar esta venta?')) {
    await destroy(id)
    router.push({ name: 'itemventas_list' })
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
.acciones {
  display: flex;
}

</style>
