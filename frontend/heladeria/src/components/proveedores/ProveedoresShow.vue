<template>
  <div class="container">
    <v-card class="mx-auto my-8" variant="outlined" elevation="16" max-width="300">
      <v-card-title class="text-h6 text-center">Detalle del proveedor</v-card-title>
      <v-card-text>
        <p>
          <strong>ID: {{ proveedor.id }}</strong>
        </p>
        <p>
          <strong>NOMBRE: {{ proveedor.nombre }}</strong>
        </p>
        <p>
          <strong>TELEFONO: {{ proveedor.telefono }}</strong>
        </p>
        <p>
          <strong>EMAIL: {{ proveedor.email }}</strong>
        </p>
        <div class="acciones">
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
          <ButtonComponent @click="deleteProveedor(proveedor.id as number)" style="color: red">
            <template #pre-icon
              ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
            ></template>
            Eliminar
          </ButtonComponent>
        </div>
      </v-card-text>
    </v-card>
    <ButtonComponent class="volver" :to="{ name: 'proveedores_list' }">
      <template #pre-icon><Icon icon="ic:twotone-list" width="28" height="28"  style="color: black" /></template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import useProveedoresStore from '@/stores/proveedores'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const store = useProveedoresStore()
const { proveedor } = toRefs(store)
const { getOne, destroy } = store
const route = useRoute()
const router = useRouter()

const deleteProveedor = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este proveedor?')) {
    await destroy(id)
    router.push({ name: 'proveedores_list' })
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
