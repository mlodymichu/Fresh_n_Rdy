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
    path: '/user',
    name: 'user',
    component: () => import('@/components/user/data-table-dropdown.vue')
  },
    {
    path: '/register',
    name: 'register',
    component: () => import('@/views/RegisterView.vue'),
  },

]

const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

export default router
