<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16">
      <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>

      <v-form @submit.prevent="actualizar" ref="form">
        <v-text-field
          v-model="categoria.nombre"
          label="Nombre de la categoría"
          variant="outlined"
          :rules="[
            (v) => !!v || 'El nombre es obligatorio',
            (v) => v.length <= 30 || 'Máximo 30 caracteres',
            (v) => v.length >= 3 || 'Mínimo 3 caracteres',
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
          :disabled="desabilitar()"
          required
        >
        </v-select>

        <v-text-field
          v-model="categoria.descripcion"
          label="Descripción"
          variant="outlined"
          :rules="[
            (v) => !!v || 'La descripción es obligatoria',
            (v) => v.length >= 10 || 'Mínimo 10 caracteres',
            (v) => v.length <= 100 || 'Máximo 100 caracteres',
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
import { ref, toRefs, onMounted, onBeforeUnmount } from 'vue'
import { useRoute } from 'vue-router'
import { Icon } from '@iconify/vue'
import useCategoriasStore from '@/stores/categorias'
import ButtonComponent from '../ButtonComponent.vue'
import useProductosStore from '@/stores/productos'
import useSaboresStore from '@/stores/sabores'

const store = useCategoriasStore()
const { categoria } = toRefs(store)
const productostore = useProductosStore()
const { productos } = toRefs(productostore)
const saboresstore = useSaboresStore()
const { sabores } = toRefs(saboresstore)
const { getOne, update } = store
const route = useRoute()
const form = ref()
const tipos = ['Producto', 'Sabor']

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
  productostore.getAll()
  saboresstore.getAll()

})

const desabilitar = () => {
  if (categoria.value.tipo === 'Producto') {
    const asociados = productos.value.filter((p) => p.categoria?.id === categoria.value.id)

    return asociados.length > 0
  } else if (categoria.value.tipo === 'Sabor') {
    const asociados = sabores.value.filter((s) => s.categoria?.id === categoria.value.id)

    return asociados.length > 0
  }
  return false
}

function limpiarCategoria() {
  categoria.value = {
    id: 0,
    nombre: '',
    tipo: '',
    descripcion: '',
  }
}

const actualizar = async () => {
  const valid = await form.value?.validate()
  if (!valid) {
    alert('Por favor, complete los campos.')
    return
  } else {
    const data = {
      id: categoria.value.id,
      nombre: categoria.value.nombre,
      tipo: categoria.value.tipo,
      descripcion: categoria.value.descripcion,
    }
    await update(data)

    alert('Categoría ACTUALIZADA con éxito.')
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
