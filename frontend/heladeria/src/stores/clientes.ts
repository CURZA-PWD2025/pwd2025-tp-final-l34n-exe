import type { Cliente } from "@/interfaces/Cliente";
import { defineStore } from "pinia";
import ApiService from '@/services/ApiService';
import { ref } from 'vue';

const useClientesStore = defineStore('clientes',() => {
  const clientes = ref<Array<Cliente>>([])
  const cliente = ref<Cliente>({
    id: 0,
    nombre: '',
    apellido: '',
    telefono: '',
    direccion: ''
  })
  const url = 'clientes'
  async function getAll(){
    const data = await ApiService.getAll(url)
    if(data){
      clientes.value = data
    }
  }
  async function getOne(id: number){
    const data = await ApiService.getOne(url, id)
    if(data){
      cliente.value = data
    }
  }
  async function create(nuevoCliente: Cliente){
    const data = await ApiService.create(url, nuevoCliente)
    if(data){
      cliente.value = data
    }
  }
  async function update(actCliente: Cliente){
    if(actCliente.id){
      const data = await ApiService.update(url, actCliente.id, actCliente)
      if(data){
        cliente.value = data
    }
  }
}
  async function destroy(id: number){
    const data = await ApiService.destroy(url, id)
    if(data){
      cliente.value = data
    }
  }
  return {clientes, cliente, getAll, getOne, create, update, destroy}
})

export default useClientesStore;
