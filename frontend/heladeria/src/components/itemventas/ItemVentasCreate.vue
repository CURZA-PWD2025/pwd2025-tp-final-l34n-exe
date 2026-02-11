<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16" color="aliceblue">
      <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>
      <v-alert v-if="ventaCerrada" type="warning" variant="tonal" class="mb-4">
        Esta venta está cerrada. No se pueden agregar ítems.
      </v-alert>

      <v-form @submit.prevent="crear" ref="form">
        <v-text-field
          v-model.number="itemventa.cantidad"
          label="Cantidad"
          type="number"
          variant="outlined"
          :rules="[
            (v) => !!v || 'La cantidad es obligatoria',
            (v) => v > 0 || 'Debe ser mayor a 0',
            (v) => Number.isInteger(Number(v)) || 'Debe ser un número entero',
            (v) =>
              itemventa.producto && v <= itemventa.producto.stock
                ? true
                : 'La cantidad no puede superar el stock disponible',
          ]"
          required
        />

        <v-select
          v-model="itemventa.producto"
          :items="productos"
          label="Producto"
          variant="outlined"
          return-object
          :rules="[(v) => !!v || 'Debe elegir un producto']"
          required
        >
          <template #item="{ props, item }">
            <v-list-item
              v-bind="props"
              :title="item.raw.nombre"
              :subtitle="`Precio: $${item.raw.precio} | Stock: ${item.raw.stock}`"
              :disabled="item.raw.stock === 0"
            />
          </template>
          <template #selection="{ item }">
            {{ item.raw.nombre }}
          </template>
        </v-select>

        <v-select
          v-model="itemventa.venta"
          :items="ventas"
          :rules="[(v) => v?.id > 0 || 'Debe seleccionar una venta válida']"
          item-title="id"
          item-value="id"
          label="Venta"
          variant="outlined"
          return-object
          @update:model-value="verificarVentaCerrada"
        >
          <template #item="{ props, item }">
            <v-list-item
              v-bind="props"
              :title="`Venta #${item.raw.id}`"
              :disabled="item.raw.estado === 'cerrada'"
            />
          </template>

          <template #selection="{ item }">
            Venta #{{ item.raw.id }} - {{ item.raw.fecha }}
          </template>
        </v-select>

        <v-text-field
          v-model="itemventa.subtotal"
          label="Subtotal"
          type="number"
          variant="outlined"
          :readonly="true"
        />

        <ButtonComponent type="submit" class="crear mt-4">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Crear Item
        </ButtonComponent>
      </v-form>
    </v-card>

    <ButtonComponent class="volver mt-4" :to="{ name: 'itemventas_list' }">
      <template #pre-icon>
        <Icon icon="ic:twotone-list" width="28" height="28" style="color: black" />
      </template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted, onBeforeUnmount, watch } from 'vue'
import { computed } from 'vue'
import useItemVentasStore from '@/stores/itemventas'
import useProductosStore from '@/stores/productos'
import useVentasStore from '@/stores/ventas'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
import type { Producto } from '@/interfaces/Producto'
import type { Venta } from '@/interfaces/Venta'
import type { ItemVenta } from '@/interfaces/ItemVenta'

const itemventastore = useItemVentasStore()
const productostore = useProductosStore()
const ventastore = useVentasStore()
const { itemventa } = toRefs(itemventastore)
const { create } = itemventastore

const productos = ref<Producto[]>([])
const ventas = ref<Venta[]>([])
const form = ref()

//* Verificar si la venta seleccionada está cerrada *//
const ventaCerrada = computed(() => itemventa.value.venta?.estado === 'cerrada')

onMounted(async () => {
  await productostore.getAll()
  productos.value = productostore.productos

  await ventastore.getAll()
  ventas.value = ventastore.ventas
})

//* Verificar si la venta está cerrada *//
function verificarVentaCerrada(ventaSeleccionada: Venta | undefined) {
  if (!ventaSeleccionada) return

  if (ventaSeleccionada.estado === 'cerrada') {
    alert('⚠️ Esta venta está cerrada. No se pueden agregar más ítems.')
    itemventa.value.venta = { id: 0 } as Venta
  }
}

watch(
  () => [itemventa.value.cantidad, itemventa.value.producto],
  () => {
    const cantidad = itemventa.value.cantidad ?? 0
    const precio = itemventa.value.producto?.precio ?? 0
    itemventa.value.subtotal = cantidad * precio
  },
)

function limpiarItemVenta() {
  itemventa.value = {
    id: 0,
    cantidad: 0,
    subtotal: 0,
    producto: { id: 0, precio: 0 } as Producto,
    venta: { id: 0 } as Venta,
  } as ItemVenta
}

const crear = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  }

  try {
    const idVenta = itemventa.value.venta?.id ?? 0
    if (idVenta <= 0) {
      alert('Debe seleccionar una venta válida.')
      return
    }

    if (itemventa.value.venta?.estado === 'cerrada') {
      alert('No se pueden agregar ítems a una venta cerrada.')
      return
    }

    const data = {
      cantidad: itemventa.value.cantidad,
      id_producto: itemventa.value.producto?.id,
      id_venta: idVenta,
    }

    await create(data)

    alert('Item agregado correctamente.')

    form.value.reset()
    limpiarItemVenta()
  } catch (error) {
    console.error(error)
    alert('Error al crear el item de venta.')
  }
}

onBeforeUnmount(() => {
  limpiarItemVenta()
})
</script>

<style scoped>
.crear {
  text-align: center;
}
</style>
