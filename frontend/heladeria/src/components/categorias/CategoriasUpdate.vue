<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16" color="aliceblue">
      <v-card-title class="text-h6 text-center">ACTUALIZAR CATEGORÍA</v-card-title>

      <v-form @submit.prevent="actualizar" ref="form">
        <v-text-field
          v-model.trim="categoria.nombre"
          label="Nombre de la categoría"
          variant="outlined"
          :rules="[
            (v) => !!v || 'El nombre es obligatorio',
            (v) => v.length >= 3 || 'Mínimo 3 caracteres',
            (v) => v.length <= 30 || 'Máximo 30 caracteres',
            (v) => /^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$/.test(v) || 'Solo letras y espacios',
          ]"
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
          v-model.trim="categoria.descripcion"
          label="Descripción"
          variant="outlined"
          :rules="[
            (v) => !!v || 'La descripción es obligatoria',
            (v) => v.length >= 10 || 'Mínimo 10 caracteres',
            (v) => v.length <= 100 || 'Máximo 100 caracteres',
          ]"
          required
        />
        <ButtonComponent type="submit" class="act mt-4">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="26" height="26" style="color: #05f036" />
          </template>
          Actualizar Categoría
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
import { ref, toRefs, onMounted, onBeforeUnmount } from 'vue'
import { useRoute } from 'vue-router'
import useCategoriasStore from '@/stores/categorias'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
import type { Categoria } from '@/interfaces/Categoria'

const store = useCategoriasStore()
const { categoria } = toRefs(store)
const { getOne, update } = store
const route = useRoute()
const form = ref()
const tipos = ['Producto', 'Sabor']

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})

function limpiarCategoria() {
  categoria.value = {
    id: 0,
    nombre: '',
    tipo: '',
    descripcion: '',
  } as Categoria
}

const actualizar = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, corrija los errores del formulario.')
    return
  }

  try {
    const data = {
      id: categoria.value.id,
      nombre: categoria.value.nombre,
      tipo: categoria.value.tipo,
      descripcion: categoria.value.descripcion,
    }
    await update(data)
    alert('Categoría ACTUALIZADA con éxito.')
  } catch (error) {
    console.error(error)
    alert('Error al actualizar la categoría.')
  }
}

onBeforeUnmount(() => {
  limpiarCategoria()
})
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
