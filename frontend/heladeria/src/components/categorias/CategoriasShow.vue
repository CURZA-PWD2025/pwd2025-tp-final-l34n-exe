<template>
  <div class="container">
    <v-card class="mx-auto my-8" variant="outlined" elevation="16" max-width="300">
      <v-card-title class="text-h6 text-center">Detalle de la categoria</v-card-title>
      <v-card-text>
        <p><strong>ID:</strong> {{ categoria.id }}</p>
        <p><strong>NOMBRE:</strong> {{ categoria.nombre }}</p>
        <p><strong>TIPO:</strong> {{ categoria.tipo }}</p>
        <p><strong>DESCRIPCIÓN:</strong> {{ categoria.descripcion }}</p>
        <div class="acciones">
          <ButtonComponent
            :to="{ name: 'categorias_edit', params: { id: categoria.id } }"
            style="color: #1976d2"
          >
            <template #pre-icon
              ><Icon
                icon="material-symbols:edit-outline"
                width="28"
                height="28"
                style="color: #1976d2"
            /></template>
            EDITAR
          </ButtonComponent>
          <ButtonComponent @click="deleteCategoria(categoria.id as number)" style="color: red">
            <template #pre-icon
              ><Icon icon="typcn:delete-outline" width="28" height="28" style="color: red"></Icon
            ></template>
            Eliminar
          </ButtonComponent>
        </div>
      </v-card-text>
    </v-card>
    <ButtonComponent class="volver" :to="{ name: 'categorias_list' }">
      <template #pre-icon><Icon icon="ic:twotone-list" width="28" height="28"  style="color: black" /></template>
      VOLVER A LA LISTA
    </ButtonComponent>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import useCategoriasStore from '@/stores/categorias'
import ButtonComponent from '../ButtonComponent.vue'
import { Icon } from '@iconify/vue'
const store = useCategoriasStore()
const { categoria } = toRefs(store)
const { getOne, destroy } = store
const route = useRoute()
const router = useRouter()

const deleteCategoria = async (id: number) => {
  if (confirm('¿Está seguro que desea eliminar este CategdeleteCategoria?')) {
    await destroy(id)
    router.push({ name: 'categorias_list' })
  }
}

onMounted(async () => {
  const id = Number(route.params.id)
  if (id) {
    await getOne(id)
  }
})
</script>

<style scoped>
.acciones{
  display: flex;
}
</style>
