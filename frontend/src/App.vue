<script setup>
import AppHeader from "./components/AppHeader.vue";
import { useUserStore } from '../stores/user'

const loginData = JSON.parse(localStorage.getItem('userData')) || { expiry: null, token: null, isLogin: false }
console.log('loginData', loginData.isLogin)
const userData = useUserStore()
userData.expiry = (loginData.isLogin ? loginData.expiry : "")
userData.token = (loginData.isLogin ? loginData.token : "")
userData.isLogin = (loginData.isLogin ? loginData.isLogin :false)

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