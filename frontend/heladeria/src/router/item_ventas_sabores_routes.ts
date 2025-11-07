const itemventasabores_routes = [
  {
    path: '/itemventasabores',
    name: 'itemventasabores',
    component: () => import('../views/ItemVentaSaboresView.vue'),
    children: [
      {
        path: '',
        name: 'itemventasabores_list',
        component: () => import('../components/itemventasabores/ItemVentaSaboresList.vue')
      },
      {
        path: ':id/show',
        name: 'itemventasabores_show',
        component: () => import('../components/itemventasabores/ItemVentaSaboresShow.vue')
      },
      {
        path: 'create',
        name: 'itemventasabores_create',
        component: () => import('../components/itemventasabores/ItemVentaSaboresCreate.vue')
      },
      {
        path: ':id/edit',
        name: 'itemventasabores_edit',
        component: () => import('../components/itemventasabores/ItemVentaSaboresUpdate.vue'),
      }
    ]
  }
]

export default itemventasabores_routes
