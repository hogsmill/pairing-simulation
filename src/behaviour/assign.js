'use strict'

// Team Stuff

const getMemberSkill = function(member, skill) {
  for (let i = 0; i < member.skills.length; i++) {
    if (member.skills[i].name == skill) {
      return member.skills[i]
    }
  }
}

const getMemberNotSkill = function(member, skill) {
  for (let i = 0; i < member.skills.length; i++) {
    if (member.skills[i].name != skill) {
      return member.skills[i]
    }
  }
}

const getRandomMember = function(team) {
  const index = Math.floor(Math.random() * Math.floor(team.length))
  return team[index]
}

// Board Stuff

const assignMemberToCard = function(card, member, board) {
  card.assigned.push(member)
  let index = -1
  for (let i = 0; i < board.team.length; i++) {
    if (board.team[i].name == member.name) {
      index = i
    }
  }
  if (index >= 0) {
    board.team.splice(index, 1)
  }
}

const moveCards = function(board, cards, fromQueue, toQueue) {
  for (let i = 0; i < cards.length; i++) {
    board.backlog[toQueue].push(cards[i])
    const newFromQueue = []
    for (let j = 0; j < board.backlog[fromQueue].length; j++) {
      if (board.backlog[fromQueue][j].id != cards[i].id) {
        newFromQueue.push(board.backlog[fromQueue][j])
      }
    }
    board.backlog[fromQueue] = newFromQueue
  }
}

// Assigning Stuff

const assignBest = function(card, board, expert) {
  let bestMatch, bestMatchSkill
  let i = 0
  while (i < board.team.length) {
    const member = board.team[i]
    const skill = getMemberSkill(member, card.needed)
    if (skill) {
      if (! bestMatch) {
        bestMatch = member
        bestMatchSkill = skill
      } else {
        if (skill.level > bestMatchSkill.level) {
          bestMatch = member
          bestMatchSkill = skill
        }
      }
    }
    i++
  }
  if (! bestMatch && board.team.length > 0) {
    bestMatch = getRandomMember(board.team)
  }
  if (bestMatch) {
    bestMatch.expert = expert
    assignMemberToCard(card, bestMatch, board)
  }
}

const assignWorst = function(card, board) {
  let worstMatch
  let i = 0
  while (! worstMatch && i < board.team.length && board.team.length > 0) {
    const skill = getMemberSkill(board.team[i], card.needed)
    const notSkill = getMemberNotSkill(board.team[i], card.needed)
    if (notSkill && ! skill) {
      worstMatch = board.team[i]
    }
    i = i + 1
  }
  if (! worstMatch && board.team.length > 0) {
    worstMatch = getRandomMember(board.team)
  }
  if (worstMatch) {
    worstMatch.expert = false
    assignMemberToCard(card, worstMatch, board)
  }
}

const noPairing = {
  assignCard: function(card, board) {
    assignBest(card, board, false)
  }
}

const bestPair = {
  assignCard: function(card, board, expert) {
    assignBest(card, board, expert)
  }
}

const bestShare = {
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

const assignCardByStrategy = function(card, board, strategy) {
  switch(strategy) {
    case 'no-pairing':
      noPairing.assignCard(card, board)
      break
    case 'best-pair':
      bestPair.assignCard(card, board, true)
      bestPair.assignCard(card, board, false)
      break
    case 'best-share':
      bestShare.assignCardBest(card, board)
      bestShare.assignCardWorst(card, board)
      break
    //case 'random':
    //  randomPair.assignCardRandom(card, board)
    //  randomPair.assignCardRandom(card, board)
    //  break;
    default:
      console.log('Unknown Strategy')
  }
}

const assignCardsByStrategy = function(board, strategy) {
  let i = 0
  const cards = []
  while (i < board.backlog['to do'].length && board.team.length) {
    const card = board.backlog['to do'][i]
    assignCardByStrategy(card, board, strategy)
    if (card.assigned.length > 0) {
      cards.push(card)
    }
    i++
  }
  moveCards(board, cards, 'to do', 'doing')
}

const Assign = {

  test: function(strategy) { return strategy == 'x' },

  assignCards: function(state, strategy) {
    assignCardsByStrategy(state.strategies[strategy], strategy)
    return state
  }
}

export default Assign
