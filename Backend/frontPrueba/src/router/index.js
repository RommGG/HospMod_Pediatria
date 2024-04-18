import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import EditView from '../views/EditView.vue'
import EditmView from '../views/EditmView.vue'
import GraficaView from '../views/GraficaView.vue'
import GraficaMView from '../views/GraficaMView.vue'
import EmView from '../views/EmView.vue'
import TablamView from '../views/TablamView.vue'
import ConView from '@/views/ConView.vue'
import TablaView from '@/views/TablaView.vue'
import AboutView from '@/views/AboutView.vue'
import GraficaMongoView from '@/views/GraficaMongoView.vue'
import GraficaMongoView2 from '@/views/GraficaMongoView2.vue'
import DashboardView from '@/views/dashboardView.vue'


const routes = [

  {
    path :'/dash',
    name : 'dash',
    component: DashboardView

  },
  {
    path :'/contador',
    name : 'contador',
    component: ConView

  },
  {
    path :'/mongof1',
    name : 'mongof1',
    component: GraficaMongoView

  },

  {
    path :'/mongof2',
    name : 'mongof2',
    component: GraficaMongoView2

  },


  {
    path: '/',
    name: 'home',
    component: HomeView
    
  },
  {
    path: '/tablam',
    name: 'tablam',
    component: TablamView
  },
  {
    path: '/tablas',
    name: 'tablas',
    component: TablaView
  },
  {
    path: '/about',
    name: 'about',
  
    component:AboutView
   
  },

  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  
  {
    path: '/editar/:id',
    name:'editar',
    component: EditView
  },
  {
    path: '/grafica/',
    name:'grafica',
    component: GraficaView
  },
  {
    path: '/grafica2/',
    name:'grafica2',
    component: GraficaMView
  },
  {
    path: '/formm/',
    name:'formm',
    component: EmView
  },

  {
    path: '/editarm/:id',
    name:'editarm',
    component: EditmView
  }
 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
