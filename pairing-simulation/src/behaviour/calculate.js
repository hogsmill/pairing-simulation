'use strict';

var cardIsComplete = function(card) {
  return card['remaining'] <= 0
}

var completeWorkOnCard = function(card, skillLevel, maxWorkPerCycle) {
  var amount = Math.min(skillLevel, maxWorkPerCycle)
  card['completed'] = card['completed'] + amount
  card['remaining'] = card['remaining'] - amount
  if (card['completed'] > card['amount']) {
    card['completed'] = card['amount']
    card['remaining'] = 0
  }
}

var calculateWorkDoneOnCard = function(card, board, state) {
  var i, j
  for (i = 0; i < card['assigned'].length; i++) {
    var member = card['assigned'][i]
    if (member['expert'] || card['assigned'].length == 1) {
      for (j = 0; j < member['skills'].length; j++) {
        var skill = member['skills'][j]
        if (skill['name'] == card['needed']) {
          completeWorkOnCard(card, skill['level'], state.maxWorkPerCycle)
        }
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
    var i
    var board = state['strategies'][strategy]
    for (i = 0; i < board['backlog']['doing'].length; i++) {
      calculateWorkDoneOnCard(board['backlog']['doing'][i], board, state)
    }
    for (i = 0; i < board['backlog']['doing'].length; i++) {
      var card = board['backlog']['doing'][i]
      if (cardIsComplete(card)) {
        moveCard(board, card, 'doing', 'done')
        unassignMembersFromCard(board, card)
      }
    }
  }

}

export default Calculate
