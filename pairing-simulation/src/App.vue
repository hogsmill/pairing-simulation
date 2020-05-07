<template>
  <div id="app">
    <div class="menu">
      <span @click="function() { showAbout = false}" :class="{ selected: !showAbout }">Simulation</span>
      <span @click="function() { showAbout = true}" :class="{ selected: showAbout }">About</span>
    </div>
    <div v-if="showAbout">
      <AboutView />
    </div>
    <div v-if="!showAbout">
      <h1>Pairing Simulation</h1>
      <div class="setup">
        <h2>Set Up</h2>
        <button @click="setUp" :disabled="state['running']">Create Team and Backlog</button>
        <div v-if="state.backlogCreated">
          <div class="member" v-for="member in state['team']" :key="member['name']">
            <div class="name">{{member['name']}}</div>
            <div class="skills">
              <span v-for="skill in member['skills']" :key="skill['name']" class="skill">
                [{{skill['name']}}: {{skill['level']}}]
              </span>
            </div>
          </div>
        </div>
      </div>
      <div class="run-type">
        <h2>Run Type</h2>
        <div class="radio">
          <input type="radio" id="fullRun" name="runType" value="Full Run" v-model="state['runType']">
          <label for="fullRun">Full Run</label>
        </div>
        <div class="radio">
          <input type="radio" id="stepThrough" name="runType" value="Step Through" v-model="state['runType']">
          <label for="stepThrough">Step-Through</label>
        </div>
        <button @click="nextSprint()" class="start" :disabled="state['running'] || ! state['backlogCreated']">Go</button>
      </div>
      <div class="strategies">
        <h2>Strategies</h2>
        <div class="radio">
          <input type="checkbox" id="noPairing" name="noPairing" value="No Pairing" v-model="state['strategies']['no-pairing']['run']">
          <label for="noPairing">No Pairing</label>
        </div>
        <div class="radio">
          <input type="checkbox" id="bestPair" name="bestPair" value="Best Pairing" v-model="state['strategies']['best-pair']['run']">
          <label for="bestPair">Best Pairing</label>
        </div>
        <div class="radio">
          <input type="checkbox" id="bestShare" name="bestShare" value="Best Share" v-model="state['strategies']['best-share']['run']">
          <label for="randomShare">Best Share</label>
        </div>
        <div class="radio">
          <input type="checkbox" id="randomShare" name="randomShare" value="Best Share" v-model="state['strategies']['random-share']['run']">
          <label for="randomShare">Random Share</label>
        </div>
      </div>
      <ResultsView v-bind:state="state" />
    </div>
  </div>
</template>

<script>
import ResultsView from './components/ResultsView.vue'
import AboutView from './components/AboutView.vue'

export default {
  name: 'App',
  components: {
    ResultsView,
    AboutView
  },
  data() {
    return {
      showAbout: false,
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
      roleSkills: {
        'front end': [{'name': 'javascript', 'level': 30}, {'name': 'css', 'level': 30}],
        'back end': [{'name': 'java', 'level': 30}],
        'devops': [{'name': 'jenkins', 'level': 30}],
        'dba': [{'name': 'sql', 'level': 30}, {'name': 'mongo', 'level': 30}]
      },
      state: {
        backlogCreated: false,
        runType: false,
        running: false,
        sprint: 0,
        team: [
          { 'name': 'FE 1', 'skills': 'front end' },
          { 'name': 'FE 2', 'skills': 'front end' },
          { 'name': 'BE 1', 'skills': 'back end' },
          { 'name': 'BE 2', 'skills': 'back end' },
          { 'name': 'DEVOPS', 'skills': 'devops' },
          { 'name': 'DBA', 'skills': 'dba' }
        ],
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
    getRoleSkills(skill) {
      return this.roleSkills[skill]
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
    setUp() {

      // Create team

      for (var i = 0; i < this.state['team'].length; i++) {
        this.state['team'][i]['skills'] = this.roleSkills[this.state['team'][i]['skills']]
      }

      console.log(this.state)

      // Create backlog

      var noOfCards = this.calculateNumberOfCards()
      var cards = []
      var id = 1
      for (var skill in this.skills) {
        i = 1
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
      this.state.backlogCreated = true
    },
    nextSprint() {
      for (var strategy in this.state['strategies']) {
        this.assignCards(strategy)
        this.playCards(strategy)
      }
      this.state['sprint'] = this.state['sprint'] + 1
      if (this.state['runType'] == "Full Run" && this.state['sprint'] < 20) {
        setTimeout(this.nextSprint, 300);
      } else {
        this.state['running'] = false
      }
    }
  }
}
</script>

<style>
  .menu { text-align: right; background-color: #ccc; padding: 6px; }
  .menu span { margin: 0 4px 0 4px; }
  .menu span:hover { text-decoration: underline; }
  .selected { text-decoration: underline; font-weight: bold; }

  .setup{ width: 40%; display: inline-block; vertical-align: top; }
  .member { border: 1px solid;  vertical-align: top; }
  .member .name { width: 20%; display: inline-block; vertical-align: top; }
  .member .skills { width: 70%; display: inline-block; vertical-align: top; text-align: left; }

  .run-type { width: 15%; display: inline-block; vertical-align: top; }
  .run-type div { text-align: left; }

  .strategies { width: 20%; display: inline-block; vertical-align: top; }
  .strategies div { text-align: left; }
</style>
