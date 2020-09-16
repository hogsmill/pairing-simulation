'use strict'

function getMemberSkill(member, skill) {
  for (let i = 0; i < member.skills.length; i++) {
    if (member.skills[i].name == skill) {
      return member.skills[i]
    }
  }
}

function findMostExpertOnCard(card) {
  let expert
  let level = 0
  for (let i = 0; i < card.assigned.length; i++) {
    const member = card.assigned[i]
    for (let j = 0; j < member.skills.length; j++) {
      const skill = member.skills[j]
      if (card.needed == skill.name) {
        if (!expert) {
          expert = member
          level = skill.level
        } else if (skill.level > level) {
          expert = member
          level = skill.level
        }
      }
    }
  }
  return expert
}

function addExpertLevel(card, expert, state) {
  const expertSkill = getMemberSkill(expert, card.needed)
  const shareLevel = Math.max(1, Math.round(expertSkill.level * state.expertLevelPercentage / 100))
  for (let i = 0; i < card.assigned.length; i++) {
    addShare(card.assigned[i], card.needed, shareLevel, state)
  }
}

function addDefaultLevel(card, state) {
  for (let i = 0; i < card.assigned.length; i++) {
    addShare(card.assigned[i], card.needed, state.defaultLevel, state)
  }
}

function addShare(member, card_skill, level, state) {
  let added
  for (let i = 0; i < member.skills.length; i++) {
    const skill = member.skills[i]
    if (skill.name == card_skill) {
      skill.level = Math.min(state.expertLevel, skill.level + level)
      added = true
    }
  }
  if (! added) {
    member.skills.push({'name': card_skill, 'level': level})
  }
}

function addMemberKnowledge(card, state) {
  // Rules:
  //   1) If there is somebody on the card with the needed skill, everybody
  //      gets 10% of the skill level of the highest expert
  //   2) If there is nobody on the card with the skill, everybody gets 1
  //
  const expert = findMostExpertOnCard(card)
  if (expert) {
    addExpertLevel(card, expert, state)
  } else {
    addDefaultLevel(card, state)
  }
}

const Knowledge = {

  calculateKnowledgeShare: function(state, strategy) {
    const board = state.strategies[strategy]
    for (let i = 0; i < board.backlog.doing.length; i++) {
      addMemberKnowledge(board.backlog.doing[i], state)
    }
    return state
  }
}

export default Knowledge
