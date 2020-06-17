<template>
  <div v-if="state['strategies'][name]['run']" class="aboard">
    <h3>{{state['strategies'][name]['name']}}</h3>
    <div class="skills">
      <div v-for="(member, index) in getTeam(name)" :key="index">{{member}}</div>
    </div>
    <div class="unassigned">Unassigned: {{getUnassigned(state['strategies'][name]['team'])}}</div>
    <div v-for="(queue, label) in state['strategies'][name]['backlog']" :key="label" class="queue">
      <h4>{{label}} ({{queue.length}})</h4>
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
  methods: {
    getUnassigned(team) {
      if (team) {
        var members = []
        for (var i = 0; i < team.length; i++) {
          members.push(team[i]['name'])
        }
        return members.join(', ')
      }
    },
    getTeam(strategy) {
      var team = []
      var i, j
      if (this.state['strategies'][strategy]['team']) {
        for (i = 0; i < this.state['strategies'][strategy]['team'].length; i++) {
          team.push(this.state['strategies'][strategy]['team'][i])
        }
      }
      if (this.state['strategies'][strategy]['backlog']) {
        for (i = 0; i < this.state['strategies'][strategy]['backlog']['doing'].length; i++) {
          var assigned = this.state['strategies'][strategy]['backlog']['doing'][i]['assigned']
          for (j = 0; j < assigned.length; j++) {
            team.push(assigned[j])
          }
        }
      }
      team = team.sort(
        function(a, b) {
        if (a['name'] < b['name']) { return -1 }
        if (a['name'] > b['name']) { return  1 }
        return 0
      })
      var teamVals = []
      for (i = 0; i < team.length; i++) {
        var skills = []
        for (j = 0; j < team[i]['skills'].length; j++) {
          var skill = team[i]['skills'][j]
          skills.push(skill['name'] + ':' + skill['level'])
        }
        teamVals.push(team[i]['name'] + ': ' + skills.join(', '))
      }
      return teamVals
    }
  }
}
</script>

<style>
  .aboard { border: 1px solid; }
  .aboard h3 { text-align: center; }
  .skills, .unassigned { text-align: left; margin: 0 6px 6px 6px; font-size: smaller; }
  .queue { display: inline-block; width: 31%; margin: 2px; vertical-align: top; }
  .card { border: 1px solid; margin: 0 0 2px 0; text-align: left; font-size: 60%; }
</style>
