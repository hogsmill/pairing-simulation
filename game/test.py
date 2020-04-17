

import unittest

from data import roles as r, board as b, team as t, card as c
from behaviour import flow as f, strategies as s
from utils.list import remove_from_list

def create_board():
  roles = r.Roles()
  team = t.Team(roles)
  board = b.Board(team)
  return board

class TestRoles(unittest.TestCase):

  def test_roles(self):
    roles = r.Roles()
    roles.roles = [
      {
        'name': 'front end',
        'skills': {
          'javascript': 10,
          'css': 10
        }
      }
    ]

    self.assertEqual(roles.get_role('front end')['skills']['javascript'], 10)
    self.assertEqual(roles.get_role('front end')['skills']['css'], 10)

  def test_role_skills(self):
    roles = r.Roles()
    roles.roles = [
      {
        'name': 'front end',
        'skills': {
          'javascript': 10,
          'css': 10
        }
      }
    ]

    self.assertEqual(roles.get_role_skill('front end', 'javascript'), 10)
    self.assertEqual(roles.get_role_skill('front end', 'css'), 10)

class TestCard(unittest.TestCase):

  def test_prepare_card(self):
      #board = create_board()
    card = c.Card()
    test_card = {'skill': 'a', 'level': 10}

    card.prepare_card(test_card)
    self.assertEqual(test_card['assigned'], [])
    self.assertEqual(test_card['completed'], 0)
    self.assertEqual(test_card['remaining'], 10)

  def test_card_is_complete(self):
    card = c.Card()
    test_card = {'skill': 'skill1', 'level': 10}
    card.prepare_card(test_card)

    self.assertFalse(card.card_is_complete(test_card))

    test_card['completed'] = 5
    self.assertFalse(card.card_is_complete(test_card))

    test_card['completed'] = 10
    self.assertTrue(card.card_is_complete(test_card))

    test_card['completed'] = 15
    self.assertTrue(card.card_is_complete(test_card))

  def test_complete_work_on_card(self):
    card = c.Card()
    test_card = {'id': 1, 'name': '1', 'skill': 'javascript', 'level': 30}
    card.prepare_card(test_card)

    card.complete_work_on_card(test_card, 10)
    self.assertEqual(test_card['remaining'], 20)
    self.assertEqual(test_card['completed'], 10)

    card.complete_work_on_card(test_card, 10)
    self.assertEqual(test_card['remaining'], 10)
    self.assertEqual(test_card['completed'], 20)

class TestBoard(unittest.TestCase):

  def test_board_complete(self):
    board = create_board()

    board.cards = {'to do': ['a'], 'doing': [],'done': []}
    self.assertFalse(board.board_complete())

    board.cards = {'to do': [], 'doing': ['b'],'done': []}
    self.assertFalse(board.board_complete())

    board.cards = {'to do': [], 'doing': [],'done': ['c']}
    self.assertTrue(board.board_complete())

  def test_card_is_assigned(self):
    board = create_board()
    card = c.Card()
    test_card = {'id': 1, 'name': '1', 'skill': 'java', 'level': 10}
    card.prepare_card(test_card)

    board.strategy = 'No Pairing'
    self.assertFalse(board.card_is_assigned(test_card))
    test_card['assigned'] = ['a']
    self.assertTrue(board.card_is_assigned(test_card))

    board.strategy = 'Best Match'
    test_card['assigned'] = []
    self.assertFalse(board.card_is_assigned(test_card))
    test_card['assigned'] = ['a']
    self.assertFalse(board.card_is_assigned(test_card))
    test_card['assigned'] = ['a', 'b']
    self.assertTrue(board.card_is_assigned(test_card))

  def test_number_to_assign(self):
    board = create_board()

    board.strategy = 'No Pairing'
    self.assertEqual(board.number_to_assign(), 1)

    board.strategy = 'Best Match'
    self.assertEqual(board.number_to_assign(), 2)

  def test_assign_member_to_card(self):
    board = create_board()
    card = c.Card()
    test_card = {'id': 1, 'name': '1', 'skill': 'java', 'level': 10}
    card.prepare_card(test_card)

    team_length = len(board.team.team)
    assigned_length = len(test_card['assigned'])

    board.assign_member_to_card(test_card, board.team.team[0])

    self.assertEqual(len(board.team.team), team_length - 1)
    self.assertEqual(len(test_card['assigned']), assigned_length + 1)

  def test_unassign_members_from_card(self):
    board = create_board()
    card = c.Card()
    test_card = {'id': 1, 'name': '1', 'skill': 'java', 'level': 10}
    card.prepare_card(test_card)
    team_length = len(board.team.team)
    test_card['assigned'] = board.team.team
    board.team.team = []

    board.unassign_members_from_card(test_card)

    self.assertEqual(len(board.team.team), team_length)
    self.assertEqual(len(test_card['assigned']), 0)

  def test_move_card(self):
    board = create_board()
    card = board.cards['to do'][0]

    todo = len(board.cards['to do'])
    doing = len(board.cards['doing'])

    board.move_card(card, 'to do', 'doing')
    self.assertEqual(len(board.cards['to do']), todo - 1)
    self.assertEqual(len(board.cards['doing']), doing + 1)

