import type { ItemVenta } from '@/interfaces/ItemVenta'
import type { Sabor } from '@/interfaces/Sabor'
import { defineStore } from 'pinia'
import ApiService from '@/services/ApiService'
import { ref } from 'vue'
import type { ItemVentaSabor } from '@/interfaces/ItemVentaSabor'

const useItemVentasSaboresStore = defineStore('itemventasabores', () => {
  const itemventasabores = ref<Array<ItemVentaSabor>>([])
  const itemventasabor = ref<ItemVentaSabor>({
    id: 0,
    itemventa: {
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
      },
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
      },
      cantidad: 0,
    } as ItemVenta,
    sabor: {
      id: 0,
      nombre: '',
      stock: 0,
      disponible: true,
      categoria: {
        id: 0,
        nombre: '',
        tipo: '',
        descripcion: '',
      },
    } as Sabor,
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
  function limpiarItemVentaSabor() {
    itemventasabor.value = {
      id: 0,
      itemventa: {
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
        },
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
        },
        cantidad: 0,
      } as ItemVenta,
      sabor: {
        id: 0,
        nombre: '',
        stock: 0,
        disponible: true,
        categoria: {
          id: 0,
          nombre: '',
          tipo: '',
          descripcion: '',
        },
      } as Sabor,
    }
  }
  return {
    itemventasabores,
    itemventasabor,
    getAll,
    getOne,
    create,
    update,
    destroy,
    limpiarItemVentaSabor,
  }
})

export default useItemVentasSaboresStore
