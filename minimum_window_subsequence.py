class Solution:
  def solve(self, S, sub):
    if not sub or not S:
      return None
    D = {}
    for i in range(0, len(S)):
      c = S[i]
      if c not in D:
        D[c] = []
      D[c] += [i]
    first = sub[0]
    ret = None
    for i in D[first]:
      tmp = []
      tmp += [i]
      for j in sub[1:]:
        found = False
        for pos in D[j]:
          if pos < tmp[-1]:
            continue
          else:
            tmp += [pos]
            found = True
            break
        if not found:
          break
      if len(tmp) == len(sub):
        if not ret or (tmp[-1] - tmp[0]+1) < len(ret):
          ret = S[tmp[0]:tmp[-1]+1]

    return ret

s = Solution()
print s.solve("aaaaaabcadefg", "acaeg")
print s.solve("aaaaaabcadefg", "g")
print s.solve("", "g")
print s.solve("", "")
print s.solve("sssaaa", "")

