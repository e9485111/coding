class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.helper(k, n, 0, [])

    def helper(self, k, n, last, res):
        if k == 0 and n == 0:
            return [res[:]]
        else:
            ret = []
            for i in range(last+1, 10):
                if n >= i:
                    res.append(i)
                    ret += self.helper(k-1, n-i, i, res)
                    res.pop()
            return ret

s = Solution()
print s.combinationSum3(3,9)
