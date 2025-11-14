<template>
  <div>
    <h3>Editar Empleado</h3>
    <form @submit.prevent="actualizar">
      <div>
        <label for="nombre">Nombre:</label>
        <input type="text" name="nombre" v-model="empleado.nombre" />
      </div>
      <div>
        <label for="apellido">Apellido:</label>
        <input type="text" name="apellido" v-model="empleado.apellido" />
      </div>
      <div>
        <label for="telefono">Teléfono:</label>
        <input type="text" name="telefono" v-model="empleado.telefono" />
      </div>
      <div>
        <label for="direccion">Dirección:</label>
        <input type="text" name="direccion" v-model="empleado.email" />
      </div>
      <div>
        <label for="puesto">Puesto:</label>
        <input type="text" name="puesto" v-model="empleado.puesto" />
      </div>
      <button type="submit">Actualizar Empleado</button>
    </form>

    <RouterLink :to="{ name: 'empleados_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useEmpleadosStore from '@/stores/empleados'

const store = useEmpleadosStore()
const { empleado } = toRefs(store)
const { getOne, update } = store
const route = useRoute()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})

const actualizar = async () => {
  if (
    !empleado.value.nombre ||
    !empleado.value.apellido ||
    !empleado.value.telefono ||
    !empleado.value.email ||
    !empleado.value.puesto
  ) {
    alert('Por favor, complete los campos.')
    return
  }
  await update(empleado.value)
  alert('Empleado actualizado con éxito.')
}
</script>

<style scoped></style>
