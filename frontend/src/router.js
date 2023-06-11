import {createRouter, createWebHistory} from 'vue-router'
import CardSet from "./pages/CardSets.vue"
import GamesMain from "./pages/GamesMain.vue"
import WelcomeMain from "./pages/WelcomeMain.vue"

const routes = [
  { path: '/', component: WelcomeMain, name: 'WelcomeMain' },
  { path: '/cardset', component: CardSet, name:'CardSet'},
  { path: '/study', component: GamesMain},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router