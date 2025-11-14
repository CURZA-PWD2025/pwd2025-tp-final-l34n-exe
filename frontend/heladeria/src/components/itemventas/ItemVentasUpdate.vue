<template>
  <div>
    <h3>ItemVentasUpdate</h3>
    <form @submit.prevent="actualizar">
      <div>
        <label for="cantidad">Cantidad:</label>
        <input type="number" name="cantidad" v-model="itemventa.cantidad" />
      </div>
      <div>
        <label for="producto">Producto:</label>
        <select v-model="itemventa.producto" required>
          <option disabled value="">Seleccione un producto</option>
          <option v-for="producto in productos" :key="producto.id" :value="producto">
            {{ producto.id }} {{ producto.nombre }}
          </option>
        </select>
      </div>
      <div>
        <label for="venta">Venta:</label>
        <select v-model="itemventa.venta" required>
          <option disabled value="">Seleccione una venta</option>
          <option v-for="venta in ventas" :key="venta.id" :value="venta">
            {{ venta.id }} - {{ venta.fecha }}
          </option>
        </select>
      </div>
      <button type="submit">Actualizar Item de Venta</button>
    </form>
    <RouterLink :to="{ name: 'itemventas_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
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

    alert('Item de venta actualizado con éxito.')
  }
}
</script>

<style scoped></style>
