import type { Categoria } from "./Categoria";
import type { Proveedor } from "./Proveedor";
export interface Producto{
  id?: number,
  nombre: string,
  precio: number,
  stock: number,
  max_sabores: number,
  proveedor?: Proveedor,
  categoria?: Categoria
}
