from copy import copy
def match(pattern, data, dict, rev_dict):
  nr = copy(rev_dict)
  nd = copy(dict)
  result = False
  if not pattern and not data:
    return True
  if not (pattern and data):
    return False
  p = pattern[0]
  start = 0

  if p in dict:
    start = len(dict[p])

  for j in range(start,len(data)):
    token = data[0:j]
    if p in dict:
      if dict[p] != token:
        continue
    else:
      if token in rev_dict and rev_dict[token] != p:
        continue
      nr[token] = p
      nd[p] = token
    result |= match(pattern[1:], data[j+1:], nd, nr)
    if result:
      return result
  return False

assert match('abba', 'redbluebluered', {}, {})
assert not match('abba', 'redblueyellowred', {}, {})
assert match('aaaa', 'redredredred', {}, {})
assert not match('abba', 'redredredred', {}, {})
