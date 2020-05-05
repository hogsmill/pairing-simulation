<template>
  <div id="app">
  <h1>Pairing Simulation</h1>
  <button @click="createBacklog" :disabled="state['running']">Create Backlog</button>
  <div class="run-type">
    Type of Run:
    <div class="radio">
      <input type="radio" id="fullRun" name="runType" value="Full Run" v-model="state['runType']">
      <label for="fullRun">Full Run</label>
    </div>
    <div class="radio">
      <input type="radio" id="stepThrough" name="runType" value="Step Through" v-model="state['runType']">
      <label for="stepThrough">Step-Through</label>
    </div>
    <button @click="start" class="start" :disabled="state['running']">Start Run</button>
    <button v-if="state['runType'] != 'Full Run'" @click="nextSprint" class="next-sprint" :disabled="state['complete'] == true || state['running']">Continue</button>
  </div>
  <div class="strategy">
      Strategies:
      <div class="radio">
        <input type="checkbox" id="noPairing" name="noPairing" value="No Pairing" v-model="state['strategies']['no-pairing']['run']">
        <label for="noPairing">No Pairing</label>
        <input type="checkbox" id="bestPair" name="bestPair" value="Best Pairing" v-model="state['strategies']['best-pair']['run']">
        <label for="bestPair">Best Pairing</label>
        <input type="checkbox" id="bestShare" name="bestShare" value="Best Share" v-model="state['strategies']['best-share']['run']">
        <label for="randomShare">Random Share</label>
        <input type="checkbox" id="randomShare" name="randomShare" value="Best Share" v-model="state['strategies']['random-share']['run']">
        <label for="randomShare">Random Share</label>
      </div>
    </div>
  <ResultsView v-bind:state="state" />
  </div>
</template>

<script>
import ResultsView from './components/ResultsView.vue'

export default {
  name: 'App',
  components: {
    ResultsView
  },
  data() {
    return {
      noOfCards: 100,
      percentages: {
        'Front End': 5,
        'Back End': 50,
        'Database': 10,
        'Devops': 15,
        'Other': 20
      },
      levels: [100, 150, 200],
      skills: {
        'Front End': ['javascript', 'css', 'react'],
        'Back End': ['java', 'apis'],
        'Database': ['sql', 'mongo'],
        'Devops': ['jenkins', 'firewalls'],
        'Other': ['SEO', 'security']
      },
      state: {
        runType: false,
        running: false,
        sprint: 0,
        strategies: {
          'no-pairing': { run: true, backlog: {'to do': [], 'doing': [], 'done': []} },
          'best-pair': { run: true, backlog: {'to do': [], 'doing': [], 'done': []} },
          'best-share': { run: true, backlog: {'to do': [], 'doing': [], 'done': []} },
          'random-share': { run: true, backlog: {'to do': [], 'doing': [], 'done': []} }
        }
      }
    }
  },
  methods: {
    getRandomIndex(n) {
      return Math.floor(Math.random() * Math.floor(n))
    },
    calculateNumberOfCards() {
      var cards = {}
      for (var key in this.percentages) {
        cards[key] = parseInt(this.noOfCards * this.percentages[key] / 100)
      }
      return cards
    },
    generateCard(area, i, id) {
      var skill = this.getRandomIndex(this.skills[area].length - 1)
      var level = this.getRandomIndex(this.levels.length - 1)
      return {
        'id': id,
        'name': "Card " + i,
        'needed': this.skills[area][skill],
        'amount': this.levels[level],

        // TODO: Remove these - they are added by prepare_card
        'assigned': [],
        'remaining': this.levels[level],
        'completed': 0
      }
    },
    createBacklog() {
      var noOfCards = this.calculateNumberOfCards()
      var cards = []
      var id = 1
      for (var skill in this.skills) {
        var i = 1
        while (i <= noOfCards[skill]) {
          cards.push(this.generateCard(skill, i, id))
          i = i + 1
          id = id + 1
        }
      }
      for (var strategy in this.state['strategies']) {
        for (i = 0; i < cards.length; i++) {
        this.state['strategies'][strategy]['backlog']['to do'].push(cards[i])
        }
      }
    },
    nextSprint() {
      for (var strategy in this.state['strategies']) {
        this.state['strategies'][strategy]['backlog']['doing'].push(this.state['strategies'][strategy]['backlog']['to do'][0])
        this.state['strategies'][strategy]['backlog']['to do'].shift()
        if (this.state['strategies'][strategy]['backlog']['doing'].length > 2) {
          console.log('here')
          this.state['strategies'][strategy]['backlog']['done'].push(this.state['strategies'][strategy]['backlog']['doing'][0])
          this.state['strategies'][strategy]['backlog']['doing'].shift()
        }
      }
      this.state['sprint'] = this.state['sprint'] + 1
      if (this.state['runType'] == "Full Run" && this.state['sprint'] < 20) {
        setTimeout(this.nextSprint, 500);
      } else {
        this.state['running'] = false
      }
    },
    start() {
      this.nextSprint()
    }
  }
}
</script>
