class Solution(object):
  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    results = []
    possible = []
    possible = [True]*len(s)
    ret = self.helper(s,0,wordDict, results, possible)
    return ret

  def helper(self, s, start, wordDict, results, possible):
    ret = []
    if start == len(s):
      str = ' '.join(results)
      return [str]
    for i in wordDict:
      l = len(i)
      if len(s) < start+l:
        continue
      else:
        sub = s[start:start+l]
        if i == sub and possible[start]:
          results += [i]
          r = self.helper(s, start+l, wordDict, results, possible)
          if not r:
            possible[start+l] = False
          ret += r
          results.pop()
    return ret

s = Solution()
wordDict = ['cat','cats', 'and', 'sand', 'dog']
print s.wordBreak('catsanddog', wordDict)

wordDict = ["aaaa","aaa","aa"]
print s.wordBreak("aaaaaaaa", wordDict)

wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaab", wordDict)
print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", wordDict)
