<template>
  <div>
    <ButtonComponent @click="volverAlInicio">
      <template #pre-icon>
        <Icon icon="stash:arrow-left-duotone" width="48" height="48"  style="color: #05f036" />
      </template>
      VOLVER AL INICIO
    </ButtonComponent>
    <RouterView></RouterView>

  </div>
</template>

<script setup lang="ts">
import ButtonComponent from '@/components/ButtonComponent.vue'
import { useRouter } from 'vue-router'
import { Icon } from '@iconify/vue'
const router = useRouter()

const volverAlInicio = () => {
  router.push({name:'HomeView'})
}

</script>

<style scoped>

</style>
