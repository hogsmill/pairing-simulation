
from data import card as c

class Board:

    def __init__(self, team):

      self.card = c.Card()

      self.team = team
      self.cards = {
        'to do': [
          {
            'id': 1,
            'name': 'Front End 1',
            'skill': 'javascript',
            'level': 30
          },
          {
            'id': 2,
            'name': 'Back End 1',
            'skill': 'java',
            'level': 50
          }
      ],
      'doing': [],
      'done': []
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
      self.team.team.remove(member)
      card['assigned'].append(member)

    def unassign_members_from_card(self, card):
      for member in card[assigned]:
        self.team.team.append(member)
      card['assigned'] = []

    def move_card(self, card, from_queue, to_queue):
      self.cards[to_queue].append(card)
      self.cards[from_queue].remove(card)

    def calculate_work_done_on_cards(self, board):
      for card in board.cards['doing']:
        self.calculate_work_done_on_card(card)

    def calculate_work_done_on_card(self, card):
      print("      Working on card Id:'{}', required: {}:{}".format(card['id'], card['skill'], card['level']))
      done = 0
      for assigned in card['assigned']:
        for skill in assigned['skills']:
          if (skill['name'] == card['skill']):
            self.card.complete_work_on_card(card, skill['level'])
      if (self.card.card_is_complete(card)):
        self.move_card(card, 'doing', 'done')
