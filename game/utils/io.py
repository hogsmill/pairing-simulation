
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
  print("        {} - to do: [{}], doing: [{}], done: [{}]".format(when, todo, doing, done))

def queue_string(board, type):
  items = []
  for card in board.cards[type]:
    items.append("Id: {}".format(card['id']))
  comma = ", "
  return comma.join(items)
