<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16">
      <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>

      <v-form @submit.prevent="actualizar" ref="form">
        <v-text-field
          v-model="categoria.nombre"
          label="Nombre de la categoría"
          variant="outlined"
          :rules="[(v) => !!v || 'El nombre es obligatorio',
            (v) => v.length <= 30 || 'Máximo 30 caracteres',
            (v) => v.length >= 3 || 'Mínimo 3 caracteres',
            (v) => /^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$/.test(v) || 'Solo letras y espacios'
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
          v-model="categoria.descripcion"
          label="Descripción"
          variant="outlined"
          :rules="[(v) => !!v || 'La descripción es obligatoria',
            (v) => /^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$/.test(v) || 'Solo letras y espacios',
            (v) => v.length >= 10 || 'Mínimo 10 caracteres',
            (v) => v.length <= 100 || 'Máximo 100 caracteres'
          ]"
          required
        />
        <ButtonComponent type="submit" class="act">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Actualizar Categoría
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
import { ref, toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useCategoriasStore from '@/stores/categorias'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
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

const actualizar = async () => {
  const valid = await form.value?.validate()
  if (!valid) return
  if (!categoria.value.nombre || !categoria.value.tipo || !categoria.value.descripcion) {
    alert('Por favor, complete los campos.')
    return
  }else {
    const data = {
      id: categoria.value.id,
      nombre: categoria.value.nombre,
      tipo: categoria.value.tipo,
      descripcion: categoria.value.descripcion,
    }
    await update(data)
    categoria.value = {
      nombre: '',
      tipo: '',
      descripcion: '',
    }
    alert('Categoría creada con éxito.')
    form.value.reset()
  }}
</script>

<style scoped>
.act{
  text-align: center;
}
</style>
