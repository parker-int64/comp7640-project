import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'

// General format
import 'vfonts/Lato.css'
// Mono format
import 'vfonts/FiraCode.css'

const routes = [
    {
        path: '/', 
        component: App
    },

    {
        path: '/home', 
        component: () => import('./pages/HomePage.vue')
    },
    {
        path: '/login',
        component: () => import('./pages/LoginPage.vue')
    },
    {
        path: '/register',
        component: () => import('./pages/RegisterPage.vue')
    },
]

const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL),
    routes, // your routes
})

const app = createApp(App)

// use vue-router
app.use(router)

// mount the app
app.mount('#app')

