import copy

from utils.io import print_queues, print_team, print_status
from generate import backlog as b

class Flow:

  def __init__(self, board, strategies, strategy):
    self.board = board
    self.strategies = strategies
    if (strategy):
      self.strategies.strategies = [strategy]

    backlog = b.Backlog()
    self.board.cards['to do'] = backlog.generate_backlog()

  def run(self):
    print_status("Running")
    f = open("results.txt", "a")
    for strategy in self.strategies.strategies:
      board = copy.deepcopy(self.board)
      board.strategy = strategy
      board.pairing = False
      board.swap = False

      print_team('Start', board.team.team)

      self.run_strategy(board)

      print_team('End', board.team.team)

      # TODO: Swap pairs
      #board.pairing = True
      #self.run_strategy(board)

  def run_strategy(self, board):
    print_status("  Running {}, Pairing is {}".format(board.strategy, board.pairing))
    cycles = 0
    board.prepare_board(board)
    while(not board.board_complete() and cycles < board.max_cycles):
      print_status("    Cycle {}".format(cycles))
      print_queues('Start', board)

      self.strategies.assign_cards_based_on_strategy(board)
      board.calculate_work_done_on_cards(board)

      print_queues('End  ', board)
      cycles = cycles + 1

    total_cards = len(board.cards['to do']) + len(board.cards['doing']) + len(board.cards['done'])
    done_cards = len(board.cards['done'])
    print("----------------------------------------------------------------------------")
    print("Finished - Strategy '{}', Cards complete {}/{}, Cycles {}".format(board.strategy, done_cards, total_cards, cycles))
    print("----------------------------------------------------------------------------")
