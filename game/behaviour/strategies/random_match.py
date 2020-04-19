
class RandomMatch:

  def assign(self, card, board):
    if (not board.card_is_assigned(card)):
      self.do_assign(card, board)
      self.do_assign(card, board)

  def do_assign(self, card, board):
    assigned = False
    if (len(board.team.team) > 0):
      assigned = board.team.get_random_member()
    if (assigned):
      board.assign_member_to_card(card, assigned)
