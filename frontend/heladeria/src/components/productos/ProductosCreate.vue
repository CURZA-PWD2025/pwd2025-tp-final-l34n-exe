<template>
  <v-card class="mx-auto pa-6" max-width="500" elevation="16">
    <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>
    <v-form @submit.prevent="crear" ref="form">
      <v-text-field
        v-model="producto.nombre"
        label="Nombre del producto"
        variant="outlined"
        :rules="[
          (v) => !!v || 'El nombre es obligatorio',
          (v) => v.length <= 50 || 'Máximo 50 caracteres',
          (v) => v.length >= 5 || 'Mínimo 5 caracteres',
        ]"
        required
      ></v-text-field>
      <v-text-field
        v-model="producto.precio"
        label="Precio del producto"
        variant="outlined"
        :rules="[
          (v) => !!v || 'El precio es obligatorio',
          (v) => v > 0 || 'El precio debe ser mayor a 0',
        ]"
        required
      ></v-text-field>
      <v-text-field
        v-model="producto.stock"
        label="Stock del producto"
        variant="outlined"
        :rules="[
          (v) => (v !== null && v !== undefined) || 'El stock es obligatorio',
          (v) => v >= 0 || 'El stock no puede ser negativo',
        ]"
        @input="actualizarDisponibilidad"
        required
      ></v-text-field>
      <v-text-field
        v-model="producto.max_sabores"
        label="Maximo de sabores del producto"
        variant="outlined"
        :rules="[
          (v) => !!v || 'El maximo de sabores es obligatorio',
          (v) => (v >= 1 && v <= 4) || 'El maximo de sabores debe estar entre 1 y 4',
        ]"
        required
      ></v-text-field>
      <label class="chk">
        <input type="checkbox" v-model="producto.disponible" />
        Disponible?
      </label>
      <v-select
        v-model="producto.categoria"
        :items="categorias"
        item-title="nombre"
        item-value="id"
        label="Categoría"
        variant="outlined"
        :rules="[(v) => !!v || 'Seleccione una categoría']"
        return-object
      />

      <v-select
        v-model="producto.proveedor"
        :items="proveedores"
        item-title="nombre"
        item-value="id"
        label="Proveedor"
        variant="outlined"
        :rules="[(v) => !!v || 'Seleccione un proveedor']"
        return-object
      />
      <ButtonComponent type="submit" class="crear">
        <template #pre-icon>
          <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
        </template>
        Crear Producto
      </ButtonComponent>
    </v-form>
  </v-card>
  <ButtonComponent class="volver" :to="{ name: 'productos_list' }">
    <template #pre-icon
      ><Icon icon="ic:twotone-list" width="28" height="28" style="color: black"
    /></template>
    VOLVER A LA LISTA
  </ButtonComponent>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted } from 'vue'
import useProductosStore from '@/stores/productos'
import useProveedoresStore from '@/stores/proveedores'
import useCategoriasStore from '@/stores/categorias'
import type { Proveedor } from '@/interfaces/Proveedor'
import type { Categoria } from '@/interfaces/Categoria'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const productosStore = useProductosStore()
const proveedoresStore = useProveedoresStore()
const categoriasStore = useCategoriasStore()
const { producto } = toRefs(productosStore)
const { create } = productosStore
const categorias = ref<Categoria[]>([])
const proveedores = ref<Proveedor[]>([])
const form = ref()

onMounted(async () => {
  try {
    await categoriasStore.getAll()
    categorias.value = categoriasStore.categorias.filter(
      (categoria) => categoria.tipo === 'Producto',
    )

    await proveedoresStore.getAll()
    proveedores.value = proveedoresStore.proveedores
  } catch (error) {
    console.error('Error al cargar datos:', error)
  }
})

function limpiarProducto() {
  producto.value = {
    id: 0,
    proveedor: {
      id: 0,
    } as Proveedor,
    categoria: {
      id: 0,
    } as Categoria,
    stock: 0,
    max_sabores: 0,
    disponible: true,
    nombre: '',
    precio: 0,
  }
}

function actualizarDisponibilidad() {
  //* Si el stock es 0, el producto no está disponible *//
  if (producto.value.stock === 0) {
    producto.value.disponible = false
  }
}

const crear = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  }
  actualizarDisponibilidad() //* Asegura que la disponibilidad se actualice antes de crear *//
  try {
    const data = {
      nombre: producto.value.nombre,
      precio: producto.value.precio,
      stock: producto.value.stock,
      max_sabores: producto.value.max_sabores,
      disponible: producto.value.disponible,
      id_categoria: producto.value.categoria?.id,
      id_proveedor: producto.value.proveedor?.id,
    }

    await create(data)
    await productosStore.getAll()

    alert('Producto creado con éxito.')

    form.value.reset()
    limpiarProducto()
  } catch (error) {
    console.error(error)
    alert('Error al crear el producto. Por favor, intente nuevamente.')
  }
}
</script>

<style scoped>
.crear {
  text-align: center;
}
</style>
