<script setup>
const loginData = JSON.parse(localStorage.getItem('userData')) || { expiry: null, token: null, isLogin: false }
console.log('loginData.isLogin:  ', loginData.isLogin)



</script>

<template>
    <div >
        <h1 v-show="!loginData.isLogin">Study False</h1>
        <h1 v-show="loginData.isLogin">Study True</h1>
    </div>
</template>


<style lang="scss" scoped></style>