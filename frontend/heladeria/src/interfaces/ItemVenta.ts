import type { Producto } from './Producto'
import type { Venta } from './Venta'

export interface ItemVenta {
  id?: number
  venta?: Venta | null
  producto?: Producto
  cantidad?: number
  subtotal?: number
}
