<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16" color="aliceblue">
      <v-card-title class="text-h6 text-center">CREAR CATEGORÍA</v-card-title>

      <v-form @submit.prevent="crear" ref="form">
        <v-text-field
          v-model.trim="categoria.nombre"
          label="Nombre de la categoría"
          variant="outlined"
          :rules="[
            (v: string) => !!v || 'El nombre es obligatorio',
            (v: string) => v.length >= 3 || 'Mínimo 3 caracteres',
            (v: string) => v.length <= 30 || 'Máximo 30 caracteres',
            (v: string) => /^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$/.test(v) || 'Solo letras y espacios',
          ]"
          required
        />

        <v-select
          v-model="categoria.tipo"
          :items="tipos"
          label="Tipo de categoría"
          variant="outlined"
          :rules="[(v: string) => !!v || 'El tipo es obligatorio']"
          required
        />

        <v-text-field
          v-model.trim="categoria.descripcion"
          label="Descripción"
          variant="outlined"
          :rules="[
            (v: string) => !!v || 'La descripción es obligatoria',
            (v: string) => v.length >= 10 || 'Mínimo 10 caracteres',
            (v: string) => v.length <= 100 || 'Máximo 100 caracteres',
          ]"
          required
        />

        <ButtonComponent type="submit" class="crear mt-4">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Crear Categoría
        </ButtonComponent>
      </v-form>
    </v-card>

    <ButtonComponent class="volver mt-4" :to="{ name: 'categorias_list' }">
      <template #pre-icon>
        <Icon icon="ic:twotone-list" width="28" height="28" style="color: black" />
      </template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs } from 'vue'
import useCategoriasStore from '@/stores/categorias'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
import type { Categoria } from '@/interfaces/Categoria'

const store = useCategoriasStore()
const { categoria } = toRefs(store)
const { create } = store

const form = ref()
const tipos = ['Producto', 'Sabor']

function limpiarCategoria() {
  categoria.value = {
    id: 0,
    nombre: '',
    tipo: '',
    descripcion: '',
  } as Categoria
}

const crear = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  }

  try {
    const data = {
      nombre: categoria.value.nombre,
      tipo: categoria.value.tipo,
      descripcion: categoria.value.descripcion,
    }
    await create(data)
    alert('Categoría creada con éxito.')

    form.value.reset()
    limpiarCategoria()
  } catch (error) {
    console.error(error)
    alert('Error al crear la categoría.')
  }
}
</script>

<style scoped>
.crear {
  text-align: center;
}
</style>
