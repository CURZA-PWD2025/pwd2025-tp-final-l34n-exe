<template>
  <div>
    <h3>ItemVentasCreate</h3>
    <form @submit.prevent="crear">
      <div>
        <label for="sabor">Sabor:</label>
        <select v-model="itemventasabor.sabor" required>
          <option disabled value="">Seleccione un sabor</option>
          <option v-for="sabor in sabores" :key="sabor.id" :value="sabor">
            {{ sabor.nombre }}
          </option>
        </select>
      </div>
      <div>
        <label for="itemventa">Item de Venta:</label>
        <select v-model="itemventasabor.itemventa" required>
          <option disabled value="">Seleccione un item de venta</option>
          <option v-for="itemventa in itemventas" :key="itemventa.id" :value="itemventa">
            {{ itemventa.id }} - Cantidad: {{ itemventa.cantidad }}
          </option>
        </select>
      </div>
      <button type="submit">Crear Item de Venta Sabor</button>
    </form>
    <RouterLink :to="{ name: 'itemventasabores_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, toRefs } from 'vue'
import useItemVentaSaboresStore from '@/stores/itemventasabores'
import useItemVentasStore from '@/stores/itemventas'
import useSaboresStore from '@/stores/sabores'
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
  if (!itemventasabor.value.sabor?.id || !itemventasabor.value.itemventa?.id) {
    alert('Por favor, complete todos los campos.')
    return
  } else {
    const data = {
      id_item: itemventasabor.value.itemventa.id,
      id_sabor: itemventasabor.value.sabor.id,
    }
    await create(data as never)
    alert('Item de Venta Sabor creado con éxito.')
  }
}

</script>

<style scoped></style>
