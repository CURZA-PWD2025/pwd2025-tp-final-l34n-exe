import type { Empleado } from "./Empleado";
import type { Cliente } from "./Cliente";

export interface Venta{
  id?: number,
  fecha: string | Date,
  total: number,
  cliente?: Cliente,
  empleado?: Empleado
}
