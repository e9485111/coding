#!/usr/bin/python
import math
class Solution:
    # @param an integer
    # @return a list of string

  def pow(self,a,b):
    if b == 0:
      return 1
    if a == 0:
      return 0
    if a == 1:
      return 1
    if b == -1:
      return 1/a

    if b % 2 == 0:
      val = pow(a, b/2)
      return val*val
    else:
      if b > 0:
        val = pow(a,b/2)
        return val*val*a
      else:
        val = pow(a,b/2+1)
        return val*val*(1/a)



s = Solution()
a = [
    5.0,
    -5.0,
    5.0,
    -0.5,
    0.23]
b = [-3,-2,-1,0,1,2,3]
for i in a:
  for j in b:
    v = math.pow(i,j) - s.pow(i,j)
    assert abs(v) < 0.000000001, s.pow(i,j)
