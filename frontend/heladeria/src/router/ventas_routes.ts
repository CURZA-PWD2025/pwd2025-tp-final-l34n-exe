const ventas_routes = [
  {
    path: '/ventas',
    name: 'ventas',
    component: () => import('../views/VentasView.vue'),
    children: [
      {
        path: '',
        name: 'ventas_list',
        component: () => import('../components/ventas/VentasList.vue')
      },
      {
        path: ':id/show',
        name: 'ventas_show',
        component: () => import('../components/ventas/VentasShow.vue')
      },
      {
        path: 'create',
        name: 'ventas_create',
        component: () => import('../components/ventas/VentasCreate.vue')
      },
      {
        path: ':id/edit',
        name: 'ventas_edit',
        component: () => import('../components/ventas/VentasUpdate.vue'),
      }
    ]
  }
]

export default ventas_routes
