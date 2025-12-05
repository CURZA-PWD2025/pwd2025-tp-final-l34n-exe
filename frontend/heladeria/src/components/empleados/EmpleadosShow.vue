<template>
  <div class="container">
    <v-card class="mx-auto my-8" variant="outlined" elevation="16" max-width="300">
      <v-card-title class="text-h6 text-center">Detalle del empleado</v-card-title>
      <v-card-text>
        <p><strong>ID:</strong> {{ empleado.id }}</p>
        <p><strong>NOMBRE:</strong> {{ empleado.nombre }}</p>
        <p><strong>APELLIDO:</strong> {{ empleado.apellido }}</p>
        <p><strong>TELEFONO:</strong> {{ empleado.telefono}} </p>
        <p><strong>EMAIL:</strong> {{ empleado.email}}</p>
        <p><strong>PUESTO:</strong> {{ empleado.puesto }}</p>
        <div class="acciones">
          <ButtonComponent
            :to="{ name: 'empleados_edit', params: { id: empleado.id } }"
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
          <ButtonComponent @click="deleteEmpleado(empleado.id as number)" style="color: red">
            <template #pre-icon
              ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
            ></template>
            Eliminar
          </ButtonComponent>
        </div>
      </v-card-text>
    </v-card>
    <ButtonComponent :to="{ name: 'empleados_list' }">
      <template #pre-icon><Icon icon="ic:twotone-list" width="28" height="28"  style="color: black" /></template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import useEmpleadosStore from '@/stores/empleados'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const store = useEmpleadosStore()
const { empleado } = toRefs(store)
const { getOne, destroy } = store
const route = useRoute()
const router = useRouter()

const deleteEmpleado = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este empleado?')) {
    await destroy(id)
    router.push({ name: 'empleados_list' })
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

.volver{
  color: #1976d2;
  text-decoration: none;
}
</style>
