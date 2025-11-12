<template>
  <div>
    <h2>ItemVentaSaboresShow</h2>
    <div>
      <p>ID: {{ itemventasabor.id }}</p>
      <p>ITEM ID: {{ itemventasabor.itemventa?.id }}</p>
      <p>SABOR: {{ itemventasabor.sabor?.nombre }}</p>
      <router-link :to="{ name: 'itemventasabores_list' }">VOLVER</router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useItemVentaSaboresStore from '@/stores/itemventasabores'

const store = useItemVentaSaboresStore()
const { itemventasabor } = toRefs(store)
const { getOne } = store
const route = useRoute()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})
</script>

<style scoped></style>
