const clientes_routes = [
  {
    path: '/clientes',
    name: 'clientes',
    component: () => import('../views/ClientesView.vue'),
    children: [
      {
        path: '',
        name: 'clientes_list',
        component: () => import('../components/clientes/ClientesList.vue')
      },
      {
        path: ':id/show',
        name: 'clientes_show',
        component: () => import('../components/clientes/ClientesShow.vue')
      },
      {
        path: 'create',
        name: 'clientes_create',
        component: () => import('../components/clientes/ClientesCreate.vue')
      },
      {
        path: ':id/edit',
        name: 'clientes_edit',
        component: () => import('../components/clientes/ClientesUpdate.vue'),
      }
    ]
  }
]

export default clientes_routes
