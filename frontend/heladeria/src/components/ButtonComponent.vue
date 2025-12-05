<template>
  <div>
    <v-btn variant="text" v-bind="$attrs">
      <slot name="pre-icon"></slot>
      <slot name="default">Default</slot>
      <slot name="post-icon"></slot>
    </v-btn>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>

</style>
