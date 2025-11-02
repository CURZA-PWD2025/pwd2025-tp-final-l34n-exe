import type { Categoria } from "./Categoria"
export interface Sabor{
  id?: number,
  nombre: string,
  stock: number,
  disponible: boolean | number,
  categoria?: Categoria
}
