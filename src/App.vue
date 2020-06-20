<template>
  <div id="app">
    <appHeader></appHeader>

    <div v-if="showAbout">
      <AboutView />
    </div>

    <div class="container" v-if="!showAbout">
      <h1>Pairing Simulation</h1>
      <div class="card-deck">
        <div class="card bg-light mb-3 col-md-3 no-padding-r-l setup" v-if="!gameState.running">
          <div class="card-body">
            <h3 class="card-title">Set Up</h3>
            <div class="radio no-of-cards">
              <label for="noOfCards">No. Of Cards </label>
              <input type="text" id="noOfCards" name="noOfCards" class="form-control" v-model="setUpState.noOfCards">
            </div>
            <button @click="setUp" :disabled="gameState.running" class="btn btn-site-primary">Create Team and Backlog</button>
          </div>
        </div>
        <div class="card bg-light mb-3 col-md-3 no-padding-r-l run-type" v-if="!(gameState.running && gameState.runType == 'Full Run')">
          <div class="card-body">
            <h3 class="card-title">Run Type</h3>
            <div class="radio">
              <input type="radio" id="fullRun" name="runType" v-model="gameState.runType" v-bind:value="'Full Run'">
              <label for="fullRun">Full Run</label>
            </div>
            <div class="radio">
              <input type="radio" id="stepThrough" name="runType" v-model="gameState.runType" v-bind:value="'Step Through'">
              <label for="stepThrough">Step-Through</label>
            </div>
            <button @click="run()" class="btn btn-site-primary start" :disabled="gameState.running || ! gameState.backlogCreated">Go</button>
          </div>
        </div>
        <div class="card bg-light mb-3 col-md-3 no-padding-r-l strategies" v-if="!gameState.running">
          <div class="card-body">
            <h3 class="card-title">Strategies</h3>
            <div class="radio">
              <input type="checkbox" id="noPairing" name="noPairing" v-model="gameState.strategies['no-pairing'].run">
              <label for="noPairing">No Pairing</label>
            </div>
            <div class="radio">
              <input type="checkbox" id="bestPair" name="bestPair" v-model="gameState.strategies['best-pair'].run">
              <label for="bestPair">Best Pairing</label>
            </div>
            <div class="radio">
              <input type="checkbox" id="bestShare" name="bestShare" v-model="gameState.strategies['best-share'].run">
              <label for="randomShare">Best Share</label>
            </div>
            <div class="radio">
              <input type="checkbox" id="randomShare" name="randomShare" v-model="gameState.strategies['random-share'].run">
              <label for="randomShare">Random Share</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <ResultsView v-bind:state="gameState" />

  </div>
</template>

<script>
import io from "socket.io-client";

import setup from './behaviour/setup.js'
import assign from './behaviour/assign.js'
import calculate from './behaviour/calculate.js'
import knowledge from './behaviour/knowledge.js'

import Header from "./components/Header.vue";
import AboutView from './components/about/AboutView.vue'
import ResultsView from './components/ResultsView.vue'

export default {
  name: 'App',
  components: {
    appHeader: Header,
    AboutView,
    ResultsView
  },
  data() {
    return {}
  },
  methods: {
    updateShowAbout(state) {
      this.$store.dispatch("updateShowAbout", state)
    },
    setRunning(state) {
      this.$store.dispatch("updateRunning", state)
    },
    incrementSprint() {
      this.$store.dispatch("updateSprint", this.sprint + 1)
    },
    setUp() {
      var gameState = setup.setup(this.setUpState, this.gameState)
      this.$store.dispatch("updateGameState", gameState)
    },
    updateGameState(state) {
      this.$store.dispatch("updateGameState", state)
    },
    boardComplete(board) {
      return board.backlog.done.length == this.gameState.noOfCards
    },
    boardsComplete() {
      var complete = true
      for (var strategy in this.gameState.strategies) {
        var board = this.gameState.strategies[strategy]
        if (board.run) {
          complete = complete && this.boardComplete(board)
        }
      }
      return complete
    },
    run() {
      this.setRunning(true)
      if (! this.boardsComplete()) {
        var state = this.gameState
        for (var strategy in state.strategies) {
          var board = state.strategies[strategy]
          if (board.run) {
            state = assign.assignCards(state, strategy)
            state = calculate.calculateWorkDoneOnCards(state, strategy)
            state = knowledge.calculateKnowledgeShare(state, strategy)
            if (!this.boardComplete(board)) {
              board.sprints = this.sprint + 1
            }
          }
        }
        this.updateGameState(state)
        this.incrementSprint()
        if (this.gameState.runType == "Full Run") {
          setTimeout(this.run, 300);
        } else {
          this.setRunning(false)
        }
      }
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

<style>
  .setup { width: 40%; display: inline-block; vertical-align: top; padding-right:24px; }
  .setup button { margin-bottom: 12px; }
  .no-of-cards { margin-bottom: 12px; }
  .member { vertical-align: top; }
  .member .name { width: 20%; display: inline-block; vertical-align: top; text-align: right; padding: 2px; }
  .member .skills { width: 70%; display: inline-block; vertical-align: top; text-align: left; pDDING: 2PX;  }

  .run-type { width: 15%; display: inline-block; vertical-align: top; }
  .run-type div { text-align: left; }

  .strategies { width: 20%; display: inline-block; vertical-align: top; }
  .strategies div { text-align: left; }
</style>
