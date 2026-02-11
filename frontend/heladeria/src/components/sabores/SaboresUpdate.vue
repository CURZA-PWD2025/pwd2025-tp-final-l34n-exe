<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16" color="aliceblue">
      <v-card-title class="text-h6 text-center">ACTUALIZAR SABOR</v-card-title>

      <v-form @submit.prevent="actualizar" ref="form">
        <v-text-field
          v-model.trim="sabor.nombre"
          label="Nombre del sabor"
          variant="outlined"
          :rules="[
            (v) => !!v || 'El nombre es obligatorio',
            (v) => v.length >= 3 || 'Mínimo 3 caracteres',
            (v) => v.length <= 50 || 'Máximo 50 caracteres',
            (v) => /^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\\s]+$/.test(v) || 'Solo letras y espacios',
          ]"
          required
        />

        <v-text-field
          v-model.number="sabor.stock"
          label="Stock"
          type="number"
          variant="outlined"
          :rules="[
            (v) => (v !== null && v !== undefined) || 'El stock es obligatorio',
            (v) => Number.isInteger(v) || 'El stock debe ser un número entero',
            (v) => v >= 0 || 'Stock inválido',
          ]"
          required
        />

        <v-select
          v-model="sabor.categoria"
          :items="categorias"
          item-title="nombre"
          item-value="id"
          label="Categoría"
          variant="outlined"
          :rules="[(v) => !!v || 'Seleccione una categoría']"
          return-object
          required
        />

        <label class="chk">
          <input type="checkbox" v-model="sabor.disponible" class="chkbox" />
          ¿Disponible?
        </label>

        <ButtonComponent type="submit" class="act mt-4">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="26" height="26" style="color: #05f036" />
          </template>
          Actualizar Sabor
        </ButtonComponent>
      </v-form>
    </v-card>

    <ButtonComponent class="volver mt-4" :to="{ name: 'sabores_list' }">
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
import useSaboresStore from '@/stores/sabores'
import useCategoriasStore from '@/stores/categorias'
import type { Categoria } from '@/interfaces/Categoria'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const saboresStore = useSaboresStore()
const categoriasStore = useCategoriasStore()

const { sabor } = toRefs(saboresStore)
const { getOne, update } = saboresStore

const categorias = ref<Categoria[]>([])
const route = useRoute()
const form = ref()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) await getOne(id)

  await categoriasStore.getAll()
  categorias.value = categoriasStore.categorias.filter((categoria) => categoria.tipo === 'Sabor')

  if (!sabor.value.categoria) {
    sabor.value.categoria = { id: 0 } as Categoria
  }
})

function limpiarSabor() {
  sabor.value = {
    id: 0,
    nombre: '',
    stock: 0,
    disponible: true,
    categoria: { id: 0 } as Categoria,
  }
}

const actualizar = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  }

  try {
    const data = {
      id: sabor.value.id,
      nombre: sabor.value.nombre,
      stock: sabor.value.stock,
      disponible: sabor.value.disponible ? 1 : 0,
      id_categoria: sabor.value.categoria?.id,
    }

    await update(data)
    alert('Sabor actualizado con éxito.')
  } catch (error) {
    console.error(error)
    alert('Error al actualizar el sabor. Por favor, intente nuevamente.')
  }
}

onBeforeUnmount(() => {
  limpiarSabor()
})
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
