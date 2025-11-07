import type { Categoria } from "@/interfaces/Categoria";
import { defineStore } from "pinia";
import ApiService from '@/services/ApiService';
import { ref } from 'vue';

const useCategoriasStore = defineStore('categorias',() => {
  const categorias = ref<Array<Categoria>>([])
  const categoria = ref<Categoria>({
    id: 0,
    nombre: '',
    tipo: '',
    descripcion: ''
  })
  const url = 'categorias'
  async function getAll(){
    const data = await ApiService.getAll(url)
    if(data){
      categorias.value = data
    }
  }
  async function getOne(id: number){
    const data = await ApiService.getOne(url, id)
    if(data){
      categoria.value = data
    }
  }
  async function create(nuevaCategoria: Categoria){
    const data = await ApiService.create(url, nuevaCategoria)
    if(data){
      categoria.value = data
    }
  }
  async function update(actCategoria: Categoria){
    if(actCategoria.id){
      const data = await ApiService.update(url, actCategoria.id, actCategoria)
      if(data){
        categoria.value = data
    }
  }
}
  async function destroy(id: number){
    const data = await ApiService.destroy(url, id)
    if(data){
      categoria.value = data
    }
  }
  return {categorias, categoria, getAll, getOne, create, update, destroy}
})

export default useCategoriasStore;
