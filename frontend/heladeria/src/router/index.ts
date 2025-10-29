import HomeView from '@/views/HomeView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import proveedores_routes from './proveedores_routes'
const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  ...proveedores_routes,

]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes

})

export default router
