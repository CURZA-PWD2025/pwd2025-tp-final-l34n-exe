<template>
  <div>
    <h1>TEST</h1>
    <div>
      <button><RouterLink :to="{ name: 'proveedores_list' }">Click para ver los proveedores</RouterLink></button>
      <button><RouterLink :to="{ name: 'empleados_list' }">Click para ver los empleados</RouterLink></button>
      <button><RouterLink :to="{ name: 'categorias_list' }">Click para ver las categorias</RouterLink></button>
      <button><RouterLink :to="{ name: 'clientes_list' }">Click para ver los clientes</RouterLink></button>
      <button><RouterLink :to="{ name: 'sabores_list' }">Click para ver los sabores</RouterLink></button>
      <button><RouterLink :to="{ name: 'productos_list' }">Click para ver los productos</RouterLink></button>
      <button><RouterLink :to="{ name: 'ventas_list' }">Click para ver las ventas</RouterLink></button>
      <button><RouterLink :to="{ name: 'itemventas_list' }">Click para ver los item ventas</RouterLink></button>
      <button><RouterLink :to="{ name: 'itemventasabores_list' }">Click para ver los item venta sabores</RouterLink></button>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped></style>
