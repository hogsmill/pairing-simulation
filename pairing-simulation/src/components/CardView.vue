<template>
  <div class="card">
    Id: {{card['id']}}<br />
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
}
</script>
