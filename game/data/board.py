
class Board:

    def __init__(self, team):

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

    def board_complete(self):
      return len(self.cards['to do']) == 0 and len(self.cards['doing']) == 0

    def move_card(self, card, from_queue, to_queue):
      self.cards[to_queue].append(card)
      self.cards[from_queue].remove(card)

    def card_is_complete(self, card):
      return card['completed'] >= card['level']

    def prepare_card(self, card):
      card['assigned'] = []
      card['remaining'] = []
      card['available'] = []
      card['completed'] = 0

    def match_members_to_cards(self, board):
      #for card in board.cards['doing']:
      #  self.check_members_on_card(card, team)
      for card in board.cards['to do']:
        self.prepare_card(card)
        self.team.add_available_members(card, board)

# =================== Orig ================

    def work_on_card(self, card):
      print("Working on Id:{}".format(card['id']))
      self.get_card_team_members(card)
      self.calculate_work_on_card(card)

    def get_card_team_members(self, card):
      pass

    def calculate_work_on_card(self, card):
      pass

    def skill_is_complete(self, skill, dones):
      if (len(dones) == 0):
        return False
      complete = True
      for done in dones:
        if (skill['skill'] == done['skill']):
          if (done['done'] < skill['level']):
            print("Not complete: {}:{} is less than {}:{}".format(
              done['skill'], done['done'], skill['skill'], skill['level']))
            complete = False
      return complete
