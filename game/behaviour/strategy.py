

from behaviour.strategies import best_match as bm
from behaviour.strategies import best_share as bs
from behaviour.strategies import random_match as r

class Strategies:

  def __init__(self):

    self.best_match = bm.BestMatch()
    self.best_share = bs.BestShare()
    self.random_match = r.RandomMatch()

    self.strategies = [
      'Best Match',
      'Best Share',
      'Random'
      #'Worst Match'
    ]

  def assign_cards_based_on_strategy(self, board, swap = False):
    for card in board.cards['doing']:
      print('  DOING')
      self.assign_card_based_on_strategy(card, board, swap)
    for card in board.cards['to do']:
      print('  TO DO')
      self.assign_card_based_on_strategy(card, board, swap)
      if (len(card['assigned']) > 0):
        board.move_card(card, 'to do', 'doing')

  def assign_card_based_on_strategy(self, card, board, swap):
    if (board.strategy == 'Best Match'):
      self.best_match.assign(card, board, swap)
    elif (board.strategy == 'Best Share'):
      self.best_share.assign(card, board, swap)
    elif (board.strategy == 'Random'):
      self.random_match.assign(card, board, swap)
    else:
      print("UNKNOWN STRATEGY")

    s = []
    for member in card['assigned']:
      s.append(member['name'])
    print(s)
