import type { Producto } from '@/interfaces/Producto'
import type { Proveedor } from '@/interfaces/Proveedor'
import type { Categoria } from '@/interfaces/Categoria'
import { defineStore } from 'pinia'
import ApiService from '@/services/ApiService'
import { ref } from 'vue'

const useProductosStore = defineStore('productos', () => {
  const productos = ref<Array<Producto>>([])
  const producto = ref<Producto>({
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
    } as Proveedor,
    categoria: {
      id: 0,
      nombre: '',
      tipo: '',
      descripcion: '',
    } as Categoria,
  })
  const url = 'productos'
  async function getAll() {
    const data = await ApiService.getAll(url)
    if (data) {
      productos.value = data
    }
  }
  async function getOne(id: number) {
    const data = await ApiService.getOne(url, id)
    if (data) {
      producto.value = data
    }
  }
  async function create(nuevoProducto: Producto) {
    const data = await ApiService.create(url, nuevoProducto)
    if (data) {
      producto.value = data
    }
  }
  async function update(actProducto: Producto) {
    if (actProducto.id) {
      const data = await ApiService.update(url, actProducto.id, actProducto)
      if (data) {
        producto.value = data
      }
    }
  }
  async function destroy(id: number) {
    const data = await ApiService.destroy(url, id)
    if (data) {
      producto.value = data
    }
  }

  return { productos, producto, getAll, getOne, create, update, destroy }
})

export default useProductosStore
