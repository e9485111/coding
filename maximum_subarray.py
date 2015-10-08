class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
      ret = []
      curr = []
      val = 0
      dp = []
      if len(nums):
        m = nums[0]
        for i in nums[1:]:
          m = max(m,i)
        if m <= 0:
          return m
        if nums[0] >=0:
          val = nums[0]
          dp += [nums[0]]
          ret += [nums[0]]
          curr += [nums[0]]
        else:
          dp += [0]
      else:
        return None


      for i in nums[1:]:
        n = dp[-1] + i
        if n >= 0:
          dp += [n]
          curr += [i]
          if dp[-1] > val:
            val = dp[-1]
            ret = curr[:]
        else:
          dp += [0]
          curr = []

      return val

s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print s.maxSubArray([-2,-2,-3])
