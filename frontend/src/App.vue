<script setup>
import AppHeader from "./components/AppHeader.vue";
import { useUserStore } from '../stores/user'
import router from './router.js'

const loginData = JSON.parse(localStorage.getItem('userData')) || { expiry: null, token: null, isLogin: false }
const userData = useUserStore()
userData.expiry = (loginData.isLogin ? loginData.expiry : "")
userData.token = (loginData.isLogin ? loginData.token : "")
userData.isLogin = loginData.isLogin
console.log('AppVue isLogin:  ', userData.isLogin)

const isLastApiCallRecent =
  new Date(loginData.expiry).getTime() - new Date().getTime()
console.log('AppVue Date:  ', isLastApiCallRecent)
if (isLastApiCallRecent > (1000 * 60 * 10)) {
  userData.isLogin = true;
} else {
  userData.isLogin = false;
}


console.log('loginData', loginData.isLogin)

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
      <main>
        <router-view></router-view>
      </main>
    </div>
  </body>

  </html>
</template>


<style>
.df {
  display: flex;
  gap: 1rem;
}
main {
    padding: 10vh 0.5rem 22vh 0.5rem;
    overflow: scroll;
  }
</style>
