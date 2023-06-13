// stores/user.js
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => {
    return {
        expiry: null,
        token: null,
        isLogin: false,
    };
  },
});
