import type { Empleado } from "./Empleado";
import type { Cliente } from "./Cliente";

export interface Venta {
  id?: number
  fecha?: string | Date
  total?: number
  estado?: string
  cliente?: Cliente
  empleado?: Empleado
}
