'use strict'

const cardIsComplete = function(card) {
  return card.remaining <= 0
}

const completeWorkOnCard = function(card, skillLevel, maxWorkPerCycle) {
  const amount = Math.min(skillLevel, maxWorkPerCycle)
  card.completed = card.completed + amount
  card.remaining = card.remaining - amount
  if (card.completed > card.amount) {
    card.completed = card.amount
    card.remaining = 0
  }
}

const calculateWorkDoneOnCard = function(card, board, state) {
  let i, j
  for (i = 0; i < card.assigned.length; i++) {
    const member = card.assigned[i]
    if (member.expert || card.assigned.length == 1) {
      for (j = 0; j < member.skills.length; j++) {
        const skill = member.skills[j]
        if (skill.name == card.needed) {
          completeWorkOnCard(card, skill.level, state.maxWorkPerCycle)
        }
      }
    }
  }
}

const unassignMembersFromCard = function(board, card) {
  for (let i = 0; i < card.assigned.length; i++) {
    board.team.push(card.assigned[i])
  }
  card.assigned = []
}

const moveCard = function(board, card, fromQueue, toQueue) {
  board.backlog[toQueue].push(card)
  let index = -1
  for (let i = 0; i < board.backlog[fromQueue].length; i++) {
    if (board.backlog[fromQueue][i].id == card.id) {
      index = i
    }
  }
  if (index >= 0) {
    board.backlog[fromQueue].splice(index, 1)
  }
}

const Calculate = {

  calculateWorkDoneOnCards: function(state, strategy) {
    let i
    const board = state.strategies[strategy]
    for (i = 0; i < board.backlog.doing.length; i++) {
      calculateWorkDoneOnCard(board.backlog.doing[i], board, state)
    }
    for (i = 0; i < board.backlog.doing.length; i++) {
      const card = board.backlog.doing[i]
      if (cardIsComplete(card)) {
        moveCard(board, card, 'doing', 'done')
        unassignMembersFromCard(board, card)
      }
    }
    return state
  }

}

export default Calculate
