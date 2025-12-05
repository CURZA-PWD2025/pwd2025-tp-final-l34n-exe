<template>
  <div>
    <BaseLayout>
      <template #logo>
        <LogoComponent />
      </template>

      <template #nav>
        <nav>
          <ul class="menu">
            <li><RouterLink :to="{ name: 'categorias_list' }"><Icon icon="ep:list" width="28" height="28" />Categorías</RouterLink></li>
            <li><RouterLink :to="{ name: 'sabores_list' }"><Icon icon="noto:soft-ice-cream" width="28" height="28" />Sabores</RouterLink></li>
            <li><RouterLink :to="{ name: 'productos_list' }"><Icon icon="logos:producthunt" width="28" height="28" />Productos</RouterLink></li>
            <li><RouterLink :to="{ name: 'proveedores_list' }"><Icon icon="streamline-freehand:business-product-supplier-2" width="28" height="28" style="color: aliceblue;" />Proveedores</RouterLink></li>
          </ul>
        </nav>
      </template>

      <template #main>
        <router-view></router-view>
      </template>

      <template #aside>
        <aside>
          <ul class="menu-vertical">
            <li>
              <RouterLink :to="{ name: 'clientes_list' }">
                <Icon icon="gravity-ui:person-fill" width="28" /> Clientes
              </RouterLink>
            </li>

            <li>
              <RouterLink :to="{ name: 'empleados_list' }">
                <Icon icon="streamline-cyber:person" width="28" /> Empleados
              </RouterLink>
            </li>

            <li>
              <RouterLink :to="{ name: 'ventas_list' }">
                <Icon icon="streamline-emojis:money-bag" width="32" /> Ventas
              </RouterLink>
            </li>
          </ul>
        </aside>
      </template>

      <template #footer>
        <FooterComponent />
      </template>
    </BaseLayout>
  </div>
</template>

<script setup lang="ts">
import { Icon } from '@iconify/vue'
import BaseLayout from './layouts/BaseLayout.vue'
import FooterComponent from './components/FooterComponent.vue'
import LogoComponent from './components/LogoComponent.vue'
</script>

<style scoped>
.menu,
.menu-vertical {
  list-style: none;
  margin: 0;
  padding: 0;
}

.menu li a,
.menu-vertical li a {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  text-decoration: none;
  font-weight: bold;
  color: #060707;
  transition: 0.2s;
  font-size: large;
}

.menu-vertical li a:hover {
  background: #00aaff;
  color: white;
  border-color: #0088cc;
}

.menu li a:hover{
  background: #0ce679;
  color: #000;
  border-color: #0ce677 ;
}

nav .menu {
  display: flex;
  gap: 12px;
}

.menu-vertical {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

</style>
