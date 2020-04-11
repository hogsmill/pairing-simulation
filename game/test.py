

import unittest

from data import roles as r, board as b, team as t
from behaviour import flow as f, strategies as s

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

class TestBoard(unittest.TestCase):

  def test_prepare_card(self):
    board = create_board()
    card = {'skill': 'a', 'level': 10}

    board.prepare_card(card)
    self.assertEqual(card['completed'], 0)

  def test_card_is_complete(self):
    board = create_board()
    card = {'skill': 'skill1', 'level': 10}
    board.prepare_card(card)

    self.assertFalse(board.card_is_complete(card))

    card['completed'] = 5
    self.assertFalse(board.card_is_complete(card))

    card['completed'] = 10
    self.assertTrue(board.card_is_complete(card))

    card['completed'] = 15
    self.assertTrue(board.card_is_complete(card))

  def test_board_complete(self):
    board = create_board()

    board.cards = {'to do': ['a'], 'doing': [],'done': []}
    self.assertFalse(board.board_complete())

    board.cards = {'to do': [], 'doing': ['b'],'done': []}
    self.assertFalse(board.board_complete())

    board.cards = {'to do': [], 'doing': [],'done': ['c']}
    self.assertTrue(board.board_complete())

class TestTeam(unittest.TestCase):

  def test_team(self):
    roles = r.Roles()
    team = t.Team(roles)

    self.assertEqual(len(team.team), 5)

class TestFlow(unittest.TestCase):

  pass

if __name__ == '__main__':
    unittest.main()
