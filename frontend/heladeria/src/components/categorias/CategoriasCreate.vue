<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16">
      <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>

      <v-form @submit.prevent="crear" ref="form">
        <v-text-field
          v-model="categoria.nombre"
          label="Nombre de la categoría"
          variant="outlined"
          :rules="[(v) => !!v || 'El nombre es obligatorio']"
          required
        />
        <v-select
          v-model="categoria.tipo"
          :items="tipos"
          label="Tipo de categoría"
          variant="outlined"
          :rules="[(v) => !!v || 'El tipo es obligatorio']"
          required
        />
        <v-text-field
          v-model="categoria.descripcion"
          label="Descripción"
          variant="outlined"
          :rules="[(v) => !!v || 'La descripción es obligatoria']"
          required
        />
        <ButtonComponent type="submit">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Crear Categoría
        </ButtonComponent>
      </v-form>
    </v-card>
    <ButtonComponent class="volver" :to="{ name: 'categorias_list' }">
      <template #pre-icon
        ><Icon icon="ic:twotone-list" width="28" height="28" style="color: black"
      /></template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs } from 'vue'
import useCategoriasStore from '@/stores/categorias'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const store = useCategoriasStore()
const { categoria } = toRefs(store)
const { create } = store

const form = ref()
const tipos = ['Producto', 'Sabor']

const crear = async () => {
  const valid = await form.value?.validate()
  if (!valid) return

  if (!categoria.value.nombre || !categoria.value.tipo || !categoria.value.descripcion) {
    alert('Complete todos los campos.')
    return
  } else {
    const data = {
      nombre: categoria.value.nombre,
      tipo: categoria.value.tipo,
      descripcion: categoria.value.descripcion,
    }
    await create(data)
    categoria.value = {
      nombre: '',
      tipo: '',
      descripcion: '',
    }
    alert('Categoría creada con éxito.')
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
