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

  createTeam: function(state, roleSkills) {
    for (var i = 0; i < state['team'].length; i++) {
      state['team'][i]['skills'] = roleSkills[state['team'][i]['skills']]
    }
    return state
  },

  createBacklog: function(state, skills, levels, numberOfCards, percentages) {
    var i, total = 0
    var cards = []
    var id = 1
    var noOfCards = calculateNumberOfCards(numberOfCards, percentages)
    for (var skill in skills) {
      i = 1
      while (i <= noOfCards[skill]) {
        cards.push(generateCard(skill, skills, levels, i, id))
        i = i + 1
        id = id + 1
        total = total + 1
      }
    }
    state['noOfCards'] = total
    for (var strategy in state['strategies']) {
      //for (i = 0; i < cards.length; i++) {
      //  state['strategies'][strategy]['backlog']['to do'].push(cards[i])
      //}
      state['strategies'][strategy]['backlog']['to do'] = JSON.parse(JSON.stringify(cards))
      state['strategies'][strategy]['team'] = JSON.parse(JSON.stringify(state['team']))
      state['strategies'][strategy]['noOfCards'] = numberOfCards
    }
  }
}

export default SetUp
