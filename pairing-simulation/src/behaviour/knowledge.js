'use strict';

var getMemberSkill = function(member, skill) {
  for (var i = 0; i < member['skills'].length; i++) {
    if (member['skills'][i]['name'] == skill) {
      return member['skills'][i]
    }
  }
}

var findMostExpertOnCard = function(card) {
  var expert
  var level = 0
  for (var i = 0; i < card['assigned'].length; i++) {
    var member = card['assigned'][i]
    for (var j = 0; j < member['skills'].length; j++) {
      var skill = member['skills'][j]
      if (card['needed'] == skill['name']) {
        if (!expert) {
          expert = member
          level = skill['level']
        } else if (skill['level'] > level) {
          expert = member
          level = skill['level']
        }
      }
    }
  }
  return expert
}

var addExpertLevel = function(card, expert, state) {
  var expertSkill = getMemberSkill(expert, card['needed'])
  var shareLevel = Math.max(1, Math.round(expertSkill['level'] * state['expertLevelPercentage'] / 100))
  for (var i = 0; i < card['assigned'].length; i++) {
    addShare(card['assigned'][i], card['needed'], shareLevel, state)
  }
}

var addDefaultLevel = function(card, state) {
  for (var i = 0; i < card['assigned'].length; i++) {
    addShare(card['assigned'][i], card['needed'], state['defaultLevel'], state)
  }
}

var addShare = function(member, card_skill, level, state) {
  var added
  for (var i = 0; i < member['skills'].length; i++) {
    var skill = member['skills'][i]
    if (skill['name'] == card_skill) {
      skill['level'] = Math.min(state['expertLevel'], skill['level'] + level)
      added = true
    }
  }
  if (! added) {
    member['skills'].push({'name': card_skill, 'level': level})
  }
}

var addMemberKnowledge = function(card, state) {
  // Rules:
  //   1) If there is somebody on the card with the needed skill, everybody
  //      gets 10% of the skill level of the highest expert
  //   2) If there is nobody on the card with the skill, everybody gets 1
  //
  var expert = findMostExpertOnCard(card)
  if (expert) {
    addExpertLevel(card, expert, state)
  } else {
    addDefaultLevel(card, state)
  }
}

var Knowledge = {

  calculateKnowledgeShare: function(state, strategy) {
    var board = state['strategies'][strategy]
    for (var i = 0; i < board['backlog']['doing'].length; i++) {
      addMemberKnowledge(board['backlog']['doing'][i], state)
    }
  }
}

export default Knowledge
