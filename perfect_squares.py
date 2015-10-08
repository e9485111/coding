class Solution(object):
  def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    DP = range(0, n+1)
    for i in range(1,n+1):
      for j in range(1, int(i**0.5)+1):
        DP[i] = min(DP[i], DP[i-j*j]+1)
    return DP[n]
s = Solution()
print s.numSquares(4635)
