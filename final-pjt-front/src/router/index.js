import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import SearchView from '../views/SearchView.vue'
import MyPageView from '@/views/MyPageView.vue'
import ArticleView from '../views/ArticleView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import MapsView from '@/views/MapsView.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import AddInfoView from '@/views/AddInfoView.vue'
import HiddenView from '@/views/HiddenView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/mypage',
      name: 'mypage',
      component: MyPageView
    },
    {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/product/:id',
      name: 'productDetail',
      component: ProductDetailView
    },
    {
      path: '/exchange_rate',
      name: 'exchangeRateView',
      component: ExchangeRateView
    },
    {
      path: '/article/:id',
      name: 'article_detail',
      component: ArticleDetailView
    },
    {
      path: '/article_create',
      name: 'article_create',
      component: ArticleCreateView
    },
    {
      path: '/maps',
      name: 'maps',
      component: MapsView
    },
    {
      path: '/article_update/:id',
      name: 'article_update',
      component: ArticleUpdateView
    },
    {
      path: '/add_info/',
      name: 'addInfo',
      component: AddInfoView
    },
    {
      path: '/hidden',
      name: 'hidden',
      component: HiddenView
    },
  ]
})


export default router
