
from random import seed
from random import randint

class Backlog:

  # Card format is (e.g.)
  # {
  #   'id': 1,
  #   'name': 'Front End 1',
  #   'skill': 'javascript',
  #   'level': 30
  # }

  def  __init__(self, no_of_cards = 100):

    self.skills = {
      'Front End': ['javascript', 'css', 'react'],
      'Back End': ['java', 'apis'],
      'Database': ['sql', 'mongo'],
      'Devops': ['jenkins', 'firewalls'],
      'Other': ['SEO', 'security']
    }
    self.levels = [30, 50, 80]
    self.percentages = {
      'Front End': 10,
      'Back End': 50,
      'Database': 10,
      'Devops': 10,
      'Other': 20
    }

    self.no_of_cards = no_of_cards

  def generate_backlog(self):
    no_of_cards = self.calculate_number_of_cards()
    cards = []
    id = 1
    for key in self.skills:
      i = 1
      while (i <= no_of_cards[key]):
        cards.append(self.generate_card(key, i, id))
        i = i + 1
        id = id + 1
    return cards

  def calculate_number_of_cards(self):
    cards = {}
    for key in self.percentages:
      cards[key] = int(self.no_of_cards * self.percentages[key] / 100)
    return cards

  def generate_card(self, area, i, id):
    skill = randint(0, len(self.skills[area]) - 1)
    level = randint(0, len(self.levels) - 1)
    return {
      'id': id,
      'name': "Card {}".format(i),
      'skill': self.skills[area][skill],
      'level': self.levels[level],

      # TODO: Rmeove these - they are added by prepare_card
      'assigned': [],
      'remaining': self.levels[level],
      'completed': 0
    }
