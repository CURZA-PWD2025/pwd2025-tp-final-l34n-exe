<template>
  <div>
    <h2>Los proveedores</h2>
    <router-link :to="{ name: 'proveedores_create' }">Crear proveedor </router-link>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>NOMBRE</th>
          <th>EMAIL</th>
          <th>TELEFONO</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="proveedor in proveedores" :key="proveedor.id">
          <td>{{ proveedor.id }}</td>
          <td>{{ proveedor.nombre }}</td>
          <td>{{ proveedor.email }}</td>
          <td>{{ proveedor.telefono }}</td>
          <td>
            <router-link :to="{ name: 'proveedores_edit', params: { id: proveedor.id } }"
              >Editar</router-link
            >
            <router-link :to="{ name: 'proveedores_show', params: { id: proveedor.id } }"
              >Mostrar</router-link
            >
            <button @click="deleteProveedor(proveedor.id ? proveedor.id : 0)" class="btn-delete">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import useProveedoresStore from '@/stores/proveedores'
import { toRefs, onMounted } from 'vue'

const { proveedores } = toRefs(useProveedoresStore())
const { getAll, destroy } = useProveedoresStore()

const deleteProveedor = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este proveedor?')) {
    await destroy(id)
    await getAll()
  }
}

onMounted(async () => {
  await getAll()
})
</script>

<style scoped></style>
