import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    showAbout: false,
    host: false,
    setUpState: {
      noOfCards: 100,
      percentages: {
        'Front End': 20,
        'Back End': 30,
        'Database': 10,
        'Devops': 15,
        'Other': 20
      },
      levels: [100, 150, 200],
      skills: {
        'Front End': ['JS', 'css', 'react'],
        'Back End': ['java', 'apis'],
        'Database': ['sql', 'mongo'],
        'Devops': ['jenkins', 'firewalls', 'azure'],
        'Other': ['SEO', 'security']
      },
      roleSkills: {
        'front end': [{'name': 'JS', 'level': 50}, {'name': 'css', 'level': 50}],
        'back end': [{'name': 'java', 'level': 50}],
        'devops': [{'name': 'jenkins', 'level': 50}],
        'dba': [{'name': 'sql', 'level': 50}, {'name': 'mongo', 'level': 50}]
      }
    },
    gameState: {
      backlogCreated: false,
      runType: false,
      running: false,
      noOfCards: 0,
      sprint: 0,
      team: [
        { 'name': 'FE 1', 'skills': 'front end' },
        { 'name': 'FE 2', 'skills': 'front end' },
        { 'name': 'BE 1', 'skills': 'back end' },
        { 'name': 'BE 2', 'skills': 'back end' },
        { 'name': 'DEVOPS', 'skills': 'devops' },
        { 'name': 'DBA', 'skills': 'dba' }
      ],
      strategies: {
        'no-pairing': { name: 'No Pairing', run: true, backlog: {'to do': [], 'doing': [], 'done': []} },
        'best-pair': { name: 'Best Pair', run: true, backlog: {'to do': [], 'doing': [], 'done': []} },
        'best-share': { name: 'Best Share', run: true, backlog: {'to do': [], 'doing': [], 'done': []} },
        'random-share': { name: 'Random Share', run: false, backlog: {'to do': [], 'doing': [], 'done': []} }
      },
      maxWorkPerCycle: 20,
      defaultLevel: 1,
      expertLevel: 100,
      expertLevelPercentage: 20
    }
  },
  getters: {
    getShowAbout: (state) => {
      return state.showAbout
    },
    getHost: (state) => {
      return state.host
    },
    getSetUpState: (state) => {
      return state.setUpState
    },
    getGameState: (state) => {
      return state.gameState
    },
    getRunning: (state) => {
      return state.gameState.running
    },
    getSprint: (state) => {
      return state.gameState.sprint
    },
  },
  mutations: {
    updateShowAbout: (state, payload) => {
      state.showAbout = payload
    },
    updateHost: (state, payload) => {
      state.host = payload
    },
    updateGameState: (state, payload) => {
      state.gameState = payload
    },
    updateRunning: (state, payload) => {
      state.gameState.running = payload
    },
    updateSprint: (state, payload) => {
      state.gameState.sprint = payload
    }
  },
  actions: {
    updateShowAbout: ({ commit }, payload) => {
      commit('updateShowAbout', payload)
    },
    updateHost: ({ commit }, payload) => {
      commit('updateHost', payload)
    },
    updateGameState: ({ commit }, payload) => {
      commit('updateGameState', payload)
    },
    updateRunning: ({ commit }, payload) => {
      commit('updateRunning', payload)
    },
    updateSprint: ({ commit }, payload) => {
      commit('updateSprint', payload)
    }
  }
})
