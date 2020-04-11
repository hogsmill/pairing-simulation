import copy

from utils.io import print_queues, print_status

class Flow:

  def __init__(self, board, strategies):
    self.board = board
    self.strategies = strategies

  def run(self):
    print_status("Running")
    for strategy in self.strategies.strategies:
      board = copy.deepcopy(self.board)
      board.strategy = strategy
      board.pairing = False
      self.run_strategy(board)
      board.pairing = True
      self.run_strategy(board)

  def run_strategy(self, board):
    print_status("  Running " + board.strategy)
    board.cycles = 0
    while(not board.board_complete() and board.cycles < 3):
      print_status("    Cycle {}".format(board.cycles))
      print_queues('Start', board)

      board.match_members_to_cards(board)
      self.strategies.assign_cards_based_on_strategy(board)
      print("calculate work done in cycle")

      print_queues('End  ', board)
      board.cycles = board.cycles + 1
