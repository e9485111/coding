def match(pattern, data):
  dict = {}
  rev_dict = {}
  arr = data.split(' ');
  if len(arr) != len(pattern):
    return False
  for i, v in enumerate(pattern):
    if v in dict:
      if dict[v] != arr[i]:
        return False
    else:
      dict[v] = arr[i]
      if arr[i] in rev_dict and v != rev_dict[arr[i]]:
        return False
      rev_dict[arr[i]] = v
  return True


assert match('abba', 'red blue blue red')
assert not match('abba', 'red blue yellow red')
assert match('aaaa', 'red red red red')
assert not match('abba', 'red red red red')
