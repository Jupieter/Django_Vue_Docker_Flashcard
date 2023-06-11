import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'


import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
// import { faTrashAlt } from '@fortawesome/free-regular-svg-icons';
import { faTrash, faPen, faPlus, faSpinner, faUserAstronaut, faUserSecret } from '@fortawesome/free-solid-svg-icons'

library.add(faTrash, faPen, faPlus, faSpinner, faUserAstronaut,faUserSecret)

createApp(App)
.use(router)
.use(createPinia())
.component('font-awesome-icon', FontAwesomeIcon)
.mount('#app')