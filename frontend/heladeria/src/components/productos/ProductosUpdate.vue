<template>
  <div>
    <h3>ProductosUpdate</h3>
    <div>
      <form @submit.prevent="actualizar">
        <div>
          <label for="nombre">Nombre:</label>
          <input type="text" name="nombre" v-model="producto.nombre" />
        </div>

        <div>
          <label for="precio">Precio:</label>
          <input type="number" name="precio" v-model.number="producto.precio" />
        </div>

        <div>
          <label for="stock">Stock:</label>
          <input type="number" name="stock" v-model.number="producto.stock" />
        </div>

        <div>
          <label for="max_sabores">Max Sabores:</label>
          <input type="number" name="max_sabores" v-model.number="producto.max_sabores" />
        </div>

        <div>
          <label for="categoria">Categoría:</label>
          <select v-model="producto.categoria" required>
            <option disabled value="">Seleccione una categoría</option>
            <option v-for="categoria in categorias" :key="categoria.id" :value="categoria">
              {{ categoria.nombre }}
            </option>
          </select>
        </div>

        <div>
          <label for="proveedor">Proveedor:</label>
          <select v-model="producto.proveedor" required>
            <option disabled value="">Seleccione un proveedor</option>
            <option v-for="proveedor in proveedores" :key="proveedor.id" :value="proveedor">
              {{ proveedor.nombre }}
            </option>
          </select>
        </div>

        <button type="submit">Actualizar Producto</button>
      </form>
    </div>
    <RouterLink :to="{ name: 'productos_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useProductosStore from '@/stores/productos'
import useProveedoresStore from '@/stores/proveedores'
import useCategoriasStore from '@/stores/categorias'
import type { Proveedor } from '@/interfaces/Proveedor'
import type { Categoria } from '@/interfaces/Categoria'

const productosStore = useProductosStore()
const proveedoresStore = useProveedoresStore()
const categoriasStore = useCategoriasStore()
const { producto } = toRefs(productosStore)
const { getOne, update } = productosStore
const route = useRoute()
const categorias = ref(<Categoria[]>[])
const proveedores = ref(<Proveedor[]>[])

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) await getOne(id)

  await categoriasStore.getAll()
  categorias.value = categoriasStore.categorias

  await proveedoresStore.getAll()
  proveedores.value = proveedoresStore.proveedores
})

const actualizar = async () => {
  if (
    !producto.value.nombre ||
    !producto.value.precio ||
    !producto.value.stock ||
    producto.value.max_sabores < 1 ||
    producto.value.max_sabores > 4 ||
    !producto.value.categoria?.id ||
    !producto.value.proveedor?.id
  ) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  }

  const data = {
    id: producto.value.id,
    nombre: producto.value.nombre,
    precio: producto.value.precio,
    stock: producto.value.stock,
    max_sabores: producto.value.max_sabores,
    id_categoria: producto.value.categoria?.id,
    id_proveedor: producto.value.proveedor?.id,
  }

  await update(data)

  alert('Producto actualizado con éxito.')
}
</script>

<style scoped></style>
