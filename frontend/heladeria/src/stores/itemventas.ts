import type { ItemVenta } from '@/interfaces/ItemVenta'
import { defineStore } from 'pinia'
import ApiService from '@/services/ApiService'
import { ref } from 'vue'

const useItemVentasStore = defineStore('itemventas', () => {
  const itemventas = ref<Array<ItemVenta>>([])
  const itemventa = ref<ItemVenta>({
    id: 0,
    cantidad: 0,
    subtotal: 0,
    venta: { id: 0 },
    producto: { id: 0 },
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

  return { itemventas, itemventa, getAll, getOne, create, update, destroy }
})

export default useItemVentasStore
