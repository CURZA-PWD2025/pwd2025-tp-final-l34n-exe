<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" color="aliceblue" elevation="16">
      <v-card-title class="text-h6 text-center">ACTUALIZAR EMPLEADO</v-card-title>

      <v-form @submit.prevent="actualizar" ref="form">
        <v-text-field
          v-model.trim="empleado.nombre"
          label="Nombre del empleado"
          variant="outlined"
          :rules="[
            (v) => !!v || 'El nombre es obligatorio',
            (v) => v.length >= 3 || 'Mínimo 3 caracteres',
            (v) => v.length <= 30 || 'Máximo 30 caracteres',
            (v) => /^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\\s]+$/.test(v) || 'Solo letras y espacios',
          ]"
          required
        />

        <v-text-field
          v-model.trim="empleado.apellido"
          label="Apellido del empleado"
          variant="outlined"
          :rules="[
            (v) => !!v || 'El apellido es obligatorio',
            (v) => v.length >= 3 || 'Mínimo 3 caracteres',
            (v) => v.length <= 50 || 'Máximo 50 caracteres',
            (v) => /^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\\s]+$/.test(v) || 'Solo letras y espacios',
          ]"
          required
        />

        <v-text-field
          v-model.trim="empleado.telefono"
          label="Teléfono del empleado"
          variant="outlined"
          :rules="[
            (v) => !!v || 'Campo obligatorio',
            (v) => /^[0-9]+$/.test(v) || 'Solo números',
            (v) => v.length === 10 || 'Debe tener 10 dígitos',
          ]"
          required
        />

        <v-text-field
          v-model.trim="empleado.email"
          label="Email del empleado"
          variant="outlined"
          :rules="[
            (v) => !!v || 'El email es obligatorio',
            (v) => /.+@.+\..+/.test(v) || 'Debe ser un email válido',
            (v) => v.length <= 100 || 'Máximo 100 caracteres',
          ]"
          required
        />

        <v-select
          v-model="empleado.puesto"
          :items="puestos"
          label="Puesto"
          variant="outlined"
          :rules="[(v) => !!v || 'Seleccione un puesto']"
          required
        />

        <ButtonComponent type="submit" class="act mt-4">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Actualizar Empleado
        </ButtonComponent>
      </v-form>
    </v-card>

    <ButtonComponent class="volver mt-4" :to="{ name: 'empleados_list' }">
      <template #pre-icon>
        <Icon icon="ic:twotone-list" width="28" height="28" style="color: black" />
      </template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted, onBeforeUnmount } from 'vue'
import { useRoute } from 'vue-router'
import useEmpleadosStore from '@/stores/empleados'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
import type { Empleado } from '@/interfaces/Empleado'

const store = useEmpleadosStore()
const { empleado } = toRefs(store)
const { getOne, update } = store
const route = useRoute()
const form = ref()

const puestos = ['Limpieza', 'Cajero', 'Gerente']

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})

function limpiarEmpleado() {
  empleado.value = {
    id: 0,
    nombre: '',
    apellido: '',
    telefono: '',
    email: '',
    puesto: '',
  } as Empleado
}

const actualizar = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, corrija los errores del formulario.')
    return
  }

  try {
    const data = {
      id: empleado.value.id,
      nombre: empleado.value.nombre,
      apellido: empleado.value.apellido,
      telefono: empleado.value.telefono,
      email: empleado.value.email,
      puesto: empleado.value.puesto,
    }

    await update(data)
    alert('Empleado actualizado con éxito.')
  } catch (error) {
    console.error(error)
    alert('Hubo un error al actualizar el empleado.')
  }
}

onBeforeUnmount(() => {
  limpiarEmpleado()
})
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
