<template>
  <v-card class="mx-auto pa-6" max-width="500" elevation="16">
    <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>

    <v-form @submit.prevent="actualizar" ref="form">
      <v-text-field
        v-model="cliente.nombre"
        label="Nombre del cliente"
        variant="outlined"
        :rules="[
          (v) => !!v || 'El nombre es obligatorio',
          (v) => v.length >= 4 || 'Mínimo 4 caracteres',
          (v) => v.length <= 30 || 'Máximo 30 caracteres',
        ]"
        required
      ></v-text-field>
      <v-text-field
        v-model="cliente.apellido"
        label="Apellido del cliente"
        variant="outlined"
        :rules="[
          (v) => !!v || 'El apellido es obligatorio',
          (v) => v.length >= 4 || 'Mínimo 4 caracteres',
          (v) => v.length <= 50 || 'Máximo 50 caracteres',
        ]"
        required
      ></v-text-field>
      <v-text-field
        v-model="cliente.telefono"
        label="Teléfono del cliente"
        variant="outlined"
        :rules="[
          (v) => !!v || 'Campo obligatorio',
          (v) => /^[0-9]+$/.test(v) || 'Solo números',
          (v) => v.length === 10 || 'Debe tener 10 dígitos',
        ]"
        required
      ></v-text-field>
      <v-text-field
        v-model="cliente.direccion"
        label="Dirección del cliente"
        variant="outlined"
        :rules="[
          (v) => !!v || 'La dirección es obligatorio',
          (v) => v.length >= 10 || 'Mínimo 10 caracteres',
          (v) => v.length <= 100 || 'Máximo 100 caracteres',
        ]"
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
import { ref, toRefs, onMounted, onBeforeUnmount } from 'vue'
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

function limpiarCliente(){
    cliente.value = {
      id: 0,
      nombre: '',
      apellido: '',
      telefono: '',
      direccion: ''
    }
  }

const actualizar = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, corrija los errores en el formulario.')
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

    alert('Cliente ACTUALIZADO con éxito.')
  }
}

onBeforeUnmount(() => {
  limpiarCliente()
})
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
