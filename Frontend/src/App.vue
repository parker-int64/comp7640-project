<script setup>
import { RouterView } from 'vue-router';
import { NLayout, NLayoutContent, NFlex, NScrollbar } from 'naive-ui'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

</script>

<template>
  

  <n-layout class="main-layout">
    <n-flex vertical class="main-layout">
      <Header />
      <n-layout-content :content-style="{ width: '80%', margin: '20px auto'}">
        <n-scrollbar>
          <RouterView />
        </n-scrollbar>
      </n-layout-content>
      <Footer/>
    </n-flex>
    
  </n-layout>
 
</template>


<style>
html, body, #app, .main-layout {
  width: 100%;
  height: 100%;
}

html, body {
  margin: 0;
}

</style>
