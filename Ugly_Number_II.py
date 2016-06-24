import copy
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        num = [0,0,0]
        while len(res) < n:
            print num
            n2 = res[num[0]]*2
            n3 = res[num[1]]*3
            n5 = res[num[2]]*5
            m = min(n2,n3,n5)
            if m == n2:
                num[0] += 1
            if m == n3:
                num[1] += 1
            if m == n5:
                num[2] += 1
            res.append(m)
        print res

s = Solution()
s.nthUglyNumber(389)
