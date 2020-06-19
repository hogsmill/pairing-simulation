<template>
  <div class="graph">
    <div class="label">{{gameState.strategies[name].name}}</div>
    <div class="graph-container">
      <div class="status" :style="{ width: setStatusWidth(backlog) }">
      <span v-if="backlog['backlog']['done'].length == gameState['noOfCards']">({{backlog['sprints']}} Sprints)</span>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'Graph',
  props: [
    'name',
    'backlog'
  ],
  methods: {
    setStatusWidth(backlog) {
      return parseInt(backlog.backlog.done.length / this.gameState.noOfCards * 100) + '%'
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
  .graph { vertical-align: top; height: 24px; }
  .graph .label { display: inline-block; width: 13%; text-align: right; padding-right: 2px; height: 20px; vertical-align: top; }
  .graph .graph-container { display: inline-block; width: 80%; border: 1px solid; height: 20px;  }
  .graph .status { height: 20px; background-color: green; color: white;  width: 0px }
</style>
