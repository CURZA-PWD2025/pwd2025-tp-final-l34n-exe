import { defineStore } from 'pinia'
import ApiService from '@/services/ApiService'
import { ref } from 'vue'
import type { ItemVentaSabor } from '@/interfaces/ItemVentaSabor'

const useItemVentasSaboresStore = defineStore('itemventasabores', () => {
  const itemventasabores = ref<Array<ItemVentaSabor>>([])
  const itemventasabor = ref<ItemVentaSabor>({
    id: 0,
    itemventa: { id: 0 },
    sabor: { id: 0 },
  })

  const url = 'itemventasabores'
  async function getAll() {
    const data = await ApiService.getAll(url)
    if (data) {
      itemventasabores.value = data
    }
  }
  async function getOne(id: number) {
    const data = await ApiService.getOne(url, id)
    if (data) {
      itemventasabor.value = data
    }
  }
  async function create(nuevoItemVentaSabor: ItemVentaSabor) {
    const data = await ApiService.create(url, nuevoItemVentaSabor)
    if (data) {
      itemventasabor.value = data
    }
  }
  async function update(actItemVentaSabor: ItemVentaSabor) {
    if (actItemVentaSabor.id) {
      const data = await ApiService.update(url, actItemVentaSabor.id, actItemVentaSabor)
      if (data) {
        itemventasabor.value = data
      }
    }
  }
  async function destroy(id: number) {
    const data = await ApiService.destroy(url, id)
    if (data) {
      itemventasabor.value = data
    }
  }

  return {
    itemventasabores,
    itemventasabor,
    getAll,
    getOne,
    create,
    update,
    destroy
  }
})

export default useItemVentasSaboresStore
