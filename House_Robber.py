class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
          return 0
        DP = {"R":[0]*len(nums), "N":[0]*len(nums)}
        DP['R'][0] = nums[0]
        DP['N'][0] = 0
        for i in range(1, len(nums)):
          DP['R'][i] = DP['N'][i-1]+nums[i]
          DP['N'][i] = max(DP['R'][i-1], DP['N'][i-1])

        print DP
        return max(DP['R'][-1], DP['N'][-1])

s = Solution()
print s.rob([4,2,5,7])
