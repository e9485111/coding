class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
      q1 = []
      q2 = []
      ret = []
      m = None
      if not nums:
        return ret
      for i in range(0,k):
        q1.append(nums[i])
        if not q2:
          q2 += [nums[i]]
        else:
          while q2 and nums[i] > q2[-1]:
            q2.pop()
          q2 += [nums[i]]
      for n in range(k, len(nums)):
        i = nums[n]
        ret.append(q2[0])
        if q2[0] == q1[0]:
          q2.pop(0)
        while q2 and i > q2[-1]:
          q2.pop()
        q2 += [i]

        q1.pop(0)
        q1.append(i)

      ret.append(q2[0])
      return ret
s = Solution()
i = [4,-2]
print s.maxSlidingWindow(i, 2)
i = [7,2,4]
print s.maxSlidingWindow(i, 2)
i = [1,-1]
print s.maxSlidingWindow(i, 1)
i = [1,3,-1,-3,5,3,6,7]
print s.maxSlidingWindow(i, 3)
i = []
print s.maxSlidingWindow(i, 0)
i = [1,3,-1,-3,5,3,6,7]
print s.maxSlidingWindow(i, 8)
