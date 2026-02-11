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
        :items="saboresDisponibles"
        label="Sabor"
        variant="outlined"
        return-object
        :disabled="ventaCerrada || !producto || maxSabores === 0"
        :rules="[
          (v) => !!v || 'Debe elegir un sabor',
          (v) => saborDisponible(v) || 'El sabor ya está asignado o no hay stock suficiente',
          () => saboresAsignados < maxSabores || 'Se alcanzó el máximo de sabores',
        ]"
        required
      >
        <template #item="{ props, item }">
          <v-list-item
            v-bind="props"
            :title="item.raw.nombre"
            :subtitle="`Stock: ${item.raw.stock}`"
            :disabled="!saborDisponible(item.raw)"
          />
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

//* Filtra los sabores que ya fueron asignados al item de venta actual *//
const saboresDisponibles = computed(() => {
  const idItem = itemventasabor.value.itemventa?.id
  if (!idItem) return sabores.value

  const usados = itemventasaborestore.itemventasabores
    .filter((s) => s.itemventa?.id === idItem)
    .map((s) => s.sabor?.id)

  return sabores.value.filter((s) => !usados.includes(s.id))
})

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
