<template>
  <div>
    <h3>EmpleadosCreate</h3>
    <form @submit.prevent="crear">
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
        <label for="email">Email:</label>
        <input type="text" name="email" v-model="empleado.email" />
      </div>
      <div>
        <label for="puesto">Puesto:</label>
        <select v-model="empleado.puesto" required>
          <option disabled value="">Seleccione un puesto</option>
          <option value="Cajero">Cajero</option>
          <option value="Limpieza">Limpieza</option>
          <option value="Gerente">Gerente</option>
        </select>
      </div>
      <button type="submit">Crear Empleado</button>
    </form>
    <RouterLink :to="{ name: 'empleados_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { toRefs } from 'vue'
import useEmpleadosStore from '@/stores/empleados'

const store = useEmpleadosStore()
const { empleado } = toRefs(store)
const { create } = store

const crear = async () => {
  if (
    !empleado.value.nombre ||
    !empleado.value.apellido ||
    !empleado.value.telefono ||
    !empleado.value.email ||
    !empleado.value.puesto
  ) {
    alert('Por favor, complete todos los campos.')
    return
  } else {
    await create(empleado.value)
    empleado.value = { nombre: '', apellido: '', telefono: '', email: '', puesto: '' }
    alert('Empleado creado con éxito.')
  }
}
</script>

<style scoped></style>
