def printPalindromes(str):
  M = {}
  odds = set()
  for i in str:
    if i not in M:
      M[i] = 0
    M[i] += 1
    if M[i] % 2 == 1:
      odds.add(i)
    else:
      odds.remove(i)
  ret = ""
  if odds:
    ret = odds.pop()
    M[ret] -= 1
    assert(len(odds) == 0)
  helper(M, ret)

def helper(M, curr):
  all_zero = True
  for i in M:
    if M[i] > 0:
      assert M[i] % 2 == 0
      all_zero = False
      M[i] -= 2
      tmp = helper(M, i+curr+i)
      M[i] += 2
  if all_zero:
    print curr


printPalindromes("aaaaccd")
