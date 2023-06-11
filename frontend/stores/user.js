// stores/user.js
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => {
    return ({ user: {
        expiry: null,
        token: null
    } })
  },
})