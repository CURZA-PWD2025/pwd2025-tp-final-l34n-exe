<template>
  <div>
    <h3>ItemVentasCreate</h3>
    <form @submit.prevent="crear">
      <div>
        <label for="cantidad">Cantidad:</label>
        <input type="number"  name="cantidad" v-model="itemventa.cantidad" />
      </div>
      <div>
        <label for="producto">Producto:</label>
       <select v-model="itemventa.producto" required>
          <option disabled value="">Seleccione un producto</option>
          <option v-for="producto in productos" :key="producto.id" :value="producto">
            {{ producto.nombre }}
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
      <button type="submit">Crear Item de Venta</button>
    </form>
    <RouterLink :to="{ name: 'itemventas_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, toRefs } from 'vue'
import useItemVentasStore from '@/stores/itemventas';
import useProductosStore from '@/stores/productos';
import useVentasStore from '@/stores/ventas';
import type { Producto } from '@/interfaces/Producto';
import type { Venta } from '@/interfaces/Venta';
const itemventastore = useItemVentasStore()
const productostore = useProductosStore()
const ventastore = useVentasStore()
const { itemventa } = toRefs(itemventastore)

const { create } = itemventastore;

const productos = ref(<Producto[]>[])
const ventas = ref(<Venta[]>[])

onMounted(async () => {
  await productostore.getAll()
  productos.value = productostore.productos

  await ventastore.getAll()
  ventas.value = ventastore.ventas
})

const crear = async () => {
  if(!itemventa.value.cantidad || !itemventa.value.producto?.id || !itemventa.value.venta?.id) {
    alert('Por favor, complete todos los campos.');
    return
  }else{
    const data = {
      cantidad: itemventa.value.cantidad,
      id_producto: itemventa.value.producto?.id ,
      id_venta:  itemventa.value.venta?.id
    }
    await create(data);

    alert('Item de venta creado con éxito.');
  }
}
</script>

<style scoped></style>
