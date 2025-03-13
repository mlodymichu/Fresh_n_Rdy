<script setup lang="ts">
import {ref} from "vue";
import {RouterLink, RouterView} from 'vue-router'
import {computed} from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()


import NavBar from '@/views/NavBar.vue'

const hiddenNavRoutes = ['/login','/']
const shouldShowNavbar = computed(() => !hiddenNavRoutes.includes(route.path))
</script>

<template>
  <NavBar v-if="shouldShowNavbar"/>

  <!--  <div class="absolute top-0 left-0 size-16 ...">-->
  <!--    <DarkMode/>-->
  <!--  </div>-->


  <RouterView/>

</template>

<style scoped>


</style>
