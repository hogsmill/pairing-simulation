<template>
  <div id="app">
    <appHeader></appHeader>

    <div v-if="showAbout">
      <AboutView />
    </div>

    <div class="container" v-if="!showAbout">
      <h1>Pairing Simulation</h1>
      <div class="card-deck">
        <TeamAndBacklogView />
        <RunView />
        <StrategiesView />
      </div>
    </div>
    <ResultsView v-bind:state="gameState" />

  </div>
</template>

<script>
import io from "socket.io-client";

import Header from "./components/Header.vue";

import AboutView from './components/about/AboutView.vue'

import TeamAndBacklogView from './components/control/TeamAndBacklogView.vue'
import RunView from './components/control/RunView.vue'
import StrategiesView from './components/control/StrategiesView.vue'

import ResultsView from './components/results/ResultsView.vue'

export default {
  name: 'App',
  components: {
    appHeader: Header,
    AboutView,
    TeamAndBacklogView,
    RunView,
    StrategiesView,
    ResultsView
  },
  data() {
    return {}
  },
  methods: {
    updateShowAbout(state) {
      this.$store.dispatch("updateShowAbout", state)
    }
  },
  computed: {
    isHost() {
      return this.$store.getters.getHost;
    },
    showAbout() {
      return this.$store.getters.getShowAbout;
    },
    setUpState() {
      return this.$store.getters.getSetUpState;
    },
    gameState() {
      return this.$store.getters.getGameState;
    },
    sprint() {
      return this.$store.getters.getSprint;
    }
  },
  created() {
    var host = "77.68.122.69"
      if (location.hostname == 'localhost') {
        host = 'localhost'
      }
      var connStr = "http://" + host + ":3002"
      console.log("Connecting to: " + connStr)
      this.socket = io(connStr)
  },
  mounted() {
    if (location.search == "?host") {
      this.$store.dispatch("updateHost", true)
    }
  }
}
</script>
