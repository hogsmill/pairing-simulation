<template>
  <div class="card">
    Id: {{card['id']}}<br />
    <div class="progress-container">
      <div class="progress" :style="{ width: setWidth(card) }"></div>
    </div>
    Needed: {{card['needed']}}<br />
    Amount: {{card['amount']}}<br />
    Left: {{card['remaining']}}<br />
    Assigned: {{getAssigned(card)}}
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: ['card'],
  methods: {
    setWidth(card) {
      return 100 * card['completed'] / card['amount'] + '%'
    },
    getAssigned(card) {
      var assigned = []
      for (var i = 0; i < card['assigned'].length; i++) {
        assigned.push(card['assigned'][i]['name'])
      }
      return assigned.join(', ')
    }
  }
}
</script>

<style>
.progress-container { margin: 1px; height: 6px; background-color: #bbb; }
.progress { width: 50%; background-color: green; height: 6px; }
</style>
