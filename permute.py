def permute(str):
  map = {}
  for i in str:
    if i not in map:
      map[i] = 0
    map[i] += 1

  return helper(str, map, 0)

def helper(str, map, index):
  if index == len(str):
    return [str]

  ret = []
  for i in map.keys():
    if map[i] > 0:
      map[i] -= 1
      str = list(str)
      str[index] = i
      str = "".join(str)
      ret += helper(str, map, index+1)
      map[i] += 1
  return ret

print permute("aac")
