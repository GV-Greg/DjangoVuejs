import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import DirhmHomeView from '@/views/dirhm/DirhmHomeView.vue'
import DirhmConfigView from '@/views/dirhm/DirhmConfigView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/dirhm',
    children: [
      {
        path: '',
        name: 'dirhm-home',
        component: DirhmHomeView
      },
      {
        path: 'config',
        name: 'dirhm-config',
        component: DirhmConfigView
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
