<script setup lang="ts">
import { ref } from "vue";
import { RouterLink, RouterView } from 'vue-router'

import DarkMode from "@/components/DarkMode.vue";
</script>

<template>

  <div class="absolute top-0 left-0 size-16 ...">
    <DarkMode/>
  </div>


  <RouterView/>

</template>

<style scoped>




</style>
