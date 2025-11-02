<template>
  <div>
  <h1>
    TEST
  </h1>
  <div>
    <ProveedoresList></ProveedoresList>
    <EmpleadosList></EmpleadosList>
    <CategoriasList></CategoriasList>
    <ClientesList></ClientesList>
    <SaboresList></SaboresList>
    <ProductosList></ProductosList>
    <VentasList></VentasList>
    <ItemVentasList></ItemVentasList>


  </div>
  </div>


</template>

<script setup lang="ts">
import EmpleadosList from '@/components/empleados/EmpleadosList.vue';
import ProveedoresList from '@/components/proveedores/ProveedoresList.vue';
import CategoriasList from '@/components/categorias/CategoriasList.vue';
import ClientesList from '@/components/clientes/ClientesList.vue';
import SaboresList from '@/components/sabores/SaboresList.vue';
import ProductosList from '@/components/productos/ProductosList.vue';
import VentasList from '@/components/ventas/VentasList.vue';
import ItemVentasList from '@/components/itemventas/ItemVentasList.vue';
</script>

<style scoped>

</style>
