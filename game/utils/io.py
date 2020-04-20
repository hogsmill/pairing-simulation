
debug = False
record = True

def print_status(str, d = False):
  if (debug or d):
    print(str)

def print_queues(when, board):
  todo = queue_string(board, 'to do')
  doing = queue_string(board, 'doing')
  done = queue_string(board, 'done')
  free = len(board.team.team)
  print_status("      {} - to do: [{}], doing: [{}], done: [{}], free: {}".format(when, todo, doing, done, free))

def print_team(when, team):
  print_status("Knowledge at " + when)
  for member in team:
    comma = ", "
    skills = []
    for skill in member['skills']:
      skills.append("{}:{}".format(skill['name'], skill['level']))
    print_status("Member: {}, skills {}".format(member['name'], comma.join(skills)), True)

def print_working_on_card(card):
      print_status("        Working on card Id:'{}', required: {}:{}/{}".format(card['id'], card['needed'], card['completed'], card['amount']))

def queue_string(board, type):
  items = []
  comma = ", "
  for card in board.cards[type]:
    status = "[{} {}/{}]".format(card['needed'], card['completed'], card['amount'])
    assigned = []
    for a in card['assigned']:
      assigned.append(a['name'])
    assigned = comma.join(assigned)
    items.append("Id: {} {} [{}]".format(card['id'], status, assigned))
  return comma.join(items)


def start_results_file(file, n):
  f = open(file, "a")
  return f

def save_results(f, results):
  results_str = results['strategy'] + ", " + ", ".join(results['done'])
  f.write(results_str + "\n")
