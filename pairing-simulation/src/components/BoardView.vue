<template>
  <div v-if="state['strategies'][name]['run']" class="aboard">
    <h3>{{name}}</h3>
    <div v-for="(queue, label) in state['strategies'][name]['backlog']" :key="label" class="queue">
      <h4>{{label}}</h4>
      <div v-for="card in queue" :key="card['id']">
        <CardView  v-bind:card="card" />
      </div>
    </div>
  </div>
</template>

<script>
import CardView from './CardView.vue'

export default {
  name: 'Board',
  components: {
    CardView
  },
  props: [
    'state',
    'board',
    'name'
  ],
}
</script>

<style>
  .board { display: inline-block; width: 24%; margin: 2px; }
  .aboard { border: 1px solid; }
  .queue { display: inline-block; width: 31%; margin: 2px; vertical-align: top; }
  .card { border: 1px solid; margin: 0 0 2px 0; text-align: left; font-size: 60%; }
</style>
