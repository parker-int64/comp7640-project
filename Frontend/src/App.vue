<script setup>
import { RouterView } from 'vue-router';
import { NLayout, NLayoutContent, NScrollbar, NDivider } from 'naive-ui'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import LoginRegister from './pages/LoginRegisterPage.vue';
</script>

<template>
  <n-layout>
    <Header />
    <n-divider />

    <n-scrollbar trigger="hover" style="height: 100vh;">
      <n-layout-content content-style="padding: 24px;">
        <p>Content...
          <LoginRegister>

          </LoginRegister>
        </p>
      </n-layout-content>
      <Footer />
    </n-scrollbar>



  </n-layout>

  <!-- <RouterView /> -->

</template>

<style scoped>
body,
html {
  margin: 0;
  padding: 0;
}

.main-container {
  width: 100%;
  height: 100vh;
}
</style>
