const itemventas_routes = [
  {
    path: '/itemventas',
    name: 'itemventas',
    component: () => import('../views/ItemVentasView.vue'),
    children: [
      {
        path: '',
        name: 'itemventas_list',
        component: () => import('../components/itemventas/ItemVentasList.vue')
      },
      {
        path: ':id/show',
        name: 'itemventas_show',
        component: () => import('../components/itemventas/ItemVentasShow.vue')
      },
      {
        path: 'create',
        name: 'itemventas_create',
        component: () => import('../components/itemventas/ItemVentasCreate.vue')
      },
      {
        path: ':id/edit',
        name: 'itemventas_edit',
        component: () => import('../components/itemventas/ItemVentasUpdate.vue'),
      }
    ]
  }
]

export default itemventas_routes
