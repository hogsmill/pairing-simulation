<template>
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
</template>

<script>
import setup from '../../behaviour/setup.js'

export default {
  methods: {
    setUp() {
      var gameState = setup.setup(this.setUpState, this.gameState)
      this.$store.dispatch("updateGameState", gameState)
    }
  },
  computed: {
    setUpState() {
      return this.$store.getters.getSetUpState;
    },
    gameState() {
      return this.$store.getters.getGameState;
    }
  }
}
</script>

<style>
  .setup { width: 40%; display: inline-block; vertical-align: top; padding-right:24px; }
  .setup button { margin-bottom: 12px; }
  .no-of-cards { margin-bottom: 12px; }
</style>
