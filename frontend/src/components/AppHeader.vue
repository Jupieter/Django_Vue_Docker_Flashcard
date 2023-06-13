<script setup>
import { ref } from 'vue'
const loginData = JSON.parse(localStorage.getItem('userData')) || { expiry: null, token: null, isLogin: false }
console.log('loginData', loginData.isLogin)
const isActive =ref("")
if (loginData.isLogin) {
  isActive.value = "disabled"
} else isActive.value = ""
console.log('isActive', isActive.value)

</script>


<template>
  <nav class="navbar navbar-expand-sm navbar-light bg-light">
    <div class="container">
      <img src="../../public/VUE_Django_1.png" class="logo rounded float-start pe-5" alt="VUE_Django">
      <a class="navbar-brand" href="/"> Flash Card</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li v-show="loginData.isLogin" class="nav-item">
            <a class="nav-link" href="/cardset">Card Sets</a>
          </li>
          <li class="nav-item">
            <a :class="{ 'nav-link': true, 'active': isActive }" href="/study">Study</a>
          </li>
          <li class="nav-item">
            <a v-show="loginData.isLogin" class="nav-link" href="/login">Log Out</a>
            <a v-show="!loginData.isLogin" class="nav-link" href="/login">Log In</a>
          </li>
        </ul>
        <img src="../../public/Under_Construction_1.png" class="logo rounded float-end ps-5" alt="Under_Construction">
      </div>
    </div>
  </nav>
</template>


<style scoped>
.logo {
  height: 3rem;
}
.disabled {
  cursor: not-allowed;
  color: gray
}
</style>