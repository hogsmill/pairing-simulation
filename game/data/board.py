
from data import card as c
from utils.list import remove_from_list
from utils.io import print_working_on_card

class Board:

    def __init__(self, team, cycles = 50, max_work_per_cycle = 20):

      self.max_cycles = cycles
      self.max_work_per_cycle = max_work_per_cycle
      self.card = c.Card()
      self.team = team

      self.cards = {
        'to do': [],
        'doing': [],
        'done': []
      }

      self.results = {
        'strategy':'', 'to do': [], 'doing': [], 'done': []
      }

    def prepare_board(self, board):
      for card in board.cards['to do']:
        self.card.prepare_card(card)

    def board_complete(self):
      return len(self.cards['to do']) == 0 and len(self.cards['doing']) == 0

    def card_is_assigned(self, card):
      return len(card['assigned']) == self.number_to_assign()

    def number_to_assign(self):
      return 1 if self.strategy == 'No Pairing' else 2

    def assign_member_to_card(self, card, member):
      card['assigned'].append(member)
      self.team.team = remove_from_list(self.team.team, 'name', member['name'])

    def unassign_members_from_card(self, card):
      for member in card['assigned']:
        self.team.team.append(member)
      card['assigned'] = []

    def move_card(self, move_card, from_queue, to_queue):
      self.cards[to_queue].append(move_card)
      self.cards[from_queue] = remove_from_list(self.cards[from_queue], 'id', move_card['id'])

    def calculate_work_done_on_cards(self, board):
      for card in board.cards['doing']:
        self.calculate_work_done_on_card(card)

    def calculate_work_done_on_card(self, card):
      print_working_on_card(card)
      done = 0
      for assigned in card['assigned']:
        for skill in assigned['skills']:
          if (skill['name'] == card['needed']):
            self.card.complete_work_on_card(card, skill['level'], self.max_work_per_cycle)
      self.calculate_knowledge_share(card)
      if (self.card.card_is_complete(card)):
        self.move_card(card, 'doing', 'done')
        self.unassign_members_from_card(card)

    def calculate_knowledge_share(self, card):
      self.team.add_member_knowledge(card)

    def save_status(self):
      self.results['to do'].append("{}".format(len(self.cards['to do'])))
      self.results['doing'].append("{}".format(len(self.cards['doing'])))
      self.results['done'].append("{}".format(len(self.cards['done'])))
