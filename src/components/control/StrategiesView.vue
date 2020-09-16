<template>
  <div class="card bg-light mb-3 col-md-3 no-padding-r-l strategies" v-if="!gameState.running">
    <div class="card-body">
      <h3 class="card-title">
        Strategies
      </h3>
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
</template>

<script>
export default {
  computed: {
    gameState() {
      return this.$store.getters.getGameState
    }
  },
  methods: {
  }
}
</script>

<style>
  .strategies { width: 20%; display: inline-block; vertical-align: top; }
  .strategies div { text-align: left; }
</style>
