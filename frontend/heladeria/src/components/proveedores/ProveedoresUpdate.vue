<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" variant="outlined">
      <v-card-title class="text-h6 text-center">Actualizar Proveedor</v-card-title>
      <v-form @submit.prevent="actualizar" ref="form">
        <v-text-field
          v-model="proveedor.nombre"
          label="Nombre del proveedor"
          variant="outlined"
          :rules="[(v) => !!v || 'El nombre es obligatorio']"
          required
        ></v-text-field>
        <v-text-field
          v-model="proveedor.telefono"
          label="Teléfono del proveedor"
          variant="outlined"
          :rules="[(v) => !!v || 'El teléfono es obligatorio']"
          required
        ></v-text-field>
        <v-text-field
          v-model="proveedor.email"
          label="Email del proveedor"
          variant="outlined"
          :rules="[(v) => !!v || 'El email es obligatorio']"
          required
        ></v-text-field>
        <ButtonComponent type="submit" class="act">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Actualizar Proveedor
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
import { toRefs, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import useProveedoresStore from '@/stores/proveedores'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const store = useProveedoresStore()
const { proveedor } = toRefs(store)
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
  if (!proveedor.value.nombre || !proveedor.value.telefono || !proveedor.value.email) {
    alert('Por favor, complete los campos.')
    return
  }
  const data = {
    id: proveedor.value.id,
    nombre: proveedor.value.nombre,
    telefono: proveedor.value.telefono,
    email: proveedor.value.email,
  }
  await update(data)
  proveedor.value = { nombre: '', telefono: '', email: '' }
  alert('Proveedor actualizado con éxito.')
  form.value.reset()
}
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
