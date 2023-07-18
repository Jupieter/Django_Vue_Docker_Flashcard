<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useUserStore } from '../../stores/user'
import router from '../router'

const username = ref('')
const pass = ref('')
const error = ref('')

const userData = useUserStore()
const waitingForServerResponse = ref(false)

if (!userData.isLogin) {
  logIn()
} else { router.push('/') }

function logIn() {
  if (!username.value || !pass.value) {
    error.value = 'Fill in both fields!'
    return
  }

  waitingForServerResponse.value = true;
  axios
    .post(`${import.meta.env.VITE_APP_API_URL}login/`, {
      username: username.value,
      password: pass.value,
    })
    .then(resp => {
      console.log('resp.data', resp.data)
      userData.expiry = resp.data.expiry
      userData.token = resp.data.token
      userData.isLogin = true
      console.log('userData', userData)
      localStorage.setItem('userData', JSON.stringify(userData))
      // Token protection has been addedlocalStorage.setItem('lastApiCall', new Date().getTime())
      // waitingForServerResponse.value = false
      router.push('/main')
    })
    .catch(err => (error.value = 'Hibás bejelentkezés, próbáld meg újra'))
}
</script>

<template>
  <div class="d-flex flex-row justify-content-between">
    <h1>Login</h1>
    <img class='d-2' alt="logo" src="../assets/flash-cards.png" />
  </div>
  <h1> </h1>

  <div class="df spinner" v-show="waitingForServerResponse">
    <font-awesome-icon icon="spinner" spin="true" />
  </div>

  <div class="card custom-gradient" v-show="!waitingForServerResponse">
    <div class="card-body">
      <div class="row">
        <div class="col-md-8 offset-md-2">
          <form class="df" v-on:submit.prevent="logIn()" >
            <div class="text-center mb-4">
              <font-awesome-icon icon="user-astronaut" class="text-white" style="font-size: 3rem;" />
            </div>

            <p class="text-white">{{ error }}</p>

            <div class="mb-3">
              <input id="form-username" type="username" class="form-control" placeholder="Username" v-model="username" />
            </div>

            <div class="mb-3">
              <input id="form-password" type="password" class="form-control" placeholder="Password" v-model="pass" />
            </div>

            <button v-if=!userData.isLogin type="submit" id="btn_login_submit"  class="btn btn-success">Belépés</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-size: 7rem;
  text-align: center;
}

h2 {
  font-size: 2rem;
  text-align: right;
  font-weight: normal;
}

img {
  width: 100px;
  height: 100px;
}

form {
  /* background-color: var(--blue); */
  border-radius: 0.5rem;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  margin-top: 2rem;
}

svg {
  font-size: 2rem;
}

input {
  background-color: #fff;
  font-size: 1.5rem;
  border: none;
  border-radius: 0.5rem;
  background-color: var(--inputBg);
  padding: 0.5rem;
}

button {
  /* background-color: var(--blue); */
  color: #fff;
  border: 1px;
  font-size: 1.5rem;
}

.spinner {
  justify-content: center;
}

.custom-gradient {
  background: linear-gradient(to bottom right, #04ff00, #0000ff);
}
</style>