
class Roles:

  def __init__(self):
    self.roles = [
      {
        'name': 'front end',
        'skills': [
          {'name': 'javascript', 'level': 30},
          {'name': 'css', 'level': 30}
        ]
      },
      {
        'name': 'back end',
        'skills': [
          {'name': 'java', 'level': 30}
         ]
      },
      {
        'name': 'devops',
        'skills': [
          {'name': 'jenkins', 'level': 30}
         ]
      },
      {
        'name': 'dba',
        'skills': [
          {'name': 'sql', 'level': 30},
          {'name': 'mongo', 'level': 30}
         ]
      }
    ]

  def get_role(self, role_name):
    for role in self.roles:
      if (role['name'] == role_name):
        return role

  def get_role_skill(self, role_name, skill):
    role = self.get_role(role_name)
    if (skill in role['skills']):
      return role['skills'][skill]
