<template>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16">
    <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>

      <v-form @submit.prevent="crear" ref="form">
        <v-text-field
          v-model="cliente.nombre"
          label="Nombre del cliente"
          variant="outlined"
          :rules="[(v) => !!v || 'El nombre es obligatorio']"
          required
        ></v-text-field>
        <v-text-field
          v-model="cliente.apellido"
          label="Apellido del cliente"
          variant="outlined"
          :rules="[(v) => !!v || 'El apellido es obligatorio']"
          required
        ></v-text-field>
        <v-text-field
          v-model="cliente.telefono"
          label="Telefono del cliente"
          variant="outlined"
          :rules="[(v) => !!v || 'El telefono es obligatorio']"
          required
        ></v-text-field>
        <v-text-field
          v-model="cliente.direccion"
          label="Dirección del cliente"
          variant="outlined"
          :rules="[(v) => !!v || 'La dirección es obligatorio']"
          required
        ></v-text-field>
        <ButtonComponent type="submit">
        <template #pre-icon>
          <Icon icon="mdi-light:check" width="28" height="28"  style="color: #05f036" />
        </template>
        Crear Cliente
      </ButtonComponent>
      </v-form>
    </v-card>
    <ButtonComponent class="volver" :to="{ name: 'clientes_list' }">
      <template #pre-icon><Icon icon="ic:twotone-list" width="28" height="28"  style="color: black" /></template>
      VOLVER A LA LISTA
    </ButtonComponent>
</template>

<script setup lang="ts">
import { ref, toRefs } from 'vue'
import useClientesStore from '@/stores/clientes'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const store = useClientesStore()
const { cliente } = toRefs(store)
const { create } = store
const form = ref()
const crear = async () => {
  const valid = await form.value?.validate()
  if (!valid) return
  if (
    !cliente.value.nombre ||
    !cliente.value.telefono ||
    !cliente.value.apellido ||
    !cliente.value.direccion
  ) {
    alert('Por favor, complete todos los campos.')
    return
  } else {
    const data={
      nombre: cliente.value.nombre,
      apellido: cliente.value.apellido,
      telefono: cliente.value.telefono,
      direccion: cliente.value.direccion
    }
    await create(data)
    cliente.value = { nombre: '', telefono: '', apellido: '', direccion: '' }
    alert('Cliente creado con éxito.')
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
