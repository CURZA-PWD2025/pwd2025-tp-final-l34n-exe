<template>
  <v-card class="mx-auto pa-6" max-width="500" color="aliceblue" elevation="16">
    <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>
    <v-form @submit.prevent="crear" ref="form">
      <v-select
        v-model="itemventasabor.itemventa"
        :items="itemventas"
        label="Item"
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
        :rules="[
          (v) => !!v || 'Debe elegir un sabor',
          (v) => v?.stock > 0 || 'No hay stock disponible',
          (v) => !!v?.disponible || 'El sabor no está disponible',
          (v) =>
            saboresAsignados < (itemventasabor.itemventa?.producto?.max_sabores ?? 0) ||
            'Se ha alcanzado el máximo de sabores para este item',
          (v) => !saboresRepetidos || 'El sabor ya ha sido asignado a este item',
        ]"
        required
      >
        <template #item="{ props, item }">
          <v-list-item
            v-bind="props"
            :title="item.raw.nombre"
            :subtitle="`Stock: ${item.raw.stock}`"
          />
        </template>
        <template #selection="{ item }">
          {{ item.raw.nombre }}
        </template>
      </v-select>
      <p>Sabores: {{ saboresAsignados }} / {{ itemventasabor.itemventa?.producto?.max_sabores }}</p>
      <ButtonComponent type="submit" class="crear">
        <template #pre-icon>
          <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
        </template>
        Crear Sabor del Item
      </ButtonComponent>
    </v-form>
  </v-card>
  <ButtonComponent class="volver" :to="{ name: 'itemventasabores_list' }">
    <template #pre-icon>
      <Icon icon="ic:twotone-list" width="28" height="28" style="color: black" />
    </template>
    VOLVER A LA LISTA
  </ButtonComponent>
</template>

<script setup lang="ts">
import { onMounted, ref, toRefs, computed } from 'vue'
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
const sabores = ref(<Sabor[]>[])
const itemventas = ref(<ItemVenta[]>[])
const form = ref()

onMounted(async () => {
  await saborestore.getAll()
  sabores.value = saborestore.sabores

  await itemventastore.getAll()
  itemventas.value = itemventastore.itemventas
})

//*Para no asignar más sabores de los permitidos al item de venta */
const saboresAsignados = computed(() => {
  return itemventasaborestore.itemventasabores.filter(
    (sabor) => sabor.itemventa?.id === itemventasabor.value.itemventa?.id,
  ).length
})
//* Para no repetir sabores en un mismo item de venta */
const saboresRepetidos = computed(() => {
  return (
    itemventasaborestore.itemventasabores.filter(
      (sabor) =>
        sabor.itemventa?.id === itemventasabor.value.itemventa?.id &&
        sabor.sabor?.id === itemventasabor.value.sabor?.id,
    ).length > 0
  )
})

const crear = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  } else {
    const data = {
      id_item: itemventasabor.value.itemventa?.id,
      id_sabor: itemventasabor.value.sabor?.id,
    }
    await create(data as never)

    alert('Item de Venta Sabor creado con éxito.')

    form.value.reset()
  }
}
</script>

<style scoped>
.crear {
  text-align: center;
}
</style>
