// src/router.ts
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/HomeView.vue'),  // Dynamically import Home.vue
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/LoginForms.vue'),  // Dynamically import LoginPage.vue
  },
    {
    path: '/navbar',
    name: 'NavBar',
    component: () => import('@/views/NavBar.vue'),  // Dynamically import LoginPage.vue
  },
  // Możesz dodać inne ścieżki tutaj
]

const router = createRouter({
  history: createWebHistory('/'), // Użyj stałej wartości
  routes,
});

export default router
