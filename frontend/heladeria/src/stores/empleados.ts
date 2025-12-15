import type { Empleado } from '@/interfaces/Empleado'
import { defineStore } from 'pinia'
import ApiService from '@/services/ApiService'
import { ref } from 'vue'

const useEmpleadosStore = defineStore('empleados', () => {
  const empleados = ref<Array<Empleado>>([])
  const empleado = ref<Empleado>({
    id: 0,
    nombre: '',
    apellido: '',
    telefono: '',
    email: '',
    puesto: '',
  })
  const url = 'empleados'
  async function getAll() {
    const data = await ApiService.getAll(url)
    if (data) {
      empleados.value = data
    }
  }
  async function getOne(id: number) {
    const data = await ApiService.getOne(url, id)
    if (data) {
      empleado.value = data
    }
  }
  async function create(nuevoEmpleado: Empleado) {
    const data = await ApiService.create(url, nuevoEmpleado)
    if (data) {
      empleado.value = data
    }
  }
  async function update(actEmpleado: Empleado) {
    if (actEmpleado.id) {
      const data = await ApiService.update(url, actEmpleado.id, actEmpleado)
      if (data) {
        empleado.value = data
      }
    }
  }
  async function destroy(id: number) {
    const data = await ApiService.destroy(url, id)
    if (data) {
      empleado.value = data
    }
  }

  return { empleados, empleado, getAll, getOne, create, update, destroy }
})

export default useEmpleadosStore
