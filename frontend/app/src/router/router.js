import { createRouter, createWebHistory } from 'vue-router'
import PieChart from '../components/PieChart.vue'
import RankPage from '../components/RankPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: RankPage
  },
  {
    path: '/novel/:index',
    component: PieChart
  },

]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router