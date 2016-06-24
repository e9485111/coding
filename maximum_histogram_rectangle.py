class Solution(object):
  def largestRectangleArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    st = []
    ret = 0
    for i in range(0, len(height)+1):
      if i == len(height):
        val = 0
      else:
        val = height[i]

      if not st or val > st[-1][0]:
        st.append((val, i))
      else:
        while st and val <= st[-1][0]:
          h = st[-1][0]
          st.pop()
          if not st:
            left = -1
          else:
            left = st[-1][1]
          ret = max(ret, h*(i-1-left))
        st.append((val,i))

    return ret

s = Solution()
print s.largestRectangleArea([3,2,1,2,3,3])

