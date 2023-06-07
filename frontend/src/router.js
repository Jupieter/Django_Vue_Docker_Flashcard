import {createRouter, createWebHistory} from 'vue-router'
import CardSet from "./components/CardSets.vue"
import CardSet from "./pages/GamesMain.vue"

const routes = [
  { path: '/', component: Welcome },
  { path: '/cardset', component: CardSet},
  { path: '/study', component: CardSet},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router