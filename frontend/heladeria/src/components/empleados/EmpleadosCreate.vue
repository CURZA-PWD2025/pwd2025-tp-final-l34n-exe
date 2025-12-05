<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" color="aliceblue" elevation="16">
      <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>
      <v-form @submit.prevent="crear" ref="form">
        <v-text-field
          v-model="empleado.nombre"
          label="Nombre del empleado"
          variant="outlined"
          :rules="[(v) => !!v || 'El nombre es obligatorio']"
          required
        ></v-text-field>
        <v-text-field
          v-model="empleado.apellido"
          label="Apellido del empleado"
          variant="outlined"
          :rules="[(v) => !!v || 'El apellido es obligatorio']"
          required
        ></v-text-field>
        <v-text-field
          v-model="empleado.telefono"
          label="Telefono del empleado"
          variant="outlined"
          :rules="[(v) => !!v || 'El telefono es obligatorio']"
          required
        ></v-text-field>
        <v-text-field
          v-model="empleado.email"
          label="Email del empleado"
          variant="outlined"
          :rules="[(v) => !!v || 'El email es obligatorio']"
          required
        ></v-text-field>
        <v-select
          v-model="empleado.puesto"
          :items="puestos"
          item-title="nombre"
          item-value="id"
          label="Categoría"
          variant="outlined"
          :rules="[(v) => !!v || 'Seleccione una categoría']"
          required
        />
        <ButtonComponent type="submit">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Crear Empleado
        </ButtonComponent>
      </v-form>
    </v-card>
    <ButtonComponent :to="{ name: 'empleados_list' }">
      <template #pre-icon
        ><Icon icon="ic:twotone-list" width="28" height="28" style="color: black"
      /></template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs } from 'vue'
import useEmpleadosStore from '@/stores/empleados'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const store = useEmpleadosStore()
const { empleado } = toRefs(store)
const { create } = store
const puestos = ['Limpieza', 'Cajero', 'Gerente']
const form = ref()
const crear = async () => {
  const valid = await form.value?.validate()
  if (!valid) return
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
    const data = {
      nombre: empleado.value.nombre,
      apellido: empleado.value.apellido,
      telefono: empleado.value.telefono,
      email: empleado.value.email,
      puesto: empleado.value.puesto,
    }
    await create(data)
    empleado.value = { nombre: '', apellido: '', telefono: '', email: '', puesto: '' }
    alert('Empleado creado con éxito.')
    form.value.reset()
  }
}
</script>

<style scoped>
a {
  display: inline-block;
  margin-top: 16px;
  text-decoration: none;
  color: #1976d2;
  font-weight: 500;
  text-align: center;
}

a:hover {
  text-decoration: underline;
}
</style>
