<template>
  <div class="card">
    Id: {{card['id']}}<br />
    <div class="progress-container">
      <div class="progress" :style="{ width: setWidth(card) }"></div>
    </div>
    Needed: {{card['needed']}}<br />
    Amount: {{card['amount']}}<br />
    Left: {{card['remaining']}}<br />
    Assigned: {{card['assigned'].join(', ')}}
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: ['card'],
  methods: {
    setWidth(card) {
      return 100 * card['completed'] / card['amount'] + '%'
    }
  }
}
</script>

<style>
.progress-container { margin: 1px; height: 6px; background-color: #bbb; }
.progress { width: 50%; background-color: green; height: 6px; }
</style>
