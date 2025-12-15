<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16">
      <v-card-title class="text-h6 text-center">INSERTE DATOS</v-card-title>
      <v-form @submit.prevent="actualizar" ref="form">
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
          :rules="[
            (v) => !!v || 'El dato es obligatorio',
            (v) => !isNaN(new Date(v).getTime()) || 'Debe ser una fecha y hora válida',
          ]"
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
        <ButtonComponent type="submit" class="act">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Actualizar Venta
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
import { ref, toRefs, onMounted, onBeforeUnmount } from 'vue'
import { useRoute } from 'vue-router'
import useVentasStore from '@/stores/ventas'
import useClientesStore from '@/stores/clientes'
import useEmpleadosStore from '@/stores/empleados'
import type { Empleado } from '@/interfaces/Empleado'
import type { Cliente } from '@/interfaces/Cliente'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const ventasStore = useVentasStore()
const clientesStore = useClientesStore()
const empleadosStore = useEmpleadosStore()
const { venta } = toRefs(ventasStore)
const { getOne, update } = ventasStore
const empleados = ref(<Empleado[]>[])
const clientes = ref(<Cliente[]>[])
const route = useRoute()
const form = ref()

onMounted(async () => {
  const valid = await form.value?.validate()
  if (!valid) return
  const id = Number(route.params.id)
  if (id) await getOne(id)

  await clientesStore.getAll()
  clientes.value = clientesStore.clientes
  await empleadosStore.getAll()
  empleados.value = empleadosStore.empleados
})

function limpiarVenta() {
  venta.value = {
    id: 0,
    fecha: '',
    total: 0,
    cliente: {
      id: 0,
      nombre: '',
      apellido: '',
      telefono: '',
      direccion: '',
    } as Cliente,
    empleado: {
      id: 0,
      nombre: '',
      apellido: '',
      telefono: '',
      email: '',
      puesto: '',
    } as Empleado,
  }
}

const actualizar = async () => {
  const result = await form.value?.validate()
  if (!result.valid) {
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

  alert('Venta ACTUALIZADO con éxito.')
}

onBeforeUnmount(() => {
  limpiarVenta()
})
</script>

<style scoped>
.act {
  text-align: center;
}
</style>
