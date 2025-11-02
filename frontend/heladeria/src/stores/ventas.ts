import type { Venta } from "@/interfaces/Venta";
import type { Empleado } from "@/interfaces/Empleado";
import type { Cliente } from "@/interfaces/Cliente";
import { defineStore } from "pinia";
import ApiService from '@/services/ApiService';
import { ref } from 'vue';

const useVentasStore = defineStore('ventas',() => {
  const ventas = ref<Array<Venta>>([])
  const venta = ref<Venta>({
    id: 0,
    fecha: '',
    total: 0,
    cliente: {
      id: 0,
      nombre: '',
      apellido: '',
      telefono: '',
      direccion: ''
    } as Cliente,
    empleado: {
      id: 0,
      nombre: '',
      apellido: '',
      telefono: '',
      email: '',
      puesto: ''
    } as Empleado
  })
  const url = 'ventas'
  async function getAll(){
    const data = await ApiService.getAll(url)
    if(data){
      ventas.value = data
    }
  }
  async function getOne(id: number){
    const data = await ApiService.getOne(url, id)
    if(data){
      venta.value = data
    }
  }
  async function create(nuevaVenta: Venta){
    const data = await ApiService.create(url, nuevaVenta)
    if(data){
      venta.value = data
    }
  }
  async function update(actVenta: Venta){
    if(actVenta.id){
      const data = await ApiService.update(url, actVenta.id, actVenta)
      if(data){
        venta.value = data
    }
  }
}
  async function destroy(id: number){
    const data = await ApiService.destroy(url, id)
    if(data){
      venta.value = data
    }
  }
  return {ventas, venta, getAll, getOne, create, update, destroy}
})

export default useVentasStore;
