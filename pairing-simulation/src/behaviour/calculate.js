
var cardIsComplete = function(card) {
  return card['remaining'] <= 0
}

var calculateKnowledgeShare = function(card) {
  console.log(card)
  return true
}

var completeWorkOnCard = function(card, skillLevel, maxWorkPerCycle) {
  var amount = Math.min(skillLevel, maxWorkPerCycle)
  card['completed'] = card['completed'] + amount
  card['remaining'] = card['remaining'] - amount
  if (card['completed'] > card['needed']) {
    card['completed'] = card['needed']
    card['remaining'] = 0
  }
}

var calculateWorkDoneOnCard = function(card, board, state) {
  console.log('  calculating', card)
  var i, j
  for (i = 0; i < card['assigned'].length; i++) {
    for (j = 0; j < card['assigned'][i]['skills'].length; j++) {
      var skill = card['assigned'][i]['skills'][j]
      if (skill['name'] == card['needed']) {
        completeWorkOnCard(card, skill['level'], state.maxWorkPerCycle)
      }
      calculateKnowledgeShare(card)
      if (cardIsComplete(card)) {
        moveCard(board, card, 'doing', 'done')
        unassignMembersFromCard(board, card)
      }
    }
  }
}

var unassignMembersFromCard = function(board, card) {
  for (var i = 0; i < card['assigned'].length; i++) {
    board['team'].push(card['assigned'][i])
  }
  card['assigned'] = []
}

var moveCard = function(board, card, fromQueue, toQueue) {
  board['backlog'][toQueue].push(card)
  var index = -1
  for (var i = 0; i < board['backlog'][fromQueue].length; i++) {
    if (board['backlog'][fromQueue][i]['id'] == card['id']) {
      index = i
    }
  }
  if (index >= 0) {
    board['backlog'][fromQueue].splice(index, 1)
  }
}

var Calculate = {

  calculateWorkDoneOnCards: function(state, strategy) {
    console.log('calculating', strategy)
    var board = state['strategies'][strategy]
    for (var i = 0; i < board['backlog']['doing'].length; i++) {
      console.log(board['backlog']['doing'][i])
      calculateWorkDoneOnCard(board['backlog']['doing'][i], board, state)
    }
  }

}

export default Calculate
