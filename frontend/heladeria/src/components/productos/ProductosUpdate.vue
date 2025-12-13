<template>
  <v-card class="mx-auto pa-6" max-width="500" elevation="16">
    <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>
    <v-form @submit.prevent="actualizar" ref="form">
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
          (v) => !!v || 'El stock es obligatorio',
          (v) => v > 0 || 'El stock no puede ser negativo o cero',
        ]"
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
      <v-select
        v-model="producto.categoria"
        :items="categorias"
        item-title="nombre"
        item-value="id"
        label="Categoría"
        variant="outlined"
        :rules="[
          (v) => !!v || 'Seleccione una categoría'
        ]"
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
      <ButtonComponent type="submit" class="act">
        <template #pre-icon>
          <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
        </template>
        Actualizar Producto
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
import { ref, toRefs, onMounted, onBeforeUnmount } from 'vue'
import { useRoute } from 'vue-router'
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
const { getOne, update } = productosStore
const route = useRoute()
const categorias = ref(<Categoria[]>[])
const proveedores = ref(<Proveedor[]>[])
const form = ref()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) await getOne(id)

  await categoriasStore.getAll()
  categorias.value = categoriasStore.categorias

  categorias.value = categoriasStore.categorias.filter(
    (categoria) => categoria.tipo === "Producto"
  )

  await proveedoresStore.getAll()
  proveedores.value = proveedoresStore.proveedores
})

const actualizar = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  } else {
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

    alert('Producto ACTUALIZADO con éxito.')
  }
}
onBeforeUnmount(() => {
  productosStore.limpiarProducto()
})
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
