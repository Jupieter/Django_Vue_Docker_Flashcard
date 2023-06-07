import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'


// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'


import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
// import { faTrashAlt } from '@fortawesome/free-regular-svg-icons';
import { faTrash, faPen, faPlus, faUserSecret } from '@fortawesome/free-solid-svg-icons'

library.add(faTrash, faPen, faPlus, faUserSecret)

createApp(App)
.use(router)
.component('font-awesome-icon', FontAwesomeIcon)
.mount('#app')