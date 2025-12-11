<template>
  <div class="container">
    <v-card class="mx-auto my-8" variant="outlined" elevation="16" max-width="300">
      <v-card-title class="text-h6 text-center">Detalle del cliente</v-card-title>
      <v-card-text>
        <p><strong>ID:</strong> {{ cliente.id }}</p>
        <p><strong>NOMBRE:</strong> {{ cliente.nombre }}</p>
        <p><strong>APELLIDO:</strong> {{ cliente.apellido }}</p>
        <p><strong>TELEFONO:</strong> {{ cliente.telefono }}</p>
        <p><strong>EMAIL:</strong> {{ cliente.direccion }}</p>
        <div class="acciones">
          <ButtonComponent
            :to="{ name: 'clientes_edit', params: { id: cliente.id } }"
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
          <ButtonComponent @click="deleteCliente(cliente.id as number)" style="color: red">
            <template #pre-icon
              ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
            ></template>
            Eliminar
          </ButtonComponent>
        </div>
      </v-card-text>
    </v-card>
    <ButtonComponent class="volver" :to="{ name: 'clientes_list' }">
      <template #pre-icon><Icon icon="ic:twotone-list" width="28" height="28"  style="color: black" /></template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import useClientesStore from '@/stores/clientes'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const store = useClientesStore()
const { cliente } = toRefs(store)
const { getOne, destroy } = store
const route = useRoute()
const router = useRouter()

const deleteCliente = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este cliente?')) {
    await destroy(id)
    router.push({ name: 'clientes_list' })
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
