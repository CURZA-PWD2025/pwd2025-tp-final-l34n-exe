<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" variant="outlined">
      <v-card-title class="text-h6 text-center">Actualizar Empleado</v-card-title>
      <v-form @submit.prevent="actualizar" ref="form">
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
          label="Categoría"
          variant="outlined"
          :rules="[(v) => !!v || 'Seleccione una categoría']"
          required
        />
        <ButtonComponent type="submit" class="act">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Actualizar Empleado
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
import { ref, toRefs, onMounted, onBeforeUnmount } from 'vue'
import { useRoute } from 'vue-router'
import useEmpleadosStore from '@/stores/empleados'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const store = useEmpleadosStore()
const { empleado } = toRefs(store)
const { getOne, update } = store
const route = useRoute()
const puestos = ['Limpieza', 'Cajero', 'Gerente']
const form = ref()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})

const actualizar = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  } else {
    const data = {
      id: empleado.value.id,
      nombre: empleado.value.nombre,
      apellido: empleado.value.apellido,
      telefono: empleado.value.telefono,
      email: empleado.value.email,
      puesto: empleado.value.puesto,
    }
    await update(data)

    alert('Empleado ACTUALIZADO con éxito.')
  }
}
onBeforeUnmount(() => {
  store.limpiarEmpleado()
})
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
