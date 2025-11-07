import HomeView from '@/views/HomeView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import proveedores_routes from './proveedores_routes'
import empleados_routes from './empleados_routes'
import categorias_routes from './categorias_routes'
import clientes_routes from './clientes_routes'
import sabores_routes from './sabores_routes'
import productos_routes from './productos_routes'
import ventas_routes from './ventas_routes'
import itemventas_routes from './item_ventas_routes'
import itemventasabores_routes from './item_ventas_sabores_routes'
const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  ...proveedores_routes,
  ...empleados_routes,
  ...categorias_routes,
  ...clientes_routes,
  ...sabores_routes,
  ...productos_routes,
  ...ventas_routes,
  ...itemventas_routes,
  ...itemventasabores_routes

]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes

})

export default router
