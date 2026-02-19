<template>
  <v-card class="mx-auto pa-6" max-width="500" color="aliceblue" elevation="16">
    <v-card-title class="text-h6 text-center mb-4">ACTUALIZAR SABOR AL ITEM</v-card-title>
    <v-alert v-if="ventaCerrada" type="warning" variant="tonal" class="mb-4">
      La venta está cerrada. No se pueden agregar sabores a este ítem.
    </v-alert>

    <v-form @submit.prevent="actualizar" ref="form">
      <v-select
        v-model="itemventasabor.itemventa"
        :items="itemventas"
        label="Item de Venta"
        variant="outlined"
        return-object
        :rules="[(v) => !!v || 'Debe elegir un item']"
        required
      >
        <template #item="{ props, item }">
          <v-list-item
            v-bind="props"
            :title="`#${item.raw.id} - ${item.raw.producto?.nombre}`"
            :subtitle="`Cantidad: ${item.raw.cantidad}`"
          />
        </template>

        <template #selection="{ item }">
          #{{ item.raw.id }} - {{ item.raw.producto?.nombre }}
        </template>
      </v-select>

      <v-select
        v-model="itemventasabor.sabor"
        :items="sabores"
        label="Sabor"
        variant="outlined"
        return-object
        :disabled="!itemventasabor.itemventa?.producto || ventaCerrada"
        :rules="[
          (v) => !!v || 'Debe elegir un sabor',
          (v) => !saborNoDisponible(v) || 'El sabor no está disponible',
          (v) => saborDisponible(v) || 'El sabor ya está asignado o no hay stock suficiente',
        ]"
        required
      >
        <template #item="{ props, item }">
          <v-list-item
            v-bind="props"
            :title="item.raw.nombre"
            :subtitle="getSubtitle(item.raw)"
            :disabled="!saborDisponible(item.raw)"
          >
            <template #append>
              <v-chip
                :color="saborDisponible(item.raw) ? 'success' : 'error'"
                size="small"
                variant="tonal"
              >
                {{ saborDisponible(item.raw) ? 'Disponible' : 'No disponible' }}
              </v-chip>
            </template>
          </v-list-item>
        </template>

        <template #selection="{ item }">
          {{ item.raw.nombre }}
        </template>
      </v-select>

      <p class="text-center mt-2">
        Sabores seleccionados:
        <strong>{{ saboresAsignados }}</strong> /
        <strong>{{ itemventasabor.itemventa?.producto?.max_sabores ?? 0 }}</strong>
      </p>

      <ButtonComponent
        type="submit"
        class="act mt-4"
        :disabled="ventaCerrada || !puedeActualizarSabor"
      >
        <template #pre-icon>
          <Icon icon="mdi-light:check" width="26" height="26" style="color: #05f036" />
        </template>
        Actualizar Sabor
      </ButtonComponent>
    </v-form>
  </v-card>

  <ButtonComponent class="volver mt-4" :to="{ name: 'itemventasabores_list' }">
    <template #pre-icon>
      <Icon icon="ic:twotone-list" width="28" height="28" style="color: black" />
    </template>
    VOLVER A LA LISTA
  </ButtonComponent>
</template>

<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref, toRefs, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import useItemVentaSaboresStore from '@/stores/itemventasabores'
import useItemVentasStore from '@/stores/itemventas'
import useSaboresStore from '@/stores/sabores'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
import type { ItemVenta } from '@/interfaces/ItemVenta'
import type { Sabor } from '@/interfaces/Sabor'

const itemventasaborestore = useItemVentaSaboresStore()
const itemventastore = useItemVentasStore()
const saborestore = useSaboresStore()
const { itemventasabor } = toRefs(itemventasaborestore)
const { getOne, update, getAll } = itemventasaborestore
const sabores = ref<Sabor[]>([])
const itemventas = ref<ItemVenta[]>([])
const route = useRoute()
const form = ref()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) await getOne(id)

  await saborestore.getAll()
  sabores.value = saborestore.sabores

  await itemventastore.getAll()
  itemventas.value = itemventastore.itemventas

  await getAll()
})

