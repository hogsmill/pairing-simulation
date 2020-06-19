'use strict';


var getRandomIndex = function(n) {
  return Math.floor(Math.random() * Math.floor(n))
}

var calculateNumberOfCards = function(noOfCards, percentages) {
  var cards = {}
  for (var key in percentages) {
    cards[key] = parseInt(noOfCards * percentages[key] / 100)
  }
  return cards
}

var generateCard = function(area, skills, levels, i, id) {
  var skill = getRandomIndex(skills[area].length - 1)
  var level = getRandomIndex(levels.length - 1)
  return {
    'id': id,
    'name': "Card " + i,
    'needed': skills[area][skill],
    'amount': levels[level],

    // TODO: Remove these - they are added by prepare_card
    'assigned': [],
    'remaining': levels[level],
    'completed': 0
  }
}

var SetUp = {

  setup: function(setUpState, gameState) {
    this.setUpState = setUpState
    this.gameState = gameState
    this.createTeam()
    this.createBacklog()
    this.gameState.backlogCreated = true
    this.gameState['sprint'] = 0

    console.log(this.gameState)
    return this.gameState
  },

  createTeam: function() {
    var roleSkills = this.setUpState.roleSkills
    for (var i = 0; i < this.gameState['team'].length; i++) {
      var team = this.gameState['team'][i]
      team['skills'] = roleSkills[team['skills']]
    }
  },

  createBacklog: function() {
    var i, total = 0
    var cards = []
    var id = 1
    var noOfCards = calculateNumberOfCards(this.setUpState.noOfCards, this.setUpState.percentages)
    var skills = this.setUpState.skills
    for (var skill in skills) {
      i = 1
      while (i <= noOfCards[skill]) {
        cards.push(generateCard(skill, skills, this.setUpState.levels, i, id))
        i = i + 1
        id = id + 1
        total = total + 1
      }
    }
    this.gameState.noOfCards = total
    for (var strategy in this.gameState['strategies']) {
      this.gameState['strategies'][strategy]['backlog']['to do'] = JSON.parse(JSON.stringify(cards))
      this.gameState['strategies'][strategy]['team'] = JSON.parse(JSON.stringify(this.gameState['team']))
      this.gameState['strategies'][strategy]['noOfCards'] = total
    }
  }
}

export default SetUp
