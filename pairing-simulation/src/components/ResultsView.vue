<template>
  <div class="results">
    <h2>Results  <span v-if="state['sprint'] > 0">(Sprint {{state['sprint']}})</span></h2>
    <div class="graph">
      <div v-for="(backlog, name) in state['strategies']" :key="name" class="graph">
        <div class="label">{{state['strategies'][name]['name']}}</div>
        <div class="container">
          <div class="status" :style="{ width: setStatusWidth(backlog) }">
            {{backlog['backlog']['done'].length}}
            <span v-if="backlog['backlog']['done'].length == state['noOfCards']">({{backlog['sprints']}} Sprints)</span>
          </div>
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
    setStatusWidth(backlog) {
      return parseInt(backlog['backlog']['done'].length / this.state.noOfCards * 100) + '%'
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
  .graph { vertical-align: top; }
  .graph .label { display: inline-block; width: 13%; text-align: right; padding-right: 2px; height: 20px; vertical-align: top; }
  .graph .container { display: inline-block; width: 80%; border: 1px solid; height: 20px;  }
  .graph .status { height: 20px; background-color: green; color: white; border: 1px solid; }

  .board { display: inline-block; width: 24%; margin: 2px; vertical-align: top; }
</style>
