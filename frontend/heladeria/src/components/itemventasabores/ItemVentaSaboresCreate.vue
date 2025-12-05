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
        :rules="[(v) => !!v || 'Debe elegir un sabor']"
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
import { onMounted, ref, toRefs } from 'vue'
import useItemVentaSaboresStore from '@/stores/itemventasabores'
import useItemVentasStore from '@/stores/itemventas'
import useSaboresStore from '@/stores/sabores'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const form = ref()
import type { Sabor } from '@/interfaces/Sabor'
import type { ItemVenta } from '@/interfaces/ItemVenta'
const itemventasaborestore = useItemVentaSaboresStore()
const itemventastore = useItemVentasStore()
const saborestore = useSaboresStore()
const { itemventasabor } = toRefs(itemventasaborestore)

const { create } = itemventasaborestore
const sabores = ref(<Sabor[]>[])
const itemventas = ref(<ItemVenta[]>[])

onMounted(async () => {
  await saborestore.getAll()
  sabores.value = saborestore.sabores

  await itemventastore.getAll()
  itemventas.value = itemventastore.itemventas
})

const crear = async () => {
  const valid = await form.value?.validate()
  if (!valid) return
  if (!itemventasabor.value.itemventa?.id || !itemventasabor.value.sabor?.id) {
    alert('Por favor, complete todos los campos.')
    return
  } else {
    const data = {
      id_item: itemventasabor.value.itemventa.id,
      id_sabor: itemventasabor.value.sabor.id,
    }
    await create(data as never)

    itemventasabor.value = {
      id: 0,
      itemventa: {
        id: 0,
        cantidad: 0,
        producto: {
          id: 0,
          nombre: '',
          precio: 0,
          stock: 0,
          max_sabores: 0,
          proveedor: { id: 0, nombre: '', telefono: '', email: '' },
          categoria: { id: 0, nombre: '', tipo: '', descripcion: '' },
        },
        venta: {
          id: 0,
          fecha: '',
          total: 0,
          cliente: { id: 0, nombre: '', apellido: '', telefono: '', direccion:'' },
          empleado: { id: 0, nombre: '', apellido: '', telefono: '', email:'', puesto:'' },
        },
      },
      sabor: {
        id: 0,
        nombre: '',
        stock: 0,
        disponible: true,
        categoria: { id: 0, nombre: '', tipo: '', descripcion: '' },
      },
    }

    alert('Item de Venta Sabor creado con éxito.')

    form.value.reset()
  }
}
</script>

<style scoped></style>
