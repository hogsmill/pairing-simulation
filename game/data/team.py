
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

  def get_member_skill(self, member, skill):
    for member_skill in member['skills']:
      if (member_skill['name'] == skill):
        return member_skill
