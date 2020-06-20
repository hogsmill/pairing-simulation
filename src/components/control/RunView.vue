<template>
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
</template>

<script>
import assign from '../../behaviour/assign.js'
import calculate from '../../behaviour/calculate.js'
import knowledge from '../../behaviour/knowledge.js'

export default {
  methods: {
    setRunning(state) {
      this.$store.dispatch("updateRunning", state)
    },
    incrementSprint() {
      this.$store.dispatch("updateSprint", this.sprint + 1)
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
    gameState() {
      return this.$store.getters.getGameState;
    }
  }
}
</script>

<style>
  .run-type { width: 15%; display: inline-block; vertical-align: top; }
  .run-type div { text-align: left; }
</style>
