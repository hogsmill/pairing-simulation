
class Team:

  def __init__(self, roles):

    self.team = [
      {'name': 'FE 1', 'skills': roles.get_role('front end')['skills']},
      {'name': 'FE 2', 'skills': roles.get_role('front end')['skills']},
      {'name': 'BE 1', 'skills': roles.get_role('back end')['skills']},
      {'name': 'BE 2', 'skills': roles.get_role('back end')['skills']},
      {'name': 'DEVOPS', 'skills': roles.get_role('devops')['skills']},
      {'name': 'DBA', 'skills': roles.get_role('dba')['skills']}
    ]

  def add_available_members(self, card, board):
    for member in self.team:
      unassigned = True
      for card_in_play in board.cards['doing']:
        for assigned in card_in_play['assigned']:
          if (member['name'] == assigned['name']):
            unassigned = False
      if (unassigned):
        card['available'].append(member)
