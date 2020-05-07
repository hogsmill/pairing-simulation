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
    <div v-for="(backlog, name) in state['strategies']" :key="name" class="board">
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
  }
}
</script>

<style>
  .sprint { text-align: right; }
  .graph .label { display: inline-block; width: 13%; text-align: right; padding-right: 2px; }
  .graph .container { display: inline-block; width: 80%; border: 1px solid; height: 20px; }
  .graph .status { height: 100%; background-color: green; }

  .xboard { display: inline-block; width: 24%; margin: 2px; }
  .xaboard { border: 1px solid; }
  .xqueue { display: inline-block; width: 31%; margin: 2px; vertical-align: top; }
  .xcard { border: 1px solid; margin: 0 0 2px 0; text-align: left; font-size: 60%; }
</style>
