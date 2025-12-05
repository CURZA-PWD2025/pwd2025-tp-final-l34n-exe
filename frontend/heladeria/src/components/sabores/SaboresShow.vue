<template>
  <div class="container">
    <v-card class="mx-auto my-8" variant="outlined" elevation="16" max-width="300">
      <v-card-title class="text-h6 text-center">Detalle del sabor</v-card-title>
      <v-card-text>
        <p><strong>ID:</strong> {{ sabor.id }}</p>
        <p><strong>NOMBRE:</strong> {{ sabor.nombre }}</p>
        <p><strong>STOCK:</strong> {{ sabor.stock }}</p>
        <p><strong>CATEGORIA:</strong> {{ sabor.categoria?.nombre }}</p>
        <p><strong>DISPONIBLE:</strong> {{ sabor.disponible }}</p>
        <div class="acciones">
          <ButtonComponent
            :to="{ name: 'sabores_edit', params: { id: sabor.id } }"
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
          <ButtonComponent @click="deleteSabor(sabor.id as number)" style="color: red">
            <template #pre-icon
              ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
            ></template>
            Eliminar
          </ButtonComponent>
        </div>
      </v-card-text>
    </v-card>
    <ButtonComponent :to="{ name: 'sabores_list' }">
      <template #pre-icon><Icon icon="ic:twotone-list" width="28" height="28"  style="color: black" /></template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import useSaboresStore from '@/stores/sabores'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const store = useSaboresStore()
const { sabor } = toRefs(store)
const { getOne, destroy } = store
const route = useRoute()
const router = useRouter()

const deleteSabor = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este Sabor?')) {
    await destroy(id)
    router.push({ name: 'sabores_list' })
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
