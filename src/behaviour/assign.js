'use strict';

// Team Stuff

var getMemberSkill = function(member, skill) {
  for (var i = 0; i < member['skills'].length; i++) {
    if (member['skills'][i]['name'] == skill) {
      return member['skills'][i]
    }
  }
}

var getMemberNotSkill = function(member, skill) {
  for (var i = 0; i < member['skills'].length; i++) {
    if (member['skills'][i]['name'] != skill) {
      return member['skills'][i]
    }
  }
}

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

var moveCards = function(board, cards, fromQueue, toQueue) {
  for (var i = 0; i < cards.length; i++) {
    board['backlog'][toQueue].push(cards[i])
    var newFromQueue = []
    for (var j = 0; j < board['backlog'][fromQueue].length; j++) {
      if (board['backlog'][fromQueue][j]['id'] != cards[i]['id']) {
        newFromQueue.push(board['backlog'][fromQueue][j])
      }
    }
    board['backlog'][fromQueue] = newFromQueue
  }
}

// Assigning Stuff

var assignBest = function(card, board, expert) {
  var bestMatch, bestMatchSkill
  var i = 0
  while (i < board['team'].length) {
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
    i++
  }
  if (! bestMatch && board['team'].length > 0) {
    bestMatch = getRandomMember(board['team'])
  }
  if (bestMatch) {
    bestMatch['expert'] = expert
    assignMemberToCard(card, bestMatch, board)
  }
}

var assignWorst = function(card, board) {
  var worstMatch
  var i = 0
  while (! worstMatch && i < board['team'].length && board['team'].length > 0) {
    var skill = getMemberSkill(board['team'][i], card['needed'])
    var notSkill = getMemberNotSkill(board['team'][i], card['needed'])
    if (notSkill && ! skill) {
      worstMatch = board['team'][i]
    }
    i = i + 1
  }
  if (! worstMatch && board['team'].length > 0) {
    worstMatch = getRandomMember(board['team'])
  }
  if (worstMatch) {
    worstMatch['expert'] = false
    assignMemberToCard(card, worstMatch, board)
  }
}

var noPairing = {
  assignCard: function(card, board) {
    assignBest(card, board, false)
  }
}

var bestPair = {
  assignCard: function(card, board, expert) {
    assignBest(card, board, expert)
  }
}

var bestShare = {
  assignCardBest: function(card, board) {
    assignBest(card, board, true)
  },
  assignCardWorst: function(card, board) {
    assignWorst(card, board)
  }
}

//var randomPair = {
//  assignCard: function(card, board) {
//    console.log('Assigning random')
//    assignRandom(card, board)
//  }
//}

var assignCardByStrategy = function(card, board, strategy) {
  switch(strategy) {
    case 'no-pairing':
      noPairing.assignCard(card, board)
      break;
    case 'best-pair':
      bestPair.assignCard(card, board, true)
      bestPair.assignCard(card, board, false)
      break;
    case 'best-share':
      bestShare.assignCardBest(card, board)
      bestShare.assignCardWorst(card, board)
      break;
    //case 'random':
    //  randomPair.assignCardRandom(card, board)
    //  randomPair.assignCardRandom(card, board)
    //  break;
    default:
      console.log('Unknown Strategy')
  }
}

var assignCardsByStrategy = function(board, strategy) {
  var i, cards
  //for (i = 0; i < board['backlog']['doing'].length; i++) {
  //  assignCardByStrategy(board['backlog']['doing'][i], board, strategy)
  //}7
  i = 0
  cards = []
  while (i < board['backlog']['to do'].length && board['team'].length) {
    var card = board['backlog']['to do'][i]
    assignCardByStrategy(card, board, strategy)
    if (card['assigned'].length > 0) {
      cards.push(card)
    }
    i++
  }
  moveCards(board, cards, 'to do', 'doing')
}

var Assign = {

  test: function(strategy) { return strategy == 'x' },

  assignCards: function(state, strategy) {
    assignCardsByStrategy(state['strategies'][strategy], strategy)
  }
}

export default Assign
