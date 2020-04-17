
import os
import sys

from data import roles as r, board as b, team as t
from behaviour import flow as f, strategy as s

roles = r.Roles()
team = t.Team(roles)
board = b.Board(team)
strategies = s.Strategies()

strategy = False
if (len(sys.argv) > 1):
  strategy = sys.argv[1]

flow = f.Flow(board, strategies, strategy)

flow.run()
