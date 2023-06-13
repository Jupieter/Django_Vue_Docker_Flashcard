<script setup>
import { useUserStore } from '../../stores/user'
import { ref } from 'vue'
const loginData = JSON.parse(localStorage.getItem('userData')) || { expiry: null, token: null, isLogin: false }
console.log('loginData', loginData.isLogin)


const userData = useUserStore()

</script>


<template>
  <nav v-show="userData.isLogin" class="navbar navbar-expand-sm navbar-light bg-light">
    <div class="container">
      <img src="../../public/VUE_Django_1.png" class="logo rounded float-start pe-5" alt="VUE_Django">
      <a class="navbar-brand" href="/"> Flash Card</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="/cardset">Card Sets</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/study">Study</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/login">Log Out</a>
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
</style>