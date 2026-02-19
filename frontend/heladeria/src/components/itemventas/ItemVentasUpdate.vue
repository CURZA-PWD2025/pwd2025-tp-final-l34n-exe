<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16" color="aliceblue">
      <v-card-title class="text-h6 text-center">ACTUALIZAR ITEM DE VENTA</v-card-title>
      <!-- Alerta si la venta está cerrada -->
      <v-alert v-if="ventaCerrada" type="warning" variant="tonal" class="mb-4">
        Esta venta está cerrada. No se puede modificar este ítem.
      </v-alert>

      <v-form @submit.prevent="actualizar" ref="form" :disabled="ventaCerrada">
        <v-text-field
          v-model="itemventa.cantidad"
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
              :subtitle="getProductSubtitle(item.raw)"
              :disabled="item.raw.stock === 0"
            >
              <template #append>
                <v-chip
                  :color="item.raw.stock > 0 ? 'success' : 'error'"
                  size="small"
                  variant="tonal"
                >
                  {{ item.raw.stock > 0 ? `Stock: ${item.raw.stock}` : 'Sin stock' }}
                </v-chip>
              </template>
            </v-list-item>
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
          required
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
          readonly
        />

        <ButtonComponent type="submit" class="act mt-4" :disabled="ventaCerrada">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Actualizar Item
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
import { ref, toRefs, onMounted, onBeforeUnmount, watch, computed } from 'vue'
import { useRoute } from 'vue-router'
import useItemVentasStore from '@/stores/itemventas'
import useProductosStore from '@/stores/productos'
import useVentasStore from '@/stores/ventas'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
import type { Producto } from '@/interfaces/Producto'
import type { Venta } from '@/interfaces/Venta'

const route = useRoute()
const itemventastore = useItemVentasStore()
const productostore = useProductosStore()
const ventastore = useVentasStore()
const { itemventa } = toRefs(itemventastore)
const { getOne, update } = itemventastore

const productos = ref<Producto[]>([])
const ventas = ref<Venta[]>([])
const form = ref()

const ventaCerrada = computed(() => itemventa.value.venta?.estado === 'cerrada')

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) await getOne(id)

  await productostore.getAll()
  productos.value = productostore.productos

  await ventastore.getAll()
  ventas.value = ventastore.ventas
})

watch(
  () => [itemventa.value.cantidad, itemventa.value.producto],
  () => {
    const cantidad = itemventa.value.cantidad ?? 0
    const precio = itemventa.value.producto?.precio ?? 0
    itemventa.value.subtotal = cantidad * precio
  },
)

//* Función para obtener el subtítulo del producto según su stock *//
function getProductSubtitle(producto: Producto): string {
  if (producto.stock === 0) {
    return `Precio: $${producto.precio} | Sin stock disponible`
  }
  return `Precio: $${producto.precio} | Stock: ${producto.stock}`
}

function limpiarItemVenta() {
  itemventa.value = {
    id: 0,
    cantidad: 0,
    subtotal: 0,
    producto: { id: 0, precio: 0 } as Producto,
    venta: { id: 0 } as Venta,
  }
}

const actualizar = async () => {
  if (ventaCerrada.value) return

  const result = await form.value?.validate()
  if (!result.valid) return

  try {
    const idVenta = itemventa.value.venta?.id ?? 0

    const data = {
      id: itemventa.value.id,
      cantidad: itemventa.value.cantidad,
      id_producto: itemventa.value.producto?.id,
      id_venta: idVenta,
    }

    await update(data)
    alert('Item actualizado correctamente.')
    form.value.reset()
    limpiarItemVenta()
  } catch (error) {
    console.error(error)
    alert('Error al actualizar el item de venta.')
  }
}

onBeforeUnmount(limpiarItemVenta)
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
