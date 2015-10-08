class Solution:
    def pt(self, M, l, r, u, d):
#      print l,r,u,d
      if l == r and u == d:
        return [M[l][d]]
      if l == r:
        ret = []
        for i in range(u, d+1):
          ret += [M[i][l]]
        return ret
      if u == d:
        ret = []
        for i in range(l, r+1):
          ret += [M[u][i]]
        return ret
      ret = []
      ret += M[u][l:r+1]
      for i in range(u+1, d):
        ret += [M[i][r]]
      ret += reversed(M[d][l:r+1])
      tmp = []
      for i in range(u+1, d):
        tmp += [M[i][l]]
      ret += reversed(tmp)
      return ret

    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
      H = len(matrix)-1
      if H >= 0:
        L = len(matrix[0])-1
      else:
        return matrix

      ret = []
      steps = 0
      while H >=0 and L >= 0 and L > steps and H > steps:
        print steps, H, L
        ret += self.pt(matrix, steps, L, steps, H)
        H -= 1
        L -= 1
        steps += 1
      return ret
s = Solution()
print s.spiralOrder([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])
"""
print s.spiralOrder([[2,3]])
print s.spiralOrder([[1],[2],[3]])
print s.spiralOrder([[1]])
print s.spiralOrder(
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ])
    """
