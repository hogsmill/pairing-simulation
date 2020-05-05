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
      <h3>{{name}}</h3>
      <div v-for="(queue, label) in state['strategies'][name]['backlog']" :key="label" class="queue">
        <h4>{{label}}</h4>
        <div v-for="card in queue" :key="card['id']" class="card">
          Id: {{card['id']}}<br />
          Needed: {{card['needed']}}<br />
          Amount: {{card['amount']}}<br />
          Left: {{card['remaining']}}<br />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Results',
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
  .board { display: inline-block; width: 24%; border: 1px solid; margin: 2px; }
  .queue { display: inline-block; width: 31%; margin: 2px; vertical-align: top; }
  .card { border: 1px solid; margin: 0 0 2px 0; text-align: left; font-size: 60%; }
</style>
