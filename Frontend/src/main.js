import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia';

// General format
import 'vfonts/Lato.css'
// Mono format
import 'vfonts/FiraCode.css'

import router from "./router/router";

const app = createApp(App)

const pinia = createPinia(App)

// use vue-router
app.use(router)

// use pinia for states management
app.use(pinia)

// mount the app
app.mount('#app')

