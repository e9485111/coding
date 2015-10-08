class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
      leftx = max(A,E)
      lefty = max(B,F)
      rightx = min(C,G)
      righty = min(D,H)
      print leftx, lefty, rightx, righty
      return (C-A)*(D-B)+(G-E)*(H-F) - max(rightx-leftx,0)*max(righty-lefty,0)

s=Solution()
#print s.computeArea(-3,0,3,4,0,-1,9,2)
print s.computeArea(0, 0, 0, 0, -1, -1, 1, 1)
print s.computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
print s.computeArea(-2, -2, 2, 2, -1, 4, 1, 6)
