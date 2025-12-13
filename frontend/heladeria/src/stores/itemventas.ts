import type { ItemVenta } from '@/interfaces/ItemVenta'
import type { Producto } from '@/interfaces/Producto'
import { defineStore } from 'pinia'
import ApiService from '@/services/ApiService'
import { ref } from 'vue'
import type { Venta } from '@/interfaces/Venta'

const useItemVentasStore = defineStore('itemventas', () => {
  const itemventas = ref<Array<ItemVenta>>([])
  const itemventa = ref<ItemVenta>({
    id: 0,
    venta: {
      id: 0,
      fecha: '',
      total: 0,
      cliente: {
        id: 0,
        nombre: '',
        apellido: '',
      },
      empleado: {
        id: 0,
        nombre: '',
        apellido: '',
      },
    } as Venta,
    producto: {
      id: 0,
      nombre: '',
      precio: 0,
      stock: 0,
      max_sabores: 0,
      proveedor: {
        id: 0,
        nombre: '',
        telefono: '',
        email: '',
      },
      categoria: {
        id: 0,
        nombre: '',
        tipo: '',
        descripcion: '',
      },
    } as Producto,
    cantidad: 0,
  })

  const url = 'itemventas'
  async function getAll() {
    const data = await ApiService.getAll(url)
    if (data) {
      itemventas.value = data
    }
  }
  async function getOne(id: number) {
    const data = await ApiService.getOne(url, id)
    if (data) {
      itemventa.value = data
    }
  }
  async function create(nuevoItemVenta: ItemVenta) {
    const data = await ApiService.create(url, nuevoItemVenta)
    if (data) {
      itemventa.value = data
    }
  }
  async function update(actItemVenta: ItemVenta) {
    if (actItemVenta.id) {
      const data = await ApiService.update(url, actItemVenta.id, actItemVenta)
      if (data) {
        itemventa.value = data
      }
    }
  }
  async function destroy(id: number) {
    const data = await ApiService.destroy(url, id)
    if (data) {
      itemventa.value = data
    }
  }
  function limpiarItemVenta() {
    itemventa.value = {
    id: 0,
    venta: {
      id: 0,
      fecha: '',
      total: 0,
      cliente: {
        id: 0,
        nombre: '',
        apellido: '',
      },
      empleado: {
        id: 0,
        nombre: '',
        apellido: '',
      },
    } as Venta,
    producto: {
      id: 0,
      nombre: '',
      precio: 0,
      stock: 0,
      max_sabores: 0,
      proveedor: {
        id: 0,
        nombre: '',
        telefono: '',
        email: '',
      },
      categoria: {
        id: 0,
        nombre: '',
        tipo: '',
        descripcion: '',
      },
    } as Producto,
    cantidad: 0,
  }}
  return { itemventas, itemventa, getAll, getOne, create, update, destroy, limpiarItemVenta}
})

export default useItemVentasStore
