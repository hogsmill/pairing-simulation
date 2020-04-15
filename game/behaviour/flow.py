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
      board.swap = False
      self.run_strategy(board)

      # TODO: Swap pairs
      #board.pairing = True
      #self.run_strategy(board)

  def run_strategy(self, board):
    print_status("  Running {}, Pairing is {}".format(board.strategy, board.pairing))
    board.cycles = 0
    board.prepare_board(board)
    while(not board.board_complete() and board.cycles < 5):
      print_status("    Cycle {}".format(board.cycles))
      print_queues('Start', board)

      self.strategies.assign_cards_based_on_strategy(board)
      board.calculate_work_done_on_cards(board)

      print_queues('End  ', board)
      board.cycles = board.cycles + 1
