<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" elevation="16" color="aliceblue">
      <v-card-title class="text-h6 text-center">EDITAR VENTA</v-card-title>

      <v-form @submit.prevent="guardarVenta" ref="form">
        <v-text-field :model-value="Number(venta.total).toFixed(2)" label="Total" readonly />

        <v-text-field
          v-model="venta.fecha"
          label="Fecha y Hora"
          type="datetime-local"
          variant="outlined"
          :rules="[(v) => !!v || 'La fecha es obligatoria']"
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
            (v) => (v && !!v.puesto) || 'El empleado seleccionado no tiene un puesto válido',
            (v) =>
              (v && v.puesto !== 'Limpieza') || 'El personal de limpieza no puede realizar ventas',
          ]"
          required
        >
          <template #item="{ props, item }">
            <v-list-item
              v-bind="props"
              :title="`${item.raw.nombre} ${item.raw.apellido}`"
              :subtitle="`Puesto: ${item.raw.puesto}`"
            />
          </template>
          <template #selection="{ item }">
            {{ item.raw.nombre }} {{ item.raw.apellido }} ({{ item.raw.puesto }})
          </template>
        </v-select>

        <v-select
          v-model="venta.cliente"
          :items="clientes"
          label="Cliente"
          variant="outlined"
          return-object
          :rules="[(v) => !!v || 'Debe elegir un cliente']"
          required
        >
          <template #item="{ props, item }">
            <v-list-item
              v-bind="props"
              :title="`${item.raw.nombre} ${item.raw.apellido}`"
              :subtitle="`ID: ${item.raw.id}`"
            />
          </template>
          <template #selection="{ item }">
            {{ item.raw.nombre }} {{ item.raw.apellido }} (ID: {{ item.raw.id }})
          </template>
        </v-select>

        <v-select
          v-model="venta.estado"
          :items="['abierta', 'cerrada']"
          label="Estado de la venta"
          variant="outlined"
          :rules="[(v) => !!v || 'Debe seleccionar un estado']"
          required
        >
          <template #selection="{ item }">
            <v-chip :color="item.raw === 'abierta' ? 'green' : 'red'" text-color="white" small>
              {{ item.raw }}
            </v-chip>
          </template>

          <template #item="{ props, item }">
            <v-list-item v-bind="props">
              <v-chip :color="item.raw === 'abierta' ? 'green' : 'red'" text-color="white" small>
                {{ item.raw }}
              </v-chip>
            </v-list-item>
          </template>
        </v-select>

        <ButtonComponent type="submit" class="act mt-4">
          <template #pre-icon>
            <Icon icon="mdi-light:check" width="28" height="28" style="color: #05f036" />
          </template>
          Actualizar Venta
        </ButtonComponent>
      </v-form>
    </v-card>

    <ButtonComponent class="volver mt-4" :to="{ name: 'ventas_list' }">
      <template #pre-icon>
        <Icon icon="ic:twotone-list" width="28" height="28" style="color: black" />
      </template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { ref, toRefs, onMounted, onBeforeUnmount, computed } from 'vue'
import { useRoute } from 'vue-router'
import useVentasStore from '@/stores/ventas'
import useClientesStore from '@/stores/clientes'
import useEmpleadosStore from '@/stores/empleados'
import useItemVentasStore from '@/stores/itemventas'
import useItemVentaSaboresStore from '@/stores/itemventasabores'
import type { Empleado } from '@/interfaces/Empleado'
import type { Cliente } from '@/interfaces/Cliente'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const ventasStore = useVentasStore()
const clientesStore = useClientesStore()
const empleadosStore = useEmpleadosStore()
const itemVentasStore = useItemVentasStore()
const itemVentaSaboresStore = useItemVentaSaboresStore()
const { venta } = toRefs(ventasStore)
const { getOne, update } = ventasStore

const empleados = ref<Empleado[]>([])
const clientes = ref<Cliente[]>([])
const route = useRoute()
const form = ref()

//* Verificar si la venta tiene ítems *//
const tieneItems = computed(() =>
  itemVentasStore.itemventas.some((item) => item.venta?.id === venta.value.id),
)

//* Verifica si todos los items de la venta tienen al menos un sabor asignado *//
const itemsConSabores = computed(() => {
  //* Filtrar los items de esta venta *//
  const itemsVenta = itemVentasStore.itemventas.filter((item) => item.venta?.id === venta.value.id)
  if (itemsVenta.length === 0) return false
  //* Para cada item, verificar que tenga al menos un sabor asignado *//
  return itemsVenta.every((item) =>
    itemVentaSaboresStore.itemventasabores.some((sabor) => sabor.itemventa?.id === item.id),
  )
})

//* Formatear fecha para input datetime-local *//
function formatFechaInput(fecha: string): string {
  if (!fecha) return ''
  // Si ya está en formato correcto, devolver
  if (/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}/.test(fecha)) return fecha
  // Si viene en formato ISO, convertir
  const d = new Date(fecha)
  if (isNaN(d.getTime())) return ''
  const pad = (n: number) => n.toString().padStart(2, '0')
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}T${pad(d.getHours())}:${pad(d.getMinutes())}`
}

onMounted(async () => {
  const id = Number(route.params.id)
  if (id > 0) {
    await getOne(id)
    //* Formatear fecha para el input *//
    venta.value.fecha = formatFechaInput(
      typeof venta.value.fecha === 'string'
        ? venta.value.fecha
        : venta.value.fecha instanceof Date
          ? venta.value.fecha.toISOString()
          : '',
    )
  } else {
    alert('ID de venta inválido.')
  }
  await itemVentasStore.getAll()

  await clientesStore.getAll()
  clientes.value = clientesStore.clientes

  await empleadosStore.getAll()
  empleados.value = empleadosStore.empleados

  //* Evitar errores si el backend no envía relaciones *//
  if (!venta.value.cliente) {
    venta.value.cliente = { id: 0 } as Cliente
  }
  if (!venta.value.empleado) {
    venta.value.empleado = { id: 0 } as Empleado
  }
})

function limpiarVenta() {
  venta.value = {
    id: 0,
    fecha: '',
    total: 0,
    estado: 'abierta',
    cliente: { id: 0 } as Cliente,
    empleado: { id: 0 } as Empleado,
  }
}

const guardarVenta = async () => {
  const result = await form.value?.validate()
  if (!result.valid) return

  if (venta.value.estado === 'cerrada') {
    if (!tieneItems.value) {
      alert('No se puede cerrar una venta sin ítems.')
      return
    }
    if (!itemsConSabores.value) {
      alert('No se puede cerrar la venta: todos los ítems deben tener al menos un sabor asignado.')
      return
    }
  }

  try {
    const data = {
      id: venta.value.id,
      fecha: venta.value.fecha,
      total: venta.value.total ?? 0,
      estado: venta.value.estado,
      id_empleado: venta.value.empleado?.id,
      id_cliente: venta.value.cliente?.id,
    }

    await update(data)

    alert(
      venta.value.estado === 'cerrada'
        ? 'Venta cerrada correctamente'
        : 'Venta actualizada con éxito',
    )
  } catch (error) {
    console.error(error)
    alert('Error al guardar la venta')
  }
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