class TestTeam(unittest.TestCase):

  def test_team(self):

    # TODO: Define roles in here to pass in to t.Team
    roles = r.Roles()
    expert_level = 50
    expert_level_percentage = 5
    default_share = 2
    team = t.Team(roles, expert_level, expert_level_percentage, default_share)

    self.assertEqual(team.expert_level, expert_level)
    self.assertEqual(team.expert_level_percentage, expert_level_percentage)
    self.assertEqual(team.default_share, default_share)
    self.assertEqual(len(team.team), 6)

  def test_get_member_skill(self):
    roles = r.Roles()
    team = t.Team(roles)
    skill = {'name': 'java', 'level': 10}
    member = {'name': 'FE', 'skills': [{'name': 'sql', 'level': 10}, skill]}

    self.assertEqual(team.get_member_skill(member, 'java'), skill)

  def test_get_member_not_skill(self):
    roles = r.Roles()
    team = t.Team(roles)
    skill = {'name': 'java', 'level': 10}
    not_skill = {'name': 'sql', 'level': 10}
    member = {'name': 'FE', 'skills': [not_skill, skill]}

    self.assertEqual(team.get_member_not_skill(member, 'java'), not_skill)

  def test_add_share(self):
    roles = r.Roles()
    team = t.Team(roles)

    card_skill = 'javascript'
    skills = [{'name': 'javascript', 'level': 10}, {'name': 'css', 'level': 20}]
    member = {'name': 'FE 1', 'skills': skills}

    new_skills = [{'name': 'javascript', 'level': 10}, {'name': 'css', 'level': 25}]

    team.add_share(member, 'css', 5)
    self.assertEqual(member['skills'], new_skills)

    new_skills.append({'name': 'java', 'level': 10})

    team.add_share(member, 'java', 10)
    self.assertEqual(member['skills'], new_skills)

  def test_find_most_expert_on_card(self):
    roles = r.Roles()
    team = t.Team(roles)

    expert = {'name': 'expert', 'skills':[{'name': 'java', 'level': 48}]}
    member = {'skills':[]}

    card = {'skill':'java', 'level': 10, 'assigned': [member, expert]}

    expert = team.find_most_expert_on_card(card)
    self.assertEqual(expert['name'], 'expert')

  def test_add_default_level(self):
    roles = r.Roles()
    team = t.Team(roles)
    team.default_share = 1

    member1 = {'skills':[]}
    member2 = {'skills':[]}
    card = {'skill':'java', 'level': 10, 'assigned': [member1, member2]}

    team.add_default_level(card)
    self.assertEqual(member1['skills'], [{'name': 'java', 'level': 1}])
    self.assertEqual(member2['skills'], [{'name': 'java', 'level': 1}])

  def test_add_expert_level(self):
    roles = r.Roles()
    team = t.Team(roles)
    team.expert_level = 50
    team.expert_level_percentage = 10

    expert = {'skills':[{'name': 'java', 'level': 48}]}
    member = {'skills':[]}

    card = {'skill':'java', 'level': 10, 'assigned': [member, expert]}

    team.add_expert_level(card, expert)
    self.assertEqual(member['skills'], [{'name': 'java', 'level': 5}])
    self.assertEqual(expert['skills'], [{'name': 'java', 'level': 50}])

    team.add_expert_level(card, expert)
    self.assertEqual(member['skills'], [{'name': 'java', 'level': 10}])
    self.assertEqual(expert['skills'], [{'name': 'java', 'level': 50}])

  def test_add_member_knowledge(self):
    roles = r.Roles()
    team = t.Team(roles)
    team.expert_level = 50
    team.expert_level_percentage = 10
    team.default_share = 1

    expert = {'skills':[{'name': 'java', 'level': 48}]}
    member1 = {'skills':[]}
    member2 = {'skills':[]}

    card = {'skill': 'java', 'level': 5, 'assigned': [member1, member2]}

    team.add_member_knowledge(card)
    self.assertEqual(member1['skills'], [{'name': 'java', 'level': 1}])
    self.assertEqual(member2['skills'], [{'name': 'java', 'level': 1}])

    card = {'skill': 'java', 'level': 5, 'assigned': [expert, member2]}

    team.add_member_knowledge(card)
    self.assertEqual(expert['skills'], [{'name': 'java', 'level': 50}])
    self.assertEqual(member2['skills'], [{'name': 'java', 'level': 6}])

class TestFlow(unittest.TestCase):

  pass

class TestList(unittest.TestCase):

  def test_remove_from_list(self):
    list = [
      {'id': 1, 'name': 'One'},
      {'id': 2, 'name': 'Two'},
      {'id': 3, 'name': 'Three'}
    ]
    new_list = [list[0], list[2]]

    list = remove_from_list(list, 'id', 99)
    self.assertEqual(len(list), 3)
    self.assertEqual(list, list)

    list = remove_from_list(list, 'id', 2)
    self.assertEqual(len(list), 2)
    self.assertEqual(list, new_list)

if __name__ == '__main__':
    unittest.main()
