<template>
  <div>
    <h3>ClienteCreate</h3>
    <form @submit.prevent="crear">
      <div>
        <label for="nombre">Nombre:</label>
        <input type="text"  name="nombre" v-model="cliente.nombre" />
      </div>
      <div>
        <label for="apellido">Apellido:</label>
        <input type="text"  name="apellido" v-model="cliente.apellido" />
      </div>
      <div>
        <label for="telefono">Teléfono:</label>
        <input type="text"  name="telefono" v-model="cliente.telefono" />
      </div>
      <div>
        <label for="direccion">Dirección:</label>
        <input type="text"  name="direccion" v-model="cliente.direccion" />
      </div>
      <button type="submit">Crear Cliente</button>
    </form>
    <RouterLink :to="{name: 'clientes_list'}">VOLVER</RouterLink>

  </div>
</template>

<script setup lang="ts">
import { toRefs } from 'vue';
import useClientesStore from '@/stores/clientes';

const store = useClientesStore();
const { cliente } = toRefs(store);
const { create } = store;


const crear = async () => {
  if(!cliente.value.nombre || !cliente.value.telefono || !cliente.value.apellido || !cliente.value.direccion) {
    alert('Por favor, complete todos los campos.');
    return;
  }else{
    await create(cliente.value);
    cliente.value = { nombre: '', telefono: '', apellido: '', direccion: '' };
    alert('Cliente creado con éxito.');
  }
};

</script>

<style scoped>

</style>
