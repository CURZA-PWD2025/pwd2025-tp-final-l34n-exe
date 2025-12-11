<template>
  <div>
    <v-card class="mx-auto my-8" variant="outlined" elevation="16" max-width="300">
      <v-card-title class="text-h6 text-center">Detalle del item</v-card-title>
      <v-card-text>
        <p>
          <strong>ID: {{ itemventasabor.id }}</strong>
        </p>
        <p>
          <strong>ITEM ID: {{ itemventasabor.itemventa?.id }}</strong>
        </p>
        <p>
          <strong>SABOR: {{ itemventasabor.sabor?.nombre }}</strong>
        </p>
        <div class="acciones">
          <ButtonComponent
            :to="{ name: 'itemventasabores_edit', params: { id: itemventasabor.id } }"
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
          <ButtonComponent
            @click="deleteItemVentaSabor(itemventasabor.id as number)"
            style="color: red"
          >
            <template #pre-icon
              ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
            ></template>
            Eliminar
          </ButtonComponent>
        </div>
      </v-card-text>
    </v-card>
  </div>
  <ButtonComponent class="volver" :to="{ name: 'itemventasabores_list' }">
    <template #pre-icon
      ><Icon icon="ic:twotone-list" width="28" height="28" style="color: black"
    /></template>
    VOLVER A LA LISTA
  </ButtonComponent>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import useItemVentaSaboresStore from '@/stores/itemventasabores'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const store = useItemVentaSaboresStore()
const { itemventasabor } = toRefs(store)
const { getOne, destroy } = store
const route = useRoute()
const router = useRouter()

const deleteItemVentaSabor = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar esta venta?')) {
    await destroy(id)
    router.push({ name: 'itemventasabores_list' })
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
