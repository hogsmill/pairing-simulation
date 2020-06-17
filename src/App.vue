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
      <div class="setup" v-if="!state['running']">
        <h2>Set Up</h2>
        <div class="radio no-of-cards">
          <label for="noOfCardws">No. Of Cards </label>
          <input type="text" id="noOfCards" name="noOfCards" v-model="state.noOfCards">
        </div>
        <button @click="setUp" :disabled="state['running']">Create Team and Backlog</button>
        <div v-if="state.backlogCreated">
          <div class="member" v-for="member in state['team']" :key="member['name']">
            <div class="name">{{member['name']}}: </div>
            <div class="skills">
              <span v-for="skill in member['skills']" :key="skill['name']" class="skill">
                [{{skill['name']}}: {{skill['level']}}]
              </span>
            </div>
          </div>
        </div>
      </div>
      <div class="run-type" v-if="!state['running']">
        <h2>Run Type</h2>
        <div class="radio">
          <input type="radio" id="fullRun" name="runType" v-model="state['runType']" v-bind:value="'Full Run'">
          <label for="fullRun">Full Run</label>
        </div>
        <div class="radio">
          <input type="radio" id="stepThrough" name="runType" v-model="state['runType']" v-bind:value="'Step Through'">
          <label for="stepThrough">Step-Through</label>
        </div>
        <button @click="run()" class="start" :disabled="state['running'] || ! state['backlogCreated']">Go</button>
      </div>
      <div class="strategies" v-if="!state['running']">
        <h2>Strategies</h2>
        <div class="radio">
          <input type="checkbox" id="noPairing" name="noPairing" v-model="state['strategies']['no-pairing']['run']">
          <label for="noPairing">No Pairing</label>
        </div>
        <div class="radio">
          <input type="checkbox" id="bestPair" name="bestPair" v-model="state['strategies']['best-pair']['run']">
          <label for="bestPair">Best Pairing</label>
        </div>
        <div class="radio">
          <input type="checkbox" id="bestShare" name="bestShare" v-model="state['strategies']['best-share']['run']">
          <label for="randomShare">Best Share</label>
        </div>
        <div class="radio">
          <input type="checkbox" id="randomShare" name="randomShare" v-model="state['strategies']['random-share']['run']">
          <label for="randomShare">Random Share</label>
        </div>
      </div>
      <ResultsView v-bind:state="state" />
    </div>
  </div>
</template>

<script>
import setup from './behaviour/setup.js'
import assign from './behaviour/assign.js'
import calculate from './behaviour/calculate.js'
import knowledge from './behaviour/knowledge.js'
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
      percentages: {
        'Front End': 20,
        'Back End': 30,
        'Database': 10,
        'Devops': 15,
        'Other': 20
      },
      levels: [100, 150, 200],
      skills: {
        'Front End': ['JS', 'css', 'react'],
        'Back End': ['java', 'apis'],
        'Database': ['sql', 'mongo'],
        'Devops': ['jenkins', 'firewalls', 'azure'],
        'Other': ['SEO', 'security']
      },
      roleSkills: {
        'front end': [{'name': 'JS', 'level': 50}, {'name': 'css', 'level': 50}],
        'back end': [{'name': 'java', 'level': 50}],
        'devops': [{'name': 'jenkins', 'level': 50}],
        'dba': [{'name': 'sql', 'level': 50}, {'name': 'mongo', 'level': 50}]
      },
      state: {
        noOfCards: 100,
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
          'no-pairing': { name: 'No Pairing', run: true, backlog: {'to do': [], 'doing': [], 'done': []} },
          'best-pair': { name: 'Best Pair', run: true, backlog: {'to do': [], 'doing': [], 'done': []} },
          'best-share': { name: 'Best Share', run: true, backlog: {'to do': [], 'doing': [], 'done': []} },
          'random-share': { name: 'Random Share', run: false, backlog: {'to do': [], 'doing': [], 'done': []} }
        },
        maxWorkPerCycle: 20,
        defaultLevel: 1,
        expertLevel: 100,
        expertLevelPercentage: 20
      }
    }
  },
  methods: {
    setUp() {
      setup.createTeam(this.state, this.roleSkills)
      setup.createBacklog(this.state, this.skills, this.levels, this.state.noOfCards, this.percentages)
      this.state.backlogCreated = true
      this.state['sprint'] = 0
      console.log(this.state)
    },
    boardComplete(board) {
      return board['backlog']['done'].length == this.state['noOfCards']
    },
    boardsComplete() {
      var complete = true
      for (var strategy in this.state['strategies']) {
        var board = this.state['strategies'][strategy]
        if (board['run']) {
          complete = complete && this.boardComplete(board)
        }
      }
      return complete
    },
    run() {
      this.state['running'] = true
      console.log('Running', this.state['runType'])
      if (! this.boardsComplete()) {
        for (var strategy in this.state['strategies']) {
        var board = this.state['strategies'][strategy]
          if (board['run']) {
            assign.assignCards(this.state, strategy)
            calculate.calculateWorkDoneOnCards(this.state, strategy)
            knowledge.calculateKnowledgeShare(this.state, strategy)
            if (!this.boardComplete(board)) {
              board['sprints'] = this.state['sprint'] + 1
            }
          }
        }
        this.state['sprint'] = this.state['sprint'] + 1
        if (this.state['runType'] == "Full Run") {
          setTimeout(this.run, 300);
        } else {
          this.state['running'] = false
        }
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

  .setup { width: 40%; display: inline-block; vertical-align: top; padding-right:24px; }
  .setup button { margin-bottom: 12px; }
  .no-of-cards { margin-bottom: 12px; }
  .no-of-cards input { width: 30px; }
  .member { vertical-align: top; }
  .member .name { width: 20%; display: inline-block; vertical-align: top; text-align: right; padding: 2px; }
  .member .skills { width: 70%; display: inline-block; vertical-align: top; text-align: left; pDDING: 2PX;  }

  .run-type { width: 15%; display: inline-block; vertical-align: top; }
  .run-type div { text-align: left; }

  .strategies { width: 20%; display: inline-block; vertical-align: top; }
  .strategies div { text-align: left; }
</style>
