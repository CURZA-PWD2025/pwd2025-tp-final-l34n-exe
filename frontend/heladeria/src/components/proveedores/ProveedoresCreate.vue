<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16">
      <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>
      <v-form @submit.prevent="crear" ref="form">
        <v-text-field
          v-model="proveedor.nombre"
          label="Nombre del proveedor"
          variant="outlined"
          :rules="[
            (v) => !!v || 'El nombre es obligatorio',
            (v) => v.length >= 3 || 'Mínimo 3 caracteres',
            (v) => v.length <= 20 || 'Máximo 20 caracteres',
          ]"
          required
        ></v-text-field>
        <v-text-field
          v-model="proveedor.telefono"
          label="Teléfono del proveedor"
          variant="outlined"
          :rules="[
            (v) => !!v || 'El teléfono es obligatorio',
            (v) => /^[0-9]+$/.test(v) || 'Solo números',
            (v) => v.length === 10 || 'Debe tener 10 dígitos',
          ]"
          required
        />
        <v-text-field
          v-model="proveedor.email"
          label="Email del proveedor"
          variant="outlined"
          :rules="[
            (v) => !!v || 'El email es obligatorio',
            (v) => /.+@.+\..+/.test(v) || 'Email inválido',
          ]"
          required
        ></v-text-field>
        <ButtonComponent type="submit" class="act">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Crear Proveedor
        </ButtonComponent>
      </v-form>
    </v-card>
    <ButtonComponent class="volver" :to="{ name: 'proveedores_list' }">
      <template #pre-icon
        ><Icon icon="ic:twotone-list" width="28" height="28" style="color: black"
      /></template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs } from 'vue'
import useProveedoresStore from '@/stores/proveedores'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const store = useProveedoresStore()
const { proveedor } = toRefs(store)
const { create } = store
const form = ref()

const crear = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  }else{
    const data = {
    nombre: proveedor.value.nombre,
    telefono: proveedor.value.telefono,
    email: proveedor.value.email,
  }
  await create(data)

  alert('Proveedor creado con éxito.')

  form.value.reset()
  }
}
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
