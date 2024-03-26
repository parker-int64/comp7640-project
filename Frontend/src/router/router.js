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
        path: "/item/:id",
        name: "product",
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
      path: '/manage',
      name: 'manage',
      component: () => import('../views/RoleSelect.vue')
    },


    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfilePage.vue')
    },


    {
      path: '/search/:searchParam',
      name: 'search',
      component: () => import('../views/SearchPage.vue')
    }
  ],
});

export default router;