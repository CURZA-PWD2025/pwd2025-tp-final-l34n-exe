const empleados_routes = [
  {
    path: '/empleados',
    name: 'empleados',
    component: () => import('../views/EmpleadosView.vue'),
    children: [
      {
        path: '',
        name: 'empleados_list',
        component: () => import('../components/empleados/EmpleadosList.vue')
      },
      {
        path: ':id/show',
        name: 'empleados_show',
        component: () => import('../components/empleados/EmpleadosShow.vue')
      },
      {
        path: 'create',
        name: 'empleados_create',
        component: () => import('../components/empleados/EmpleadosCreate.vue')
      },
      {
        path: ':id/edit',
        name: 'empleados_edit',
        component: () => import('../components/empleados/EmpleadosUpdate.vue'),
      }
    ]
  }
]

export default empleados_routes
