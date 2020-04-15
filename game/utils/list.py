
def remove_from_list(list, key, value):
  l = []
  for item in list:
    if (item[key] != value):
      l.append(item)
  return l
