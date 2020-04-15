
class BestMatch():

  def assign(self, card, board):
    while (len(board.team.team) > 0 and not board.card_is_assigned(card)):
      self.find_best_match(card, board)

  def find_best_match(self, card, board):
    best_match = False
    best_match_skill = False
    for member in board.team.team:
      skill = board.team.get_member_skill(member, card['skill'])
      if (skill):
        if (not best_match):
          best_match = member
          best_match_skill = skill
        else:
          if (skill['level'] > best_match_skill['level']):
            best_match = member
            best_match_skill = skill
    if (not best_match):
      best_match = board.team.team[0]
    if (best_match):
      card['assigned'].append(best_match)
      team = []
      for member in board.team.team:
        if (member['name'] != best_match['name']):
          team.append(member)
      board.team.team = team
