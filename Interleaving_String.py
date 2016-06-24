class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.not_possible = []
        return self.check(s1,s2,s3)

    def check(self, s1, s2, s3):
        if not s1 and not s2 and not s3:
            return True
        if (s1 or s2) and not s3:
            return False
        if not s1 and not s2 and s3:
            return False
        if (s1, s2) in self.not_possible:
            return False
        res = False
        if s1:
            if s1[0] == s3[0]:
                res = res or self.check(s1[1:], s2, s3[1:])
        if s2:
            if s2[0] == s3[0]:
                res = res or self.check(s1, s2[1:], s3[1:])
        if res == False:
            self.not_possible.append((s1,s2))
        return res

s = Solution()
print s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')

