<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" variant="outlined">
      <v-card-title class="text-h6 text-center">Actualizar Sabor</v-card-title>
      <v-form @submit.prevent="actualizar" ref="form">
        <v-text-field
          v-model="sabor.nombre"
          label="Nombre del sabor"
          variant="outlined"
          :rules="[(v) => !!v || 'El nombre es obligatorio']"
          required
        ></v-text-field>
        <v-text-field
          v-model.number="sabor.stock"
          label="Stock"
          type="number"
          variant="outlined"
          :rules="[(v) => v >= 0 || 'Stock inválido']"
          required
        ></v-text-field>
        <v-select
          v-model="sabor.categoria"
          :items="categorias"
          item-title="nombre"
          item-value="id"
          label="Categoría"
          variant="outlined"
          :rules="[
            (v) => !!v || 'Seleccione una categoría',
            (v) =>
              !['Vasos', 'Potes', 'Cucuruchos', 'Paletas', 'Tortas', 'Batidos', 'Bebidas'].includes(
                v?.nombre,
              ) || 'Esta categoría no está permitida',
          ]"
          required
        ></v-select>

        <div>
          <label for="disponible">Disponible:</label>
          <input
            type="checkbox"
            name="disponible"
            v-model="sabor.disponible"
            :true-value="1"
            :false-value="0"
          />
        </div>

        <ButtonComponent type="submit" class="act">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Actualizar Sabor
        </ButtonComponent>
      </v-form>
    </v-card>
    <ButtonComponent class="volver" :to="{ name: 'sabores_list' }">
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
import useSaboresStore from '@/stores/sabores'
import useCategoriasStore from '@/stores/categorias'
import type { Categoria } from '@/interfaces/Categoria'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const form = ref()
const saboresStore = useSaboresStore()
const categoriasStore = useCategoriasStore()
const { sabor } = toRefs(saboresStore)
const { getOne, update } = saboresStore
const categorias = ref(<Categoria[]>[])
const route = useRoute()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) await getOne(id)

  await categoriasStore.getAll()
  categorias.value = categoriasStore.categorias
})

const actualizar = async () => {
  const valid = await form.value?.validate()
  if (!valid) return

  if (!sabor.value.nombre || !sabor.value.stock || !sabor.value.categoria?.id) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  }
  if (
    sabor.value.categoria?.nombre === 'Vasos' ||
    sabor.value.categoria?.nombre === 'Potes' ||
    sabor.value.categoria?.nombre === 'Tortas' ||
    sabor.value.categoria?.nombre === 'Batidos' ||
    sabor.value.categoria?.nombre === 'Bebidas' ||
    sabor.value.categoria?.nombre === 'Paletas' ||
    sabor.value.categoria?.nombre === 'Cucuruchos'
  ) {
    alert('No se puede asignar esta categoria al sabor.')
    return
  }

  const data = {
    id: sabor.value.id,
    nombre: sabor.value.nombre,
    stock: sabor.value.stock,
    disponible: sabor.value.disponible ? 1 : 0,
    id_categoria: sabor.value.categoria?.id,
  }

  await update(data)

  sabor.value = {
    nombre: '',
    stock: 0,
    disponible: 1,
    categoria: { id: 0, nombre: '', tipo: '', descripcion: '' },
  }

  alert('Sabor actualizado con éxito.')

  form.value.reset()
}
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
