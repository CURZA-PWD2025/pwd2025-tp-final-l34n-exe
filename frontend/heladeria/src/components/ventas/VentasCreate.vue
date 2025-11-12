<template>
  <div>
    <h3>VentasCreate</h3>
    <form @submit.prevent="crear">
      <div>
        <label for="total">Total:</label>
        <input type="number" name="total" v-model.number="venta.total" />
      </div>

      <div>
        <label for="fecha">Fecha:</label>
        <input type="date" name="fecha" v-model="venta.fecha" />
      </div>

      <div>
        <label for="empleado">Empleado:</label>
        <select v-model="venta.empleado" required>
          <option disabled value="">Seleccione un empleado</option>
          <option v-for="empleado in empleados" :key="empleado.id" :value="empleado">
            {{ empleado.nombre }} {{ empleado.apellido }}
          </option>
        </select>
      </div>

      <div>
        <label for="cliente">Cliente:</label>
        <select v-model="venta.cliente" required>
          <option disabled value="">Seleccione un cliente</option>
          <option v-for="cliente in clientes" :key="cliente.id" :value="cliente">
            {{ cliente.nombre }} {{ cliente.apellido }}
          </option>
        </select>
      </div>

      <button type="submit">Crear Venta</button>
    </form>
    <RouterLink :to="{ name: 'ventas_list' }">VOLVER</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted } from 'vue'
import useVentasStore from '@/stores/ventas'
import useClientesStore from '@/stores/clientes'
import useEmpleadosStore from '@/stores/empleados'
import type { Cliente } from '@/interfaces/Cliente'
import type { Empleado } from '@/interfaces/Empleado'

const clientesStore = useClientesStore()
const empleadosStore = useEmpleadosStore()
const ventasStore = useVentasStore()
const { venta } = toRefs(ventasStore)
const { create } = ventasStore
const clientes = ref(<Cliente[]>[])
const empleados = ref(<Empleado[]>[])

onMounted(async () => {
  await clientesStore.getAll()
  clientes.value = clientesStore.clientes

  await empleadosStore.getAll()
  empleados.value = empleadosStore.empleados
})

const crear = async () => {
  if (
    !venta.value.total ||
    !venta.value.fecha ||
    !venta.value.empleado?.id ||
    !venta.value.cliente?.id
  ) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  }
  const data = {
    total: venta.value.total,
    fecha: venta.value.fecha,
    id_empleado: venta.value.empleado?.id,
    id_cliente: venta.value.cliente?.id,
  }
  await create(data)
  /*/
  venta.value = {
    total: 0,
    fecha: '',
    cliente: { id: 0, nombre: '', apellido: '', telefono: '', direccion: '' },
    empleado: { id: 0, nombre: '', apellido: '', telefono: '', email: '', puesto: '' },
  }
  /*/

  alert('Venta creada con éxito.')
}
</script>

<style scoped></style>
