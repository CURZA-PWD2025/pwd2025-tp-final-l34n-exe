<template>
  <v-card class="mx-auto pa-6" max-width="500" color="aliceblue" elevation="16">
    <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>
    <v-form @submit.prevent="actualizar" ref="form">
      <v-text-field
        v-model="itemventa.cantidad"
        label="Cantidad"
        type="number"
        variant="outlined"
        :rules="[(v) => !!v || 'La cantidad es obligatoria']"
        required
      />
      <v-select
        v-model="itemventa.producto"
        :items="productos"
        label="Producto"
        variant="outlined"
        return-object
        :rules="[(v) => !!v || 'Debe elegir un producto']"
      >
        <template #item="{ props, item }">
          <v-list-item
            v-bind="props"
            :title="item.raw.nombre"
            :subtitle="`Precio: $${item.raw.precio}`"
          />
        </template>
        <template #selection="{ item }">
          {{ item.raw.nombre }}
        </template>
      </v-select>
      <v-select
        v-model="itemventa.venta"
        :items="ventas"
        label="Venta"
        variant="outlined"
        return-object
        :rules="[(v) => !!v || 'Debe elegir una venta']"
      >
        <template #item="{ props, item }">
          <v-list-item
            v-bind="props"
            :title="`Venta #${item.raw.id}`"
          />
        </template>
        <template #selection="{ item }">
          Venta #{{ item.raw.id }} - {{ item.raw.fecha }}
        </template>
      </v-select>

      <ButtonComponent type="submit" class="act">
        <template #pre-icon>
          <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
        </template>
        Actualizar Item
      </ButtonComponent>
    </v-form>
  </v-card>

  <ButtonComponent class="volver" :to="{ name: 'itemventas_list' }">
    <template #pre-icon>
      <Icon icon="ic:twotone-list" width="28" height="28" style="color: black" />
    </template>
    VOLVER A LA LISTA
  </ButtonComponent>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
import useItemVentasStore from '@/stores/itemventas'
import useProductosStore from '@/stores/productos'
import useVentasStore from '@/stores/ventas'
import type { Producto } from '@/interfaces/Producto'
import type { Venta } from '@/interfaces/Venta'
const itemventastore = useItemVentasStore()
const productostore = useProductosStore()
const ventastore = useVentasStore()
const { itemventa } = toRefs(itemventastore)
const route = useRoute()
const form = ref()

const { getOne, update } = itemventastore

const productos = ref(<Producto[]>[])
const ventas = ref(<Venta[]>[])

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) await getOne(id)

  await productostore.getAll()
  productos.value = productostore.productos

  await ventastore.getAll()
  ventas.value = ventastore.ventas
})

const actualizar = async () => {
  const valid = await form.value?.validate()
  if (!valid) return

  if (!itemventa.value.cantidad || !itemventa.value.producto?.id || !itemventa.value.venta?.id) {
    alert('Por favor, complete todos los campos.')
    return
  } else {
    const data = {
      id: itemventa.value.id,
      cantidad: itemventa.value.cantidad,
      id_producto: itemventa.value.producto?.id,
      id_venta: itemventa.value.venta?.id,
    }
    await update(data)

    itemventa.value = {
      cantidad: 0,
      producto: {
        id: 0,
        nombre: '',
        precio: 0,
        stock: 0,
        max_sabores: 0,
        proveedor: { id: 0, nombre: '', email: '', telefono: '' },
        categoria: { id: 0, nombre: '', tipo: '', descripcion: '' },
      },
      venta: {
        fecha: '',
        total: 0,
        cliente: { id: 0, nombre: '', apellido: '', direccion: '', telefono: '' },
        empleado: { id: 0, nombre: '', apellido: '', telefono: '', email: '', puesto: '' },
      },
    }

    alert('Item de venta actualizado con éxito.')

    form.value.reset()
  }
}
</script>

<style scoped>
.act{
  text-align: center;
}
</style>
