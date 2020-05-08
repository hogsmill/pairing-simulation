<template>
  <div class="results">
    <h2>Results</h2>
    <div class="sprint">Sprint {{state['sprint']}}</div>
    <div class="graph">
      <div v-for="(backlog, name) in state['strategies']" :key="name" class="graph">
        <div class="label">{{name}}</div>
        <div class="container">
          <div class="status" :style="{ width: backlog['backlog']['done'].length + '%' }"></div>
        </div>
      </div>
    </div>
    <div v-for="(backlog, name) in state['strategies']" :key="name" class="board" :style="{ visibility: visible(name), width: setWidth() }">
      <BoardView v-bind:state="state" v-bind:backlog="backlog" v-bind:name="name" />
    </div>
  </div>
</template>

<script>
import BoardView from './BoardView.vue'

export default {
  name: 'Results',
  components: {
    BoardView
  },
  props: ['state'],
  methods: {
    visible(strategy) {
      if (this.state['strategies'][strategy]['run']) {
        return 'visible'
      } else {
        return 'hidden'
      }
    },
    setWidth() {
      var i = 0
      for (var strategy in this.state['strategies']) {
        if (this.state['strategies'][strategy]['run']) {
          i++
        }
      }
      return 90 / i + '%'
    }
  }
}
</script>

<style>
  .sprint { text-align: right; }
  .graph .label { display: inline-block; width: 13%; text-align: right; padding-right: 2px; }
  .graph .container { display: inline-block; width: 80%; border: 1px solid; height: 20px; }
  .graph .status { height: 100%; background-color: green; }

  .board { display: inline-block; width: 24%; margin: 2px; }
</style>
