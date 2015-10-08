def toAZ(num):
  if num < 10:
    return str(num)
  elif num < 36:
    return chr(num-10+ord('a'))

  q = num / 36
  r = num % 36
  return toAZ(q) + toAZ(r)

def cton(c):
  if ord(c) - ord('0') >= 0 and ord(c) - ord('0') <10:
    return int(ord(c) - ord('0'))
  else:
    return int(ord(c) - ord('a'))+10

def fromAZ(s):
  if not s:
    return 0
  c = s[-1]
  val = cton(c)
  if len(s) == 1:
    return val

  return val + 36 * fromAZ(s[0:-1])

v = [12321,2322,122,1,4,55,22,123,2,123,5,2,1231,32,134132,1234,23423]
for i in v:
  assert fromAZ(toAZ(i)) == i, (toAZ(i), fromAZ(toAZ(i)))
