<template>
  <div>
    <h2>
      ItemVentaShow
    </h2>
    <div>
      <p>ID: {{ itemventa.id }}</p>
      <p>VENTA ID: {{ itemventa.venta?.id }}</p>
      <p>PRODUCTO: {{ itemventa.producto?.nombre }}</p>
      <p>CANTIDAD: {{ itemventa.cantidad }}</p>
      <router-link :to="{ name: 'itemventas_list' }">VOLVER</router-link>
    </div>

  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useItemVentasStore from '@/stores/itemventas'

const store = useItemVentasStore()
const { itemventa } = toRefs(store)
const { getOne } = store
const route = useRoute()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})
</script>

<style scoped>

</style>
