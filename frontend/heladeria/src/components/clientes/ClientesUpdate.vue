<template>
  <v-card class="mx-auto pa-6" max-width="500" variant="outlined">
    <v-card-title class="text-h6 text-center">Actualizar Cliente</v-card-title>
    <v-form @submit.prevent="actualizar" ref="form">
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
      <ButtonComponent type="submit" class="act">
        <template #pre-icon>
          <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
        </template>
        Actualizar Cliente
      </ButtonComponent>
    </v-form>
  </v-card>
  <ButtonComponent class="volver" :to="{ name: 'clientes_list' }">
    <template #pre-icon
      ><Icon icon="ic:twotone-list" width="28" height="28" style="color: black"
    /></template>
    VOLVER A LA LISTA
  </ButtonComponent>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useClientesStore from '@/stores/clientes'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const store = useClientesStore()
const { cliente } = toRefs(store)
const { getOne, update } = store
const route = useRoute()
const form = ref()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})

const actualizar = async () => {
  const valid = await form.value?.validate()
  if (!valid) return
  if (
    !cliente.value.nombre ||
    !cliente.value.apellido ||
    !cliente.value.telefono ||
    !cliente.value.direccion
  ) {
    alert('Por favor, complete los campos.')
    return
  } else {
    const data = {
      id: cliente.value.id,
      nombre: cliente.value.nombre,
      apellido: cliente.value.apellido,
      telefono: cliente.value.telefono,
      direccion: cliente.value.direccion,
    }
    await update(data)
    alert('Cliente actualizado con éxito.')
    form.value.reset()
  }
}
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
