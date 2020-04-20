
class BestShare:

  def assign(self, card, board):
    if (not board.card_is_assigned(card)):
      self.find_best_match(card, board)
      self.find_worst_match(card, board)

  def find_best_match(self, card, board):
    best_match = False
    best_match_skill = False
    for member in board.team.team:
      skill = board.team.get_member_skill(member, card['needed'])
      if (skill):
        if (not best_match):
          best_match = member
          best_match_skill = skill
        else:
          if (skill['level'] > best_match_skill['level']):
            best_match = member
            best_match_skill = skill
    if (not best_match and len(board.team.team) > 0):
      best_match = board.team.get_random_member()
    if (best_match):
      board.assign_member_to_card(card, best_match)

  def find_worst_match(self, card, board):
    worst_match = False
    i = 0
    while (not worst_match and i < len(board.team.team) and len(board.team.team) > 0):
      skill = board.team.get_member_skill(board.team.team[i], card['needed'])
      not_skill = board.team.get_member_not_skill(board.team.team[i], card['needed'])
      if (not_skill and not skill):
        worst_match = board.team.team[i]
      i = i + 1
    if (not worst_match and len(board.team.team) > 0):
      worst_match = board.team.get_random_member()
    if (worst_match):
      board.assign_member_to_card(card, worst_match)
