
class BestShare:

  def assign(self, card, board, swap):
    print("BEST SHARE, PAIRING IS {}".format(board.pairing))
    self.do_assign(card, board, swap)
    if (board.pairing):
      self.do_assign(card, board, swap, True)

  def do_assign(self, card, board, swap, reverse=False):
    match = 0
    assigned = False
    for member in card['available']:
      for member_skill in member['skills']:
        if (member_skill['name'] == card['skill']):
          if (not reverse and member_skill['level'] > match):
            assigned = member
          if (reverse and (match == 0 or member_skill['level'] < match)):
            assigned = member
    if (not assigned and len(card['available']) > 0):
      assigned = card['available'][0]
    if (assigned):
      card['assigned'].append(assigned)
      card['available'].remove(assigned)
