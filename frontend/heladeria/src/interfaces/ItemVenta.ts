import type { Producto } from "./Producto";
import type { Venta } from "./Venta";
export interface ItemVenta{
  id?: number,
  venta?: Venta,
  producto?: Producto,
  cantidad: number
}
