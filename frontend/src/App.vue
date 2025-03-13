<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'

import NavBar from '@/views/NavBar.vue'

const hiddenNavRoutes = ['/login', '/register', '/']
const route = useRoute()


const shouldShowNavbar = computed(() => !hiddenNavRoutes.includes(route.path))
</script>

<template>
  <NavBar v-if="shouldShowNavbar"/>
  <RouterView/>
</template>

<style scoped>
</style>
