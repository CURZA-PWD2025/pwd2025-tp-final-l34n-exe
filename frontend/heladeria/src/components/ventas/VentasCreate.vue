<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16">
      <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>
      <v-form @submit.prevent="crear" ref="form">
        <v-text-field
          v-model="venta.total"
          label="Total de la venta"
          type="number"
          variant="outlined"
          :rules="[
            (v) => !!v || 'El dato es obligatorio',
            (v) => v > 0 || 'El total debe ser mayor a 0',
            (v) => !isNaN(parseFloat(v)) || 'El total debe ser un número',
          ]"
          required
        />
        <v-text-field
          v-model="venta.fecha"
          label="Fecha y Hora"
          type="datetime-local"
          variant="outlined"
          :rules="[(v) => !!v || 'El dato es obligatorio']"
          required
        />
        <v-select
          v-model="venta.empleado"
          :items="empleados"
          label="Empleado"
          variant="outlined"
          return-object
          :rules="[
            (v) => !!v || 'Debe elegir un empleado',
            (v) => v.puesto !== 'Limpieza' || 'El personal de limpieza no puede realizar ventas',
          ]"
        >
          <template #item="{ props, item }">
            <v-list-item
              v-bind="props"
              :title="`${item.raw.nombre} ${item.raw.apellido}`"
              :subtitle="`Puesto: ${item.raw.puesto}`"
            />
          </template>
          <template #selection="{ item }">
            {{ item.raw.nombre }} {{ item.raw.apellido }} {{ item.raw.puesto }}
          </template>
        </v-select>
        <v-select
          v-model="venta.cliente"
          :items="clientes"
          label="Cliente"
          variant="outlined"
          return-object
          :rules="[(v) => !!v || 'Debe elegir un cliente']"
        >
          <template #item="{ props, item }">
            <v-list-item
              v-bind="props"
              :title="`${item.raw.nombre} ${item.raw.apellido}`"
              :subtitle="`ID: ${item.raw.id}`"
            />
          </template>
          <template #selection="{ item }">
            {{ item.raw.nombre }} {{ item.raw.apellido }} ID: {{ item.raw.id }}
          </template>
        </v-select>
        <ButtonComponent type="submit" class="crear">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Crear Venta
        </ButtonComponent>
      </v-form>
    </v-card>
    <ButtonComponent class="volver" :to="{ name: 'ventas_list' }">
      <template #pre-icon>
        <Icon icon="ic:twotone-list" width="28" height="28" style="color: black" />
      </template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted } from 'vue'
import useVentasStore from '@/stores/ventas'
import useClientesStore from '@/stores/clientes'
import useEmpleadosStore from '@/stores/empleados'
import type { Cliente } from '@/interfaces/Cliente'
import type { Empleado } from '@/interfaces/Empleado'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const clientesStore = useClientesStore()
const empleadosStore = useEmpleadosStore()
const ventasStore = useVentasStore()
const { venta } = toRefs(ventasStore)
const { create } = ventasStore
const clientes = ref(<Cliente[]>[])
const empleados = ref(<Empleado[]>[])
const form = ref()

onMounted(async () => {
  await clientesStore.getAll()
  clientes.value = clientesStore.clientes

  await empleadosStore.getAll()
  empleados.value = empleadosStore.empleados
})

const crear = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
    alert('Por favor, complete todos los campos correctamente.')
    return
  } else {
    const data = {
      total: venta.value.total,
      fecha: venta.value.fecha,
      id_empleado: venta.value.empleado?.id,
      id_cliente: venta.value.cliente?.id,
    }
    await create(data)

    venta.value = {
      total: 0,
      fecha: '',
      empleado: { id: 0, nombre: '', apellido: '', telefono: '', email: '', puesto: '' },
      cliente: { id: 0, nombre: '', apellido: '', telefono: '', direccion: '' },
    }

    alert('Venta creada con éxito.')

    form.value.reset()
  }
}
</script>

<style scoped>
.crear {
  text-align: center;
}
</style>
