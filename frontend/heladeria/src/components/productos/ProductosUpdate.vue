<template>
  <v-card class="mx-auto pa-6" max-width="500" variant="outlined">
    <v-card-title class="text-h6 text-center">Actualizar Producto</v-card-title>
    <v-form @submit.prevent="actualizar" ref="form">
      <v-text-field
        v-model="producto.nombre"
        label="Nombre del producto"
        variant="outlined"
        :rules="[(v) => !!v || 'El nombre es obligatorio']"
        required
      ></v-text-field>
      <v-text-field
        v-model="producto.precio"
        label="Precio del producto"
        variant="outlined"
        :rules="[(v) => !!v || 'El precio es obligatorio']"
        required
      ></v-text-field>
      <v-text-field
        v-model="producto.stock"
        label="Stock del producto"
        variant="outlined"
        :rules="[(v) => !!v || 'El stock es obligatorio']"
        required
      ></v-text-field>
      <v-text-field
        v-model="producto.max_sabores"
        label="Maximo de sabores del producto"
        variant="outlined"
        :rules="[(v) => !!v || 'El maximo de sabores es obligatorio']"
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
          (v) => !!v || 'Seleccione una categoría',
          (v) =>
            !['Vainilla', 'Chocolates', 'Menta', 'Frutales', 'Dulce de Leche', 'Agua'].includes(
              v?.nombre,
            ) || 'Esta categoría no está permitida',
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
import { ref, toRefs, onMounted } from 'vue'
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

  await proveedoresStore.getAll()
  proveedores.value = proveedoresStore.proveedores
})

const actualizar = async () => {
  const valid = await form.value?.validate()
  if (!valid) return
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
  if (
    producto.value.categoria?.nombre === 'Vainilla' ||
    producto.value.categoria?.nombre === 'Chocolates' ||
    producto.value.categoria?.nombre === 'Menta' ||
    producto.value.categoria?.nombre === 'Frutales' ||
    producto.value.categoria?.nombre === 'Agua' ||
    producto.value.categoria?.nombre === 'Dulce de Leche'
  ) {
    alert('No se puede asignar esta categoria al producto.')
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

  producto.value = {
    nombre: '',
    precio: 0,
    stock: 0,
    max_sabores: 0,
    categoria: { id: 0, nombre: '', tipo: '', descripcion: '' },
    proveedor: { id: 0, nombre: '', email: '', telefono: '' },
  }

  alert('Producto actualizado con éxito.')

  form.value.reset()
}
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
