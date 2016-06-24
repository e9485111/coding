class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        self.impossible = set()
        return self.helper(s, wordDict)

    def helper(self, s, wordDict):
        if s in self.impossible:
            return False
        if not s:
            return True
        else:
            for i in wordDict:
                if s.startswith(i):
                    if self.helper(s[len(i):], wordDict):
                        return True
            self.impossible.add(s)
            return False

s = Solution()

print s.wordBreak('a', [])
print s.wordBreak('leetcode', ["leet", "code"])
