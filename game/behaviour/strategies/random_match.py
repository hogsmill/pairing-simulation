
from random import seed
from random import randint

class RandomMatch:

  def assign(self, card, board, swap):
    print("RANDOM, PAIRING IS {}".format(board.pairing))
    self.do_assign(card, board, swap)
    if (board.pairing):
      self.do_assign(card, board, swap)

  def do_assign(self, card, board, swap):
    assigned = False
    if (len(card['available']) > 0):
      assigned = card['available'][randint(0, len(card['available']) - 1)]
    if (assigned):
      card['assigned'].append(assigned)
      card['available'].remove(assigned)
