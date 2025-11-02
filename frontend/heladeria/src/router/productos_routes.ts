const productos_routes = [
  {
    path: '/productos',
    name: 'productos',
    component: () => import('../views/ProductosView.vue'),
    children: [
      {
        path: '',
        name: 'productos_list',
        component: () => import('../components/productos/ProductosList.vue')
      },
      {
        path: ':id/show',
        name: 'productos_show',
        component: () => import('../components/productos/ProductosShow.vue')
      },
      {
        path: 'create',
        name: 'productos_create',
        component: () => import('../components/productos/ProductosCreate.vue')
      },
      {
        path: ':id/edit',
        name: 'productos_edit',
        component: () => import('../components/productos/ProductosUpdate.vue'),
      }
    ]
  }
]

export default productos_routes
