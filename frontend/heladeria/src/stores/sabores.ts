import type { Sabor } from "@/interfaces/Sabor";
import { defineStore } from "pinia";
import ApiService from '@/services/ApiService';
import { ref } from 'vue';
import type { Categoria } from "@/interfaces/Categoria";

const useSaboresStore = defineStore('sabores',() => {
  const sabores = ref<Array<Sabor>>([])
  const sabor = ref<Sabor>({
    id: 0,
    nombre: '',
    stock: 0,
    disponible: 0,
    categoria: {
      id: 0,
      nombre: '',
      tipo: '',
      descripcion: ''
    } as Categoria
  })
  const url = 'sabores'
  async function getAll(){
    const data = await ApiService.getAll(url)
    if(data){
      sabores.value = data
    }
  }
  async function getOne(id: number){
    const data = await ApiService.getOne(url, id)
    if(data){
      sabor.value = data
    }
  }
  async function create(nuevoSabor: Sabor){
    const data = await ApiService.create(url, nuevoSabor)
    if(data){
      sabor.value = data
    }
  }
  async function update(actSabor: Sabor){
    if(actSabor.id){
      const data = await ApiService.update(url, actSabor.id, actSabor)
      if(data){
        sabor.value = data
    }
  }
}
  async function destroy(id: number){
    const data = await ApiService.destroy(url, id)
    if(data){
      sabor.value = data
    }
  }
  return {sabores, sabor, getAll, getOne, create, update, destroy}
})

export default useSaboresStore;
