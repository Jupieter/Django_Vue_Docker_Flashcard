import {createRouter, createWebHistory} from 'vue-router'
import CardSet from "./pages/CardSets.vue"
import StudyMain from "./pages/StudyMain.vue"
import WelcomeMain from "./pages/WelcomeMain.vue"
import LogIn from "./pages/LogIn.vue"

const routes = [
  { path: '/main', component: WelcomeMain, name: 'WelcomeMain' },
  { path: '/', component: LogIn, name: 'LogIn' },
  { path: '/cardset', component: CardSet, name:'CardSet'},
  { path: '/study', component: StudyMain},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router