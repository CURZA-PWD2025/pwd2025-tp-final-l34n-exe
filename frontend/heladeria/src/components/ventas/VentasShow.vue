<template>
  <div class="container">
    <v-card class="mx-auto my-8" variant="outlined" elevation="16" max-width="300">
      <v-card-title class="text-h6 text-center">Detalle de la venta</v-card-title>
      <v-card-text>
        <p><strong>ID:</strong> {{ venta.id }}</p>
        <p><strong>FECHA:</strong> {{ venta.fecha }}</p>
        <p><strong>TOTAL:</strong> {{ venta.total }}</p>
        <p><strong>CLIENTE:</strong> {{ venta.cliente?.nombre }} {{ venta.cliente?.apellido }}</p>
        <p>
          <strong>EMPLEADO:</strong> {{ venta.empleado?.nombre }} {{ venta.empleado?.apellido }}
        </p>
        <div class="acciones">
          <ButtonComponent
            :to="{ name: 'ventas_edit', params: { id: venta.id } }"
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
          <ButtonComponent @click="deleteVenta(venta.id as number)" style="color: red">
            <template #pre-icon
              ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
            ></template>
            Eliminar
          </ButtonComponent>
        </div>
      </v-card-text>
    </v-card>
    <ButtonComponent class="volver" :to="{ name: 'ventas_list' }">
      <template #pre-icon>
        <Icon icon="ic:twotone-list" width="28" height="28"  style="color: black" />
      </template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import useVentasStore from '@/stores/ventas'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const store = useVentasStore()
const { venta } = toRefs(store)
const { getOne, destroy } = store
const route = useRoute()
const router = useRouter()

const deleteVenta = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar esta venta?')) {
    await destroy(id)
    router.push({ name: 'ventas_list' })
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
