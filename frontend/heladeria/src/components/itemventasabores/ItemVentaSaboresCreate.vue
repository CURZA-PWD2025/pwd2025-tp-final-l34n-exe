<template>
  <v-card class="mx-auto pa-6" max-width="500" color="aliceblue" elevation="16">
    <v-card-title class="text-h6 text-center mb-4"> AGREGAR SABOR AL ITEM </v-card-title>

    <v-form @submit.prevent="crear" ref="form">
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
            :subtitle="`Cantidad: ${item.raw.cantidad} | Stock: ${item.raw.producto?.stock}`"
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
        :disabled="ventaCerrada || !producto || maxSabores === 0"
        :rules="[
          (v) => !!v || 'Debe elegir un sabor',
          (v) => saborDisponible(v) || 'El sabor ya está asignado o no hay stock suficiente',
          (v) => !saborNoDisponible(v) || 'El sabor no está disponible',
          () => saboresAsignados < maxSabores || 'Se alcanzó el máximo de sabores',
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
        <strong>{{ maxSabores }}</strong>
      </p>

      <ButtonComponent type="submit" class="crear mt-4" :disabled="!puedeAgregarSabor">
        <template #pre-icon>
          <Icon icon="mdi-light:check" width="26" height="26" style="color: #05f036" />
        </template>
        Agregar Sabor
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
import { onMounted, ref, toRefs, computed, onBeforeUnmount, watch } from 'vue'
import useItemVentaSaboresStore from '@/stores/itemventasabores'
import useItemVentasStore from '@/stores/itemventas'
import useSaboresStore from '@/stores/sabores'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
import type { Sabor } from '@/interfaces/Sabor'
import type { ItemVenta } from '@/interfaces/ItemVenta'

const itemventasaborestore = useItemVentaSaboresStore()
const itemventastore = useItemVentasStore()
const saborestore = useSaboresStore()

const { itemventasabor } = toRefs(itemventasaborestore)
const { create } = itemventasaborestore

const sabores = ref<Sabor[]>([])
const itemventas = ref<ItemVenta[]>([])
const form = ref()

onMounted(async () => {
  await saborestore.getAll()
  sabores.value = saborestore.sabores

  await itemventastore.getAll()
  itemventas.value = itemventastore.itemventas

  await itemventasaborestore.getAll()
})

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

//* Verifica si la venta está cerrada *//
const ventaCerrada = computed(() => itemventasabor.value.itemventa?.venta?.estado === 'cerrada')

//* Cuenta cuántos sabores ya fueron asignados al item de venta actual *//
const saboresAsignados = computed(() => {
  const idItem = itemventasabor.value.itemventa?.id
  if (!idItem) return 0
  return itemventasaborestore.itemventasabores.filter((s) => s.itemventa?.id === idItem).length
})

//* Función para obtener el subtítulo del sabor según su disponibilidad *//
function getSubtitle(sabor: Sabor): string {
  if (!saborDisponible(sabor)) {
    if (saborNoDisponible(sabor)) {
      return 'Sabor no disponible'
    }
    const idItem = itemventasabor.value.itemventa?.id
    const yaAsignado = itemventasaborestore.itemventasabores.some(
      (s) => s.itemventa?.id === idItem && s.sabor?.id === sabor.id,
    )
    if (yaAsignado) {
      return 'Ya asignado a este item'
    }
    return `Stock insuficiente (necesita: ${cantidadItem.value}, disponible: ${sabor.stock})`
  }
  return `Stock: ${sabor.stock}`
}

//* Verifica si el sabor seleccionado tiene stock insuficiente *//
function saborDisponible(sabor: Sabor): boolean {
  if (!sabor) return false
  const idItem = itemventasabor.value.itemventa?.id
  if (!idItem) return false
  //* No permitir si ya está asignado o no hay stock suficiente *//
  const yaAsignado = itemventasaborestore.itemventasabores.some(
    (s) => s.itemventa?.id === idItem && s.sabor?.id === sabor.id,
  )
  const stockOk = (sabor.stock ?? 0) >= cantidadItem.value
  return !yaAsignado && stockOk
}

//* Si un sabor no esta disponible osea disponible = 0 este no se puede elegir *//
function saborNoDisponible(sabor: Sabor): boolean {
  return sabor?.disponible === 0
}

//* Verifica si se puede agregar el sabor *//
const puedeAgregarSabor = computed(() => {
  if (ventaCerrada.value) {
    alert('Esta venta está cerrada. No se pueden agregar sabores.')
    return false
  }
  if (!producto.value) return false
  if (maxSabores.value === 0) return false
  if (!itemventasabor.value.sabor) return false
  if (!saborDisponible(itemventasabor.value.sabor)) return false
  if (saboresAsignados.value >= maxSabores.value) return false
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

const crear = async () => {
  if (!puedeAgregarSabor.value) {
    alert('No se puede agregar el sabor seleccionado.')
    return
  }

  const result = await form.value?.validate()
  if (!result.valid) return

  try {
    const data = {
      id_item: itemventasabor.value.itemventa?.id,
      id_sabor: itemventasabor.value.sabor?.id,
    }
    await create(data as never)

    await itemventasaborestore.getAll()
    alert('Sabor agregado correctamente')

    form.value.reset()
    limpiarItemVentaSabor()
  } catch (error) {
    console.error(error)
    alert('Error al agregar el sabor')
  }
}

onBeforeUnmount(limpiarItemVentaSabor)
</script>

<style scoped>
.crear {
  text-align: center;
}
</style>
