// Team Stuff

var getMemberSkill = function(member, skill) {
  for (var i = 0; i < member['skills'].length; i++) {
    if (member['skills'][i]['name'] == skill) {
      return member['skills'][i]
    }
  }
}

//var getMemberNotSkill = function(member, skill) {
//  for (var i = 0; i < member['skills'].length; i++) {
//    if (member['skills'][i]['name'] != skill) {
//      return member['skills'][i]
//    }
//  }
//}

var getRandomMember = function(team) {
  var index = Math.floor(Math.random() * Math.floor(team.length))
  return team[index]
}

// Board Stuff

var assignMemberToCard = function(card, member, board) {
  card['assigned'].push(member)
  var index = -1
  for (var i = 0; i < board['team'].length; i++) {
    if (board['team'][i]['name'] == member['name']) {
      index = i
    }
  }
  if (index >= 0) {
    board['team'].splice(index, 1)
  }
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

// Assigning Stuff

var noPairing = {

  assigned: function(card) {
    return card['assigned'].length == 1
  },
  assignCard: function(card, board) {
    var bestMatch = false
    var bestMatchSkill = false
    var i = 0
    while (! this.assigned(card) && board['team'].length) {
      var member = board['team'][i]
      var skill = getMemberSkill(member, card['needed'])
      if (skill) {
        if (! bestMatch) {
          bestMatch = member
          bestMatchSkill = skill
        } else {
          if (skill['level'] > bestMatchSkill['level']) {
            bestMatch = member
            bestMatchSkill = skill
          }
        }
      }
      if (! bestMatch && board['team'].length > 0) {
        bestMatch = getRandomMember(board['team'])
      }
      if (bestMatch) {
        assignMemberToCard(card, bestMatch, board)
      }
      i++
    }
  }
}

var assignCardByStrategy = function(card, board, strategy) {
  switch(strategy) {
    case 'no-pairing':
      noPairing.assignCard(card, board)
      break;
    default:
      console.log('Unknown Strategy')
  }
}

var assignCardsByStrategy = function(board, strategy) {
  var i
  //for (i = 0; i < board['backlog']['doing'].length; i++) {
  //  assignCardByStrategy(board['backlog']['doing'][i], board, strategy)
  //}7
  i = 0
  while (i < board['backlog']['to do'].length && board['team'].length) {
    var card = board['backlog']['to do'][i]
    assignCardByStrategy(card, board, strategy)
    if (card['assigned'].length > 0) {
      moveCard(board, card, 'to do', 'doing')
    }
    i++
  }
}

var assigned = function(board) {
  console.log('assigned', board)
}

var Assign = {

  test: function(strategy) { return strategy == 'x' },

  assignCards: function(state, strategy) {
    var n = 0
    var board = state['strategies'][strategy]
    while (! assigned(board) && n < 3) {
      if (board['run']) {
        assignCardsByStrategy(board, strategy)
      }
      n++
    }
  }
}

export default Assign
