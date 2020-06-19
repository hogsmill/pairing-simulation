<template>
  <div class="results">
    <h2>Results  <span v-if="gameState.sprint > 0">(Sprint {{gameState.sprint}})</span></h2>
    <div v-for="(backlog, name) in gameState['strategies']" :key="'graph-' + name" :class="{ hidden: !visible(name) }">
      <GraphView v-bind:name="name" v-bind:backlog="backlog" />
    </div>
    <div v-for="(backlog, name) in gameState.strategies" :key="'board-' + name" class="board"
      :class="{ hidden: !visible(name) }" :style="{ width: setWidth() }">
      <BoardView v-bind:board="backlog" v-bind:name="name" />
    </div>
  </div>
</template>

<script>
import BoardView from './BoardView.vue'
import GraphView from './GraphView.vue'

export default {
  name: 'Results',
  components: {
    GraphView,
    BoardView
  },
  methods: {
    visible(strategy) {
      return this.gameState.strategies[strategy].run
    },
    setWidth() {
      var i = 0
      for (var strategy in this.gameState['strategies']) {
        if (this.gameState['strategies'][strategy]['run']) {
          i++
        }
      }
      return 90 / i + '%'
    }
  },
  computed: {
    gameState() {
      return this.$store.getters.getGameState;
    }
  }
}
</script>
