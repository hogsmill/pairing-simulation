
import os
import sys

from data import roles as r, board as b, team as t
from behaviour import flow as f, strategy as s

sys.path.append(os.getcwd())

roles = r.Roles()
team = t.Team(roles)
board = b.Board(team)
strategies = s.Strategies()

flow = f.Flow(board, strategies)

flow.run()
