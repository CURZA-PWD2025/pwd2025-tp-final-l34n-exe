const sabores_routes = [
  {
    path: '/sabores',
    name: 'sabores',
    component: () => import('../views/SaboresView.vue'),
    children: [
      {
        path: '',
        name: 'sabores_list',
        component: () => import('../components/sabores/SaboresList.vue')
      },
      {
        path: ':id/show',
        name: 'sabores_show',
        component: () => import('../components/sabores/SaboresShow.vue')
      },
      {
        path: 'create',
        name: 'sabores_create',
        component: () => import('../components/sabores/SaboresCreate.vue')
      },
      {
        path: ':id/edit',
        name: 'sabores_edit',
        component: () => import('../components/sabores/SaboresUpdate.vue'),
      }
    ]
  }
]

export default sabores_routes
