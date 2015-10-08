class Solution:
    def minWindow(self, s, t):
      if not t:
        return ""
      T = {}
      S = {}

      for c in t:
        T[c] = 1 if c not in T else T[c]+1
      for i in T.keys():
        S[i] = 0

      matched_all = len(T.keys())
      matched = 0
      if not s:
        return ""
      head = 0
      tail = 0

      if s[head] in T:
        S[s[head]] = 1
        if S[s[head]] == T[s[head]]:
          matched += 1

      found = False
      ret = s
      while head < len(s):
        if matched == matched_all:
          found = True
          str = s[tail:head+1]
          if len(str) < len(ret):
            ret = str
          c = s[tail]
          tail += 1
          if c in S:
            S[c] -= 1
            if S[c] < T[c]:
              matched -= 1
        else:
          head += 1
          if head == len(s):
            break
          c = s[head]
          if c in S:
            S[c] += 1
            if T[c] == S[c]:
              matched += 1
              if matched == matched_all:
                found = True
                str = s[tail:head+1]
                if len(str) < len(ret):
                  ret = str
      if found:
        return ret
      else:
        return ""



s = Solution()
print s.minWindow("ADOBECODEBANC", "ABC")
print s.minWindow("a", "aa")
print s.minWindow("", "ABC")
print s.minWindow("", "")
print s.minWindow("ADOBECODEBANC", "")
print s.minWindow("If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.", "iii")

