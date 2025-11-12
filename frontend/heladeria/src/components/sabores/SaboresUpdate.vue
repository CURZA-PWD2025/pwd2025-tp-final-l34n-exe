<template>
  <div>
    <h3>Actualizar Sabor</h3>
    <form @submit.prevent="actualizar">
      <div>
        <label for="nombre">Nombre:</label>
        <input type="text" name="nombre" v-model="sabor.nombre" />
      </div>

      <div>
        <label for="stock">Stock:</label>
        <input type="number" name="stock" v-model.number="sabor.stock" />
      </div>

      <div>
        <label for="categoria">Categoría:</label>
        <select v-model="sabor.categoria" required>
          <option disabled value="">Seleccione una categoría</option>
          <option v-for="categoria in categorias" :key="categoria.id" :value="categoria">
            {{ categoria.nombre }}
          </option>
        </select>
      </div>

      <div>
        <label for="disponible">Disponible:</label>
        <input type="checkbox" name="disponible" v-model="sabor.disponible" />
      </div>

      <button type="submit">Actualizar Sabor</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useSaboresStore from '@/stores/sabores'
import useCategoriasStore from '@/stores/categorias'
import type { Categoria } from '@/interfaces/Categoria'

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
  if (!sabor.value.nombre || !sabor.value.stock || !sabor.value.categoria?.id) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  }

  const data = {
    id: sabor.value.id,
    nombre: sabor.value.nombre,
    stock: sabor.value.stock,
    disponible: sabor.value.disponible,
    id_categoria: sabor.value.categoria?.id
  }

  await update(data)


  alert('Sabor actualizado con éxito.')
}
</script>
