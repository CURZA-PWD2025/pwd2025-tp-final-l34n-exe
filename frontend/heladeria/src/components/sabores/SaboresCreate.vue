<template>
  <div>
    <h3>Crear Sabor</h3>
    <form @submit.prevent="crear">
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

      <button type="submit">Crear Sabor</button>
    </form>

    <RouterLink :to="{ name: 'sabores_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted } from 'vue'
import useSaboresStore from '@/stores/sabores'
import useCategoriasStore from '@/stores/categorias'
import type { Categoria } from '@/interfaces/Categoria'

const saboresStore = useSaboresStore()
const categoriasStore = useCategoriasStore()

const { sabor } = toRefs(saboresStore)
const { create } = saboresStore
const categorias = ref(<Categoria[]>[])

onMounted(async () => {
  await categoriasStore.getAll()
  categorias.value = categoriasStore.categorias
})

const crear = async () => {
  if (!sabor.value.nombre || !sabor.value.stock || sabor.value.disponible || !sabor.value.categoria?.id) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  }
  const data = {
    nombre: sabor.value.nombre,
    stock: sabor.value.stock,
    disponible: sabor.value.disponible,
    id_categoria: sabor.value.categoria?.id,
  }

  await create(data)
  sabor.value = {
    nombre: '',
    stock: 0,
    disponible: true,
    categoria: { id: 0, nombre: '', tipo: '', descripcion: '' },
  }
  alert('Sabor creado con éxito.')
}
</script>

<style scoped></style>
