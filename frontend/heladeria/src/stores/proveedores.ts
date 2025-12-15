import type { Proveedor } from '@/interfaces/Proveedor'
import { defineStore } from 'pinia'
import ApiService from '@/services/ApiService'
import { ref } from 'vue'

const useProveedoresStore = defineStore('proveedores', () => {
  const proveedores = ref<Array<Proveedor>>([])
  const proveedor = ref<Proveedor>({
    id: 0,
    nombre: '',
    email: '',
    telefono: '',
  })
  const url = 'proveedores'
  async function getAll() {
    const data = await ApiService.getAll(url)
    if (data) {
      proveedores.value = data
    }
  }
  async function getOne(id: number) {
    const data = await ApiService.getOne(url, id)
    if (data) {
      proveedor.value = data
    }
  }
  async function create(nuevoProveedor: Proveedor) {
    const data = await ApiService.create(url, nuevoProveedor)
    if (data) {
      proveedor.value = data
    }
  }
  async function update(actProveedor: Proveedor) {
    if (actProveedor.id) {
      const data = await ApiService.update(url, actProveedor.id, actProveedor)
      if (data) {
        proveedor.value = data
      }
    }
  }
  async function destroy(id: number) {
    const data = await ApiService.destroy(url, id)
    if (data) {
      proveedor.value = data
    }
  }

  return { proveedores, proveedor, getAll, getOne, create, update, destroy }
})

export default useProveedoresStore
