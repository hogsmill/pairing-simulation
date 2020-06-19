import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    showAbout: false,
    host: false
  },
  getters: {
    getShowAbout: (state) => {
      return state.showAbout;
    },
    getHost: (state) => {
      return state.host;
    }
  },
  mutations: {
    updateShowAbout: (state, payload) => {
      state.showAbout = payload;
    },
    updateHost: (state, payload) => {
      state.host = payload;
    }
  },
  actions: {
    updateShowAbout: ({ commit }, payload) => {
      commit("updateShowAbout", payload);
    },
    updateHost: ({ commit }, payload) => {
      commit("updateHost", payload);
    }
  }
});
