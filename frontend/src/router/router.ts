// src/router.ts
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/HomeView.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/LoginForms.vue'),
  },
    {
    path: '/navbar',
    name: 'NavBar',
    component: () => import('@/views/NavBar.vue'),
  },
  {
    path: '/user',
    name: 'user',
    component: () => import('@/components/user/data-table-dropdown.vue')

  },
]

const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

export default router
