<script setup>
  // import { useUserStore } from '../stores/user.js'
  import router from './router'
  import AppHeader from "./components/AppHeader.vue";

  // const userData = useUserStore()
  // userData.isLogin = false;

const MyComponent = {
  name: 'MyComponent',
  AppHeader,
};

 
</script>


<template>
  <!DOCTYPE html>
  <html lang="en">

  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  </head>

  <body>
    <div id="app">
      <AppHeader />
      <router-view></router-view>
      <!-- <CardSets /> -->
    </div>
  </body>

  </html>
</template>


<style>
.df {
  display: flex;
  gap: 1rem;
}
</style>