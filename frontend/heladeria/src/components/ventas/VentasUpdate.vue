<template>
  <div>
    <h3>
      Actualizar Venta
    </h3>
    <form @submit.prevent="actualizar">
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
      <button type="submit">Actualizar Venta</button>
    </form>

  </div>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import useVentasStore from '@/stores/ventas'
import useClientesStore from '@/stores/clientes'
import useEmpleadosStore from '@/stores/empleados'
import type { Empleado } from '@/interfaces/Empleado'
import type { Cliente } from '@/interfaces/Cliente'

const ventasStore = useVentasStore()
const clientesStore = useClientesStore()
const empleadosStore = useEmpleadosStore()
const { venta } = toRefs(ventasStore)
const { getOne, update } = ventasStore
const empleados = ref(<Empleado[]>[])
const clientes = ref(<Cliente[]>[])
const route = useRoute()

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) await getOne(id)

  await clientesStore.getAll()
  clientes.value = clientesStore.clientes
  await empleadosStore.getAll()
  empleados.value = empleadosStore.empleados
})

const actualizar = async () => {
  if (
    !venta.value.total ||
    !venta.value.fecha  ||
    !venta.value.empleado?.id ||
    !venta.value.cliente?.id
  ) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  }

  const data = {
    id: venta.value.id,
    total: venta.value.total,
    fecha: venta.value.fecha,
    id_empleado: venta.value.empleado?.id,
    id_cliente: venta.value.cliente?.id,
  }

  await update(data)


  alert('Venta actualizada con éxito.')
}
</script>

<style scoped></style>
