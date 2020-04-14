
debug = True

def print_status(str):
  if (debug):
    print(str)

def print_queues(when, board):
  if (not debug):
    return
  todo = queue_string(board, 'to do')
  doing = queue_string(board, 'doing')
  done = queue_string(board, 'done')
  print("      {} - to do: [{}], doing: [{}], done: [{}]".format(when, todo, doing, done))

def queue_string(board, type):
  items = []
  comma = ", "
  for card in board.cards[type]:
    status = "[{} {}/{}]".format(card['skill'], card['completed'], card['level'])
    assigned = []
    for a in card['assigned']:
      assigned.append(a['name'])
    assigned = comma.join(assigned)
    items.append("Id: {} {} [{}]".format(card['id'], status, assigned))
  return comma.join(items)
