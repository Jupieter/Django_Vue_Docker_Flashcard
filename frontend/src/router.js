import {createRouter, createWebHistory} from 'vue-router'
import CardSet from "./components/CardSets.vue"
import GamesMain from "./pages/GamesMain.vue"

const routes = [
  // { path: '/', component: Welcome, name: 'Welcome' },
  { path: '/cardset', component: CardSet, name:'CardSet'},
  { path: '/study', component: GamesMain},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router