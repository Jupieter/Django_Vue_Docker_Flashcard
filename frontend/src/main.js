import { createApp } from 'vue'
import App from './App.vue'


// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/js/bootstrap.js'
import bootstrap from 'bootstrap'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { library } from "@fortawesome/fontawesome-svg-core";
import { far } from '@fortawesome/free-regular-svg-icons';

library.add(far)

createApp(App)
.use(bootstrap)
.component('fa', FontAwesomeIcon)
.mount('#app')