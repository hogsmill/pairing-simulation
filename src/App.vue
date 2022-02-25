<template>
  <div id="app">
    <appHeader />

    <div v-if="showAbout">
      <AboutView />
    </div>

    <div class="container" v-if="!showAbout">
      <div class="card-deck">
        <TeamAndBacklogView />
        <RunView />
        <StrategiesView />
      </div>
    </div>
    <ResultsView :state="gameState" />
    <Modals />
  </div>
</template>

<script>
import io from 'socket.io-client'

import Header from './components/Header.vue'
import Modals from './components/Modals.vue'

import AboutView from './components/about/AboutView.vue'

import TeamAndBacklogView from './components/control/TeamAndBacklogView.vue'
import RunView from './components/control/RunView.vue'
import StrategiesView from './components/control/StrategiesView.vue'

import ResultsView from './components/results/ResultsView.vue'

export default {
  name: 'App',
  components: {
    appHeader: Header,
    Modals,
    AboutView,
    TeamAndBacklogView,
    RunView,
    StrategiesView,
    ResultsView
  },
  data() {
    return {}
  },
  computed: {
    isHost() {
      return this.$store.getters.getHost
    },
    showAbout() {
      return this.$store.getters.getShowAbout
    },
    setUpState() {
      return this.$store.getters.getSetUpState
    },
    gameState() {
      return this.$store.getters.getGameState
    },
    sprint() {
      return this.$store.getters.getSprint
    }
  },
  created() {
    let connStr
    if (location.hostname == 'localhost') {
      connStr = 'http://localhost:3002'
    } else {
      connStr = 'https://agilesimulations.co.uk:3002'
    }
    console.log('Connecting to: ' + connStr)
    this.socket = io(connStr)
  },
  mounted() {
    if (location.search == '?host') {
      this.$store.dispatch('updateHost', true)
    }
  },
  methods: {
  }
}
</script>
