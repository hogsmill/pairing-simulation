<template>
  <div class="results">
    <h2>Results  <span v-if="gameState.sprint > 0">(Sprint {{ gameState.sprint }})</span></h2>
    <div v-for="(backlog, name) in gameState['strategies']" :key="'graph-' + name" :class="{ hidden: !visible(name) }">
      <GraphView :name="name" :backlog="backlog" />
    </div>
    <div v-for="(backlog, name) in gameState.strategies" :key="'board-' + name" class="board"
         :class="{ hidden: !visible(name) }" :style="{ width: setWidth() }"
    >
      <BoardView :board="backlog" :name="name" />
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
  computed: {
    gameState() {
      return this.$store.getters.getGameState
    }
  },
  methods: {
    visible(strategy) {
      return this.gameState.strategies[strategy].run
    },
    setWidth() {
      let i = 0
      for (const strategy in this.gameState['strategies']) {
        if (this.gameState['strategies'][strategy]['run']) {
          i++
        }
      }
      return 90 / i + '%'
    }
  }
}
</script>
