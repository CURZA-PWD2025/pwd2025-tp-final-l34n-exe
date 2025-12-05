<template>
  <div>
    <h2>Sabores en cada item</h2>

    <ButtonComponent :to="{ name: 'itemventasabores_create' }">
      <template #pre-icon>
        <Icon
          icon="oui:ml-create-single-metric-job"
          width="28"
          height="28"
          style="color: green"
        />
      </template>
      CREAR SABOR DEL ITEM
    </ButtonComponent>

    <v-table density="comfortable">
      <thead>
        <tr>
          <th>ID</th>
          <th>ID ITEM</th>
          <th>SABOR</th>
          <th>ACCIONES</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="itemventasabor in itemventasabores" :key="itemventasabor.id">
          <td>{{ itemventasabor.id }}</td>
          <td>{{ itemventasabor.itemventa?.id }}</td>
          <td>{{ itemventasabor.sabor?.nombre }}</td>

          <td class="acciones">
            <ButtonComponent
              :to="{ name: 'itemventasabores_edit', params: { id: itemventasabor.id } }"
              style="color: #1976d2"
            >
              <template #pre-icon>
                <Icon
                  icon="material-symbols:edit-outline"
                  width="28"
                  height="28"
                  style="color: #1976d2"
                />
              </template>
              EDITAR
            </ButtonComponent>

            <ButtonComponent
              :to="{ name: 'itemventasabores_show', params: { id: itemventasabor.id } }"
            >
              <template #post-icon>
                <Icon icon="iconoir:eye" width="28" height="28" />
              </template>
              MOSTRAR
            </ButtonComponent>

            <ButtonComponent
              @click="deleteItemVentaSabor(itemventasabor.id as number)"
              style="color: red"
            >
              <template #pre-icon>
                <Icon
                  icon="typcn:delete-outline"
                  width="28"
                  height="28"
                  style="color: red"
                />
              </template>
              ELIMINAR
            </ButtonComponent>
          </td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import useItemVentaSaboresStore from '@/stores/itemventasabores'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'

const itemVentaSaboresStore = useItemVentaSaboresStore()
const { itemventasabores } = toRefs(itemVentaSaboresStore)
const { getAll, destroy } = itemVentaSaboresStore

const deleteItemVentaSabor = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este producto?')) {
    await destroy(id)
    await getAll()
  }
}

onMounted(async () => {
  await getAll()
})
</script>

<style scoped>
h2 {
  margin-bottom: 15px;
  font-size: 26px;
  font-weight: 600;
  color: #333;
  text-align: center;
}

.acciones {
  display: flex;
  gap: 10px;
  align-items: center;
}
</style>
