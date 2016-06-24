class Solution(object):
    def largestRectangleArea(self, height):
        st = []
        ret = 0
        for i in range(0, len(height)+1):
            if i == len(height):
                h=0
            else:
                h = height[i]
            if not st or h > height[st[-1]]:
                st.append(i)
            else:
                while st and h <= height[st[-1]]:
                    last = st.pop()
                    if st:
                        start = st[-1]
                    else:
                        start = -1
                    ret = max(ret, height[last] * (i-start-1))
                st.append(i)
        return ret

s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3])

