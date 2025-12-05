<template>
  <div>
    <v-card class="mx-auto pa-6" max-width="500" variant="outlined">
      <v-card-title class="text-h6 text-center">Actualizar Venta</v-card-title>
      <v-form @submit.prevent="actualizar" ref="form">
        <v-text-field
          v-model="venta.total"
          label="Total de la venta"
          variant="outlined"
          :rules="[(v) => !!v || 'El dato es obligatorio']"
          required
        ></v-text-field>
        <v-text-field
          v-model="venta.fecha"
          label="Fecha y hora"
          type="datetime-local"
          variant="outlined"
          :rules="[(v) => !!v || 'El dato es obligatorio']"
          required
        ></v-text-field>

        <v-select
          v-model="venta.empleado"
          :items="empleados"
          item-title="nombre"
          item-value="id"
          label="Empleado"
          variant="outlined"
          return-object
          :rules="[
            (v) => !!v || 'Debe elegir un empleado',
            (v) => v.puesto !== 'Limpieza' || 'El personal de limpieza no puede realizar ventas',
          ]"
        >
        <template #item="{ props, item }">
          <v-list-item v-bind="props" :title="item.raw.nombre" :subtitle="item.raw.apellido" />
        </template>
        <template #selection="{ item }">
          ID: {{ item.raw.id }} {{ item.raw.nombre }} {{ item.raw.apellido }}
        </template>
        </v-select>

        <v-select
          v-model="venta.cliente"
          :items="clientes"
          item-value="id"
          label="Cliente"
          variant="outlined"
          :rules="[(v) => !!v || 'Debe elegir un cliente']"
          return-object
        >
          <template #item="{ props, item }">
            <v-list-item v-bind="props" :title="item.raw.nombre" :subtitle="item.raw.apellido" />
          </template>

          <template #selection="{ item }">
           ID: {{ item.raw.id }} {{ item.raw.nombre }} {{ item.raw.apellido }}
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
        <Icon icon="ic:twotone-list" width="28" height="28"  style="color: black" />
      </template>
      VOLVER A LA LISTA
    </ButtonComponent>
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
const form=ref()

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
  if (venta.value.empleado.puesto === "Limpieza") {
    alert("Un empleado de limpieza no puede realizar ventas.")
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

  venta.value = {
    total: 0,
    fecha: '',
    empleado: { id: 0, nombre: '', apellido: '', telefono: '', email: '', puesto: '' },
    cliente: { id: 0, nombre: '', apellido: '', telefono: '', direccion: '' },
  }

  alert('Venta actualizada con éxito.')

  form.value.reset()
}
</script>

<style scoped>
.act{
  text-align: center;
}
</style>
