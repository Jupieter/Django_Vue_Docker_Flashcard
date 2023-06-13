<script setup>
import router from '../router'


const loginData = JSON.parse(localStorage.getItem('userData')) || { expiry: null, token: null, isLogin: false }
console.log('AppVue 10 minute:  ', new Date().getTime("0000-01-01T00:00:57.0Z"))
console.log('AppVue loginData:  ', loginData)
const isLastApiCallRecent =
    new Date(loginData.expiry).getTime() - new Date().getTime()
console.log('AppVue Date:  ', isLastApiCallRecent)
if (isLastApiCallRecent < 35977237) {
    console.log('AppVue False:  ', isLastApiCallRecent)
    // isLogin = false;
    router.push('/login')
}
else {
    // isLogin = true;
    console.log('AppVue True:  ')
    // router.push('/')
};
</script>

<template>
    <div>
        <h1>MAIN</h1>
    </div>
</template>


<style lang="scss" scoped>
</style>