//* Limpia el sabor seleccionado cuando se cambia el item de venta *//
watch(
  () => itemventasabor.value.itemventa,
  (nuevo, anterior) => {
    if (nuevo?.id !== anterior?.id) {
      itemventasabor.value.sabor = undefined
    }
  },
)
//* Producto del item de venta actual *//
const producto = computed(() => itemventasabor.value.itemventa?.producto)
//* Máximo de sabores permitidos para el producto del item de venta *//
const maxSabores = computed(() => producto.value?.max_sabores ?? 0)
//* Cantidad del item de venta actual *//
const cantidadItem = computed(() => itemventasabor.value.itemventa?.cantidad ?? 0)
//* Venta del item de venta actual está cerrada? *//
const ventaCerrada = computed(() => itemventasabor.value.itemventa?.venta?.estado === 'cerrada')

//* Cantidad de sabores ya asignados al item de venta actual *//
const saboresAsignados = computed(() => {
  return itemventasaborestore.itemventasabores.filter(
    (sabor) => sabor.itemventa?.id === itemventasabor.value.itemventa?.id,
  ).length
})

//* Función centralizada para saber si un sabor es válido *//
function saborDisponible(sabor: Sabor): boolean {
  if (!sabor) return false
  const idItem = itemventasabor.value.itemventa?.id
  if (!idItem) return false
  //* No permitir si ya está asignado (excepto el actual) *//
  const yaAsignado = itemventasaborestore.itemventasabores.some(
    (s) =>
      s.itemventa?.id === idItem &&
      s.sabor?.id === sabor.id &&
      sabor.id !== itemventasabor.value.sabor?.id,
  )
  const stockOk = (sabor.stock ?? 0) >= cantidadItem.value
  return !yaAsignado && stockOk
}

//* Función para obtener el subtítulo del sabor según su disponibilidad *//
function getSubtitle(sabor: Sabor): string {
  if (!saborDisponible(sabor)) {
    if (saborNoDisponible(sabor)) {
      return 'Sabor no disponible'
    }
    const idItem = itemventasabor.value.itemventa?.id
    const yaAsignado = itemventasaborestore.itemventasabores.some(
      (s) =>
        s.itemventa?.id === idItem &&
        s.sabor?.id === sabor.id &&
        sabor.id !== itemventasabor.value.sabor?.id,
    )
    if (yaAsignado) {
      return 'Ya asignado a este item'
    }
    return `Stock insuficiente (necesita: ${cantidadItem.value}, disponible: ${sabor.stock})`
  }
  return `Stock: ${sabor.stock}`
}

//* Si un sabor no esta disponible osea disponible = 0 este no se puede elegir *//
function saborNoDisponible(sabor: Sabor): boolean {
  return sabor?.disponible === 0
}

//* Verifica si se puede actualizar el sabor seleccionado *//
const puedeActualizarSabor = computed(() => {
  if (ventaCerrada.value) return false
  if (!producto.value) return false
  if (maxSabores.value === 0) return false
  if (!itemventasabor.value.sabor) return false
  if (!saborDisponible(itemventasabor.value.sabor)) return false
  if (saboresAsignados.value > maxSabores.value) return false
  if (saborNoDisponible(itemventasabor.value.sabor)) return false
  return true
})

function limpiarItemVentaSabor() {
  itemventasabor.value = {
    id: 0,
    itemventa: { id: 0 } as ItemVenta,
    sabor: { id: 0 } as Sabor,
  }
}

const actualizar = async () => {
  if (!puedeActualizarSabor.value) {
    alert('No se puede actualizar el sabor seleccionado.')
    return
  }

  const result = await form.value?.validate()
  if (!result.valid) return

  try {
    const data = {
      id: itemventasabor.value.id,
      id_item: itemventasabor.value.itemventa?.id,
      id_sabor: itemventasabor.value.sabor?.id,
    }

    await update(data as never)
    await itemventasaborestore.getAll()

    alert('Item de Venta Sabor actualizado con éxito.')
    form.value.reset()
    limpiarItemVentaSabor()
  } catch (error) {
    console.error(error)
    alert('Error al actualizar el Item de Venta Sabor.')
  }
}

onBeforeUnmount(() => {
  limpiarItemVentaSabor()
})
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
