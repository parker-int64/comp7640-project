import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomePage,
    },

    {
        path: "/item",
        name: "Title",
        component: () => import("../views/ItemDetailPage.vue")
    },

    {
      path: "/trans",
        name: "Transactions",
        component: () => import("../views/TransPage.vue")
    },

    {
      path: '/404',
      name: '404',
      component: () => import('../views/404.vue')
    },

    {
      path: '/403',
      name: '403',
      component: () => import('../views/403.vue')
    },

    {
        path: '/:pathMatch(.*)',
        redirect: '/404'
    }, 
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginRegPage.vue')
    },

    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfilePage.vue')
    }
    
  ],
});

export default router;