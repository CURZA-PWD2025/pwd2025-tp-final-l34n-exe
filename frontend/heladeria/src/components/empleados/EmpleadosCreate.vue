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
          label="Teléfono del empleado"
          variant="outlined"
          :rules="[
            (v) => !!v || 'Campo obligatorio',
            (v) => /^[0-9]+$/.test(v) || 'Solo números',
            (v) => v.length === 10 || 'Debe tener 10 dígitos',
          ]"
          required
        ></v-text-field>

        <v-text-field
          v-model="empleado.email"
          label="Email del empleado"
          variant="outlined"
          :rules="[
            (v) => !!v || 'El email es obligatorio',
            (v) => /.+@.+\..+/.test(v) || 'Email inválido',
          ]"
          required
        ></v-text-field>
        <v-select
          v-model="empleado.puesto"
          :items="puestos"
          item-title="nombre"
          item-value="id"
          label="Puesto"
          variant="outlined"
          :rules="[(v) => !!v || 'Seleccione un puesto']"
          required
        />
        <ButtonComponent type="submit" class="crear">
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
  const result = await form.value?.validate()
  if (!result.valid){
    alert('Por favor, complete todos los campos correctamente.')
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

    alert('Empleado creado con éxito.')

    form.value.reset()
  }
}
</script>

<style scoped>
.crear {
  text-align: center;
}
</style>
