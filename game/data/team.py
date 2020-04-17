
class Team:

  def __init__(self, roles, expert_level = 100, expert_level_percentage = 10, default_share = 1):

    self.expert_level = expert_level
    self.expert_level_percentage = expert_level_percentage
    self.default_share = default_share
    self.team = [
      {'name': 'FE 1', 'skills': roles.get_role('front end')['skills']},
      {'name': 'FE 2', 'skills': roles.get_role('front end')['skills']},
      {'name': 'BE 1', 'skills': roles.get_role('back end')['skills']},
      {'name': 'BE 2', 'skills': roles.get_role('back end')['skills']},
      {'name': 'DEVOPS', 'skills': roles.get_role('devops')['skills']},
      {'name': 'DBA', 'skills': roles.get_role('dba')['skills']}
    ]

  def get_member_skill(self, member, skill):
    for member_skill in member['skills']:
      if (member_skill['name'] == skill):
        return member_skill

  def get_member_not_skill(self, member, skill):
    for member_skill in member['skills']:
      if (member_skill['name'] != skill):
        return member_skill

  def add_member_knowledge(self, card):
    # Rules:
    #   1) If there is somebody on the card with the needed skill, everybody
    #      gets 10% of the skill level of the highest expert
    #   2) If there is nobody on the card with the skill, everybody gets 1
    #
    expert = self.find_most_expert_on_card(card)
    if (expert):
      self.add_expert_level(card, expert)
    else:
      self.add_default_level(card)

  def find_most_expert_on_card(self, card):
    expert = False
    level = 0
    for member in card['assigned']:
      for skill in member['skills']:
        if (card['skill'] == skill['name']):
          if (not expert):
            expert = member
            level = skill['level']
          elif (skill['level'] > level):
            expert = member
            level = skill['level']
    return expert

  def add_expert_level(self, card, expert):
    expert_skill = self.get_member_skill(expert, card['skill'])
    expert_level = min(expert_skill['level'], self.expert_level)
    share_level = max(1, round(expert_skill['level'] * self.expert_level_percentage / 100))
    for member in card['assigned']:
      self.add_share(member, card['skill'], share_level)

  def add_default_level(self, card):
    for member in card['assigned']:
      self.add_share(member, card['skill'], self.default_share)

  def add_share(self, member, card_skill, level):
    added = False
    for skill in member['skills']:
      if (skill['name'] == card_skill):
        skill['level'] = min(self.expert_level, skill['level'] + level)
        added = True
    if (not added):
      member['skills'].append({'name': card_skill, 'level': level})
